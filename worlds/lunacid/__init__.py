from typing import Dict, List, Set, Any, Iterable, Optional, Union
from BaseClasses import Region, Entrance, Location, Item, Tutorial, ItemClassification, MultiWorld
from Options import PerGameCommonOptions
from worlds.AutoWorld import World, WebWorld
from .data.location_data import events
from .Items import all_items, create_items
from .Locations import all_locations, create_locations, all_event_locations, LocationDict
from .Regions import create_regions
from .Rules import rules, LunacidLogic
from worlds.generic.Rules import set_rule
from .Options import LunacidOptions

client_version = 0


class LunacidLocation(Location):
    game: str = "Lunacid"

    def __init__(self, player: int, name: str, address: Optional[int], parent=None):
        super().__init__(player, name, address, parent)
        self.event = not address


class LunacidItem(Item):
    game: str = "Lunacid"


class LunacidWeb(WebWorld):
    theme = "partyTime"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Lunacid randomizer connected to an Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["Albrekka"]
    )]


class LunacidWorld(World):
    """
    Lunacid is a first person dungeon crawler inspired by old FROMSOFT games like Shadow Tower and King’s Field.

    Long ago a great beast arose from the sea and covered the earth in a poison fog. Now those deemed undesirable
    are thrown into a great well, which has become a pit of chaos and disease. You awaken in a moonlit subterranean world,
    having been thrown into the Great Well for crimes unknown. The only way out is to go further down and confront the
    sleeping old one below. On the way there will be many creatures and secrets to discover.
    """

    game: str = "Lunacid"
    topology_present = False

    item_name_to_id = {name: data.code for name, data in all_items.items()}
    location_name_to_id = {name: data.code for name, data in all_locations.items()}

    data_version = 0
    required_client_version = (0, 4, 3)

    options_dataclass = LunacidOptions
    options: LunacidOptions
    logic: LunacidLogic

    web = LunacidWeb()
    all_progression_items: Set[str]

    def __init__(self, world: MultiWorld, player: int):
        super().__init__(world, player)
        self.all_progression_items = set()

    def create_regions(self):
        def create_region(name: str, exits: Iterable[str]) -> Region:
            region = Region(name, self.player, self.multiworld)
            region.exits = [Entrance(self.player, exit_name, region) for exit_name in exits]
            return region

        world_regions = create_regions(create_region)

        def add_location(name: str, code: Optional[int], region_name: str):
            region = world_regions[region_name]
            location = LunacidLocation(self.player, name, code, region)
            location.access_rule = lambda _: True
            region.locations.append(location)

        create_locations(add_location, self.options)
        self.multiworld.regions.extend(world_regions.values())

    def create_items(self):
        created_items = create_items(self.create_item, self.options,
                                     self.multiworld.random)

        self.multiworld.itempool += created_items

        self.setup_victory()

    def setup_victory(self):
        if self.options.ending == self.options.ending.option_ending_cd:
            self.create_event_location(all_event_locations["Look Into The Abyss"],
                                       self.can_reach("Look Into The Abyss"),
                                       "Victory")
        else:
            self.create_event_location(all_event_locations["Wake the Dreamer"],
                                       self.can_reach("Wake the Dreamer"),
                                       "Victory")

        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def create_item(self, item: Union[str, Item]) -> LunacidItem:
        if isinstance(item, str):
            item = all_items[item]

        if item.classification == ItemClassification.progression:
            self.all_progression_items.add(item.name)
        return LunacidItem(item.name, item.classification, item.code, self.player)

    def create_event_location(self, location_data: LocationDict, rule: bool = True, item: Optional[str] = None):
        if item is None:
            item = location_data.name

        region = self.multiworld.get_region(location_data.region, self.player)
        location = LunacidLocation(self.player, location_data.name, None, region)
        location.access_rule = rule
        region.locations.append(location)
        location.place_locked_item(self.create_item(item))

    def set_rules(self):
        rules(self)

    def fill_slot_data(self) -> Dict[str, Any]:

        modified_bundles = {}
        for bundle_key in self.modified_bundles:
            key, value = self.modified_bundles[bundle_key].to_pair()
            modified_bundles[key] = value

        excluded_options = []
        excluded_option_names = [option.internal_name for option in excluded_options]
        generic_option_names = [option_name for option_name in PerGameCommonOptions.type_hints]
        excluded_option_names.extend(generic_option_names)
        included_option_names: List[str] = [option_name for option_name in self.options_dataclass.type_hints if option_name not in excluded_option_names]
        slot_data = self.options.as_dict(*included_option_names)
        slot_data.update({
            "seed": self.multiworld.per_slot_randoms[self.player].randrange(1000000000),  # Seed should be max 9 digits
            "randomized_entrances": self.randomized_entrances,
            "modified_bundles": modified_bundles,
            "client_version": "4.0.0",
        })

        return slot_data

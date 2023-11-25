from dataclasses import dataclass
from typing import Dict, List, Set, Any, Iterable, Optional, Union
from collections import Counter
from BaseClasses import Region, Entrance, Location, Item, Tutorial, ItemClassification, MultiWorld
from Options import PerGameCommonOptions
from worlds.AutoWorld import World, WebWorld
from .data.location_data import events
from .data.item_data import money, max_item_count_by_item, all_item_data_by_name
from .strings.options import Endings, Victory
from .strings.regions_entrances import LunacidRegion
from .Items import item_table, complete_items_by_name, create_items, group_table, ITEM_CODE_START
from .Locations import location_table, create_locations, LocationDict, LOCATION_CODE_START
from .Regions import link_lunacid_areas, lunacid_entrances, lunacid_regions
from .Rules import set_rules, has_every_spell
from worlds.generic.Rules import set_rule
from .Options import LunacidOptions


@dataclass(frozen=True)
class LunacidItem:
    actual_id: Optional[int]
    name: str
    classification: ItemClassification
    player: int


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

    game = "Lunacid"
    topology_present = False
    item_name_to_id = {item.name: item.code for item in item_table}
    location_name_to_id = {location.name: location.code for location in location_table}

    data_version = 0
    required_client_version = (0, 4, 3)

    options_dataclass = LunacidOptions
    Options: LunacidOptions
    item_name_groups = group_table

    web = LunacidWeb()

    def create_item(self, name: str) -> LunacidItem:
        item_id: int = self.item_name_to_id[name]
        actual_id = ITEM_CODE_START + item_id

        return LunacidItem(actual_id, name, item_table[actual_id]["classification"], player=self.player)

    def create_event(self, event: str):
        return Item(event, ItemClassification.progression_skip_balancing, None, self.player)

    def get_filler_item_name(self) -> str:
        return self.multiworld.random.choice(money)

    def create_regions(self):
        world = self.multiworld
        player = self.player

        def lunacidregion(region_name: str, entrances):
            region = Region(region_name, player, world)
            for entrance in entrances:
                region.exits.append(Entrance(player, entrance, region))
            return region

        world.regions += [lunacidregion(*r) for r in lunacid_regions]
        link_lunacid_areas(world, player)

        ending_region = world.get_region(LunacidRegion.grave_of_the_sleeper, player)

        if self.options.ending == self.options.ending.option_ending_cd:
            victory = Location(player, Endings.look_into_abyss, None, ending_region)
        else:
            victory = Location(player, Endings.wake_dreamer, None, ending_region)
        victory.place_locked_item(self.create_event(Victory.victory))
        ending_region.locations.append(victory)

        if self.options.ending == self.options.ending.option_ending_e:
            set_rule(victory, lambda state: has_every_spell(self, state, player))

        world.completion_condition[self.player] = lambda state: state.has("Victory", player)

    def create_items(self):
        world = self.multiworld
        player = self.player

        skipped_items = []

        for item, count in world.start_inventory[player].value.items():
            item_name = complete_items_by_name[item]
            max_count = 1
            if item_name in all_item_data_by_name:
                max_count = max_item_count_by_item[item_name]
            if count > max_count:
                count = max_item_count_by_item[item_name]
            for _ in range(count):
                skipped_items.append(item)

        pool = create_items(self.options, self.multiworld.random)

        for items in skipped_items:
            item = complete_items_by_name[items]
            pool.remove(item)
            pool.append(self.create_item(self.get_filler_item_name()))

        world.itempool += pool

    def set_rules(self):
        set_rules(self)

    def fill_slot_data(self) -> Dict[str, Any]:

        excluded_options = []
        excluded_option_names = [option.internal_name for option in excluded_options]
        generic_option_names = [option_name for option_name in PerGameCommonOptions.type_hints]
        excluded_option_names.extend(generic_option_names)
        included_option_names: List[str] = [option_name for option_name in self.options_dataclass.type_hints if option_name not in excluded_option_names]
        slot_data = self.options.as_dict(*included_option_names)
        slot_data.update({
            "seed": self.multiworld.per_slot_randoms[self.player].randrange(1000000000),  # Seed should be max 9 digits
            "client_version": "0.1.0",
        })

        return slot_data

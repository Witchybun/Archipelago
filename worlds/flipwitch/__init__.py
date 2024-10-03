from time import strftime
from typing import Dict, Any, Iterable, TextIO
import logging
from BaseClasses import Region, Entrance, Location, Item, Tutorial, ItemClassification
from Fill import fill_restrictive
from worlds.AutoWorld import World, WebWorld
from . import options
from .data.items import FlipwitchItemData
from .strings.regions_entrances import FlipwitchRegion
from .items import item_table, complete_items_by_name, create_items
from .options import FlipwitchOptions
from .locations import create_locations, location_table
from .regions import link_flipwitch_areas, create_regions
from .rules import FlipwitchRules
from worlds.generic.Rules import set_rule


logger = logging.getLogger()


class FlipwitchItem(Item):
    game: str = "Flipwitch"


class FlipwitchWeb(WebWorld):
    theme = "partyTime"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Flipwitch randomizer connected to an Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["Albrekka", "Prin"]
    )]


class FlipwitchWorld(World):
    """
    Use your newly-acquired genderbending abilities as a 'FlipWitch' to conquer evil monsters, giant bosses, and Monster Girls across the land!
    You'll have to use your wits in this quirky adventure to seduce everyone around you!
    """

    game = "Flipwitch"
    topology_present = False
    item_name_to_id = {item.name: item.code for item in item_table}
    location_name_to_id = {location.name: location.location_id for location in location_table}

    item_name_groups = {
    }

    location_name_groups = {
    }

    required_client_version = (0, 5, 0)

    options_dataclass = FlipwitchOptions
    options: FlipwitchOptions
    web = FlipwitchWeb()
    logger = logging.getLogger()

    def __init__(self, multiworld, player):
        super(FlipwitchWorld, self).__init__(multiworld, player)

    def create_item(self, name: str, override_classification: ItemClassification = None) -> "FlipwitchItem":
        item_id: int = self.item_name_to_id[name]

        if override_classification is None:
            override_classification = complete_items_by_name[name].classification

        return FlipwitchItem(name, override_classification, item_id, player=self.player)

    def create_event(self, event: str):
        return Item(event, ItemClassification.progression_skip_balancing, None, self.player)

    def get_filler_item_name(self) -> str:
        return self.random.choice(["Nothing"])

    def set_rules(self):
        FlipwitchRules(self).set_flipwitch_rules()

    def create_items(self):
        locations_count = len([location
                               for location in self.multiworld.get_locations(self.player)if location.item is None])
        excluded_items = self.multiworld.precollected_items[self.player]
        potential_pool = create_items(self.create_item, locations_count, excluded_items)
        self.multiworld.itempool += potential_pool

    def create_regions(self):
        world = self.multiworld
        player = self.player

        def create_region(region_name: str, exits: Iterable[str]) -> Region:
            flipwitch_region = Region(region_name, player, world)
            flipwitch_region.exits = [Entrance(player, exit_name, flipwitch_region) for exit_name in exits]
            return flipwitch_region

        world_regions = create_regions(create_region)
        final_locations = create_locations()
        for location in final_locations:
            name = location.name
            location_id = location.location_id
            region: Region = world_regions[location.region]
            region.add_locations({name: location_id})

        self.multiworld.regions.extend(world_regions.values())

        ending_region = world.get_region(FlipwitchRegion.witch_woods, player)
        victory = Location(player, "Obtain Gender Changing Powers", None, ending_region)
        victory.place_locked_item(self.create_event("Victory"))
        ending_region.locations.append(victory)
        set_rule(victory, lambda state: FlipwitchRules(self).can_complete_quest(state))

        world.completion_condition[self.player] = lambda state: state.has("Victory", player)

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data = {
            "seed": self.random.randrange(1000000000),  # Seed should be max 9 digits
            "client_version": "0.0.1",
            **self.options.as_dict("death_link"),
        }
        return slot_data

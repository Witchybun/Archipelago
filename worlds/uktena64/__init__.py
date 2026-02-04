import logging
from typing import Dict, Any, List

from BaseClasses import Item, Tutorial, ItemClassification, Region, Entrance, Location
from worlds.AutoWorld import WebWorld, World
from worlds.uktena64.data.locations import UktenaLocation, jeb_clear_events, jeeb_clear_events
from worlds.uktena64.items import item_table, complete_items_by_name, create_items
from worlds.uktena64.locations import location_table, create_locations
from worlds.uktena64.options import UktenaOptions
from worlds.uktena64.regions import ConnectionData, create_regions
from worlds.uktena64.rules import UktenaRules
from worlds.uktena64.strings.items import BaseItem, JebItem, JeebItem
from worlds.uktena64.strings.locations import BurningGrove, BleedingGrove, JebCabin, TheBBQBasket, jeb_clears, jeeb_clears
from worlds.uktena64.strings.regions import JebRegion, JeebRegion, BaseRegion

logger = logging.getLogger()


class UktenaItem(Item):
    game: str = "Uktena 64"


class UktenaWeb(WebWorld):
    theme = "partyTime"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Uktena 64 randomizer connected to a Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["Albrekka"]
    )]


class UktenaWorld(World):
    """
    Jebidiah and Jeeb head out to take photos, make barbeque, and some other shit.
    """

    game = "Uktena 64"
    topology_present = False
    item_name_to_id = {item.name: item.code for item in item_table}
    location_name_to_id = {location.name: location.location_id for location in location_table}

    item_name_groups = {
    }

    location_name_groups = {
    }

    required_client_version = (0, 6, 6)

    options_dataclass = UktenaOptions
    options: UktenaOptions
    web = UktenaWeb()
    logger = logging.getLogger()

    def __init__(self, multiworld, player):
        super(UktenaWorld, self).__init__(multiworld, player)

    def create_item(self, name: str, override_classification: ItemClassification = None) -> "UktenaItem":
        item_id: int = self.item_name_to_id[name]

        if override_classification is None:
            override_classification = complete_items_by_name[name].classification

        return UktenaItem(name, override_classification, item_id, player=self.player)

    def create_event(self, event: str):
        return Item(event, ItemClassification.progression_skip_balancing, None, self.player)

    def get_filler_item_name(self) -> str:
        return self.random.choice(["Nothing"])

    def set_rules(self):
        UktenaRules(self).set_uktena_rules()

    def create_items(self):
        forced_items = 0
        if not self.options.randomize_camera_knife:
            forced_items += 1
            if self.options.campaign == self.options.campaign.option_both:
                forced_items += 1
        if self.options.campaign != self.options.campaign.option_jeeb:
            forced_items += 5
        if self.options.campaign != self.options.campaign.option_jebidiah:
            forced_items += 5
        locations_count = len([location
                               for location in self.get_locations() if location.item is None]) - forced_items
        excluded_items = self.multiworld.precollected_items[self.player]
        potential_pool = create_items(self.create_item, excluded_items, self.options, self.random, locations_count)
        self.multiworld.itempool += potential_pool

    def create_regions(self):
        world = self.multiworld
        player = self.player

        def create_region(region_name: str, exits: List[ConnectionData]) -> Region:
            uktena_region = Region(region_name, player, world)
            true_exits = [connector.name for connector in exits]
            uktena_region.exits = [Entrance(player, true_exit, uktena_region) for true_exit in true_exits]
            return uktena_region

        world_regions, world_entrances = create_regions(create_region, world)
        real_locations, event_locations = create_locations(self.options)

        for location in real_locations:
            name = location.name
            location_id = location.location_id
            region: Region = world_regions[location.region]
            region.add_locations({name: location_id})

        self.place_event_items_in_event_locations(event_locations, world_regions)

        if self.options.campaign == self.options.campaign.option_jebidiah:
            world_regions[JebRegion.bleeding].add_event("Uktena Defeated", "Victory")
        if self.options.campaign == self.options.campaign.option_jeeb:
            world_regions[JeebRegion.burning].add_event("Failed Rhythm Game", "Victory")
        if self.options.campaign == self.options.campaign.option_both:
            world_regions[JebRegion.bleeding].add_event("Uktena Defeated", "Complete Jeb Campaign")
            world_regions[JeebRegion.burning].add_event("Failed Rhythm Game", "Complete Jeeb Campaign")
            world_regions[BaseRegion.menu].add_event("Complete Both Campaigns", "Victory")

        self.multiworld.regions.extend(world_regions.values())

        world.completion_condition[self.player] = lambda state: state.has("Victory", player)

    def pre_fill(self) -> None:
        if not self.options.randomize_camera_knife:
            if self.options.campaign != self.options.campaign.option_jeeb:
                camera_location = self.get_location(JebCabin.camera)
                camera_location.place_locked_item(self.create_item(JebItem.camera))
            if self.options.campaign != self.options.campaign.option_jebidiah:
                butcher_location = self.get_location(TheBBQBasket.butcher_knives)
                butcher_location.place_locked_item(self.create_item(JeebItem.butcher_knives))
        if self.options.campaign != self.options.campaign.option_jebidiah:
            for clear in jeeb_clears:
                jeeb_level_done = self.get_location(clear)
                jeeb_level_done.place_locked_item(self.create_item(BaseItem.jeeb_campaign))
        if self.options.campaign != self.options.campaign.option_jeeb:
            for clear in jeb_clears:
                jeb_level_done = self.get_location(clear)
                jeb_level_done.place_locked_item(self.create_item(BaseItem.jeb_campaign))

    def get_pre_fill_items(self) -> List["Item"]:
        pre_fill_items = []
        pre_fill_items.extend([self.create_item(jeb) for jeb in [BaseItem.jeb_campaign]*5])
        pre_fill_items.extend([self.create_item(jeeb) for jeeb in [BaseItem.jeeb_campaign]*5])
        if self.options.randomize_camera_knife:
            return pre_fill_items
        if self.options.campaign != self.options.campaign.option_jeeb:
            pre_fill_items.append(self.create_item(JebItem.camera))
        if self.options.campaign != self.options.campaign.option_jebidiah:
            pre_fill_items.append(self.create_item(JeebItem.butcher_knives))
        return pre_fill_items

    def place_event_items_in_event_locations(self, event_locations_from_settings: Dict[str, List[UktenaLocation]], region_lookup: Dict[str, Region]):
        for region in event_locations_from_settings:
            for location in event_locations_from_settings[region]:
                region_lookup[region].add_event(location.name, location.forced_item)

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data = {
            "seed": self.random.randrange(1000000000),  # Seed should be max 9 digits
            "client_version": "0.1.0",
            **self.options.as_dict("campaign", "randomize_camera_knife", "photographer", "bbq_chef", "hyenas", "rogue_scholar", "death_link"),
        }
        return slot_data


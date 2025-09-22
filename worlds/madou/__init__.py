import logging
import os
import threading
from random import Random
from typing import Dict, Any, List, Iterable

import settings
from BaseClasses import Item, Tutorial, Location, Entrance, ItemClassification, Region
from Utils import visualize_regions
from worlds.AutoWorld import WebWorld, World
from . import tracker
from .options import MadouOptions
from .items import item_table, complete_items_by_name, all_filler_items, create_items
from .locations import location_table, create_locations
from .regions import create_regions
from .client import MadouSNIClient
from .rom import MadouProcedurePatch, patch_rom, HASH
from .rules import MadouRules
from .strings.items import EventItem, Special, Souvenir, Tool
from .strings.locations import EventLocation
from .strings.region_entrances import MadouRegion

logger = logging.getLogger("Madou Monogatari Hanamaru Daiyouchienji")


class MadouSettings(settings.Group):
    class RomFile(settings.SNESRomPath):
        """File name of the KDL3 JP or EN rom"""
        description = "Madou Monogatari Hanamaru Daiyouchienji ROM File"
        copy_to = "Madou Monogatari Hanamaru Daiyouchienji.sfc"
        md5s = [HASH]

    rom_file: RomFile = RomFile(RomFile.copy_to)


class  MadouItem(Item):
    game: str = "Madou Monogatari Hanamaru Daiyouchienji"


class MadouWeb(WebWorld):
    theme = "partyTime"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Madou Monogatari randomizer connected to an Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["Albrekka"]
    )]


class MadouWorld(World):
    """
    Oomf.
    """

    game = "Madou Monogatari Hanamaru Daiyouchienji"
    topology_present = False
    item_name_to_id = {item.name: item.code for item in item_table}
    location_name_to_id = {location.name: location.location_id for location in location_table}

    required_client_version = (0, 6, 2)

    options_dataclass = MadouOptions
    options: MadouOptions
    locations_for_filler: List[Location] = []
    weapon_elements: Dict[str, str] = {}
    world_entrances = dict[str, Entrance]
    randomized_entrances: Dict[str, str] = {}
    enemy_random_data: Dict[str, List[str]]
    enemy_regions: Dict[str, List[str]]
    web = MadouWeb()
    logger = logging.getLogger()
    explicit_indirect_conditions = True

    passthrough: Dict[str, Any]
    using_ut: bool
    ut_can_gen_without_yaml = True  # class var that tells it to ignore the player yaml

    def __init__(self, multiworld, player):
        self.rom_name: bytes = bytes()
        self.rom_name_available_event = threading.Event()
        super(MadouWorld, self).__init__(multiworld, player)
        slot_data = getattr(multiworld, "re_gen_passthrough", {}).get("Madou Monogatari Hanamaru Daiyouchienji")
        if slot_data:
            self.seed = slot_data.get("ut_seed")
        else:
            self.seed = self.random.getrandbits(64)
        self.random = Random(self.seed)

    def generate_early(self) -> None:
        tracker.setup_options_from_slot_data(self)

    def create_item(self, name: str, override_classification: ItemClassification = None) -> "MadouItem":
        item_id: int = self.item_name_to_id[name]

        if override_classification is None:
            override_classification = complete_items_by_name[name].classification

        return MadouItem(name, override_classification, item_id, player=self.player)

    def create_event(self, event: str):
        return Item(event, ItemClassification.progression_skip_balancing, None, self.player)

    def get_filler_item_name(self) -> str:
        return self.random.choice(all_filler_items)

    def set_rules(self):
        MadouRules(self).set_madou_rules()

    def create_items(self):
        locations_count = len([location
                               for location in self.get_locations() if location.item is None])
        excluded_items = self.multiworld.precollected_items[self.player]
        slot_data = getattr(self.multiworld, "re_gen_passthrough", {}).get("Madou Monogatari Hanamaru Daiyouchienji")
        potential_pool = create_items(self.create_item, locations_count, excluded_items, self.options, self.random)

        self.multiworld.itempool += potential_pool

    def create_regions(self):
        multiworld = self.multiworld
        player = self.player

        def create_region(region_name: str, exits: Iterable[str]) -> Region:
            madou_region = Region(region_name, player, multiworld)
            madou_region.exits = [Entrance(player, exit_name, madou_region) for exit_name in exits]
            return madou_region

        world_regions, world_entrances = create_regions(create_region, multiworld)
        self.world_entrances = world_entrances
        locations_list = create_locations(self.options)
        for location in locations_list:
            name = location.name
            location_id = location.location_id
            region: Region = world_regions[location.region]
            region.add_locations({name: location_id})

        self.multiworld.regions.extend(world_regions.values())

        self.get_region(MadouRegion.frog_swamp).add_event(EventLocation.hammer_switch, EventItem.hammer_switch, lambda state: state.has(Tool.hammer, self.player),
                                                          show_in_spoiler=True)

        if not self.options.souvenir_hunt:
            self.get_region(MadouRegion.ruins_town).add_event(EventLocation.ruins_shop, EventItem.ruins_buy, show_in_spoiler=True)
            self.get_region(MadouRegion.bazaar).add_event(EventLocation.bazaar_shop, EventItem.bazaar_buy, show_in_spoiler=True)
            self.get_region(MadouRegion.wolf_town).add_event(EventLocation.wolf_shop, EventItem.wolf_buy, show_in_spoiler=True)

        if self.options.goal == self.options.goal.option_souvenirs:
            multiworld.completion_condition[self.player] = lambda state: (state.has(Souvenir.magic_king_tusk, player) and state.has(Souvenir.magic_king_statue, player) and
                                                                          state.has(Souvenir.magic_king_picture, player) and state.has(Souvenir.magic_king_foot, player) and
                                                                          state.has(Souvenir.dark_jug, player) and state.has(Souvenir.wolf_tail, player) and
                                                                          state.has(Souvenir.waterfall_vase, player) and state.has(Souvenir.dragon_nail, player))
        elif self.options.goal == self.options.goal.option_certificate:
            ending_region = self.get_region(MadouRegion.sage_mountain)
            chest = Location(player, "Chest High on Sage Mountain", None, ending_region)
            chest.place_locked_item(self.create_event("Certificate"))
            chest.access_rule = lambda state: state.has(Special.secret_stone, player, 7)
            multiworld.completion_condition[self.player] = lambda state: state.has("Certificate", player)
        else:
            ending_region = self.get_region(MadouRegion.magical_tower)
            victory = Location(player, "Graduate!", None, ending_region)
            multiworld.completion_condition[self.player] = lambda state: state.has("Victory", player)
            victory.place_locked_item(self.create_event("Victory"))
            ending_region.locations.append(victory)

    def generate_output(self, output_directory: str) -> None:
        try:
            patch = MadouProcedurePatch(player=self.player, player_name=self.player_name)
            patch_rom(self, patch)

            self.rom_name = patch.player_name

            patch.write(os.path.join(output_directory,
                                     f"{self.multiworld.get_out_file_name_base(self.player)}{patch.patch_file_ending}"))
        except Exception:
            raise
        finally:
            self.rom_name_available_event.set()  # make sure threading continues and errors are collected

    def visualize_regions(self):
        multiworld = self.multiworld
        player = self.player
        visualize_regions(multiworld.get_region("Menu", player), f"{multiworld.get_out_file_name_base(player)}.puml", show_locations=False)

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data = {
            "ut_seed": self.seed,
            "seed": self.random.randrange(1000000000),  # Seed should be max 9 digits
        }

        return slot_data

    def interpret_slot_data(self, slot_data: Dict[str, Any]) -> Dict[str, Any]:
        return slot_data

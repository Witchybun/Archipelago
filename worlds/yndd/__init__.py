from random import Random
from typing import Dict, Any, Iterable, TextIO
import logging
from BaseClasses import Region, Entrance, Item, Tutorial, ItemClassification
from Utils import visualize_regions
from entrance_rando import disconnect_entrance_for_randomization, randomize_entrances
from worlds.AutoWorld import World, WebWorld
from . import options
from .strings import vanilla_egg_placement, vanilla_jellyfish_placement
from .strings.custom_features import DefaultColors
from .strings.items import GoalItems, Filler
from .strings.regions_entrances import DreamRegions
from .strings.locations import Streets
from .items import (item_table, complete_items_by_name, create_items)
from .options import DreamOptions
from .locations import create_locations, location_table
from .regions import create_regions, randomized_entrance_names
from .rules import DreamRules

logger = logging.getLogger()


class DreamItem(Item):
    game: str = "Yume Nikki - Dream Diary"


class DreamWeb(WebWorld):
    theme = "partyTime"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Yume Nikki - Dream Diary randomizer",
        "English",
        "setup_en.md",
        "setup/en",
        ["Albrekka"]
    )]


class DreamWorld(World):
    """
    Madotsuki is so eepy that she eeped into a rando oh no.
    """

    game = "Yume Nikki - Dream Diary"
    topology_present = False
    item_name_to_id = {item.name: item.code for item in item_table}
    location_name_to_id = {location.name: location.location_id for location in location_table}

    item_name_groups = {
        "Egg": GoalItems.eggs,
        "Jellyfish": GoalItems.jellyfish,
    }

    location_name_groups = {
    }

    required_client_version = (0, 6, 4)

    options_dataclass = DreamOptions
    options: DreamOptions
    doors: Dict[str, bool] = {}
    web = DreamWeb()
    logger = logging.getLogger()
    world_entrances: Dict[str, Entrance] = {}
    randomized_entrances: Dict[str, str] = {}
    explicit_indirect_conditions = True
    glitches_item_name = "Glitched Item"

    passthrough: Dict[str, Any]
    using_ut: bool
    # tracker_world: ClassVar = Tracker.TRACKER_WORLD
    ut_can_gen_without_yaml = True  # class var that tells it to ignore the player yaml

    def __init__(self, multiworld, player):
        super(DreamWorld, self).__init__(multiworld, player)
        slot_data = getattr(multiworld, "re_gen_passthrough", {}).get("Yume Nikki - Dream Diary")
        if slot_data:
            self.seed = slot_data.get("ut_seed")
        else:
            self.seed = self.random.getrandbits(64)
        self.random = Random(self.seed)

    def generate_early(self) -> None:
        self.verify_item_colors()
        # Tracker.setup_options_from_slot_data(self)

    def create_item(self, name: str, override_classification: ItemClassification = None) -> "DreamItem":
        if name == self.glitches_item_name:
            return DreamItem(name, ItemClassification.progression_skip_balancing, None, self.player)
        item_id: int = self.item_name_to_id[name]

        if override_classification is None:
            override_classification = complete_items_by_name[name].classification

        return DreamItem(name, override_classification, item_id, player=self.player)

    def create_event(self, event: str):
        return Item(event, ItemClassification.progression_skip_balancing, None, self.player)

    def get_filler_item_name(self) -> str:
        return Filler.nothing

    def set_rules(self):
        DreamRules(self).set_yume_nikki_rules(self.doors)

    def create_items(self):
        self.determine_locked_doors(self.random)

        locations_count = len([location
                               for location in self.get_locations() if location.item is None])
        excluded_items = self.multiworld.precollected_items[self.player]
        slot_data = getattr(self.multiworld, "re_gen_passthrough", {}).get("Yume Nikki - Dream Diary")
        potential_pool = create_items(self.create_item, locations_count, excluded_items, self.doors, self.options, self.random)

        # There's a weird edge case where very rarely there's one more item in the pool than there should be.
        all_items = potential_pool
        random_filler = [item for item in potential_pool if item.classification == 0]
        while len(set(self.get_locations())) < len(all_items):
            chosen_filler = self.random.choice(random_filler)
            random_filler.remove(chosen_filler)
            potential_pool.remove(chosen_filler)

        self.multiworld.itempool += potential_pool

    def create_regions(self):
        multiworld = self.multiworld
        player = self.player

        def create_region(region_name: str, exits: Iterable[str]) -> Region:
            dream_region = Region(region_name, player, multiworld)
            dream_region.exits = [Entrance(player, exit_name, dream_region) for exit_name in exits]
            return dream_region

        world_regions, world_entrances = create_regions(create_region, multiworld)
        self.world_entrances = world_entrances
        game_locations = create_locations(self.options)
        for location in game_locations:
            name = location.name
            location_id = location.location_id
            region: Region = world_regions[location.region]
            region.add_locations({name: location_id})

        self.multiworld.regions.extend(world_regions.values())

        self.place_local_eggs_and_jellyfish()

        if self.options.goal == self.options.goal.option_apartment:
            self.get_region(DreamRegions.normal_end).add_event("Wake From Apartment Nightmare", "Victory")
        else:
            self.get_region(DreamRegions.secret_end).add_event("Sleep on the UFO", "Victory")



        multiworld.completion_condition[self.player] = lambda state: state.has("Victory", player)

    def determine_locked_doors(self, random: Random):
        doors = {
            "Streets": True,
            "Wilderness": True,
            "Mall": True,
            "Sewers": True,
            "Docks": True,
            "School": True
        }
        if self.options.starting_doors == self.options.starting_doors.option_choice:
            for door_name in doors:
                if door_name not in self.options.starting_doors_choice:
                    doors[door_name] = False
        elif self.options.starting_doors == self.options.starting_doors.option_range:
            open_doors = random.sample(list(doors.keys()), self.options.starting_doors_range.value)
            for door_name in doors:
                if door_name not in open_doors:
                    doors[door_name] = False
        allowed_doors = [door for door in self.doors if self.doors[door]]
        logger.debug(f"Open Doors: {', '.join(allowed_doors)}")
        self.doors = doors

    def place_local_eggs_and_jellyfish(self):
        if "Eggs" in self.options.local_goals.value:
            for location in vanilla_egg_placement:
                local_location = self.get_location(location)
                egg_item = self.create_event(vanilla_egg_placement[location])
                local_location.address = None
                local_location.place_locked_item(egg_item)
        if "Jellyfish" in self.options.local_goals.value:
            for location in vanilla_jellyfish_placement:
                local_location = self.get_location(location)
                jellyfish_item = self.create_event(vanilla_jellyfish_placement[location])
                local_location.address = None
                local_location.place_locked_item(jellyfish_item)

    def connect_entrances(self) -> None:
        world_entrances = self.world_entrances
        entrances_randod = self.options.randomize_connectors
        if entrances_randod:
            randomized_entrances = [world_entrances[entrance] for entrance in world_entrances if world_entrances[entrance].name in randomized_entrance_names]
            for entrance in randomized_entrances:
                disconnect_entrance_for_randomization(entrance, None, entrance.connected_region.name)
            result = randomize_entrances(self, True, {0: [0]})
            self.randomized_entrances = dict(result.pairings)
            slot_data = getattr(self.multiworld, "re_gen_passthrough", {}).get("Yume Nikki - Dream Diary")
            if slot_data:
                e_dict = {entrance.name: entrance for region in self.multiworld.get_regions(self.player) for entrance in region.entrances}
                entrances = slot_data["entrances"]
                for connection in slot_data["entrances"]:
                    assert connection in e_dict, f"entrance {connection} in slot data not in world"
                    assert entrances[connection] in e_dict, f"entrance {entrances[connection]} in slot data not in world"

                    e_dict[connection].connected_region = e_dict[entrances[connection]].parent_region
                self.randomized_entrances = slot_data["entrances"]
        # self.visualize_regions()
        # hi = True

    def visualize_regions(self):
        multiworld = self.multiworld
        player = self.player
        visualize_regions(multiworld.get_region("Menu", player), f"{multiworld.get_out_file_name_base(player)}.puml", show_locations=False)

    def verify_item_colors(self) -> None:
        self.fix_colors("ProgUseful", DefaultColors.progression)
        self.fix_colors("Progression", DefaultColors.progression)
        self.fix_colors("Useful", DefaultColors.useful)
        self.fix_colors("Trap", DefaultColors.trap)
        self.fix_colors("Filler", DefaultColors.filler)
        self.fix_colors("Gift", DefaultColors.gift)
        self.fix_colors("Cheat", DefaultColors.cheat)

    def fix_colors(self, name: str, default_color: str) -> None:
        if name not in self.options.item_colors:
            self.options.item_colors.value[name] = default_color
        elif not self.is_hex(self.options.item_colors.value[name]):
            self.options.item_colors.value[name] = default_color
        elif "#" not in self.options.item_colors.value[name]:
            self.options.item_colors.value[name] = "#" + self.options.item_colors.value[name]

    @staticmethod
    def is_hex(possible_hex: str) -> bool:
        pure_hex = possible_hex.replace("#", "")
        # We sin in this bitch
        try:
            if len(pure_hex) != 6:
                return False
            int(pure_hex, 16)
            return True
        except ValueError:
            return False

    def write_spoiler_header(self, spoiler_handle: TextIO) -> None:
        """Write to the spoiler header. If individual it's right at the end of that player's options,
        if as stage it's right under the common header before per-player options."""
        if self.options.randomize_connectors:
            self.add_entrances_to_spoiler_log()

    def add_entrances_to_spoiler_log(self) -> None:
        for original_entrance, replaced_entrance in self.randomized_entrances.items():
            self.multiworld.spoiler.set_entrance(original_entrance, replaced_entrance, "entrance", self.player)

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data = {
            "ut_seed": self.seed,
            "seed": self.random.randrange(1000000000),  # Seed should be max 9 digits
            "client_version": "0.0.1",
            "doors": self.doors,
            **self.options.as_dict("goal", "item_colors"),
        }
        return slot_data

    def interpret_slot_data(self, slot_data: Dict[str, Any]) -> Dict[str, Any]:
        return slot_data

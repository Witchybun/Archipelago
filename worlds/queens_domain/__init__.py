import logging
from random import Random
from typing import List, Dict, Any, ClassVar

from BaseClasses import Item, Tutorial, Location, Entrance, ItemClassification, MultiWorld
from Utils import visualize_regions
from worlds.AutoWorld import WebWorld, World
from worlds.queens_domain.Options import QueensDomainOptions

logger = logging.getLogger()


class QueensDomainItem(Item):
    game: str = "Queen's Domain"


class QueensDomainWeb(WebWorld):
    theme = "partyTime"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Queen's Domain randomizer connected to an Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["put contributors here"]
    )]


class QueensDomainWorld(World):
    """
    Make a description idk
    """

    game = "Queen's Domain"
    topology_present = False
    item_name_to_id = {item.name: item.code for item in item_table}
    location_name_to_id = {location.name: location.location_id for location in location_table}

    item_name_groups = {
    }

    location_name_groups = {
    }

    required_client_version = (0, 6, 8)

    options_dataclass = QueensDomainOptions
    options: QueensDomainOptions
    starting_weapon: QueensDomainItem
    level = 0
    local_alchemy: List[Item] = []
    local_filler: List[Item] = []
    locations_for_filler: List[Location] = []
    weapon_elements: Dict[str, str] = {}
    world_entrances = dict[str, Entrance]
    randomized_entrances: Dict[str, str] = {}
    enemy_random_data: Dict[str, List[str]]
    enemy_regions: Dict[str, List[str]]
    custom_class_name: str
    custom_class_description: str
    custom_class_stats: Dict[str, int]
    web = QueensDomainWeb()
    logger = logging.getLogger()
    explicit_indirect_conditions = True
    glitches_item_name = "Glitched Item"

    passthrough: Dict[str, Any]
    using_ut: bool = False

    def __init__(self, multiworld, player):
        super(QueensDomainWorld, self).__init__(multiworld, player)
        slot_data = getattr(multiworld, "re_gen_passthrough", {}).get("Queen's Domain")
        if slot_data:
            self.seed = slot_data.get("ut_seed")
            self.using_ut = True
        else:
            self.seed = self.random.getrandbits(64)
        self.random = Random(self.seed)
        self.custom_class_name = ""
        self.custom_class_description = ""
        self.custom_class_stats = {}

    def create_item(self, name: str, override_classification: ItemClassification = None) -> "QueensDomainItem":
        if name == self.glitches_item_name:
            return QueensDomainItem(name, ItemClassification.progression_skip_balancing, None, self.player)
        item_id: int = self.item_name_to_id[name]

        if override_classification is None:
            override_classification = complete_items_by_name[name].classification

        return QueensDomainItem(name, override_classification, item_id, player=self.player)

    def create_event(self, event: str):
        return Item(event, ItemClassification.progression_skip_balancing, None, self.player)

    def get_filler_item_name(self) -> str:
        return self.random.choice(all_filler_items)

    def set_rules(self):
        QueensDomainRules(self).set_queens_domain_rules()

    def create_items(self):
        locations_count = len([location
                               for location in self.get_locations() if location.item is None]) - 1
        if self.options.etnas_pupil and self.options.dropsanity == self.options.dropsanity.option_randomized:
            locations_count -= 80
        if self.options.starting_area == self.options.starting_area.option_tomb:
            locations_count -= 1
        excluded_items = self.multiworld.precollected_items[self.player]
        slot_data = getattr(self.multiworld, "re_gen_passthrough", {}).get("Queen's Domain")
        if slot_data:
            ut_starting_weapon = slot_data["starting_weapon"]
        else:
            ut_starting_weapon = ""
        if not self.weapon_elements:
            self.weapon_elements = determine_weapon_elements(self.options, self.random)
        (potential_pool, self.local_filler, starting_weapon_choice) = create_items(self.create_item, locations_count, excluded_items,
                                                                                   self.weapon_elements, self.rolled_month, self.level, ut_starting_weapon, self.options,
                                                                                   self.random)
        self.starting_weapon = starting_weapon_choice
        if potential_pool.count(self.starting_weapon) > 1:
            potential_pool.remove(self.starting_weapon)

        # There's a weird edge case where very rarely there's one more item in the pool than there should be.
        all_items = potential_pool + self.local_filler + self.local_alchemy + [self.starting_weapon]
        if len(set(self.get_locations())) < len(all_items):
            random_filler = [item for item in potential_pool if item.classification == 0]
            potential_pool.remove(random_filler)

        self.multiworld.itempool += potential_pool

        starting_location = self.get_location(BaseLocation.wings_rest_crystal_shard)

        starting_location.place_locked_item(self.starting_weapon)
        if self.options.starting_area == self.options.starting_area.option_tomb:
            lamp = self.create_item(UniqueItem.oil_lantern, ItemClassification.progression | ItemClassification.useful)
            bony_friend = self.get_location(BaseLocation.wings_rest_clives_gift)
            bony_friend.place_locked_item(lamp)

        if self.options.etnas_pupil and self.options.dropsanity == self.options.dropsanity.option_randomized:
            alchemy_items = []
            for _ in range(5):  # make sure there's enough of them to go around
                for alchemy_item in Alchemy.necessary_alchemy_items:
                    alchemy_items.append(Item(alchemy_item, ItemClassification.progression | ItemClassification.useful,
                                              self.item_name_to_id[alchemy_item], self.player))
            self.local_alchemy = alchemy_items

        if self.multiworld.players == 1:
            self.multiworld.itempool += self.local_filler

    def create_regions(self):
        multiworld = self.multiworld
        player = self.player
        starting_area = self.options.starting_area.current_key

        def create_region(region_name: str, exits: Iterable[str]) -> Region:
            lunacid_region = Region(region_name, player, multiworld)
            lunacid_region.exits = [Entrance(player, exit_name, lunacid_region) for exit_name in exits]
            return lunacid_region

        world_regions, world_entrances = create_regions(starting_area, create_region, multiworld)
        self.world_entrances = world_entrances
        locations = create_locations(self.options, self.rolled_month, self.level)
        for location in locations:
            name = location.name
            location_id = location.location_id
            region: Region = world_regions[location.region]
            region.add_locations({name: location_id})

        self.multiworld.regions.extend(world_regions.values())

        if self.options.ending == self.options.ending.option_ending_b:
            ending_region = self.get_region(LunacidRegion.labyrinth_of_ash)
        elif self.options.ending != self.options.ending.option_any_ending:
            ending_region = self.get_region(LunacidRegion.grave_of_the_sleeper)
        else:
            ending_region = self.get_region(LunacidRegion.grave_of_the_sleeper)
        grotto_region = self.get_region(LunacidRegion.boiling_grotto)

        hicket = Location(player, "Free Sir Hicket", None, grotto_region)
        hicket.place_locked_item(self.create_event("Sir Hicket's Freedom from Armor"))
        if self.options.ending == self.options.ending.option_ending_cd:
            victory = Location(player, Endings.look_into_abyss, None, ending_region)
        elif self.options.ending == self.options.ending.option_ending_b:
            victory = Location(player, Endings.open_door, None, ending_region)
        elif (self.options.ending == self.options.ending.option_ending_a
              or self.options.ending == self.options.ending.option_ending_e):
            victory = Location(player, Endings.wake_dreamer, None, ending_region)
        else:
            victory = Location(player, "The Dreamer or the Door", None, ending_region)
        victory.place_locked_item(self.create_event(Victory.victory))
        ending_region.locations.append(victory)

        self.set_completion_rule(Has(Victory.victory))

    # Can un-comment the method to generate a .puml to see regions better when you generate.
    #def connect_entrances(self) -> None:
        # self.visualize_regions()
        # hi = True

    def visualize_regions(self):
        multiworld = self.multiworld
        player = self.player
        visualize_regions(multiworld.get_region("Menu", player), f"{multiworld.get_out_file_name_base(player)}.puml", show_locations=False)

    def pre_fill(self) -> None:
        if len(self.local_filler) > 0:
            sphere_one_locations = [location for location in self.multiworld.get_reachable_locations(CollectionState(self.multiworld), self.player) if
                                    location.item is None]
            necessary_locations = set(self.random.sample(sphere_one_locations, 3))
            good_locations_to_fill = [location for location in self.multiworld.get_unfilled_locations(self.player)
                                      if location not in necessary_locations and location.name not in self.options.priority_locations]
            self.locations_for_filler = good_locations_to_fill

    @classmethod
    def stage_pre_fill(cls, multiworld: MultiWorld) -> None:
        queens_domain_fill_worlds: List[QueensDomainWorld] = [world for world in multiworld.get_game_worlds("Lunacid")
                                                   if world.options.filler_local_percent.value > 0]
        if not queens_domain_fill_worlds:
            return
        if multiworld.players > 1:
            for world in queens_domain_fill_worlds:
                if world.options.filler_local_percent > 0:
                    world.random.shuffle(world.locations_for_filler)
                    for item in world.local_filler:
                        world.locations_for_filler.pop().place_locked_item(item)

    def get_pre_fill_items(self) -> List["Item"]:
        pre_fill_items = []
        pre_fill_items.extend(self.local_alchemy)
        pre_fill_items.extend(self.local_filler)
        return pre_fill_items

    def fill_slot_data(self) -> Dict[str, Any]:
        item_spots = self.important_item_locations()
        slot_data = {
            "ut_seed": self.seed,
            "seed": self.random.randrange(1000000000),  # Seed should be max 9 digits
            "client_version": "1.1.2",
            "rolled_month": self.rolled_month,
            "starting_weapon": self.starting_weapon.name,
            "elements": self.weapon_elements,
            "created_class_name": self.custom_class_name,
            "created_class_description": self.custom_class_description,
            "created_class_stats": self.custom_class_stats,
            "enemy_placement": self.enemy_random_data,
            "item_spots": item_spots,
            "enemy_regions": self.enemy_regions,
            "force_no_exp": self.options.challenges == self.options.challenges.option_exp,
            "entrances": self.randomized_entrances,
            **self.options.as_dict("ending", "entrance_randomization",
                                   "required_strange_coin", "enemy_randomization", "shopsanity", "dropsanity",
                                   "quenchsanity", "etnas_pupil", "switch_locks", "door_locks", "random_elements",
                                   "secret_door_lock", "death_link", "starting_class",
                                   "starting_area", "levelsanity", "bookworm",
                                   "grasssanity", "breakables", "total_strange_coin", "random_equip_stats", "silver_link",
                                   "challenges", "tricks_and_glitches"),
        }

        return slot_data

    def interpret_slot_data(self, slot_data: Dict[str, Any]) -> Dict[str, Any]:
        return slot_data

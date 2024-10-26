from random import Random
from time import strftime
from typing import Dict, Any, Iterable, TextIO
import logging
from BaseClasses import Region, Entrance, Location, Item, Tutorial, ItemClassification
from Fill import fill_restrictive
from worlds.AutoWorld import World, WebWorld
from . import options
from .options import FlipwitchOptions
from .data.items import FlipwitchItemData
from .strings.locations import WitchyWoods, GhostCastle, ClubDemon, AngelicHallway, SlimeCitadel, UmiUmi
from .strings.regions_entrances import FlipwitchRegion
from .strings.items import Goal, Power, Upgrade, Key
from .strings.locations import Gacha
from .items import item_table, complete_items_by_name, create_items
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
        ["Albrekka", "Prin", "SomeLazyGamer"]
    )]


class FlipwitchWorld(World):
    """
    Use your newly-acquired genderbending abilities as a 'FlipWitch' to conquer evil monsters, giant bosses, and Monster Girls across the land!
    You'll have to use your wits in this quirky adventure to seduce everyone around you!
    """

    game = "Flipwitch Forbidden Sex Hex"
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
    animal_order = []
    bunny_order = []
    monster_order = []
    angel_order = []

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
        self.determine_gacha_order(self.random)
        FlipwitchRules(self).set_flipwitch_rules(self.animal_order, self.bunny_order, self.monster_order, self.angel_order)

    def create_items(self):
        chaos_count = 0
        if self.options.shuffle_chaos_pieces == self.options.shuffle_chaos_pieces.option_false:
            chaos_count += 6
        locations_count = len([location
                               for location in self.multiworld.get_locations(self.player)if location.item is None]) - chaos_count
        excluded_items = self.multiworld.precollected_items[self.player]
        potential_pool = create_items(self.create_item, locations_count, excluded_items, self.options, self.random)
        self.multiworld.itempool += potential_pool

    def create_regions(self):
        world = self.multiworld
        player = self.player

        def create_region(region_name: str, exits: Iterable[str]) -> Region:
            flipwitch_region = Region(region_name, player, world)
            flipwitch_region.exits = [Entrance(player, exit_name, flipwitch_region) for exit_name in exits]
            return flipwitch_region

        world_regions = create_regions(create_region)
        final_locations = create_locations(self.options)
        for location in final_locations:
            name = location.name
            location_id = location.location_id
            region: Region = world_regions[location.region]
            region.add_locations({name: location_id})

        self.multiworld.regions.extend(world_regions.values())

        ending_region = world.get_region(FlipwitchRegion.witch_woods, player)
        victory = Location(player, "Defeat the Chaos Queen", None, ending_region)
        victory.place_locked_item(self.create_event("Victory"))
        ending_region.locations.append(victory)
        set_rule(victory, lambda state: state.has(Goal.chaos_piece, self.player, 6) and state.has(Power.slime_form, self.player) and
                                        state.has(Upgrade.angel_feathers, self.player) and state.has(Key.chaos_sanctum, self.player))

        world.completion_condition[self.player] = lambda state: state.has("Victory", player)

    def pre_fill(self) -> None:
        state = self.multiworld.get_all_state(False)
        chaos_pieces = [chaos_piece for chaos_piece in [Item(Goal.chaos_piece, ItemClassification.progression | ItemClassification.useful,
                                                             self.item_name_to_id[Goal.chaos_piece], self.player)]*6]
        if self.options.shuffle_chaos_pieces == self.options.shuffle_chaos_pieces.option_false:
            boss_location_names = [WitchyWoods.goblin_queen_chaos, GhostCastle.ghost_chaos, ClubDemon.demon_boss_chaos,
                                   AngelicHallway.angelica_chaos, SlimeCitadel.slimy_princess_chaos, UmiUmi.frog_boss_chaos]
            boss_locations = [location for location in self.multiworld.get_locations(self.player) if location.name in boss_location_names]
            fill_restrictive(self.multiworld, state, boss_locations, chaos_pieces, single_player_placement=True, lock=True, allow_excluded=True)

    def determine_gacha_order(self, random: Random):
        bunny_order = Gacha.bunny_gacha.copy()
        random.shuffle(bunny_order)
        self.bunny_order = bunny_order
        animal_order = Gacha.animal_gacha.copy()
        random.shuffle(animal_order)
        self.animal_order = animal_order
        monster_order = Gacha.monster_gacha.copy()
        random.shuffle(monster_order)
        self.monster_order = monster_order
        angel_order = Gacha.angel_demon_gacha.copy()
        random.shuffle(angel_order)
        self.angel_order = angel_order

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data = {
            "seed": self.random.randrange(1000000000),  # Seed should be max 9 digits
            "client_version": "0.1.13",
            "animal_order": self.animal_order,
            "bunny_order": self.bunny_order,
            "monster_order": self.monster_order,
            "angel_order": self.angel_order,
            **self.options.as_dict("starting_gender", "shop_prices", "gachapon", "death_link"),
        }
        return slot_data

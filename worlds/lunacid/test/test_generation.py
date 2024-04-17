import unittest
from random import random
from typing import Set

from BaseClasses import CollectionState, MultiWorld
from . import LunacidTestBase, setup_solo_multiworld, LunacidTestCase
from .. import Endings, Options
from ..Regions import consistent_entrances, RandomizationFlag, consistent_regions
from ..data import item_count_data
from ..data.item_count_data import base_weapons, base_spells
from ..data.location_data import *
from ..data.spell_data import all_spells, drop_spells
from ..strings.items import Switch


class TestAllLocationsAppended(LunacidTestBase):

    def test_if_base_locations_appended(self):
        for location in wings_rest:
            self.assertIn(location, base_locations)
        for location in the_fetid_mire:
            self.assertIn(location, base_locations)
        for location in yosei_forest:
            self.assertIn(location, base_locations)
        for location in forest_canopy:
            self.assertIn(location, base_locations)
        for location in hollow_basin:
            self.assertIn(location, base_locations)
        for location in forbidden_archives:
            self.assertIn(location, base_locations)
        for location in accursed_tomb:
            self.assertIn(location, base_locations)
        for location in the_sacrosant_sea:
            self.assertIn(location, base_locations)
        for location in laetus_chasm:
            self.assertIn(location, base_locations)
        for location in great_well_surface:
            self.assertIn(location, base_locations)
        for location in castle_le_fanu:
            self.assertIn(location, base_locations)
        for location in holy_battlefield:
            self.assertIn(location, base_locations)
        for location in tower_of_abyss:
            self.assertIn(location, base_locations)
        for location in sealed_ballroom:
            self.assertIn(location, base_locations)
        for location in boiling_grotto:
            self.assertIn(location, base_locations)
        for location in throne_room:
            self.assertIn(location, base_locations)
        for location in terminus_prison:
            self.assertIn(location, base_locations)
        for location in labyrinth_of_ash:
            self.assertIn(location, base_locations)
        for location in forlorn_arena:
            self.assertIn(location, base_locations)
        for location in chamber_of_fate:
            self.assertIn(location, base_locations)
        self.assertTrue(209 == len(base_locations), f"Location count mismatch, got {len(base_locations)}.")


class TestEndingE(LunacidTestBase):
    options = {"ending": "ending_e"}

    def can_reach_all_regions(self, state: CollectionState, spots: List[str]):
        all_rule = True
        for spot in spots:
            all_rule = all_rule and state.can_reach(spot, "Region", self.player)
        return all_rule

    def has_every_spell(self, state: CollectionState) -> bool:
        every_spell = [spell.name for spell in all_spells if spell.name not in drop_spells]
        mob_spell_regions = [LunacidRegion.forlorn_arena, LunacidRegion.castle_le_fanu_red, LunacidRegion.castle_le_fanu_white,
                             LunacidRegion.terminus_prison_dark,
                             LunacidRegion.labyrinth_of_ash, LunacidRegion.boiling_grotto, LunacidRegion.forbidden_archives_3, LunacidRegion.sand_temple,
                             LunacidRegion.temple_of_silence_interior, LunacidRegion.sealed_ballroom]
        for region in mob_spell_regions:
            self.assertTrue(state.can_reach(region, "Region", self.player), f"Can't reach {region}")
        return state.has_all(every_spell, self.player) and self.can_reach_all_regions(self.multiworld.state, mob_spell_regions)

    def test_if_goal_can_be_true(self):
        self.collect_by_name([spell for spell in item_count_data.base_spells])
        self.collect_by_name([UniqueItem.white_tape])
        symbol = self.get_item_by_name("Progressive Vampiric Symbol")
        self.collect([symbol, symbol, symbol])
        self.collect_by_name([Weapon.torch, UniqueItem.terminus_prison_key, UniqueItem.water_talisman, UniqueItem.earth_talisman, Spell.blood_strike])
        self.assertTrue(self.has_every_spell(self.multiworld.state) and self.multiworld.state.has(UniqueItem.white_tape, self.player))

    def test_if_spell_items_exist(self):
        for spell in [spell.name for spell in all_spells if spell.name not in drop_spells]:
            does_exist = False
            for item in self.multiworld.itempool:
                if item.name == spell:
                    does_exist = True
            self.assertTrue(does_exist, f"The spell {spell} does not exist in the itempool.")


class TestEndingEButDropsanity(LunacidTestBase):
    options = {"ending": "ending_e",
               "dropsanity": "true"}

    def has_spell(self, spell: str, state: CollectionState):
        return state.has(spell, self.player)

    def has_every_spell(self, state: CollectionState) -> bool:
        every_spell = [spell.name for spell in all_spells]

        return state.has_all(every_spell, self.player)

    def test_goal_state(self):
        every_spell = list(set.union(set(item_count_data.base_spells), set(item_count_data.drop_spells)))
        self.assertFalse(self.multiworld.state.can_reach(LunacidRegion.chamber_of_fate, "Region", self.player))
        self.collect_by_name([Weapon.torch, Progressives.vampiric_symbol, UniqueItem.terminus_prison_key, UniqueItem.water_talisman, UniqueItem.earth_talisman])

        self.assertFalse(self.multiworld.state.can_reach(Endings.wake_dreamer, "Location", self.player))
        self.collect_by_name(every_spell)
        self.assertFalse(self.multiworld.state.can_reach(Endings.wake_dreamer, "Location", self.player))
        self.collect_by_name(UniqueItem.white_tape)
        self.assertTrue(self.multiworld.state.can_reach(LunacidRegion.chamber_of_fate, "Region", self.player))
        self.assertTrue(self.multiworld.state.can_reach(Endings.wake_dreamer, "Location", self.player))


class SwitchLockRegionTests(LunacidTestBase):
    options = {"switch_locks": "true"}

    def test_switch_reachability(self):
        state = self.multiworld.state
        player = self.player
        for item in [Weapon.torch, Progressives.vampiric_symbol, UniqueItem.terminus_prison_key, UniqueItem.water_talisman, UniqueItem.earth_talisman]:
            self.collect_by_name(item)
        self.assertFalse(state.can_reach(LunacidRegion.temple_of_silence_interior, "Region", player))
        self.collect_by_name(Switch.temple_switch)
        self.assertTrue(state.can_reach(LunacidRegion.temple_of_silence_interior, "Region", player))
        self.assertFalse(state.can_reach(LunacidRegion.forbidden_archives_3, "Region", player))
        self.collect_by_name(Switch.archives_elevator_switches)
        self.assertTrue(state.can_reach(LunacidRegion.forbidden_archives_3, "Region", player))
        self.assertTrue(state.can_reach(LunacidRegion.fetid_mire, "Region", player))
        self.assertTrue(state.can_reach(LunacidRegion.sanguine_sea, "Region", player))
        self.assertTrue(state.can_reach(LunacidRegion.castle_le_fanu, "Region", player))
        self.assertTrue(state.can_reach(LunacidRegion.castle_le_fanu_white, "Region", player))
        self.assertTrue(state.can_reach(LunacidRegion.throne_chamber, "Region", player))
        self.assertTrue(state.can_reach(LunacidRegion.terminus_prison, "Region", player))
        self.assertFalse(state.can_reach(LunacidRegion.forlorn_arena, "Region", player))
        self.collect_by_name([Switch.prison_arena_switch, Switch.prison_shortcut_switch])
        self.assertTrue(state.can_reach(LunacidRegion.forlorn_arena, "Region", player))
        self.assertTrue(state.can_reach(LunacidRegion.chamber_of_fate, "Region", player))
        self.assertTrue(state.can_reach(LunacidRegion.grave_of_the_sleeper, "Region", player))
        self.assertTrue(self.multiworld.state.can_reach(Endings.wake_dreamer, "Location", self.player))


class SwitchLockRegionTestsEndingE(LunacidTestBase):
    options = {"switch_locks": "true",
               "ending": "ending_e"}

    def test_switch_reachability(self):
        state = self.multiworld.state
        player = self.player
        every_spell = item_count_data.base_spells
        self.collect_by_name([Weapon.torch, Progressives.vampiric_symbol, UniqueItem.terminus_prison_key, UniqueItem.water_talisman, UniqueItem.earth_talisman])
        self.assertFalse(state.can_reach(LunacidRegion.temple_of_silence_interior, "Region", player))
        self.collect_by_name(Switch.temple_switch)
        self.assertTrue(state.can_reach(LunacidRegion.temple_of_silence_interior, "Region", player))
        self.assertFalse(state.can_reach(LunacidRegion.forbidden_archives_3, "Region", player))
        self.collect_by_name(Switch.archives_elevator_switches)
        self.assertTrue(state.can_reach(LunacidRegion.forbidden_archives_3, "Region", player))
        self.assertTrue(state.can_reach(LunacidRegion.fetid_mire, "Region", player))
        self.assertTrue(state.can_reach(LunacidRegion.sanguine_sea, "Region", player))
        self.assertTrue(state.can_reach(LunacidRegion.castle_le_fanu, "Region", player))
        self.assertTrue(state.can_reach(LunacidRegion.castle_le_fanu_white, "Region", player))
        self.assertTrue(state.can_reach(LunacidRegion.throne_chamber, "Region", player))
        self.assertTrue(state.can_reach(LunacidRegion.terminus_prison, "Region", player))
        self.assertFalse(state.can_reach(LunacidRegion.forlorn_arena, "Region", player))
        self.collect_by_name([Switch.prison_arena_switch, Switch.prison_shortcut_switch])
        self.assertTrue(state.can_reach(LunacidRegion.forlorn_arena, "Region", player))
        self.assertTrue(state.can_reach(LunacidRegion.chamber_of_fate, "Region", player))
        self.assertTrue(state.can_reach(LunacidRegion.grave_of_the_sleeper, "Region", player))
        self.collect_by_name(every_spell)
        self.collect_by_name(UniqueItem.white_tape)
        self.collect_by_name(Switch.grotto_valves_switches)
        mob_spell_regions = [LunacidRegion.forlorn_arena, LunacidRegion.castle_le_fanu_red, LunacidRegion.castle_le_fanu_white,
                             LunacidRegion.terminus_prison_dark,
                             LunacidRegion.labyrinth_of_ash, LunacidRegion.boiling_grotto, LunacidRegion.forbidden_archives_3, LunacidRegion.sand_temple,
                             LunacidRegion.temple_of_silence_interior, LunacidRegion.sealed_ballroom]
        for region in mob_spell_regions:
            self.assertTrue(state.can_reach(region, "Region", player), f"Couldn't reach {region}")
        self.assertTrue(self.multiworld.state.can_reach(Endings.wake_dreamer, "Location", self.player))


class DustyTest(LunacidTestBase):
    options = {"secret_door_lock": "true"}

    def test_reachability_criteria(self):
        state = self.multiworld.state
        player = self.player
        self.collect_by_name([Weapon.torch, Progressives.vampiric_symbol, UniqueItem.terminus_prison_key, UniqueItem.water_talisman, UniqueItem.earth_talisman])
        self.assertTrue(state.can_reach(LunacidRegion.temple_of_silence_interior, "Region", player))
        self.assertFalse(state.can_reach(LunacidRegion.temple_of_silence_secret, "Region", player))
        self.assertFalse(state.can_reach(BaseLocation.temple_pillar_room_back_right, "Location", player))
        self.assertFalse(state.can_reach(BaseLocation.archives_hidden_room_upper, "Location", player))
        self.collect_by_name(UniqueItem.dusty_crystal_orb)
        self.assertTrue(state.can_reach(BaseLocation.temple_pillar_room_back_right, "Location", player))
        self.assertTrue(state.can_reach(LunacidRegion.temple_of_silence_secret, "Region", player))
        self.assertTrue(state.can_reach(BaseLocation.archives_hidden_room_upper, "Location", player))


class DustyTestER(LunacidTestBase):
    options = {"secret_door_lock": "true",
               "entrance_randomization": "true"}

    def test_reachability_criteria(self):
        state = self.multiworld.state
        player = self.player
        self.collect_by_name([Weapon.torch, Progressives.vampiric_symbol, UniqueItem.terminus_prison_key, UniqueItem.water_talisman, UniqueItem.earth_talisman])
        self.assertTrue(state.can_reach(LunacidRegion.temple_of_silence_interior, "Region", player))
        self.assertFalse(state.can_reach(LunacidRegion.temple_of_silence_secret, "Region", player))
        self.assertFalse(state.can_reach(BaseLocation.temple_pillar_room_back_right, "Location", player))
        self.assertFalse(state.can_reach(BaseLocation.archives_hidden_room_upper, "Location", player))
        self.collect_by_name(UniqueItem.dusty_crystal_orb)
        self.assertTrue(state.can_reach(BaseLocation.temple_pillar_room_back_right, "Location", player))
        self.assertTrue(state.can_reach(LunacidRegion.temple_of_silence_secret, "Region", player))


class DuplicateTest(LunacidTestBase):
    def test_base_duplicate_weapons(self):
        world = self.multiworld
        for weapon in base_weapons:
            count = 0
            for item in world.itempool:
                if item.name == weapon:
                    count += 1
            self.assertTrue(count < 2, "There are duplicate weapons.")
        for spell in base_spells:
            count = 0
            for item in world.itempool:
                if item.name == spell:
                    count += 1
            self.assertTrue(count < 2, "There are duplicate spells.")


class LightTest(LunacidTestBase):

    def test_base_light_reachability(self):
        self.collect_by_name(UniqueItem.enchanted_key)
        self.assertTrue(self.can_reach_location(BaseLocation.hollow_basin_dark_item))
        self.assertFalse(self.can_reach_region(LunacidRegion.temple_of_silence_entrance))
        self.assertFalse(self.can_reach_region(LunacidRegion.fetid_mire_secret))
        self.assertFalse(self.can_reach_region(LunacidRegion.yosei_forest))


connections_by_name = {connection.name for connection in consistent_entrances}
regions_by_name = {region.name for region in consistent_regions}


class TestRegions(unittest.TestCase):
    def test_region_exits_lead_somewhere(self):
        for region in consistent_regions:
            with self.subTest(region=region):
                for exits in region.exits:
                    self.assertIn(exits, connections_by_name,
                                  f"{region.name} is leading to {exits} but it does not exist.")

    def test_connection_lead_somewhere(self):
        for connection in consistent_entrances:
            with self.subTest(connection=connection):
                self.assertIn(connection.destination, regions_by_name,
                              f"{connection.name} is leading to {connection.destination} but it does not exist.")


def explore_connections_tree_up_to_blockers(blocked_entrances: Set[str]):
    explored_entrances = set()
    explored_regions = set()
    entrances_to_explore = set()
    current_node_name = "Menu"
    current_node = regions_by_name[current_node_name]
    entrances_to_explore.update(current_node.exits)
    while entrances_to_explore:
        current_entrance_name = entrances_to_explore.pop()
        current_entrance = connections_by_name[current_entrance_name]
        current_node_name = current_entrance.destination

        explored_entrances.add(current_entrance_name)
        explored_regions.add(current_node_name)

        if current_entrance_name in blocked_entrances:
            continue

        current_node = regions_by_name[current_node_name]
        entrances_to_explore.update({entrance for entrance in current_node.exits if entrance not in explored_entrances})
    return explored_regions


class TestEntranceRando(LunacidTestCase):
    options = {"entrance_randomization": "true"}

    def entrance_check(self, entrance: str, multiworld: MultiWorld):
        surface_entrance_destination = multiworld.get_entrance(entrance, 1).connected_region.name
        shuffled_connection = multiworld.worlds[1].randomized_entrances[entrance]
        destination = ""
        for connections in consistent_entrances:
            if connections.name == shuffled_connection:
                destination = connections.destination
                break
        self.assertTrue(destination == surface_entrance_destination, destination + " is not " + surface_entrance_destination)

    def check_entrances_are_consistent(self, multiworld: MultiWorld):
        randomized_entrances = [connection.name for connection in consistent_entrances if RandomizationFlag.RANDOMIZED in connection.flag]
        for entrance in randomized_entrances:
            self.entrance_check(entrance, multiworld)

    def test_entrances_of_several_games(self):
        option_dict = {
            Options.EntranceRandomization.internal_name: Options.EntranceRandomization.option_true
        }
        for i in range(100):
            seed = int(random() * pow(10, 18) - 1)
            with self.subTest(f"Seed: {seed}"):
                print(f"Seed: {seed}")
                multiworld = setup_solo_multiworld(option_dict, seed)
                self.check_entrances_are_consistent(multiworld)


class CheckTowerExclusion(LunacidTestBase):
    options = {"exclude_tower": "true"}

    def test_no_items_or_locations_from_tower(self):
        for location in self.multiworld.get_locations(1):
            self.assertFalse(location.name in BaseLocation.abyss_locations)
        for item in self.multiworld.get_items():
            self.assertFalse(item.name in [Weapon.moonlight, UniqueItem.crystal_lantern])


class CheckCoinExclusion(LunacidTestBase):
    options = {"exclude_coin_locations": "true"}

    def test_no_items_or_locations_from_coins(self):
        for location in self.multiworld.get_locations(1):
            self.assertFalse(location.name in BaseLocation.coin_locations)
        for item in self.multiworld.get_items():
            self.assertFalse(item.name == Coins.strange_coin)


class AnyEndingTests(LunacidTestBase):
    options = {"ending": "any_ending",
               "required_strange_coin": 20}

    def has_coins_for_door(self, state: CollectionState):
        return state.has(Coins.strange_coin, self.player, 20)

    def can_reach_any_region(self, state: CollectionState, spots: List[str]):
        any_rule = False
        for spot in spots:
            any_rule = any_rule or state.can_reach_region(spot, self.player)
        return any_rule

    def can_win(self, state: CollectionState):
        win_condition = state.can_reach_region(LunacidRegion.grave_of_the_sleeper, self.player) or (self.has_coins_for_door(state) and
        state.can_reach_region(LunacidRegion.labyrinth_of_ash, self.player))
        return win_condition

    def test_necessity_of_coins_or_talismans(self):
        state = self.multiworld.state
        self.assertFalse(self.can_reach_region(LunacidRegion.grave_of_the_sleeper))
        self.assertFalse(self.can_win(state))
        self.assertFalse(self.can_reach_region(LunacidRegion.labyrinth_of_ash))
        self.collect_by_name([Weapon.torch, UniqueItem.enchanted_key, Progressives.vampiric_symbol, Progressives.vampiric_symbol, Progressives.vampiric_symbol])
        self.assertFalse(self.can_reach_region(LunacidRegion.grave_of_the_sleeper))
        self.assertTrue(self.can_reach_region(LunacidRegion.labyrinth_of_ash))
        self.assertFalse(self.can_win(state))
        self.collect_by_name(UniqueItem.terminus_prison_key)
        self.assertFalse(self.can_win(state))
        self.collect_by_name([UniqueItem.water_talisman, UniqueItem.earth_talisman])
        self.assertTrue(self.can_win(state))
        self.remove_by_name([UniqueItem.water_talisman, UniqueItem.earth_talisman])
        self.collect_by_name([Coins.strange_coin] * 20)
        self.assertTrue(self.can_win(state))

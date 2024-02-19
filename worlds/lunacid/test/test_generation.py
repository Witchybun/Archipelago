import unittest

from BaseClasses import ItemClassification, MultiWorld
from test.general import setup_solo_multiworld
from . import LunacidTestBase
from .. import Items, LunacidWorld
from ..Options import Shopsanity, SwitchLocks
from ..data.location_data import *

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
        self.assertTrue(225 == len(base_locations), "Location count mismatch.")


class ReachTestsBase(LunacidTestBase):

    def test_enchanted_key_case(self):
        canopy_names = [location.name for location in forest_canopy]
        self.assertAccessDependency(canopy_names, [[UniqueItem.enchanted_key]])

    def test_library(self):
        archives = [location.name for location in forbidden_archives]
        self.assertAccessDependency(archives, [[Spell.rock_bridge, Spell.coffin], [Spell.icarian_flight, Progressives.vampiric_symbol, Progressives.vampiric_symbol]], True)


class ReachTestsShops(LunacidTestBase):
    options = {"shopsanity": True}

    def test_enchanted_key_case(self):
        base_location_names = [location.name for location in base_locations if location not in forbidden_archives]
        locations_before_key = [BaseLocation.wings_rest_crystal_shard,
                                BaseLocation.wings_rest_ocean_elixir,
                                BaseLocation.wings_rest_clives_gift,

                                BaseLocation.hollow_basin_starting_sword,
                                BaseLocation.hollow_basin_right_water_right,
                                BaseLocation.hollow_basin_right_water_left,
                                BaseLocation.hollow_basin_left_water,
                                BaseLocation.hollow_basin_demi_chest,
                                BaseLocation.hollow_basin_enchanted_door,
                                BaseLocation.hollow_basin_dark_item,
                                BaseLocation.surface_demi_gift,
                                BaseLocation.chasm_hidden_chest,
                                BaseLocation.chasm_invisible_cliffside]
        locations_before_keys = [location for location in base_location_names if location not in locations_before_key]
        self.assertAccessDependency(locations_before_keys, [[UniqueItem.enchanted_key]])

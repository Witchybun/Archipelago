from BaseClasses import CollectionState
from . import LunacidTestBase
from .. import Endings
from ..data import item_count_data
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
        self.assertTrue(206 == len(base_locations), f"Location count mismatch, got {len(base_locations)}.")


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
        return state.has_all(every_spell, self.player) & self.can_reach_all_regions(self.multiworld.state, mob_spell_regions)

    def test_if_goal_can_be_true(self):
        self.collect_by_name([spell for spell in item_count_data.base_spells])
        self.collect_by_name([UniqueItem.white_tape])
        symbol = self.get_item_by_name("Progressive Vampiric Symbol")
        self.collect([symbol, symbol, symbol])
        self.collect_by_name([Weapon.torch, UniqueItem.terminus_prison_key, UniqueItem.water_talisman, UniqueItem.earth_talisman, Spell.blood_strike])
        self.assertTrue(self.has_every_spell(self.multiworld.state) & self.multiworld.state.has(UniqueItem.white_tape, self.player))

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
    options = {"switchlocks": "true"}

    def test_switch_reachability(self):
        state = self.multiworld.state
        player = self.player
        self.collect_by_name([Weapon.torch, Progressives.vampiric_symbol, UniqueItem.terminus_prison_key, UniqueItem.water_talisman, UniqueItem.earth_talisman])
        self.assertFalse(state.can_reach(LunacidRegion.temple_of_silence_interior, "Region", player))
        self.collect_by_name(Switch.temple_switch)
        self.assertTrue(state.can_reach(LunacidRegion.temple_of_silence_interior, "Region", player))
        self.assertFalse(state.can_reach(LunacidRegion.forbidden_archives_3, "Region", player))
        self.collect_by_name(Switch.archives_elevator_switch_2_to_3)
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
    options = {"switchlocks": "true",
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
        self.collect_by_name(Switch.archives_elevator_switch_2_to_3)
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
        self.collect_by_name([Switch.grotto_valve_switch_2, Switch.grotto_valve_switch_1])
        mob_spell_regions = [LunacidRegion.forlorn_arena, LunacidRegion.castle_le_fanu_red, LunacidRegion.castle_le_fanu_white,
                             LunacidRegion.terminus_prison_dark,
                             LunacidRegion.labyrinth_of_ash, LunacidRegion.boiling_grotto, LunacidRegion.forbidden_archives_3, LunacidRegion.sand_temple,
                             LunacidRegion.temple_of_silence_interior, LunacidRegion.sealed_ballroom]
        for region in mob_spell_regions:
            self.assertTrue(state.can_reach(region, "Region", player), f"Couldn't reach {region}")
        self.assertTrue(self.multiworld.state.can_reach(Endings.wake_dreamer, "Location", self.player))

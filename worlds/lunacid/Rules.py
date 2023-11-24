from dataclasses import dataclass
from BaseClasses import CollectionState
from ..generic.Rules import set_rule

from .data.spell_data import all_spells, spell_drop_locations, light_spells, blood_spells, spell_light_sources, jump_spells
from .data.weapon_data import light_weapons, ranged_weapons, weapon_light_sources
from .data.item_data import item_light_sources
from .strings.regions_entrances import LunacidEntrance
from .strings.spells import Spell
from .strings.items import UniqueItem
from .strings.locations import BaseLocation
from .Options import LunacidOptions


@dataclass(frozen=True, repr=False)
class LunacidLogic:
    player: int
    options: LunacidOptions

    def can_jump_high(self, state: CollectionState, player: int):
        return state.has_any(jump_spells, player)

    def has_light_source(self, state: CollectionState, player: int):
        return state.has_any(spell_light_sources + weapon_light_sources + item_light_sources, player)

    def can_reach_spell_drop(self, state: CollectionState, drop: str):
        drop_locations = spell_drop_locations[drop]
        drop_rule = True
        for locations in drop_locations:
            drop_rule += state.can_reach(locations)
        return drop_rule

    def can_reach_every_spell_drop_region(self, state: CollectionState):
        drop_rule = True
        for drop in spell_drop_locations:
            drop_rule += self.can_reach_spell_drop(state, drop)
        return drop_rule

    def has_every_spell(self, state: CollectionState, player: int):
        return state.has_all({spell.name for spell in all_spells}, player) & self.can_reach_every_spell_drop_region(state)

    def has_light_element_access(self, state: CollectionState, player: int):
        return state.has_any(light_spells + light_weapons, player)

    def has_blood_spell_access(self, state: CollectionState, player: int):
        return state.has_any(blood_spells, player)

    def define_entrance_rules(self, state, player: int):
        entrance_rules = {}
        entrance_rules.update({
            LunacidEntrance.basin_to_archives: self.can_jump_high(state, player),
            LunacidEntrance.wings_to_surface: state.has(Spell.icarian_flight, player),
            LunacidEntrance.basin_to_surface: state.has(Spell.icarian_flight, player),
            LunacidEntrance.basin_to_temple: self.has_light_source(state, player),
            LunacidEntrance.temple_to_forest: self.has_light_source(state, player),
            LunacidEntrance.temple_to_mire: self.has_light_source(state, player),
            LunacidEntrance.tomb_to_mausoleum: state.has_any(light_spells + light_weapons, player) & self.has_light_source(state, player),
            LunacidEntrance.yosei_to_yosei_lower: state.has_any(blood_spells, player) | self.can_jump_high(state, player),
            LunacidEntrance.yosei_to_canopy: state.has(UniqueItem.enchanted_key, player),
            LunacidEntrance.archives_to_chasm: state.has(UniqueItem.vampiric_symbol_a, player),
            LunacidEntrance.white_to_throne: state.has(UniqueItem.vampiric_symbol_e, player),
            LunacidEntrance.throne_to_prison: state.can_reach("Defeat Prince Crilall Fanu", None, player),
            LunacidEntrance.castle_to_red: self.has_blood_spell_access(state, player),
            LunacidEntrance.castle_to_white: state.has(UniqueItem.vampiric_symbol_w, player),
            LunacidEntrance.white_to_blue: state.has(UniqueItem.vampiric_symbol_a, player),
            LunacidEntrance.arena_to_fate: state.has_all({UniqueItem.water_talisman, UniqueItem.earth_talisman}, player)
        })
        entrance_names = entrance_rules.keys()
        return entrance_rules, entrance_names

    def define_location_rules(self, state, player: int):
        location_rules = {}
        location_rules.update({
            BaseLocation.sea_pillar: self.can_jump_high(state, player),
            BaseLocation.tomb_demi_chest: self.can_jump_high(state, player),
            BaseLocation.catacombs_hidden_room: self.has_light_element_access(state, player),
            BaseLocation.catacombs_deep_coffin_storage: self.has_light_element_access(state, player),
            BaseLocation.catacombs_restore_vampire: self.has_light_element_access(state, player),
            BaseLocation.mausoleum_upper_table: self.can_jump_high(state, player),
            BaseLocation.corrupted_room: state.has(UniqueItem.corrupted_key, player),
            BaseLocation.yosei_hanging_in_trees: state.has_any(ranged_weapons, player),
            BaseLocation.castle_upper_floor_coffin_double: state.has(UniqueItem.vampiric_symbol_e, player),
            BaseLocation.prison_f3_bottomless_pit: state.has_any({Spell.icarian_flight, Spell.spirit_warp}, player),
            BaseLocation.sand_chest_overlooking_crypt: self.can_jump_high(state, player),
            BaseLocation.arena_water_underwater_temple: self.can_jump_high(state, player),
            BaseLocation.arena_earth_earthen_temple: self.can_jump_high(state, player)
        })
        location_names = location_rules.keys()
        return location_rules, location_names


def rules(lunacidworld):
    world = lunacidworld.multiworld
    player = lunacidworld.player
    logic = LunacidLogic
    entrance_rules, entrance_names = lambda state: logic.define_entrance_rules(world, state, player)
    location_rules, location_names = lambda state: logic.define_location_rules(world, state, player)
    for entrance in entrance_names:
        set_rule(world.get_entrance(entrance, player), entrance_rules[entrance])
    for location in location_names:
        set_rule(world.get_location(location, player), location_rules[location])

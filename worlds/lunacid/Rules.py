from typing import Dict, List, Set
from worlds.generic.Rules import set_rule, add_rule
from BaseClasses import CollectionState

from .data.spell_data import all_spells, spell_drop_locations, light_spells, blood_spells, spell_light_sources, jump_spells
from .data.weapon_data import light_weapons, ranged_weapons, weapon_light_sources
from .data.item_data import item_light_sources
from .strings.regions_entrances import Entrance
from .strings.spells import Spell
from .strings.items import UniqueItem, GenericItem
from .strings.locations import Location


def can_jump_high(state: CollectionState, player: int):
    return state.has_any(jump_spells, player)


def has_light_source(state: CollectionState, player: int):
    return state.has_any(spell_light_sources + weapon_light_sources + item_light_sources, player)


def can_reach_spell_drop(state: CollectionState, drop: str):
    drop_locations = spell_drop_locations[drop]
    drop_rule = True
    for locations in drop_locations:
        drop_rule += state.can_reach(locations)
    return drop_rule


def can_reach_every_spell_drop_region(state: CollectionState):
    drop_rule = True
    for drop in spell_drop_locations:
        drop_rule += can_reach_spell_drop(state, drop)
    return drop_rule


def has_every_spell(state: CollectionState, player: int):
    return state.has_all({spell.name for spell in all_spells}, player) & can_reach_every_spell_drop_region(state)


def has_light_element_access(state: CollectionState, player: int):
    return state.has_any(light_spells + light_weapons, player)


def has_blood_spell_access(state: CollectionState, player: int):
    return state.has_any(blood_spells, player)


def define_entrance_rules(state: CollectionState, player: int):
    entrance_rules = {}
    entrance_rules.update({
        Entrance.basin_to_archives: can_jump_high(state, player),
        Entrance.wings_to_surface: state.has(Spell.icarian_flight, player),
        Entrance.basin_to_surface: state.has(Spell.icarian_flight, player),
        Entrance.basin_to_temple: has_light_source(state, player),
        Entrance.temple_to_forest: has_light_source(state, player),
        Entrance.temple_to_mire: has_light_source(state, player),
        Entrance.tomb_to_mausoleum: state.has_any(light_spells + light_weapons, player) & has_light_source(state, player),
        Entrance.yosei_to_yosei_lower: state.has_any(blood_spells, player) | can_jump_high(state, player),
        Entrance.yosei_to_canopy: state.has(GenericItem.enchanted_key, player),
        Entrance.archives_to_chasm: state.has(UniqueItem.vampiric_symbol_a, player),
        Entrance.white_to_throne: state.has(UniqueItem.vampiric_symbol_e, player),
        Entrance.castle_to_red: has_blood_spell_access(state, player),
        Entrance.castle_to_white: state.has(UniqueItem.vampiric_symbol_w, player),
        Entrance.white_to_blue: state.has(UniqueItem.vampiric_symbol_a, player),
    })
    return entrance_rules


def define_location_rules(state: CollectionState, player: int):
    location_rules = {}
    location_rules.update({
        Location.sea_pillar: can_jump_high(state, player),
        Location.tomb_demi_chest: can_jump_high(state, player),
        Location.catacombs_hidden_room: has_light_element_access(state, player),
        Location.catacombs_deep_coffin_storage: has_light_element_access(state, player),
        Location.catacombs_restore_vampire: has_light_element_access(state, player),
        Location.mausoleum_upper_table: can_jump_high(state, player),
        Location.corrupted_room: state.has(UniqueItem.corrupted_key, player),
        Location.yosei_hanging_in_trees: state.has_any(ranged_weapons, player),
        Location.castle_upper_floor_coffin_double: state.has(UniqueItem.vampiric_symbol_e, player),
        Location.prison_f3_bottomless_pit: state.has_any({Spell.icarian_flight, Spell.spirit_warp}, player),
        Location.sand_chest_overlooking_crypt: can_jump_high(state, player),

    })
    return location_rules

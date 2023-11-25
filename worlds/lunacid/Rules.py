from BaseClasses import CollectionState
from typing import Dict, List, Tuple
from ..generic.Rules import set_rule

from .data.spell_data import all_spells, spell_drop_locations, light_spells, blood_spells, spell_light_sources, jump_spells
from .data.weapon_data import light_weapons, ranged_weapons, weapon_light_sources
from .data.item_data import item_light_sources
from .strings.regions_entrances import LunacidEntrance
from .strings.spells import Spell
from .strings.items import UniqueItem
from .strings.locations import BaseLocation
from .Options import LunacidOptions

all_light_sources = spell_light_sources + weapon_light_sources + item_light_sources


def can_jump_high(state: CollectionState, player: int) -> bool:
    return state.has_any(jump_spells, player)


def has_light_source(state: CollectionState, player: int) -> bool:
    return state.has_any(spell_light_sources + weapon_light_sources + item_light_sources, player)


def can_reach_spell_drop(state: CollectionState, drop: str) -> bool:
    drop_locations = spell_drop_locations[drop]
    drop_rule = True
    for locations in drop_locations:
        drop_rule += state.can_reach(locations)
    return drop_rule


def can_reach_every_spell_drop_region(state: CollectionState) -> bool:
    drop_rule = True
    for drop in spell_drop_locations:
        drop_rule += can_reach_spell_drop(state, drop)
    return drop_rule


def has_every_spell(state: CollectionState, player: int) -> bool:
    return state.has_all({spell.name for spell in all_spells}, player) & can_reach_every_spell_drop_region(state)


def has_light_element_access(state: CollectionState, player: int) -> bool:
    return state.has_any(light_spells + light_weapons, player)


def has_blood_spell_access(state: CollectionState, player: int) -> bool:
    return state.has_any(blood_spells, player)


def define_entrance_rules(self, player: int) -> Tuple[Dict[str, bool], List[str]]:
    entrance_rules = {}
    entrance_rules.update({
        LunacidEntrance.wings_to_surface: lambda state: state.has(Spell.icarian_flight, player),
        LunacidEntrance.basin_to_surface: lambda state: state.has(Spell.icarian_flight, player),
        LunacidEntrance.basin_to_temple: lambda state: self.has_light_source(state, player),
        LunacidEntrance.temple_to_forest: lambda state: self.has_light_source(state, player),
        LunacidEntrance.temple_to_mire: lambda state: self.has_light_source(state, player),
        LunacidEntrance.tomb_to_mausoleum: lambda state: state.has_any(light_spells + light_weapons, player) & self.has_light_source(state, player),
        LunacidEntrance.yosei_to_yosei_lower: lambda state: state.has_any(blood_spells, player) | can_jump_high(state, player),
        LunacidEntrance.yosei_to_canopy: lambda state: state.has(UniqueItem.enchanted_key, player),
        LunacidEntrance.archives_to_chasm: lambda state: state.has(UniqueItem.vampiric_symbol_a, player),
        LunacidEntrance.white_to_throne: lambda state: state.has(UniqueItem.vampiric_symbol_e, player),
        LunacidEntrance.throne_to_prison: lambda state: state.can_reach("Defeat Prince Crilall Fanu", None, player),
        LunacidEntrance.castle_to_red: lambda state: self.has_blood_spell_access(state, player),
        LunacidEntrance.castle_to_white: lambda state: state.has(UniqueItem.vampiric_symbol_w, player),
        LunacidEntrance.white_to_blue: lambda state: state.has(UniqueItem.vampiric_symbol_a, player),
        LunacidEntrance.arena_to_fate: lambda state: state.has_all({UniqueItem.water_talisman, UniqueItem.earth_talisman}, player)
    })
    entrance_names = [entrance for entrance in entrance_rules]
    return entrance_rules, entrance_names


def define_location_rules(self, player: int) -> Tuple[Dict[str, bool], List[str]]:
    location_rules = {}
    location_rules.update({
        BaseLocation.sea_pillar: lambda state: can_jump_high(state, player),
        BaseLocation.tomb_demi_chest: lambda state: can_jump_high(state, player),
        BaseLocation.catacombs_hidden_room: lambda state: self.has_light_element_access(state, player),
        BaseLocation.catacombs_deep_coffin_storage: lambda state: self.has_light_element_access(state, player),
        BaseLocation.catacombs_restore_vampire: lambda state: self.has_light_element_access(state, player),
        BaseLocation.mausoleum_upper_table: lambda state: can_jump_high(state, player),
        BaseLocation.corrupted_room: lambda state: state.has(UniqueItem.corrupted_key, player),
        BaseLocation.yosei_hanging_in_trees: lambda state: state.has_any(ranged_weapons, player),
        BaseLocation.castle_upper_floor_coffin_double: lambda state: state.has(UniqueItem.vampiric_symbol_e, player),
        BaseLocation.prison_f3_bottomless_pit: lambda state: state.has_any({Spell.icarian_flight, Spell.spirit_warp}, player),
        BaseLocation.sand_chest_overlooking_crypt: lambda state: can_jump_high(state, player),
        BaseLocation.arena_water_underwater_temple: lambda state: can_jump_high(state, player),
        BaseLocation.arena_earth_earthen_temple: lambda state: can_jump_high(state, player)
    })
    location_names = [location for location in location_rules]
    return location_rules, location_names


def set_rules(game_world):
    world = game_world.multiworld
    player = game_world.player
    set_rule(world.get_entrance(LunacidEntrance.basin_to_archives, player),
             lambda state: can_jump_high(state, player))
    set_rule(world.get_entrance(LunacidEntrance.wings_to_surface, player),
             lambda state: state.has(Spell.icarian_flight, player))
    set_rule(world.get_entrance(LunacidEntrance.basin_to_surface, player),
             lambda state: state.has(Spell.icarian_flight, player))
    set_rule(world.get_entrance(LunacidEntrance.basin_to_temple, player),
             lambda state: has_light_source(state, player))
    set_rule(world.get_entrance(LunacidEntrance.temple_to_forest, player),
             lambda state: has_light_source(state, player))
    set_rule(world.get_entrance(LunacidEntrance.temple_to_mire, player),
             lambda state: has_light_source(state, player))
    set_rule(world.get_entrance(LunacidEntrance.tomb_to_mausoleum, player),
             lambda state: state.has_any(light_spells + light_weapons, player) and has_light_source(state, player))
    set_rule(world.get_entrance(LunacidEntrance.yosei_to_yosei_lower, player),
             lambda state: state.has_any(blood_spells, player) or can_jump_high(state, player))
    set_rule(world.get_entrance(LunacidEntrance.yosei_to_canopy, player),
             lambda state: state.has(UniqueItem.enchanted_key, player))
    set_rule(world.get_entrance(LunacidEntrance.archives_to_chasm, player),
             lambda state: state.has(UniqueItem.vampiric_symbol_a, player))
    set_rule(world.get_entrance(LunacidEntrance.white_to_throne, player),
             lambda state: state.has(UniqueItem.vampiric_symbol_e, player))
    set_rule(world.get_entrance(LunacidEntrance.throne_to_prison, player),
             lambda state: state.has("Defeat Prince Crilall Fanu", player))
    set_rule(world.get_entrance(LunacidEntrance.castle_to_red, player),
             lambda state: has_blood_spell_access(state, player))
    set_rule(world.get_entrance(LunacidEntrance.castle_to_white, player),
             lambda state: state.has(UniqueItem.vampiric_symbol_w, player))
    set_rule(world.get_entrance(LunacidEntrance.white_to_blue, player),
             lambda state: state.has(UniqueItem.vampiric_symbol_a, player))
    set_rule(world.get_entrance(LunacidEntrance.arena_to_fate, player),
             lambda state: state.has_all({UniqueItem.water_talisman, UniqueItem.earth_talisman}, player))

    set_rule(world.get_location(BaseLocation.sea_pillar, player),
             lambda state: can_jump_high(state, player))
    set_rule(world.get_location(BaseLocation.tomb_demi_chest, player),
             lambda state: can_jump_high(state, player))
    set_rule(world.get_location(BaseLocation.catacombs_hidden_room, player),
             lambda state: has_light_element_access(state, player))
    set_rule(world.get_location(BaseLocation.catacombs_deep_coffin_storage, player),
             lambda state: has_light_element_access(state, player))
    set_rule(world.get_location(BaseLocation.catacombs_restore_vampire, player),
             lambda state: has_light_element_access(state, player))
    set_rule(world.get_location(BaseLocation.mausoleum_upper_table, player),
             lambda state: can_jump_high(state, player))
    set_rule(world.get_location(BaseLocation.corrupted_room, player),
             lambda state: state.has(UniqueItem.corrupted_key, player))
    set_rule(world.get_location(BaseLocation.yosei_hanging_in_trees, player),
             lambda state: state.has_any(ranged_weapons, player))
    set_rule(world.get_location(BaseLocation.castle_upper_floor_coffin_double, player),
             lambda state: state.has(UniqueItem.vampiric_symbol_e, player))
    set_rule(world.get_location(BaseLocation.prison_f3_bottomless_pit, player),
             lambda state: state.has_any({Spell.icarian_flight, Spell.spirit_warp}, player))
    set_rule(world.get_location(BaseLocation.throne_book, player),
             lambda state: state.has("Defeat Prince Crilall Fanu", player))
    set_rule(world.get_location(BaseLocation.sand_chest_overlooking_crypt, player),
             lambda state: can_jump_high(state, player))
    set_rule(world.get_location(BaseLocation.arena_water_underwater_temple, player),
             lambda state: can_jump_high(state, player))
    set_rule(world.get_location(BaseLocation.arena_earth_earthen_temple, player),
             lambda state: can_jump_high(state, player))

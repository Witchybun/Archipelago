from typing import Dict, List, Set
from worlds.generic.Rules import set_rule, add_rule
from BaseClasses import CollectionState

from .data.spell_data import all_spells
from .strings.regions_entrances import Entrance
from .strings.spells import Spell
from .strings.locations import Location


def can_jump_high(state: CollectionState, player: int):
    return state.has_any({Spell.coffin, Spell.icarian_flight}, player)


def can_reach_every_spell_drop_region(state: CollectionState, player: int):
    region_rule = state.can_reach(Location.hollow_basin_left_water)
    return region_rule


def has_every_spell(state: CollectionState, player: int):
    return state.has_all({spell.name for spell in all_spells}, player) & can_reach_every_spell_drop_region(state, player)


def define_entrance_rules(state: CollectionState, player: int):
    entrance_rules = {}
    entrance_rules.update({
        Entrance.basin_to_archives: can_jump_high(state, player)

    })
    return entrance_rules


def define_location_rules(state: CollectionState, player: int):
    location_rules = {}
    return location_rules

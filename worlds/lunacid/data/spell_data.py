from dataclasses import dataclass
from typing import List, Dict
from BaseClasses import ItemClassification

from .game_item import GameItem
from ..strings.properties import Types, Elements
from ..strings.spells import Spell, MobSpell


@dataclass(frozen=True)
class SpellInfo:
    name: str
    element: str
    style: str

    def __repr__(self):
        return f"{self.name} (Classification: {self.classification})"


all_spells: List[SpellInfo] = []


def spell_information(name: str, element: str, style: str):
    spell = SpellInfo(name, element, style)
    all_spells.append(spell)
    return spell


base_spells = [
    spell_information(Spell.barrier, Elements.normal, Types.support),
    spell_information(Spell.bestial_communion, Elements.dark, Types.support),
    spell_information(Spell.blood_drain, Elements.ignore, Types.melee),
    spell_information(Spell.blood_strike, Elements.poison, Types.ranged),
    spell_information(Spell.blue_flame_arc, Elements.fire, Types.melee),
    spell_information(Spell.coffin, Elements.ignore, Types.support),
    spell_information(Spell.corpse_transformation, Elements.dark, Types.support),
    spell_information(Spell.earth_strike, Elements.normal, Types.ranged),
    spell_information(Spell.earth_thorn, Elements.normal, Types.melee),
    spell_information(Spell.fire_worm, Elements.fire, Types.melee),
    spell_information(Spell.flame_flare, Elements.fire, Types.support),
    spell_information(Spell.flame_spear, Elements.fire, Types.ranged),
    spell_information(Spell.ghost_light, Elements.light, Types.support),
    spell_information(Spell.holy_warmth, Elements.light, Types.support),
    spell_information(Spell.icarian_flight, Elements.normal, Types.support),
    spell_information(Spell.ice_spear, Elements.ice, Types.ranged),
    spell_information(Spell.ice_tear, Elements.ice, Types.melee),
    spell_information(Spell.ignis_calor, Elements.fire, Types.melee),
    spell_information(Spell.lava_chasm, Elements.fire, Types.melee),
    spell_information(Spell.light_reveal, Elements.light, Types.support),
    spell_information(Spell.lightning, Elements.light, Types.ranged),
    spell_information(Spell.lithomancy, Elements.ignore, Types.support),
    spell_information(Spell.moon_beam, Elements.light, Types.ranged),
    spell_information(Spell.poison_mist, Elements.poison, Types.melee),
    spell_information(Spell.rock_bridge, Elements.normal, Types.support),
    spell_information(Spell.slime_orb, Elements.poison, Types.ranged),
    spell_information(Spell.spirit_warp, Elements.light, Types.support),
    spell_information(Spell.summon_fairy, Elements.light, Types.support),
    spell_information(Spell.summon_ice_sword, Elements.ice, Types.support),
    spell_information(Spell.wind_dash, Elements.normal, Types.support),
    spell_information(Spell.wind_slicer, Elements.normal, Types.ranged),
    spell_information(Spell.jingle_bells, Elements.fire, Types.melee),
]

drop_spells = [
    spell_information(MobSpell.summon_snail, Elements.normal, Types.support),
    spell_information(MobSpell.dark_skull, Elements.dark, Types.ranged),
    spell_information(MobSpell.summon_kodama, Elements.light, Types.support),
    spell_information(MobSpell.tornado, Elements.normal, Types.melee),
    spell_information(MobSpell.quick_stride, Elements.normal, Types.support),
]


spells_by_element = {spell.name: spell.element for spell in all_spells}
ranged_spells = [spell.name for spell in all_spells if spell.style == Types.ranged]
support_spells = [spell.name for spell in all_spells if spell.style == Types.support]
blood_spells = [Spell.blood_drain, Spell.blood_strike]
spell_light_sources = [Spell.flame_flare, Spell.ghost_light]

drop_spells = [MobSpell.summon_snail, MobSpell.dark_skull, MobSpell.summon_kodama, MobSpell.tornado, MobSpell.quick_stride]



all_spells_by_name: Dict[str, SpellItem] = {spell.name: spell for spell in all_spells}

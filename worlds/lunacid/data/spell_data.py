from dataclasses import dataclass
from typing import List, Dict
from BaseClasses import ItemClassification

from .game_item import GameItem
from ..strings.properties import Types, Elements
from ..strings.spells import Spell, MobSpell


@dataclass(frozen=True)
class SpellItem(GameItem):
    code: int
    name: str
    element: str
    style: str
    classification: ItemClassification

    def __repr__(self):
        return f"{self.name} (Classification: {self.classification})"


all_spells: List[SpellItem] = []


def create_spell(code: int, name: str, element: str, style: str, classification: ItemClassification):
    spell = SpellItem(name, code, element, style,  classification)
    all_spells.append(spell)
    return spell


barrier = create_spell(140, Spell.barrier, Elements.normal, Types.support, ItemClassification.progression)
bestial_communion = create_spell(141, Spell.bestial_communion, Elements.dark, Types.support, ItemClassification.useful)
blood_drain = create_spell(142, Spell.blood_drain, Elements.ignore, Types.melee, ItemClassification.progression)
blood_strike = create_spell(143, Spell.blood_strike, Elements.poison, Types.ranged, ItemClassification.progression)
blue_flame_arc = create_spell(144, Spell.blue_flame_arc, Elements.fire, Types.melee, ItemClassification.useful)
coffin = create_spell(145, Spell.coffin, Elements.ignore, Types.support, ItemClassification.progression)
corpse_transformation = create_spell(146, Spell.corpse_transformation, Elements.dark, Types.support, ItemClassification.useful)
earth_strike = create_spell(147, Spell.earth_strike, Elements.normal, Types.ranged, ItemClassification.useful)
earth_thorn = create_spell(148, Spell.earth_thorn, Elements.normal, Types.melee, ItemClassification.useful)
fire_worm = create_spell(149, Spell.fire_worm, Elements.fire, Types.melee, ItemClassification.useful)
flame_flare = create_spell(150, Spell.flame_flare, Elements.fire, Types.support, ItemClassification.useful)
flame_spear = create_spell(151, Spell.flame_spear, Elements.fire, Types.ranged, ItemClassification.useful)
ghost_light = create_spell(152, Spell.ghost_light, Elements.light, Types.support, ItemClassification.progression)
holy_warmth = create_spell(153, Spell.holy_warmth, Elements.light, Types.support, ItemClassification.useful)
icarian_flight = create_spell(154, Spell.icarian_flight, Elements.normal, Types.support, ItemClassification.progression)
ice_spear = create_spell(155, Spell.ice_spear, Elements.ice, Types.ranged, ItemClassification.useful)
ice_tear = create_spell(156, Spell.ice_tear, Elements.ice, Types.melee, ItemClassification.useful)
ignis_calor = create_spell(157, Spell.ignis_calor, Elements.fire, Types.melee, ItemClassification.progression)
lava_chasm = create_spell(158, Spell.lava_chasm, Elements.fire, Types.melee, ItemClassification.useful)
light_reveal = create_spell(159, Spell.light_reveal, Elements.light, Types.support, ItemClassification.useful)
lightning = create_spell(160, Spell.lightning, Elements.light, Types.ranged, ItemClassification.useful)
lithomancy = create_spell(161, Spell.lithomancy, Elements.ignore, Types.support, ItemClassification.useful)
moon_beam = create_spell(162, Spell.moon_beam, Elements.light, Types.ranged, ItemClassification.useful)
poison_mist = create_spell(163, Spell.poison_mist, Elements.poison, Types.melee, ItemClassification.useful)
rock_bridge = create_spell(164, Spell.rock_bridge, Elements.normal, Types.support, ItemClassification.progression)
slime_orb = create_spell(165, Spell.slime_orb, Elements.poison, Types.ranged, ItemClassification.useful)
spirit_warp = create_spell(166, Spell.spirit_warp, Elements.light, Types.support, ItemClassification.progression)
summon_fairy = create_spell(167, Spell.summon_fairy, Elements.light, Types.support, ItemClassification.useful)
summon_ice_sword = create_spell(168, Spell.summon_ice_sword, Elements.ice, Types.support, ItemClassification.useful)
wind_dash = create_spell(169, Spell.wind_dash, Elements.normal, Types.support, ItemClassification.useful)
wind_slicer = create_spell(170, Spell.wind_slicer, Elements.normal, Types.ranged, ItemClassification.useful)

summon_snail = create_spell(171, MobSpell.summon_snail, Elements.normal, Types.support, ItemClassification.useful)
dark_skull = create_spell(172, MobSpell.dark_skull, Elements.dark, Types.ranged, ItemClassification.useful)
summon_kodama = create_spell(173, MobSpell.summon_kodama, Elements.light, Types.support, ItemClassification.useful)
tornado = create_spell(174, MobSpell.tornado, Elements.normal, Types.melee, ItemClassification.useful)
quick_stride = create_spell(175, MobSpell.quick_stride, Elements.normal, Types.support, ItemClassification.useful)

jingle_bells = create_spell(176, Spell.jingle_bells, Elements.fire, Types.melee, ItemClassification.useful)

spells_by_element = {spell.name: spell.element for spell in all_spells}
ranged_spells = [spell.name for spell in all_spells if spell.style == Types.ranged]
support_spells = [spell.name for spell in all_spells if spell.style == Types.support]
blood_spells = [blood_drain.name, blood_strike.name]
spell_light_sources = [Spell.flame_flare, Spell.ghost_light]
jump_spells = [Spell.icarian_flight, Spell.rock_bridge, Spell.barrier]

drop_spells = [MobSpell.summon_snail, MobSpell.dark_skull, MobSpell.summon_kodama, MobSpell.tornado, MobSpell.quick_stride]

starting_spells = [Spell.flame_spear, Spell.ice_spear, Spell.wind_slicer, Spell.slime_orb, Spell.earth_strike]
drop_starting_spells = [MobSpell.dark_skull]

all_spells_by_name: Dict[str, SpellItem] = {spell.name: spell for spell in all_spells}

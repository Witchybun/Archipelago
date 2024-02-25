from dataclasses import dataclass
from typing import List, Dict
from BaseClasses import ItemClassification

from .game_item import GameItem
from ..strings.spells import Spell, MobSpell
from ..strings.locations import BaseLocation


@dataclass(frozen=True)
class SpellItem(GameItem):
    code: int
    name: str
    classification: ItemClassification

    def __repr__(self):
        return f"{self.name} (Classification: {self.classification})"


all_spells: List[SpellItem] = []


def create_spell(code: int, name: str, classification: ItemClassification):
    spell = SpellItem(name, code, classification)
    all_spells.append(spell)
    return spell


barrier = create_spell(120, Spell.barrier, ItemClassification.useful)
bestial_communion = create_spell(121, Spell.bestial_communion, ItemClassification.useful)
blood_drain = create_spell(122, Spell.blood_drain, ItemClassification.progression)
blood_strike = create_spell(123, Spell.blood_strike, ItemClassification.progression)
blue_flame_arc = create_spell(124, Spell.blue_flame_arc, ItemClassification.useful)
coffin = create_spell(125, Spell.coffin, ItemClassification.progression)
corpse_transformation = create_spell(126, Spell.corpse_transformation, ItemClassification.useful)
earth_strike = create_spell(127, Spell.earth_strike, ItemClassification.useful)
earth_thorn = create_spell(128, Spell.earth_thorn, ItemClassification.useful)
fire_worm = create_spell(129, Spell.fire_worm, ItemClassification.useful)
flame_flare = create_spell(130, Spell.flame_flare, ItemClassification.useful)
flame_spear = create_spell(131, Spell.flame_spear, ItemClassification.useful)
ghost_light = create_spell(132, Spell.ghost_light, ItemClassification.progression)
holy_warmth = create_spell(133, Spell.holy_warmth, ItemClassification.useful)
icarian_flight = create_spell(134, Spell.icarian_flight, ItemClassification.progression)
ice_spear = create_spell(135, Spell.ice_spear, ItemClassification.useful)
ice_tear = create_spell(136, Spell.ice_tear, ItemClassification.useful)
ignis_calor = create_spell(137, Spell.ignis_calor, ItemClassification.progression)
lava_chasm = create_spell(138, Spell.lava_chasm, ItemClassification.useful)
light_reveal = create_spell(139, Spell.light_reveal, ItemClassification.useful)
lightning = create_spell(140, Spell.lightning, ItemClassification.useful)
lithomancy = create_spell(141, Spell.lithomancy, ItemClassification.useful)
moon_beam = create_spell(142, Spell.moon_beam, ItemClassification.useful)
poison_mist = create_spell(143, Spell.poison_mist, ItemClassification.useful)
rock_bridge = create_spell(144, Spell.rock_bridge, ItemClassification.progression)
slime_orb = create_spell(145, Spell.slime_orb, ItemClassification.useful)
spirit_warp = create_spell(146, Spell.spirit_warp, ItemClassification.progression)
summon_fairy = create_spell(147, Spell.summon_fairy, ItemClassification.useful)
summon_ice_sword = create_spell(148, Spell.summon_ice_sword, ItemClassification.useful)
wind_dash = create_spell(149, Spell.wind_dash, ItemClassification.useful)
wind_slicer = create_spell(150, Spell.wind_slicer, ItemClassification.useful)

summon_snail = create_spell(151, MobSpell.summon_snail, ItemClassification.useful)
dark_skull = create_spell(152, MobSpell.dark_skull, ItemClassification.useful)
summon_kodama = create_spell(153, MobSpell.summon_kodama, ItemClassification.useful)
tornado = create_spell(154, MobSpell.tornado, ItemClassification.useful)
quick_stride = create_spell(155, MobSpell.quick_stride, ItemClassification.useful)

light_spells = [Spell.lightning, Spell.moon_beam]
blood_spells = [Spell.blood_drain, Spell.blood_strike]
spell_light_sources = [Spell.flame_flare, Spell.ghost_light]
jump_spells = [Spell.icarian_flight, Spell.rock_bridge]
fire_spells = [Spell.lava_chasm, Spell.flame_spear, Spell.fire_worm]

drop_spells = [MobSpell.summon_snail, MobSpell.dark_skull, MobSpell.summon_kodama, MobSpell.tornado, MobSpell.quick_stride]

starting_spells = [Spell.flame_spear, Spell.ice_spear, Spell.wind_slicer, Spell.slime_orb, Spell.earth_strike]
drop_starting_spells = [MobSpell.dark_skull]

all_spells_by_name: Dict[str, SpellItem] = {spell.name: spell for spell in all_spells}

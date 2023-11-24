from dataclasses import dataclass
from typing import List
from BaseClasses import ItemClassification

from .game_item import GameItem
from ..strings.spells import Spell, MobSpell
from ..strings.regions_entrances import Region
from ..strings.locations import Location


@dataclass(frozen=True)
class SpellItem(GameItem):
    name: str
    classification: ItemClassification

    def __repr__(self):
        return f"{self.name} (Classification: {self.classification})"


all_spells: List[SpellItem] = []


def create_spell(name: str, classification: ItemClassification):
    spell = SpellItem(name, classification)
    all_spells.append(spell)
    return spell


barrier = create_spell(Spell.barrier, ItemClassification.useful)
bestial_communion = create_spell(Spell.bestial_communion, ItemClassification.useful)
blood_drain = create_spell(Spell.blood_drain, ItemClassification.progression)
blood_strike = create_spell(Spell.blood_strike, ItemClassification.progression)
blue_flame_arc = create_spell(Spell.blue_flame_arc, ItemClassification.useful)
coffin = create_spell(Spell.coffin, ItemClassification.progression)
corpse_transformation = create_spell(Spell.corpse_transformation, ItemClassification.useful)
earth_strike = create_spell(Spell.earth_strike, ItemClassification.useful)
earth_thorn = create_spell(Spell.earth_thorn, ItemClassification.useful)
fire_worm = create_spell(Spell.fire_worm, ItemClassification.useful)
flame_flare = create_spell(Spell.flame_flare, ItemClassification.useful)
flame_spear = create_spell(Spell.flame_spear, ItemClassification.useful)
ghost_light = create_spell(Spell.ghost_light, ItemClassification.progression)
holy_warmth = create_spell(Spell.holy_warmth, ItemClassification.useful)
icarian_flight = create_spell(Spell.icarian_flight, ItemClassification.progression)
ice_spear = create_spell(Spell.ice_spear, ItemClassification.useful)
ice_tear = create_spell(Spell.ice_tear, ItemClassification.useful)
ignis_calor = create_spell(Spell.ignis_calor, ItemClassification.progression)
lava_chasm = create_spell(Spell.lava_chasm, ItemClassification.useful)
light_reveal = create_spell(Spell.light_reveal, ItemClassification.useful)
lightning = create_spell(Spell.lightning, ItemClassification.useful)
lithomancy = create_spell(Spell.lithomancy, ItemClassification.useful)
moon_beam = create_spell(Spell.moon_beam, ItemClassification.useful)
poison_mist = create_spell(Spell.poison_mist, ItemClassification.useful)
rock_bridge = create_spell(Spell.rock_bridge, ItemClassification.progression)
slime_orb = create_spell(Spell.slime_orb, ItemClassification.useful)
spirit_warp = create_spell(Spell.spirit_warp, ItemClassification.progression)
summon_fairy = create_spell(Spell.summon_fairy, ItemClassification.useful)
summon_ice_sword = create_spell(Spell.summon_ice_sword, ItemClassification.useful)
wind_dash = create_spell(Spell.wind_dash, ItemClassification.useful)
wind_slicer = create_spell(Spell.wind_slicer, ItemClassification.useful)

spell_drop_locations = {
    MobSpell.summon_snail: [Location.hollow_basin_left_water],
    MobSpell.dark_skull: [Location.mausoleum_hidden_chest, Location.mire_skeleton_chest, Location.sea_blood_island],
    MobSpell.summon_kodama: [Location.yosei_chest_near_tree],
}

light_spells = [Spell.lightning, Spell.moon_beam]
blood_spells = [Spell.blood_drain, Spell.blood_strike]
spell_light_sources = [Spell.flame_flare, Spell.ghost_light]
jump_spells = [Spell.icarian_flight, Spell.rock_bridge, Spell.coffin]

all_spells_by_name = {spell.name: spell for spell in all_spells}

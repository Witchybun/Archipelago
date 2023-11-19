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
    region: str
    classification: ItemClassification

    def __repr__(self):
        return f"{self.name} (Located At: {self.region} |" \
               f"(Classification: {self.classification})"


all_spells: List[SpellItem] = []


def create_spell(name: str, region: str, classification: ItemClassification):
    spell = SpellItem(name, region, classification)
    all_spells.append(spell)
    return spell


barrier = create_spell(Spell.barrier, Region.fetid_mire, ItemClassification.useful)
bestial_communion = create_spell(Spell.bestial_communion, Region.daedalus, ItemClassification.useful)
blood_drain = create_spell(Spell.blood_drain, Region.yosei_forest, ItemClassification.progression)
blood_strike = create_spell(Spell.blood_strike, Region.hollow_basin, ItemClassification.progression)
blue_flame_arc = create_spell(Spell.blue_flame_arc, Region.terminus_prison, ItemClassification.useful)
coffin = create_spell(Spell.coffin, Region.accursed_tomb, ItemClassification.progression)
corpse_transformation = create_spell(Spell.corpse_transformation, Region.forbidden_archives, ItemClassification.useful)
earth_strike = create_spell(Spell.earth_strike, Region.yosei_forest, ItemClassification.useful)
earth_thorn = create_spell(Spell.earth_thorn, Region.sealed_ballroom, ItemClassification.useful)
fire_worm = create_spell(Spell.fire_worm, Region.daedalus, ItemClassification.useful)
flame_flare = create_spell(Spell.flame_flare, Region.hollow_basin, ItemClassification.useful)
flame_spear = create_spell(Spell.flame_spear, Region.hollow_basin, ItemClassification.useful)
ghost_light = create_spell(Spell.ghost_light, Region.hollow_basin, ItemClassification.progression)
holy_warmth = create_spell(Spell.holy_warmth, Region.yosei_forest, ItemClassification.useful)
icarian_flight = create_spell(Spell.icarian_flight, Region.terminus_prison, ItemClassification.progression)
ice_spear = create_spell(Spell.ice_spear, Region.fetid_mire, ItemClassification.useful)
ice_tear = create_spell(Spell.ice_tear, Region.laetus_chasm, ItemClassification.useful)
ignis_calor = create_spell(Spell.ignis_calor, Region.boiling_grotto, ItemClassification.progression)
lava_chasm = create_spell(Spell.lava_chasm, Region.labyrinth_of_ash, ItemClassification.useful)
light_reveal = create_spell(Spell.light_reveal, Region.yosei_forest, ItemClassification.useful)
lightning = create_spell(Spell.lightning, Region.accursed_tomb, ItemClassification.useful)
lithomancy = create_spell(Spell.lithomancy, Region.hollow_basin, ItemClassification.useful)
moon_beam = create_spell(Spell.moon_beam, Region.daedalus, ItemClassification.useful)
poison_mist = create_spell(Spell.poison_mist, Region.forest_canopy, ItemClassification.useful)
rock_bridge = create_spell(Spell.rock_bridge, Region.boiling_grotto, ItemClassification.progression)
slime_orb = create_spell(Spell.slime_orb, Region.fetid_mire, ItemClassification.useful)
spirit_warp = create_spell(Spell.spirit_warp, Region.labyrinth_of_ash, ItemClassification.useful)
summon_fairy = create_spell(Spell.summon_fairy, Region.sanguine_sea, ItemClassification.useful)
summon_ice_sword = create_spell(Spell.summon_ice_sword, Region.castle_le_fanu_red, ItemClassification.useful)
wind_dash = create_spell(Spell.wind_dash, Region.fetid_mire, ItemClassification.useful)
wind_slicer = create_spell(Spell.wind_slicer, Region.forest_canopy, ItemClassification.useful)

spell_drop_locations = {
    MobSpell.summon_snail: [Location.hollow_basin_left_water],
    MobSpell.dark_skull: [Location.mausoleum_hidden_chest, Location.mire_skeleton_chest, Location.sea_blood_island],
    MobSpell.summon_kodama: [Location.yosei_chest_near_tree],
}

light_spells = [Spell.lightning, Spell.moon_beam]
blood_spells = [Spell.blood_drain, Spell.blood_strike]

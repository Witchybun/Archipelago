from dataclasses import dataclass

from .game_item import GameItem
from ..strings.spells import Spell
from ..strings.regions_entrances import Region


@dataclass(frozen=True)
class SpellItem(GameItem):
    name: str
    region: str

    def __repr__(self):
        return f"{self.name} (Located At: {self.region} |"


all_spells = []


def create_spell(name: str, region: str):
    spell = SpellItem(name, region)
    all_spells.append(spell)
    return spell


barrier = create_spell(Spell.barrier, Region.fetid_mire)
bestial_communion = create_spell(Spell.bestial_communion, Region.daedalus)
blood_drain = create_spell(Spell.blood_drain, Region.yosei_forest)
blood_strike = create_spell(Spell.blood_strike, Region.hollow_basin)
blue_flame_arc = create_spell(Spell.blue_flame_arc, Region.terminus_prison)
coffin = create_spell(Spell.coffin, Region.accursed_tomb)
corpse_transformation = create_spell(Spell.corpse_transformation, Region.forbidden_archives)
earth_strike = create_spell(Spell.earth_strike, Region.yosei_forest)
earth_thorn = create_spell(Spell.earth_thorn, Region.sealed_ballroom)
fire_worm = create_spell(Spell.fire_worm, Region.daedalus)
flame_flare = create_spell(Spell.flame_flare, Region.hollow_basin)
flame_spear = create_spell(Spell.flame_spear, Region.hollow_basin)
ghost_light = create_spell(Spell.ghost_light, Region.hollow_basin)
holy_warmth = create_spell(Spell.holy_warmth, Region.yosei_forest)
icarian_flight = create_spell(Spell.icarian_flight, Region.terminus_prison)
ice_spear = create_spell(Spell.ice_spear, Region.fetid_mire)
ice_tear = create_spell(Spell.ice_tear, Region.laetus_chasm)
ignis_calor = create_spell(Spell.ignis_calor, Region.boiling_grotto)
lava_chasm = create_spell(Spell.lava_chasm, Region.labyrinth_of_ash)
light_reveal = create_spell(Spell.light_reveal, Region.yosei_forest)
lightning = create_spell(Spell.lightning, Region.accursed_tomb)
lithomancy = create_spell(Spell.lithomancy, Region.hollow_basin)
moon_beam = create_spell(Spell.moon_beam, Region.daedalus)
poison_mist = create_spell(Spell.poison_mist, Region.forest_canopy)
rock_bridge = create_spell(Spell.rock_bridge, Region.boiling_grotto)
slime_orb = create_spell(Spell.slime_orb, Region.fetid_mire)
spirit_warp = create_spell(Spell.spirit_warp, Region.labyrinth_of_ash)
summon_fairy = create_spell(Spell.summon_fairy, Region.sanguine_sea)
summon_ice_sword = create_spell(Spell.summon_ice_sword, Region.castle_le_fanu_red)
wind_dash = create_spell(Spell.wind_dash, Region.fetid_mire)
wind_slicer = create_spell(Spell.wind_slicer, Region.forest_canopy)

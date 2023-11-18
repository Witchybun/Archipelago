from dataclasses import dataclass

from .game_item import GameItem
from ..strings.weapons import Weapon
from ..strings.regions_entrances import Region


@dataclass(frozen=True)
class WeaponItem(GameItem):
    name: str
    region: str

    def __repr__(self):
        return f"{self.name} [{self.item_id}] (Located At: {self.region} |"


all_weapons = []


def create_weapon(name: str, region: str):
    weapon = WeaponItem(name, region)
    all_weapons.append(weapon)
    return weapon


axe_of_harming = create_weapon(Weapon.axe_of_harming, Region.forbidden_archives)
battle_axe = create_weapon(Weapon.battle_axe, Region.fetid_mire)
blade_of_jusztina = create_weapon(Weapon.blade_of_jusztina, Region.accursed_tomb)
blade_of_ophelia = create_weapon(Weapon.blade_of_ophelia, Region.castle_le_fanu_blue)
blessed_wind = create_weapon(Weapon.blessed_wind, Region.laetus_chasm)
broken_hilt = create_weapon(Weapon.broken_hilt, Region.fetid_mire)
broken_lance = create_weapon(Weapon.broken_lance, Region.terminus_prison)
corrupted_dagger = create_weapon(Weapon.corrupted_dagger, Region.sanguine_sea)
dark_rapier = create_weapon(Weapon.dark_rapier, Region.sanguine_sea)
elfen_bow = create_weapon(Weapon.elfen_bow, Region.yosei_forest)
elfen_sword = create_weapon(Weapon.elfen_sword, Region.yosei_forest)
fishing_spear = create_weapon(Weapon.fishing_spear, Region.terminus_prison)
flail = create_weapon(Weapon.flail, Region.sealed_ballroom)
halberd = create_weapon(Weapon.halberd, Region.accursed_tomb)
iron_claw = create_weapon(Weapon.iron_claw, Region.boiling_grotto)
moonlight = create_weapon(Weapon.moonlight, Region.tower_abyss)
obsidian_seal = create_weapon(Weapon.obsidian_seal, Region.forlorn_arena)
replica_sword = create_weapon(Weapon.replica_sword, Region.hollow_basin)
ritual_dagger = create_weapon(Weapon.ritual_dagger, Region.hollow_basin)
serpent_fang = create_weapon(Weapon.serpent_fang, Region.labyrinth_of_ash)
shadow_blade = create_weapon(Weapon.shadow_blade, Region.forlorn_arena)
steel_spear = create_weapon(Weapon.steel_spear, Region.hollow_basin)
stone_club = create_weapon(Weapon.stone_club, Region.hollow_basin)
torch = create_weapon(Weapon.torch, Region.hollow_basin)
twisted_staff = create_weapon(Weapon.torch, Region.accursed_tomb)
vampire_hunter_sword = create_weapon(Weapon.vampire_hunter_sword, Region.accursed_tomb)
wand_of_power = create_weapon(Weapon.wand_of_power, Region.castle_le_fanu_red)
wolfram_greatsword = create_weapon(Weapon.wolfram_greatsword, Region.forbidden_archives)
wooden_shield = create_weapon(Weapon.wooden_shield, Region.hollow_basin)



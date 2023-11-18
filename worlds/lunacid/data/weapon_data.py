from dataclasses import dataclass
from BaseClasses import ItemClassification
from typing import List

from .game_item import GameItem
from ..strings.weapons import Weapon
from ..strings.regions_entrances import Region


@dataclass(frozen=True)
class WeaponItem(GameItem):
    name: str
    region: str
    classification: ItemClassification


    def __repr__(self):
        return f"{self.name} (Located At: {self.region}) |" \
               f"(Classification: {self.classification})"


all_weapons: List[WeaponItem] = []


def create_weapon(name: str, region: str, classification: ItemClassification):
    weapon = WeaponItem(name, region, classification)
    all_weapons.append(weapon)
    return weapon


axe_of_harming = create_weapon(Weapon.axe_of_harming, Region.forbidden_archives, ItemClassification.useful)
battle_axe = create_weapon(Weapon.battle_axe, Region.fetid_mire, ItemClassification.useful)
blade_of_jusztina = create_weapon(Weapon.blade_of_jusztina, Region.accursed_tomb, ItemClassification.useful)
blade_of_ophelia = create_weapon(Weapon.blade_of_ophelia, Region.castle_le_fanu_blue, ItemClassification.useful)
blessed_wind = create_weapon(Weapon.blessed_wind, Region.laetus_chasm, ItemClassification.useful)
broken_hilt = create_weapon(Weapon.broken_hilt, Region.fetid_mire, ItemClassification.useful)
broken_lance = create_weapon(Weapon.broken_lance, Region.terminus_prison, ItemClassification.useful)
corrupted_dagger = create_weapon(Weapon.corrupted_dagger, Region.sanguine_sea, ItemClassification.useful)
dark_rapier = create_weapon(Weapon.dark_rapier, Region.sanguine_sea, ItemClassification.useful)
elfen_bow = create_weapon(Weapon.elfen_bow, Region.yosei_forest, ItemClassification.useful)
elfen_sword = create_weapon(Weapon.elfen_sword, Region.yosei_forest, ItemClassification.useful)
fishing_spear = create_weapon(Weapon.fishing_spear, Region.terminus_prison, ItemClassification.useful)
flail = create_weapon(Weapon.flail, Region.sealed_ballroom, ItemClassification.useful)
halberd = create_weapon(Weapon.halberd, Region.accursed_tomb, ItemClassification.useful)
iron_claw = create_weapon(Weapon.iron_claw, Region.boiling_grotto, ItemClassification.useful)
moonlight = create_weapon(Weapon.moonlight, Region.tower_abyss, ItemClassification.useful)
obsidian_seal = create_weapon(Weapon.obsidian_seal, Region.forlorn_arena, ItemClassification.useful)
replica_sword = create_weapon(Weapon.replica_sword, Region.hollow_basin, ItemClassification.useful)
ritual_dagger = create_weapon(Weapon.ritual_dagger, Region.hollow_basin, ItemClassification.useful)
serpent_fang = create_weapon(Weapon.serpent_fang, Region.labyrinth_of_ash, ItemClassification.useful)
shadow_blade = create_weapon(Weapon.shadow_blade, Region.forlorn_arena, ItemClassification.useful)
steel_spear = create_weapon(Weapon.steel_spear, Region.hollow_basin, ItemClassification.useful)
stone_club = create_weapon(Weapon.stone_club, Region.hollow_basin, ItemClassification.useful)
torch = create_weapon(Weapon.torch, Region.hollow_basin, ItemClassification.progression)
twisted_staff = create_weapon(Weapon.torch, Region.accursed_tomb, ItemClassification.progression)
vampire_hunter_sword = create_weapon(Weapon.vampire_hunter_sword, Region.accursed_tomb, ItemClassification.useful)
wand_of_power = create_weapon(Weapon.wand_of_power, Region.castle_le_fanu_red, ItemClassification.useful)
wolfram_greatsword = create_weapon(Weapon.wolfram_greatsword, Region.forbidden_archives, ItemClassification.useful)
wooden_shield = create_weapon(Weapon.wooden_shield, Region.hollow_basin, ItemClassification.useful)



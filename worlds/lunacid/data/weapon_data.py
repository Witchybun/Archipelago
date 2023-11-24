from dataclasses import dataclass
from BaseClasses import ItemClassification
from typing import List

from .game_item import GameItem
from ..strings.weapons import Weapon
from ..strings.regions_entrances import Region


@dataclass(frozen=True)
class WeaponItem(GameItem):
    name: str
    classification: ItemClassification


    def __repr__(self):
        return f"{self.name} (Classification: {self.classification})"


all_weapons: List[WeaponItem] = []


def create_weapon(name: str, classification: ItemClassification):
    weapons = WeaponItem(name, classification)
    all_weapons.append(weapons)
    return weapons


axe_of_harming = create_weapon(Weapon.axe_of_harming, ItemClassification.useful)
battle_axe = create_weapon(Weapon.battle_axe, ItemClassification.useful)
blade_of_jusztina = create_weapon(Weapon.blade_of_jusztina, ItemClassification.useful)
blade_of_ophelia = create_weapon(Weapon.blade_of_ophelia, ItemClassification.useful)
blessed_wind = create_weapon(Weapon.blessed_wind, ItemClassification.useful)
broken_hilt = create_weapon(Weapon.broken_hilt, ItemClassification.useful)
broken_lance = create_weapon(Weapon.broken_lance, ItemClassification.useful)
corrupted_dagger = create_weapon(Weapon.corrupted_dagger, ItemClassification.useful)
dark_rapier = create_weapon(Weapon.dark_rapier, ItemClassification.useful)
elfen_bow = create_weapon(Weapon.elfen_bow, ItemClassification.progression)
elfen_sword = create_weapon(Weapon.elfen_sword, ItemClassification.useful)
fishing_spear = create_weapon(Weapon.fishing_spear, ItemClassification.useful)
flail = create_weapon(Weapon.flail, ItemClassification.useful)
halberd = create_weapon(Weapon.halberd, ItemClassification.useful)
iron_claw = create_weapon(Weapon.iron_claw, ItemClassification.useful)
moonlight = create_weapon(Weapon.moonlight, ItemClassification.progression)
obsidian_seal = create_weapon(Weapon.obsidian_seal, ItemClassification.useful)
replica_sword = create_weapon(Weapon.replica_sword, ItemClassification.useful)
ritual_dagger = create_weapon(Weapon.ritual_dagger, ItemClassification.useful)
serpent_fang = create_weapon(Weapon.serpent_fang, ItemClassification.useful)
shadow_blade = create_weapon(Weapon.shadow_blade, ItemClassification.progression)
steel_spear = create_weapon(Weapon.steel_spear, ItemClassification.useful)
stone_club = create_weapon(Weapon.stone_club, ItemClassification.useful)
torch = create_weapon(Weapon.torch, ItemClassification.progression)
twisted_staff = create_weapon(Weapon.torch, ItemClassification.progression)
vampire_hunter_sword = create_weapon(Weapon.vampire_hunter_sword, ItemClassification.progression)
wand_of_power = create_weapon(Weapon.wand_of_power, ItemClassification.progression)
wolfram_greatsword = create_weapon(Weapon.wolfram_greatsword, ItemClassification.useful)
wooden_shield = create_weapon(Weapon.wooden_shield, ItemClassification.useful)
crossbow = create_weapon(Weapon.crossbow, ItemClassification.progression)
steel_needle = create_weapon(Weapon.steel_needle, ItemClassification.useful)


light_weapons = [Weapon.moonlight, Weapon.vampire_hunter_sword, Weapon.shadow_blade]
ranged_weapons = [Weapon.elfen_bow, Weapon.twisted_staff, Weapon.wand_of_power, Weapon.crossbow]
weapon_light_sources = [Weapon.torch, Weapon.twisted_staff, Weapon.moonlight]

all_weapons_by_name = {weapon.name: weapon for weapon in all_weapons}


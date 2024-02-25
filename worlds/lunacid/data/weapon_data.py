from dataclasses import dataclass
from BaseClasses import ItemClassification
from typing import List

from .game_item import GameItem
from ..strings.weapons import Weapon


@dataclass(frozen=True)
class WeaponItem(GameItem):
    code: int
    name: str
    classification: ItemClassification

    def __repr__(self):
        return f"{self.name} (Classification: {self.classification})"


all_weapons: List[WeaponItem] = []


def create_weapon(code: int, name: str, classification: ItemClassification):
    weapons = WeaponItem(name, code, classification)
    all_weapons.append(weapons)
    return weapons


axe_of_harming = create_weapon(60, Weapon.axe_of_harming, ItemClassification.useful)
battle_axe = create_weapon(61, Weapon.battle_axe, ItemClassification.useful)
blade_of_jusztina = create_weapon(62, Weapon.blade_of_jusztina, ItemClassification.useful)
blade_of_ophelia = create_weapon(63, Weapon.blade_of_ophelia, ItemClassification.useful)
blessed_wind = create_weapon(64, Weapon.blessed_wind, ItemClassification.useful)
broken_hilt = create_weapon(65, Weapon.broken_hilt, ItemClassification.useful)
broken_lance = create_weapon(66, Weapon.broken_lance, ItemClassification.useful)
corrupted_dagger = create_weapon(67, Weapon.corrupted_dagger, ItemClassification.useful)
dark_rapier = create_weapon(68, Weapon.dark_rapier, ItemClassification.useful)
elfen_bow = create_weapon(69, Weapon.elfen_bow, ItemClassification.progression)
elfen_sword = create_weapon(70, Weapon.elfen_sword, ItemClassification.useful)
fishing_spear = create_weapon(71, Weapon.fishing_spear, ItemClassification.useful)
flail = create_weapon(72, Weapon.flail, ItemClassification.useful)
halberd = create_weapon(73, Weapon.halberd, ItemClassification.useful)
iron_claw = create_weapon(74, Weapon.iron_claw, ItemClassification.useful)
moonlight = create_weapon(75, Weapon.moonlight, ItemClassification.progression)
obsidian_seal = create_weapon(76, Weapon.obsidian_seal, ItemClassification.useful)
replica_sword = create_weapon(77, Weapon.replica_sword, ItemClassification.useful)
ritual_dagger = create_weapon(78, Weapon.ritual_dagger, ItemClassification.useful)
serpent_fang = create_weapon(79, Weapon.serpent_fang, ItemClassification.useful)
shadow_blade = create_weapon(80, Weapon.shadow_blade, ItemClassification.progression)
steel_spear = create_weapon(81, Weapon.steel_spear, ItemClassification.useful)
stone_club = create_weapon(82, Weapon.stone_club, ItemClassification.useful)
torch = create_weapon(83, Weapon.torch, ItemClassification.progression)
twisted_staff = create_weapon(84, Weapon.twisted_staff, ItemClassification.progression)
vampire_hunter_sword = create_weapon(85, Weapon.vampire_hunter_sword, ItemClassification.progression)
wand_of_power = create_weapon(86, Weapon.wand_of_power, ItemClassification.progression)
wolfram_greatsword = create_weapon(87, Weapon.wolfram_greatsword, ItemClassification.useful)
wooden_shield = create_weapon(88, Weapon.wooden_shield, ItemClassification.useful)
crossbow = create_weapon(89, Weapon.crossbow, ItemClassification.progression)
steel_needle = create_weapon(90, Weapon.steel_needle, ItemClassification.useful)
lucid_blade = create_weapon(91, Weapon.lucid_blade, ItemClassification.progression)
hammer_of_cruelty = create_weapon(93, Weapon.hammer_of_cruelty, ItemClassification.useful)

jotunn_slayer = create_weapon(92, Weapon.jotunn_slayer, ItemClassification.progression)
rapier = create_weapon(94, Weapon.rapier, ItemClassification.useful)
privateer_musket = create_weapon(95, Weapon.privateer_musket, ItemClassification.useful)

rusted_sword = create_weapon(96, Weapon.rusted_sword, ItemClassification.useful)
ice_sickle = create_weapon(97, Weapon.ice_sickle, ItemClassification.useful)
skeleton_axe = create_weapon(98, Weapon.skeleton_axe, ItemClassification.useful)
cursed_blade = create_weapon(99, Weapon.cursed_blade, ItemClassification.useful)
brittle_arming_sword = create_weapon(100, Weapon.brittle_arming_sword, ItemClassification.useful)
obsidian_cursebrand = create_weapon(101, Weapon.obsidian_cursebrand, ItemClassification.useful)
obsidian_poisonguard = create_weapon(102, Weapon.obsidian_poisonguard, ItemClassification.useful)
golden_kopesh = create_weapon(103, Weapon.golden_kopesh, ItemClassification.useful)
golden_sickle = create_weapon(104, Weapon.golden_sickle, ItemClassification.useful)
jailor_candle = create_weapon(105, Weapon.jailor_candle, ItemClassification.useful)
sucsarian_dagger = create_weapon(106, Weapon.sucsarian_dagger, ItemClassification.useful)
sucsarian_spear = create_weapon(107, Weapon.sucsarian_spear, ItemClassification.useful)
lyrian_longsword = create_weapon(108, Weapon.lyrian_longsword, ItemClassification.useful)

light_weapons = [Weapon.moonlight, Weapon.vampire_hunter_sword, Weapon.shadow_blade, Weapon.wand_of_power]
ranged_weapons = [Weapon.elfen_bow, Weapon.twisted_staff, Weapon.wand_of_power, Weapon.crossbow, Weapon.privateer_musket]
weapon_light_sources = [Weapon.torch, Weapon.twisted_staff, Weapon.moonlight]
fire_weapons = [Weapon.jailor_candle, Weapon.jotunn_slayer, Weapon.torch, Weapon.twisted_staff, Weapon.wand_of_power]

starting_weapon = [Weapon.replica_sword, Weapon.battle_axe, Weapon.stone_club, Weapon.ritual_dagger, Weapon.torch, Weapon.steel_spear,
                   Weapon.wooden_shield, Weapon.broken_hilt, Weapon.elfen_bow, Weapon.elfen_sword, ]
shop_starting_weapons = [Weapon.crossbow, Weapon.rapier, Weapon.steel_needle]
drop_starting_weapons = [Weapon.skeleton_axe, Weapon.rusted_sword, Weapon.ice_sickle]

all_weapons_by_name = {weapon.name: weapon for weapon in all_weapons}

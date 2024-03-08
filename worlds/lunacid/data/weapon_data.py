from dataclasses import dataclass
from BaseClasses import ItemClassification
from typing import List

from .game_item import GameItem
from ..strings.properties import Elements, Types
from ..strings.weapons import Weapon


@dataclass(frozen=True)
class WeaponItem(GameItem):
    code: int
    name: str
    element: str
    style: str
    classification: ItemClassification

    def __repr__(self):
        return f"{self.name} (Classification: {self.classification})"


all_weapons: List[WeaponItem] = []


def create_weapon(code: int, name: str, element: str, style: str, classification: ItemClassification):
    weapons = WeaponItem(name, code, element, style, classification)
    all_weapons.append(weapons)
    return weapons


axe_of_harming = create_weapon(80, Weapon.axe_of_harming, Elements.poison, Types.melee, ItemClassification.useful)
battle_axe = create_weapon(81, Weapon.battle_axe, Elements.normal, Types.melee, ItemClassification.useful)
blade_of_jusztina = create_weapon(82, Weapon.blade_of_jusztina, Elements.dark, Types.melee, ItemClassification.useful)
blade_of_ophelia = create_weapon(83, Weapon.blade_of_ophelia, Elements.normal, Types.melee, ItemClassification.useful)
blessed_wind = create_weapon(84, Weapon.blessed_wind, Elements.normal, Types.melee, ItemClassification.useful)
broken_hilt = create_weapon(85, Weapon.broken_hilt, Elements.normal, Types.melee, ItemClassification.useful)
broken_lance = create_weapon(86, Weapon.broken_lance, Elements.normal, Types.melee, ItemClassification.useful)
corrupted_dagger = create_weapon(87, Weapon.corrupted_dagger, Elements.dark, Types.melee, ItemClassification.useful)
dark_rapier = create_weapon(88, Weapon.dark_rapier, Elements.dark, Types.melee, ItemClassification.useful)
elfen_bow = create_weapon(89, Weapon.elfen_bow, Elements.normal, Types.ranged, ItemClassification.progression)
elfen_sword = create_weapon(90, Weapon.elfen_sword, Elements.normal, Types.melee, ItemClassification.useful)
fishing_spear = create_weapon(91, Weapon.fishing_spear, Elements.normal, Types.both, ItemClassification.useful)
flail = create_weapon(92, Weapon.marauder_black_flail, Elements.normal, Types.melee, ItemClassification.useful)
halberd = create_weapon(93, Weapon.halberd, Elements.normal, Types.melee, ItemClassification.useful)
iron_claw = create_weapon(94, Weapon.iron_claw, Elements.normal, Types.melee, ItemClassification.useful)
moonlight = create_weapon(95, Weapon.moonlight, Elements.light, Types.both, ItemClassification.progression)
obsidian_seal = create_weapon(96, Weapon.obsidian_seal, Elements.dark, Types.melee, ItemClassification.useful)
replica_sword = create_weapon(97, Weapon.replica_sword, Elements.normal, Types.melee, ItemClassification.useful)
ritual_dagger = create_weapon(98, Weapon.ritual_dagger, Elements.poison, Types.melee, ItemClassification.useful)
serpent_fang = create_weapon(99, Weapon.serpent_fang, Elements.dark, Types.melee, ItemClassification.useful)
shadow_blade = create_weapon(100, Weapon.shadow_blade, Elements.dark, Types.melee, ItemClassification.useful)
steel_spear = create_weapon(101, Weapon.steel_spear, Elements.normal, Types.melee, ItemClassification.useful)
stone_club = create_weapon(102, Weapon.stone_club, Elements.normal, Types.melee, ItemClassification.useful)
torch = create_weapon(103, Weapon.torch, Elements.fire, Types.melee, ItemClassification.progression)
twisted_staff = create_weapon(104, Weapon.twisted_staff, Elements.fire, Types.ranged, ItemClassification.progression)
vampire_hunter_sword = create_weapon(105, Weapon.vampire_hunter_sword, Elements.light, Types.melee, ItemClassification.useful)
wand_of_power = create_weapon(106, Weapon.wand_of_power, Elements.ignore, Types.ranged, ItemClassification.progression)
wolfram_greatsword = create_weapon(107, Weapon.wolfram_greatsword, Elements.normal, Types.melee, ItemClassification.useful)
wooden_shield = create_weapon(108, Weapon.wooden_shield, Elements.normal, Types.melee, ItemClassification.useful)
crossbow = create_weapon(109, Weapon.crossbow, Elements.normal, Types.ranged, ItemClassification.progression)
steel_needle = create_weapon(110, Weapon.steel_needle, Elements.normal, Types.melee, ItemClassification.useful)
lucid_blade = create_weapon(111, Weapon.lucid_blade, Elements.ignore, Types.both, ItemClassification.progression)
hammer_of_cruelty = create_weapon(112, Weapon.hammer_of_cruelty, Elements.dark_and_light, Types.melee, ItemClassification.useful)

jotunn_slayer = create_weapon(113, Weapon.jotunn_slayer, Types.melee, Types.ranged, ItemClassification.progression)
rapier = create_weapon(114, Weapon.rapier, Elements.normal, Types.melee, ItemClassification.useful)
privateer_musket = create_weapon(115, Weapon.privateer_musket, Elements.dark, Types.ranged, ItemClassification.progression)

rusted_sword = create_weapon(116, Weapon.rusted_sword, Elements.dark_and_fire, Types.melee, ItemClassification.useful)
ice_sickle = create_weapon(117, Weapon.ice_sickle, Elements.ice, Types.melee, ItemClassification.useful)
skeleton_axe = create_weapon(118, Weapon.skeleton_axe, Elements.normal, Types.melee, ItemClassification.useful)
cursed_blade = create_weapon(119, Weapon.cursed_blade, Elements.dark, Types.melee, ItemClassification.useful)
brittle_arming_sword = create_weapon(120, Weapon.brittle_arming_sword, Elements.normal, Types.melee, ItemClassification.useful)
obsidian_cursebrand = create_weapon(121, Weapon.obsidian_cursebrand, Elements.dark, Types.melee, ItemClassification.useful)
obsidian_poisonguard = create_weapon(122, Weapon.obsidian_poisonguard, Elements.dark, Types.melee, ItemClassification.useful)
golden_kopesh = create_weapon(123, Weapon.golden_kopesh, Elements.normal, Types.melee, ItemClassification.useful)
golden_sickle = create_weapon(124, Weapon.golden_sickle, Elements.normal, Types.melee, ItemClassification.useful)
jailor_candle = create_weapon(125, Weapon.jailor_candle, Elements.fire, Types.ranged, ItemClassification.progression)
sucsarian_dagger = create_weapon(126, Weapon.sucsarian_dagger, Elements.dark, Types.melee, ItemClassification.useful)
sucsarian_spear = create_weapon(127, Weapon.sucsarian_spear, Elements.dark, Types.melee, ItemClassification.useful)
lyrian_longsword = create_weapon(128, Weapon.lyrian_longsword, Elements.normal, Types.melee, ItemClassification.useful)

lyrian_greatsword = create_weapon(129, Weapon.lyrian_greatsword, Elements.normal, Types.melee, ItemClassification.useful)
dark_greatsword = create_weapon(130, Weapon.dark_greatsword, Elements.dark, Types.melee, ItemClassification.useful)
shining_blade = create_weapon(131, Weapon.shining_blade, Elements.light, Types.melee, ItemClassification.useful)
poison_claw = create_weapon(132, Weapon.poison_claw, Elements.poison, Types.melee, ItemClassification.useful)
iron_club = create_weapon(133, Weapon.iron_club, Elements.normal, Types.melee, ItemClassification.useful)
iron_torch = create_weapon(134, Weapon.iron_torch, Elements.fire, Types.melee, ItemClassification.useful)
fire_sword = create_weapon(135, Weapon.fire_sword, Elements.fire, Types.melee, ItemClassification.useful)
steel_lance = create_weapon(136, Weapon.steel_lance, Elements.normal, Types.melee, ItemClassification.useful)
double_crossbow = create_weapon(137, Weapon.double_crossbow, Elements.normal, Types.ranged, ItemClassification.progression)
death_scythe = create_weapon(138, Weapon.death_scythe, Elements.dark_and_light, Types.melee, ItemClassification.useful)
elfen_longsword = create_weapon(139, Weapon.elfen_longsword, Elements.normal, Types.melee, ItemClassification.useful)
flail_beta = create_weapon(140, Weapon.flail, Elements.normal, Types.melee, ItemClassification.useful)
steel_claw = create_weapon(141, Weapon.steel_claw, Elements.normal, Types.melee, ItemClassification.useful)
steel_club = create_weapon(142, Weapon.steel_club, Elements.normal, Types.melee, ItemClassification.useful)
saint_ishii = create_weapon(143, Weapon.saint_ishii, Elements.dark_and_fire, Types.melee, ItemClassification.useful)
silver_rapier = create_weapon(144, Weapon.silver_rapier, Elements.light, Types.melee, ItemClassification.useful)
heritage_sword = create_weapon(145, Weapon.heritage_sword, Elements.normal, Types.melee, ItemClassification.useful)

ranged_weapons = [weapon.name for weapon in all_weapons if weapon.style == Types.ranged or weapon.style == Types.both]
weapon_light_sources = [Weapon.torch, Weapon.twisted_staff, Weapon.moonlight, Weapon.broken_hilt]
weapons_by_element = {weapon.name: weapon.element for weapon in all_weapons}

starting_weapon = [Weapon.replica_sword, Weapon.battle_axe, Weapon.stone_club, Weapon.ritual_dagger, Weapon.torch, Weapon.steel_spear,
                   Weapon.wooden_shield, Weapon.broken_hilt, Weapon.elfen_bow, Weapon.elfen_sword, ]
shop_starting_weapons = [Weapon.crossbow, Weapon.rapier, Weapon.steel_needle]
drop_starting_weapons = [Weapon.skeleton_axe, Weapon.rusted_sword, Weapon.ice_sickle]

all_weapons_by_name = {weapon.name: weapon for weapon in all_weapons}

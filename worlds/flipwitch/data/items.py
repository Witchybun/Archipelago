from dataclasses import dataclass
from typing import List
from BaseClasses import ItemClassification

from ..strings.items import QuestItem, Upgrade, Coin, Gacha, Unlock, Key, Costume, Power, Warp, Goal, Accessory, Custom


@dataclass(frozen=True)
class FlipwitchItemData:
    code: int
    name: str
    classification: ItemClassification

    def __repr__(self):
        return f"{self.code} {self.name} (Classification: {self.classification})"


all_items: List[FlipwitchItemData] = []


def create_item(code: int, name: str, classification: ItemClassification):
    item = FlipwitchItemData(code, name, classification)
    all_items.append(item)

    return item

# ID - Classification Data


# Uses a structure of BASE ITEM + type offset + pseudo value.  The base item ID will eventually be deprecated in favor of starting at 1.
ITEM_CODE_START = 0


base_start_id = 0
base_items = [
    create_item(ITEM_CODE_START + base_start_id + 1, QuestItem.fairy_bubble, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 2, QuestItem.cowbell, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 3, QuestItem.gobliana_luggage, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 4, QuestItem.summon_stone, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 5, QuestItem.delicious_milk, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 6, QuestItem.belle_milkshake, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 7, QuestItem.cherry_key, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 8, QuestItem.mono_password, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 9, QuestItem.clothes, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 10, QuestItem.heavenly_daikon, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 11, QuestItem.hellish_dango, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 12, QuestItem.soul_fragment, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 13, QuestItem.legendary_halo, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 14, QuestItem.demonic_letter, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 15, QuestItem.angelic_letter, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 16, QuestItem.silky_slime, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 17, QuestItem.red_wine, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 18, QuestItem.blue_jelly_mushroom, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 19, QuestItem.maid_contract, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 20, QuestItem.deed, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 21, QuestItem.mimic_chest, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 22, QuestItem.fungal, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 23, QuestItem.goblin_apartment, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 24, Power.bomb, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 25, Power.frilly_panties, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 26, Power.disarming_bell, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 27, Power.ghost_form, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 28, Power.slime_form, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 29, Power.harpy_feather, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 30, Power.magical_mushroom, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 31, Power.slime_sentry, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 32, Power.ring_of_the_moon, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 33, Power.ring_of_the_sun, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 34, Power.haunted_scythe, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 35, Power.demonic_cuff, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 37, Accessory.fortune_cat, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 38, Accessory.heart_necklace, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 39, Accessory.star_bracelet, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 40, Accessory.magnetic_hairpin, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 41, Accessory.yellow_frog_talisman, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 42, Accessory.blue_frog_talisman, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 43, Accessory.sacrificial_dagger, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 44, Accessory.mind_mushroom, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 45, Accessory.flutterknife_garter, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 46, Accessory.cursed_talisman, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 47, Upgrade.health, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 48, Upgrade.mana, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 49, Upgrade.wand, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 50, Upgrade.peachy_peach, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 51, Upgrade.bewitched_bubble, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 52, Upgrade.progressive_crystal, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 53, Upgrade.portable_portal, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 54, Upgrade.demon_wings, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 55, Upgrade.angel_feathers, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 56, Upgrade.mermaid_scale, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 57, Coin.lucky_coin, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 58, Coin.loose_change, ItemClassification.filler),
    create_item(ITEM_CODE_START + base_start_id + 59, Unlock.crystal_block, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 60, Unlock.goblin_crystal_block, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 61, Costume.navy, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 63, Costume.red_wizard, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 64, Costume.nun, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 65, Costume.priest, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 66, Costume.miko, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 67, Costume.farmer, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 68, Costume.cat, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 69, Costume.goblin, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 70, Costume.maid, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 71, Costume.pigman, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 72, Costume.bunny, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 73, Costume.rat, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 74, Costume.nurse, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 75, Costume.angler, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 76, Costume.dominating, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 77, Costume.postman, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 78, Costume.fairy, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 79, Costume.alchemist, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 80, Key.rundown_house, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 81, Key.ghostly_castle, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 82, Key.beast, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 83, Key.secret_club, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 84, Key.slime_citadel, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 85, Key.frog_boss, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 86, Key.goblin_queen, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 87, Key.rose_garden, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 88, Key.collapsed_temple, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 89, Key.demon_boss, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 90, Key.slimy_sub_boss, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 91, Key.chaos_sanctum, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 92, Key.abandoned_apartment, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 93, Key.secret_garden, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 94, Key.demon_club, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 95, Key.slime_boss, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 96, Key.forgotten_fungal, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 97, Goal.chaos_piece, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 98, QuestItem.goblin_headshot, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 99, QuestItem.business_card, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 100, QuestItem.vip_key, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 101, Custom.hp_heal, ItemClassification.filler),
    create_item(ITEM_CODE_START + base_start_id + 102, Custom.mp_heal, ItemClassification.filler),
    create_item(ITEM_CODE_START + base_start_id + 103, Custom.peach_recharge, ItemClassification.filler),
    create_item(ITEM_CODE_START + base_start_id + 104, Custom.sexual_thoughts, ItemClassification.trap),
    create_item(ITEM_CODE_START + base_start_id + 105, Upgrade.barrier, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 106, Upgrade.peachy_upgrade, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 107, Coin.animal_coin, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 108, Coin.bunny_coin, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 109, Coin.angel_demon_coin, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 110, Coin.monster_coin, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 111, Coin.promotional_coin, ItemClassification.useful),
    create_item(ITEM_CODE_START + base_start_id + 112, "Nothing", ItemClassification.filler)  # Literally only for item links
]

gacha_item_id = 150
gacha_items = [
    create_item(ITEM_CODE_START + gacha_item_id + 1, Gacha.special_promotion, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 2, Gacha.animal_girl_1, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 3, Gacha.animal_girl_2, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 4, Gacha.animal_girl_3, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 5, Gacha.animal_girl_4, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 6, Gacha.animal_girl_5, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 7, Gacha.animal_girl_6, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 8, Gacha.animal_girl_7, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 9, Gacha.animal_girl_8, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 10, Gacha.animal_girl_9, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 11, Gacha.animal_girl_10, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 12, Gacha.bunny_girl_1, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 13, Gacha.bunny_girl_2, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 14, Gacha.bunny_girl_3, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 15, Gacha.bunny_girl_4, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 16, Gacha.bunny_girl_5, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 17, Gacha.bunny_girl_6, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 18, Gacha.bunny_girl_7, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 19, Gacha.bunny_girl_8, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 20, Gacha.bunny_girl_9, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 21, Gacha.bunny_girl_10, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 22, Gacha.angel_demon_1, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 23, Gacha.angel_demon_2, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 24, Gacha.angel_demon_3, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 25, Gacha.angel_demon_4, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 26, Gacha.angel_demon_5, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 27, Gacha.angel_demon_6, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 28, Gacha.angel_demon_7, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 29, Gacha.angel_demon_8, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 30, Gacha.angel_demon_9, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 31, Gacha.angel_demon_10, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 32, Gacha.monster_girl_1, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 33, Gacha.monster_girl_2, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 34, Gacha.monster_girl_3, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 35, Gacha.monster_girl_4, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 36, Gacha.monster_girl_5, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 37, Gacha.monster_girl_6, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 38, Gacha.monster_girl_7, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 39, Gacha.monster_girl_8, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 40, Gacha.monster_girl_9, ItemClassification.useful),
    create_item(ITEM_CODE_START + gacha_item_id + 41, Gacha.monster_girl_10, ItemClassification.useful),
]

warp_item_id = 200
warp_items = [
    create_item(ITEM_CODE_START + warp_item_id + 1, Warp.sensei, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + warp_item_id + 2, Warp.witchy, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + warp_item_id + 3, Warp.goblin, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + warp_item_id + 4, Warp.spirit, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + warp_item_id + 5, Warp.shady, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + warp_item_id + 6, Warp.ghost_entrance, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + warp_item_id + 7, Warp.ghost_castle, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + warp_item_id + 8, Warp.jigoku, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + warp_item_id + 9, Warp.club_demon, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + warp_item_id + 10, Warp.tengoku, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + warp_item_id + 11, Warp.angelic_hallway, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + warp_item_id + 12, Warp.fungal_forest, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + warp_item_id + 13, Warp.slime_citadel, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + warp_item_id + 14, Warp.slimy_depths, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + warp_item_id + 15, Warp.umi_umi, ItemClassification.progression | ItemClassification.useful),
    create_item(ITEM_CODE_START + warp_item_id + 16, Warp.chaos_castle, ItemClassification.progression | ItemClassification.useful),
]

filler_items = [item for item in all_items if item.classification == ItemClassification.filler]


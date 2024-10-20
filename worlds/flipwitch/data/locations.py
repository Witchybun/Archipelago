from dataclasses import dataclass
from typing import Optional, List

from ..strings.locations import WitchyWoods, SpiritTown, Quest, ShadySewers, GhostCastle, Gacha, FungalForest, SlimeCitadel, AngelicHallway, Tengoku, ClubDemon, Jigoku, \
    UmiUmi, ChaosCastle, CrystalPanel
from ..strings.regions_entrances import FlipwitchRegion


@dataclass(frozen=True)
class FlipwitchLocation:
    location_id: Optional[int]
    name: str
    region: str


all_locations = []
base_locations = []


# Some locations vary on multiple regions, so we default to Hollow Basin first.
def create_location(location_id: Optional[int], name: str, region: str):
    location = FlipwitchLocation(location_id, name, region)
    if location_id is not None:
        all_locations.append(location)
    if location_id < 650:  # I only did this because python can be stinky sometimes.
        base_locations.append(location)
    return location


LOCATION_CODE_START = 0
witchy_woods_location_start = 0
witchy_woods_locations = [
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 1, WitchyWoods.navy_costume, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 2, WitchyWoods.red_costume, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 3, WitchyWoods.peachy_peach, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 4, WitchyWoods.lucky_machine, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 5, WitchyWoods.hidden_chest_save, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 6, WitchyWoods.red_wine, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 7, WitchyWoods.waterfall_chest_1, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 8, WitchyWoods.waterfall_chest_2, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 9, WitchyWoods.hidden_coin_early, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 10, WitchyWoods.hidden_coin_early_chest, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 11, WitchyWoods.hidden_chest_mimic, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 12, WitchyWoods.goblin_apartment, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 13, WitchyWoods.secret_alcove, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 14, WitchyWoods.rundown_outside_chest, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 15, WitchyWoods.rundown_chest, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 16, WitchyWoods.lucky_rundown, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 17, WitchyWoods.fairy, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 18, WitchyWoods.man_cave, FlipwitchRegion.witch_woods_lower),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 19, WitchyWoods.past_man_cave, FlipwitchRegion.witch_woods_lower),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 20, WitchyWoods.bomb, FlipwitchRegion.witch_woods_lower),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 21, WitchyWoods.hidden_alcove, FlipwitchRegion.witch_woods_lower),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 22, WitchyWoods.flip_platform, FlipwitchRegion.witch_woods_lower),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 23, WitchyWoods.after_chaos, FlipwitchRegion.witch_woods_lower),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 24, WitchyWoods.boss_key_chest, FlipwitchRegion.witch_woods_lower),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 25, WitchyWoods.boss_key_big_chest, FlipwitchRegion.witch_woods_lower),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 26, WitchyWoods.boss_key_hp, FlipwitchRegion.witch_woods_lower),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 27, WitchyWoods.goblin_queen_mp, FlipwitchRegion.witch_woods_lower),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 28, WitchyWoods.goblin_queen_chaos, FlipwitchRegion.witch_woods_lower),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 29, WitchyWoods.goblin_queen_crystal, FlipwitchRegion.witch_woods_lower),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 30, WitchyWoods.post_fight, FlipwitchRegion.witch_woods_lower),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 31, WitchyWoods.fairy_chest, FlipwitchRegion.witch_woods_lower),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 32, WitchyWoods.hidden_spring, FlipwitchRegion.witch_woods_lower),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 33, WitchyWoods.sexual_experience_1, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 34, WitchyWoods.sexual_experience_2, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 35, WitchyWoods.sexual_experience_3, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 36, WitchyWoods.sexual_experience_4, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 37, WitchyWoods.sexual_experience_5, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 38, WitchyWoods.sexual_experience_6, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 39, WitchyWoods.sexual_experience_7, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 40, WitchyWoods.sexual_experience_8, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 41, WitchyWoods.sexual_experience_9, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 42, WitchyWoods.sexual_experience_10, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 43, WitchyWoods.sexual_experience_11, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 44, WitchyWoods.sexual_experience_12, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 45, WitchyWoods.sexual_experience_13, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 46, WitchyWoods.sexual_experience_14, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 48, WitchyWoods.fairy_reward, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 49, WitchyWoods.before_fairy, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 50, WitchyWoods.goblin_headshot, FlipwitchRegion.witch_woods_lower),
]

spirit_town_location_start = 60
spirit_town_locations = [
    create_location(LOCATION_CODE_START + spirit_town_location_start + 1, SpiritTown.fairy_bubble, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + spirit_town_location_start + 2, SpiritTown.city_hp, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + spirit_town_location_start + 3, SpiritTown.city_mp, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + spirit_town_location_start + 4, SpiritTown.toilet_coin, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + spirit_town_location_start + 5, SpiritTown.cabaret_girl_chest, FlipwitchRegion.cabaret_cafe),
    create_location(LOCATION_CODE_START + spirit_town_location_start + 6, SpiritTown.cabaret_delicious_milk, FlipwitchRegion.cabaret_cafe),
    create_location(LOCATION_CODE_START + spirit_town_location_start + 7, SpiritTown.cabaret_cherry_key, FlipwitchRegion.cabaret_cafe),
    create_location(LOCATION_CODE_START + spirit_town_location_start + 8, SpiritTown.cabaret_vip_chest, FlipwitchRegion.cabaret_cafe),
    create_location(LOCATION_CODE_START + spirit_town_location_start + 9, SpiritTown.shop_1, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + spirit_town_location_start + 10, SpiritTown.shop_2, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + spirit_town_location_start + 11, SpiritTown.shop_3, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + spirit_town_location_start + 12, SpiritTown.shop_4, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + spirit_town_location_start + 13, SpiritTown.shop_roof, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + spirit_town_location_start + 14, SpiritTown.fashion_1, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + spirit_town_location_start + 15, SpiritTown.fashion_2, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + spirit_town_location_start + 16, SpiritTown.ancient_chest, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + spirit_town_location_start + 17, SpiritTown.ghost_key, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + spirit_town_location_start + 18, SpiritTown.cemetery, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + spirit_town_location_start + 19, SpiritTown.chaos, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + spirit_town_location_start + 20, SpiritTown.apartment_key, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + spirit_town_location_start + 21, SpiritTown.password, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + spirit_town_location_start + 22, SpiritTown.banana, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + spirit_town_location_start + 23, SpiritTown.alley, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + spirit_town_location_start + 24, SpiritTown.home_2, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + spirit_town_location_start + 25, SpiritTown.home_1, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + spirit_town_location_start + 26, SpiritTown.home_6, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + spirit_town_location_start + 27, SpiritTown.green_house, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + spirit_town_location_start + 28, SpiritTown.lone_house, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + spirit_town_location_start + 29, SpiritTown.fungal_key, FlipwitchRegion.pig_mansion),
    create_location(LOCATION_CODE_START + spirit_town_location_start + 30, SpiritTown.maid_contract, FlipwitchRegion.pig_mansion),
    create_location(LOCATION_CODE_START + spirit_town_location_start + 31, SpiritTown.special_milkshake, FlipwitchRegion.spirit_town),

]

shady_sewers_location_start = 100
shady_sewers_locations = [
    create_location(LOCATION_CODE_START + shady_sewers_location_start + 1, ShadySewers.hidden_pipe, FlipwitchRegion.shady_sewers),
    create_location(LOCATION_CODE_START + shady_sewers_location_start + 2, ShadySewers.side_coin, FlipwitchRegion.shady_sewers),
    create_location(LOCATION_CODE_START + shady_sewers_location_start + 3, ShadySewers.side_chest, FlipwitchRegion.shady_sewers),
    create_location(LOCATION_CODE_START + shady_sewers_location_start + 4, ShadySewers.ratchel_coin, FlipwitchRegion.shady_sewers),
    create_location(LOCATION_CODE_START + shady_sewers_location_start + 5, ShadySewers.rat_chest_1, FlipwitchRegion.shady_sewers),
    create_location(LOCATION_CODE_START + shady_sewers_location_start + 6, ShadySewers.rat_chest_2, FlipwitchRegion.shady_sewers),
    create_location(LOCATION_CODE_START + shady_sewers_location_start + 7, ShadySewers.rat_chest_3, FlipwitchRegion.shady_sewers),
    create_location(LOCATION_CODE_START + shady_sewers_location_start + 8, ShadySewers.shady_hp, FlipwitchRegion.shady_sewers),
    create_location(LOCATION_CODE_START + shady_sewers_location_start + 9, ShadySewers.shady_chest, FlipwitchRegion.shady_sewers),
    create_location(LOCATION_CODE_START + shady_sewers_location_start + 10, ShadySewers.elf_1, FlipwitchRegion.shady_sewers),
    create_location(LOCATION_CODE_START + shady_sewers_location_start + 11, ShadySewers.elf_2, FlipwitchRegion.shady_sewers),
    create_location(LOCATION_CODE_START + shady_sewers_location_start + 12, ShadySewers.elf_chest, FlipwitchRegion.shady_sewers),
    create_location(LOCATION_CODE_START + shady_sewers_location_start + 13, ShadySewers.dwd_big, FlipwitchRegion.shady_sewers),
    create_location(LOCATION_CODE_START + shady_sewers_location_start + 14, ShadySewers.dwd_mp, FlipwitchRegion.shady_sewers),
    create_location(LOCATION_CODE_START + shady_sewers_location_start + 15, ShadySewers.dwd_tutorial, FlipwitchRegion.shady_sewers),
]

ghost_castle_location_start = 150
ghost_castle_locations = [
    create_location(LOCATION_CODE_START + ghost_castle_location_start + 1, GhostCastle.below_entrance, FlipwitchRegion.early_ghost),
    create_location(LOCATION_CODE_START + ghost_castle_location_start + 2, GhostCastle.slime_1, FlipwitchRegion.early_ghost),
    create_location(LOCATION_CODE_START + ghost_castle_location_start + 3, GhostCastle.slime_2, FlipwitchRegion.early_ghost),
    create_location(LOCATION_CODE_START + ghost_castle_location_start + 4, GhostCastle.slime_3, FlipwitchRegion.early_ghost),
    create_location(LOCATION_CODE_START + ghost_castle_location_start + 5, GhostCastle.giant_flip, FlipwitchRegion.early_ghost),
    create_location(LOCATION_CODE_START + ghost_castle_location_start + 6, GhostCastle.giant_coin, FlipwitchRegion.upper_ghost),
    create_location(LOCATION_CODE_START + ghost_castle_location_start + 7, GhostCastle.up_ladder, FlipwitchRegion.ghost_castle),
    create_location(LOCATION_CODE_START + ghost_castle_location_start + 8, GhostCastle.hidden_ledge, FlipwitchRegion.early_ghost),
    create_location(LOCATION_CODE_START + ghost_castle_location_start + 9, GhostCastle.elf, FlipwitchRegion.ghost_rose),
    create_location(LOCATION_CODE_START + ghost_castle_location_start + 10, GhostCastle.elf_chest, FlipwitchRegion.ghost_rose),
    create_location(LOCATION_CODE_START + ghost_castle_location_start + 11, GhostCastle.garden_key, FlipwitchRegion.ghost_rose),
    create_location(LOCATION_CODE_START + ghost_castle_location_start + 12, GhostCastle.hidden_wall, FlipwitchRegion.upper_ghost),
    create_location(LOCATION_CODE_START + ghost_castle_location_start + 13, GhostCastle.along_path, FlipwitchRegion.upper_ghost),
    create_location(LOCATION_CODE_START + ghost_castle_location_start + 14, GhostCastle.hidden_spring, FlipwitchRegion.upper_ghost),
    create_location(LOCATION_CODE_START + ghost_castle_location_start + 15, GhostCastle.behind_vines, FlipwitchRegion.upper_ghost),
    create_location(LOCATION_CODE_START + ghost_castle_location_start + 16, GhostCastle.across_boss, FlipwitchRegion.upper_ghost),
    create_location(LOCATION_CODE_START + ghost_castle_location_start + 17, GhostCastle.hidden_shrub, FlipwitchRegion.upper_ghost),
    create_location(LOCATION_CODE_START + ghost_castle_location_start + 18, GhostCastle.ghost_form, FlipwitchRegion.ghost_rose),
    create_location(LOCATION_CODE_START + ghost_castle_location_start + 19, GhostCastle.thimble_1, FlipwitchRegion.ghost_rose),
    create_location(LOCATION_CODE_START + ghost_castle_location_start + 20, GhostCastle.thimble_2, FlipwitchRegion.ghost_rose),
    create_location(LOCATION_CODE_START + ghost_castle_location_start + 21, GhostCastle.thimble_chest, FlipwitchRegion.ghost_rose),
    create_location(LOCATION_CODE_START + ghost_castle_location_start + 22, GhostCastle.willow, FlipwitchRegion.upper_ghost),
    create_location(LOCATION_CODE_START + ghost_castle_location_start + 23, GhostCastle.ghost_chaos, FlipwitchRegion.upper_ghost),
    create_location(LOCATION_CODE_START + ghost_castle_location_start + 24, GhostCastle.ghost_mp, FlipwitchRegion.upper_ghost),
    create_location(LOCATION_CODE_START + ghost_castle_location_start + 25, GhostCastle.ghost_gauntlet, FlipwitchRegion.upper_ghost),
]

jigoku_location_start = 200
jigoku_locations = [
    create_location(LOCATION_CODE_START + jigoku_location_start + 1, Jigoku.hidden_flip, FlipwitchRegion.jigoku),
    create_location(LOCATION_CODE_START + jigoku_location_start + 2, Jigoku.slime_form, FlipwitchRegion.jigoku),
    create_location(LOCATION_CODE_START + jigoku_location_start + 3, Jigoku.early_ledge, FlipwitchRegion.jigoku),
    create_location(LOCATION_CODE_START + jigoku_location_start + 4, Jigoku.spring_chest, FlipwitchRegion.jigoku),
    create_location(LOCATION_CODE_START + jigoku_location_start + 5, Jigoku.spring_coin, FlipwitchRegion.jigoku),
    create_location(LOCATION_CODE_START + jigoku_location_start + 6, Jigoku.cat_shrine, FlipwitchRegion.jigoku),
    create_location(LOCATION_CODE_START + jigoku_location_start + 7, Jigoku.beast_key, FlipwitchRegion.jigoku),
    create_location(LOCATION_CODE_START + jigoku_location_start + 8, Jigoku.hidden_ledge, FlipwitchRegion.jigoku),
    create_location(LOCATION_CODE_START + jigoku_location_start + 9, Jigoku.annahell, FlipwitchRegion.jigoku),
    create_location(LOCATION_CODE_START + jigoku_location_start + 10, Jigoku.hidden_hole, FlipwitchRegion.jigoku),
    create_location(LOCATION_CODE_START + jigoku_location_start + 11, Jigoku.near_elf, FlipwitchRegion.jigoku),
    create_location(LOCATION_CODE_START + jigoku_location_start + 12, Jigoku.elf_1, FlipwitchRegion.jigoku),
    create_location(LOCATION_CODE_START + jigoku_location_start + 13, Jigoku.elf_2, FlipwitchRegion.jigoku),
    create_location(LOCATION_CODE_START + jigoku_location_start + 14, Jigoku.hot_guy, FlipwitchRegion.jigoku),
    create_location(LOCATION_CODE_START + jigoku_location_start + 15, Jigoku.far_ledge, FlipwitchRegion.jigoku),
    create_location(LOCATION_CODE_START + jigoku_location_start + 16, Jigoku.hidden_flip_chest, FlipwitchRegion.jigoku),
    create_location(LOCATION_CODE_START + jigoku_location_start + 17, Jigoku.demon_wings, FlipwitchRegion.jigoku),
    create_location(LOCATION_CODE_START + jigoku_location_start + 18, Jigoku.demon_tutorial, FlipwitchRegion.jigoku),
    create_location(LOCATION_CODE_START + jigoku_location_start + 19, Jigoku.cat_chest, FlipwitchRegion.jigoku),
    create_location(LOCATION_CODE_START + jigoku_location_start + 20, Jigoku.cat_coin, FlipwitchRegion.jigoku),
    create_location(LOCATION_CODE_START + jigoku_location_start + 21, Jigoku.northern_cat_shrine, FlipwitchRegion.jigoku),
]

club_demon_location_start = 250
club_demon_locations = [
    create_location(LOCATION_CODE_START + club_demon_location_start + 1, ClubDemon.club_entrance, FlipwitchRegion.club_demon),
    create_location(LOCATION_CODE_START + club_demon_location_start + 2, ClubDemon.under_table, FlipwitchRegion.club_demon),
    create_location(LOCATION_CODE_START + club_demon_location_start + 3, ClubDemon.door, FlipwitchRegion.club_demon),
    create_location(LOCATION_CODE_START + club_demon_location_start + 4, ClubDemon.flip_magic_chest, FlipwitchRegion.club_demon),
    create_location(LOCATION_CODE_START + club_demon_location_start + 5, ClubDemon.flip_magic_coin, FlipwitchRegion.club_demon),
    create_location(LOCATION_CODE_START + club_demon_location_start + 6, ClubDemon.thimble_1, FlipwitchRegion.club_demon),
    create_location(LOCATION_CODE_START + club_demon_location_start + 7, ClubDemon.thimble_2, FlipwitchRegion.club_demon),
    create_location(LOCATION_CODE_START + club_demon_location_start + 8, ClubDemon.demonic_gauntlet, FlipwitchRegion.club_demon),
    create_location(LOCATION_CODE_START + club_demon_location_start + 9, ClubDemon.club_key_chest, FlipwitchRegion.club_demon),
    create_location(LOCATION_CODE_START + club_demon_location_start + 10, ClubDemon.club_key_coin, FlipwitchRegion.club_demon),
    create_location(LOCATION_CODE_START + club_demon_location_start + 11, ClubDemon.cat_shrine, FlipwitchRegion.club_demon),
    create_location(LOCATION_CODE_START + club_demon_location_start + 12, ClubDemon.demon_boss_chest, FlipwitchRegion.club_demon),
    create_location(LOCATION_CODE_START + club_demon_location_start + 13, ClubDemon.demon_boss_chaos, FlipwitchRegion.club_demon),
    create_location(LOCATION_CODE_START + club_demon_location_start + 14, ClubDemon.demon_boss_mp, FlipwitchRegion.club_demon),
    create_location(LOCATION_CODE_START + club_demon_location_start + 15, ClubDemon.demon_letter, FlipwitchRegion.club_demon),
]

tengoku_location_start = 300
tengoku_locations = [
    create_location(LOCATION_CODE_START + tengoku_location_start + 1, Tengoku.early_coin, FlipwitchRegion.tengoku),
    create_location(LOCATION_CODE_START + tengoku_location_start + 2, Tengoku.early_chest, FlipwitchRegion.tengoku),
    create_location(LOCATION_CODE_START + tengoku_location_start + 3, Tengoku.hidden_foliage, FlipwitchRegion.tengoku),
    create_location(LOCATION_CODE_START + tengoku_location_start + 4, Tengoku.hidden_flip, FlipwitchRegion.tengoku),
    create_location(LOCATION_CODE_START + tengoku_location_start + 5, Tengoku.birby, FlipwitchRegion.tengoku),
    create_location(LOCATION_CODE_START + tengoku_location_start + 6, Tengoku.flip_magic, FlipwitchRegion.tengoku_upper),
    create_location(LOCATION_CODE_START + tengoku_location_start + 7, Tengoku.hidden_ledge, FlipwitchRegion.tengoku_upper),
    create_location(LOCATION_CODE_START + tengoku_location_start + 8, Tengoku.secret_alcove, FlipwitchRegion.tengoku_upper),
]

angelic_hallway_location_start = 350
angelic_hallway_locations = [
    create_location(LOCATION_CODE_START + angelic_hallway_location_start + 1, AngelicHallway.starting_coins, FlipwitchRegion.angelic_hallway),
    create_location(LOCATION_CODE_START + angelic_hallway_location_start + 2, AngelicHallway.hidden_foliage_1, FlipwitchRegion.angelic_hallway),
    create_location(LOCATION_CODE_START + angelic_hallway_location_start + 3, AngelicHallway.hidden_foliage_2, FlipwitchRegion.angelic_upper),
    create_location(LOCATION_CODE_START + angelic_hallway_location_start + 4, AngelicHallway.elf_1, FlipwitchRegion.angelic_hallway),
    create_location(LOCATION_CODE_START + angelic_hallway_location_start + 5, AngelicHallway.elf_2, FlipwitchRegion.angelic_hallway),
    create_location(LOCATION_CODE_START + angelic_hallway_location_start + 6, AngelicHallway.elf_chest, FlipwitchRegion.angelic_hallway),
    create_location(LOCATION_CODE_START + angelic_hallway_location_start + 7, AngelicHallway.cloudia, FlipwitchRegion.angelic_hallway),
    create_location(LOCATION_CODE_START + angelic_hallway_location_start + 8, AngelicHallway.angelic_gauntlet, FlipwitchRegion.angelic_hallway),
    create_location(LOCATION_CODE_START + angelic_hallway_location_start + 9, AngelicHallway.thimble_1, FlipwitchRegion.angelic_hallway),
    create_location(LOCATION_CODE_START + angelic_hallway_location_start + 10, AngelicHallway.thimble_2, FlipwitchRegion.angelic_hallway),
    create_location(LOCATION_CODE_START + angelic_hallway_location_start + 11, AngelicHallway.thimble_chest, FlipwitchRegion.angelic_hallway),
    create_location(LOCATION_CODE_START + angelic_hallway_location_start + 12, AngelicHallway.below_thimble, FlipwitchRegion.angelic_hallway),
    create_location(LOCATION_CODE_START + angelic_hallway_location_start + 13, AngelicHallway.gabrielle, FlipwitchRegion.angelic_hallway),
    create_location(LOCATION_CODE_START + angelic_hallway_location_start + 14, AngelicHallway.behind_vines, FlipwitchRegion.angelic_upper),
    create_location(LOCATION_CODE_START + angelic_hallway_location_start + 15, AngelicHallway.flip_magic, FlipwitchRegion.angelic_upper),
    create_location(LOCATION_CODE_START + angelic_hallway_location_start + 16, AngelicHallway.angel_feathers, FlipwitchRegion.angelic_upper),
    create_location(LOCATION_CODE_START + angelic_hallway_location_start + 17, AngelicHallway.below_boss_chest, FlipwitchRegion.angelic_upper),
    create_location(LOCATION_CODE_START + angelic_hallway_location_start + 18, AngelicHallway.below_boss_coin, FlipwitchRegion.angelic_upper),
    create_location(LOCATION_CODE_START + angelic_hallway_location_start + 19, AngelicHallway.angelica_chaos, FlipwitchRegion.angelic_upper),
    create_location(LOCATION_CODE_START + angelic_hallway_location_start + 20, AngelicHallway.angelica_upgrade, FlipwitchRegion.angelic_upper),
    create_location(LOCATION_CODE_START + angelic_hallway_location_start + 21, AngelicHallway.angel_letter, FlipwitchRegion.angelic_hallway),
]

fungal_forest_location_start = 400
fungal_forest_locations = [
    create_location(LOCATION_CODE_START + fungal_forest_location_start + 1, FungalForest.thimble_1, FlipwitchRegion.fungal_forest),
    create_location(LOCATION_CODE_START + fungal_forest_location_start + 2, FungalForest.thimble_2, FlipwitchRegion.fungal_forest),
    create_location(LOCATION_CODE_START + fungal_forest_location_start + 3, FungalForest.lower_pit, FlipwitchRegion.fungal_forest),
    create_location(LOCATION_CODE_START + fungal_forest_location_start + 4, FungalForest.flip_magic, FlipwitchRegion.fungal_forest),
    create_location(LOCATION_CODE_START + fungal_forest_location_start + 5, FungalForest.fungella, FlipwitchRegion.fungal_forest),
    create_location(LOCATION_CODE_START + fungal_forest_location_start + 6, FungalForest.heavenly_daikon, FlipwitchRegion.fungal_forest),
    create_location(LOCATION_CODE_START + fungal_forest_location_start + 7, FungalForest.past_chaos, FlipwitchRegion.deep_fungal),
    create_location(LOCATION_CODE_START + fungal_forest_location_start + 8, FungalForest.closed_off, FlipwitchRegion.deep_fungal),
    create_location(LOCATION_CODE_START + fungal_forest_location_start + 9, FungalForest.between_thorns, FlipwitchRegion.deep_fungal),
    create_location(LOCATION_CODE_START + fungal_forest_location_start + 10, FungalForest.elf_1, FlipwitchRegion.deep_fungal),
    create_location(LOCATION_CODE_START + fungal_forest_location_start + 11, FungalForest.elf_2, FlipwitchRegion.deep_fungal),
    create_location(LOCATION_CODE_START + fungal_forest_location_start + 12, FungalForest.elf_chest, FlipwitchRegion.deep_fungal),
    create_location(LOCATION_CODE_START + fungal_forest_location_start + 13, FungalForest.mushroom_guard, FlipwitchRegion.deep_fungal),
    create_location(LOCATION_CODE_START + fungal_forest_location_start + 14, FungalForest.fungal_gauntlet, FlipwitchRegion.deep_fungal),
    create_location(LOCATION_CODE_START + fungal_forest_location_start + 15, FungalForest.blue_jelly, FlipwitchRegion.deep_fungal),
    create_location(LOCATION_CODE_START + fungal_forest_location_start + 16, FungalForest.fungal_door_key, FlipwitchRegion.deep_fungal),
    create_location(LOCATION_CODE_START + fungal_forest_location_start + 17, FungalForest.secret_fungus, FlipwitchRegion.deep_fungal),
    create_location(LOCATION_CODE_START + fungal_forest_location_start + 18, FungalForest.slime_form, FlipwitchRegion.deep_fungal),
    create_location(LOCATION_CODE_START + fungal_forest_location_start + 19, FungalForest.slime_citadel_key, FlipwitchRegion.deep_fungal),
    create_location(LOCATION_CODE_START + fungal_forest_location_start + 20, FungalForest.fungal_deal, FlipwitchRegion.deep_fungal),
    create_location(LOCATION_CODE_START + fungal_forest_location_start + 21, FungalForest.slime_tutorial, FlipwitchRegion.deep_fungal),
]

slime_citadel_location_start = 450
slime_citadel_locations = [
    create_location(LOCATION_CODE_START + slime_citadel_location_start + 1, SlimeCitadel.citadel_entrance, FlipwitchRegion.slime_citadel),
    create_location(LOCATION_CODE_START + slime_citadel_location_start + 2, SlimeCitadel.secret_room, FlipwitchRegion.slime_citadel),
    create_location(LOCATION_CODE_START + slime_citadel_location_start + 3, SlimeCitadel.lone_room, FlipwitchRegion.slime_citadel),
    create_location(LOCATION_CODE_START + slime_citadel_location_start + 4, SlimeCitadel.silky_slime_chest, FlipwitchRegion.slime_citadel),
    create_location(LOCATION_CODE_START + slime_citadel_location_start + 5, SlimeCitadel.silky_slime_stone, FlipwitchRegion.slime_citadel),
    create_location(LOCATION_CODE_START + slime_citadel_location_start + 6, SlimeCitadel.small_detour, FlipwitchRegion.slime_citadel),
    create_location(LOCATION_CODE_START + slime_citadel_location_start + 7, SlimeCitadel.slimy_sub_chest, FlipwitchRegion.slime_citadel),
    create_location(LOCATION_CODE_START + slime_citadel_location_start + 8, SlimeCitadel.across_key, FlipwitchRegion.slime_citadel),
    create_location(LOCATION_CODE_START + slime_citadel_location_start + 9, SlimeCitadel.thimble_1, FlipwitchRegion.slime_citadel),
    create_location(LOCATION_CODE_START + slime_citadel_location_start + 10, SlimeCitadel.thimble_2, FlipwitchRegion.slime_citadel),
    create_location(LOCATION_CODE_START + slime_citadel_location_start + 11, SlimeCitadel.slimy_gauntlet, FlipwitchRegion.slime_citadel),
    create_location(LOCATION_CODE_START + slime_citadel_location_start + 12, SlimeCitadel.near_stone, FlipwitchRegion.slime_citadel),
    create_location(LOCATION_CODE_START + slime_citadel_location_start + 13, SlimeCitadel.secret_spring_coin, FlipwitchRegion.slime_citadel),
    create_location(LOCATION_CODE_START + slime_citadel_location_start + 14, SlimeCitadel.secret_spring_stone, FlipwitchRegion.slime_citadel),
    create_location(LOCATION_CODE_START + slime_citadel_location_start + 15, SlimeCitadel.hidden_tunnel, FlipwitchRegion.slime_citadel),
    create_location(LOCATION_CODE_START + slime_citadel_location_start + 16, SlimeCitadel.elf_1, FlipwitchRegion.slime_citadel),
    create_location(LOCATION_CODE_START + slime_citadel_location_start + 17, SlimeCitadel.elf_2, FlipwitchRegion.slime_citadel),
    create_location(LOCATION_CODE_START + slime_citadel_location_start + 18, SlimeCitadel.slurp_chest, FlipwitchRegion.slime_citadel),
    create_location(LOCATION_CODE_START + slime_citadel_location_start + 19, SlimeCitadel.slurp_stone, FlipwitchRegion.slime_citadel),
    create_location(LOCATION_CODE_START + slime_citadel_location_start + 20, SlimeCitadel.slimy_princess_chaos, FlipwitchRegion.slime_citadel),
    create_location(LOCATION_CODE_START + slime_citadel_location_start + 21, SlimeCitadel.slimy_princess_mp, FlipwitchRegion.slime_citadel),
]

umi_umi_location_start = 500
umi_umi_locations = [
    create_location(LOCATION_CODE_START + umi_umi_location_start + 1, UmiUmi.early_coin, FlipwitchRegion.umi_umi),
    create_location(LOCATION_CODE_START + umi_umi_location_start + 2, UmiUmi.save_chest, FlipwitchRegion.umi_umi),
    create_location(LOCATION_CODE_START + umi_umi_location_start + 3, UmiUmi.angler_costume, FlipwitchRegion.umi_umi),
    create_location(LOCATION_CODE_START + umi_umi_location_start + 4, UmiUmi.flip_magic_chest, FlipwitchRegion.umi_umi),
    create_location(LOCATION_CODE_START + umi_umi_location_start + 5, UmiUmi.far_corner, FlipwitchRegion.umi_umi),
    create_location(LOCATION_CODE_START + umi_umi_location_start + 6, UmiUmi.sacrificial_dagger, FlipwitchRegion.umi_umi),
    create_location(LOCATION_CODE_START + umi_umi_location_start + 7, UmiUmi.flip_magic_coin, FlipwitchRegion.umi_umi),
    create_location(LOCATION_CODE_START + umi_umi_location_start + 8, UmiUmi.mermaid_chest, FlipwitchRegion.umi_umi_depths),
    create_location(LOCATION_CODE_START + umi_umi_location_start + 9, UmiUmi.chaos_fight, FlipwitchRegion.umi_umi_depths),
    create_location(LOCATION_CODE_START + umi_umi_location_start + 10, UmiUmi.above_save, FlipwitchRegion.umi_umi_depths),
    create_location(LOCATION_CODE_START + umi_umi_location_start + 11, UmiUmi.octrina_path, FlipwitchRegion.umi_umi_depths),
    create_location(LOCATION_CODE_START + umi_umi_location_start + 12, UmiUmi.octrina_chest, FlipwitchRegion.umi_umi_depths),
    create_location(LOCATION_CODE_START + umi_umi_location_start + 13, UmiUmi.watery_gauntlet, FlipwitchRegion.umi_umi_depths),
    create_location(LOCATION_CODE_START + umi_umi_location_start + 14, UmiUmi.frog_boss_path, FlipwitchRegion.umi_umi_depths),
    create_location(LOCATION_CODE_START + umi_umi_location_start + 15, UmiUmi.frog_boss_chaos, FlipwitchRegion.umi_umi_depths),
    create_location(LOCATION_CODE_START + umi_umi_location_start + 16, UmiUmi.frog_boss_mp, FlipwitchRegion.umi_umi_depths),
]

chaos_castle_location_start = 550
chaos_castle_locations = [
    create_location(LOCATION_CODE_START + chaos_castle_location_start + 1, ChaosCastle.outside_coin, FlipwitchRegion.outside_chaos),
    create_location(LOCATION_CODE_START + chaos_castle_location_start + 2, ChaosCastle.early_chest, FlipwitchRegion.chaos_castle),
    create_location(LOCATION_CODE_START + chaos_castle_location_start + 3, ChaosCastle.goblin_coin, FlipwitchRegion.chaos_castle),
    create_location(LOCATION_CODE_START + chaos_castle_location_start + 4, ChaosCastle.ghost_coin, FlipwitchRegion.chaos_castle),
    create_location(LOCATION_CODE_START + chaos_castle_location_start + 5, ChaosCastle.jigoku_coin, FlipwitchRegion.chaos_castle),
    create_location(LOCATION_CODE_START + chaos_castle_location_start + 6, ChaosCastle.sanctum, FlipwitchRegion.chaos_castle),
    create_location(LOCATION_CODE_START + chaos_castle_location_start + 7, ChaosCastle.elf_1, FlipwitchRegion.chaos_castle),
    create_location(LOCATION_CODE_START + chaos_castle_location_start + 8, ChaosCastle.elf_chest, FlipwitchRegion.chaos_castle),
    create_location(LOCATION_CODE_START + chaos_castle_location_start + 9, ChaosCastle.citadel, FlipwitchRegion.chaos_castle),
    create_location(LOCATION_CODE_START + chaos_castle_location_start + 10, ChaosCastle.fungal, FlipwitchRegion.chaos_castle),
    create_location(LOCATION_CODE_START + chaos_castle_location_start + 11, ChaosCastle.jump_hp, FlipwitchRegion.chaos_castle),
    create_location(LOCATION_CODE_START + chaos_castle_location_start + 12, ChaosCastle.jump_chest, FlipwitchRegion.chaos_castle),
    create_location(LOCATION_CODE_START + chaos_castle_location_start + 13, ChaosCastle.pandora_key, FlipwitchRegion.chaos_castle),
    create_location(LOCATION_CODE_START + chaos_castle_location_start + 14, ChaosCastle.pandora_mp, FlipwitchRegion.chaos_castle),
    create_location(LOCATION_CODE_START + chaos_castle_location_start + 15, ChaosCastle.chaos, FlipwitchRegion.chaos_castle),
]

quest_location_start = 600
quest_locations = [
    create_location(LOCATION_CODE_START + quest_location_start + 1, Quest.magic_mentor, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + quest_location_start + 2, Quest.need_my_cowbell, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + quest_location_start + 3, Quest.giant_chest_key, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + quest_location_start + 4, Quest.model_goblin, FlipwitchRegion.witch_woods_lower),
    create_location(LOCATION_CODE_START + quest_location_start + 5, Quest.fairy_mushroom, FlipwitchRegion.witch_woods_lower),
    create_location(LOCATION_CODE_START + quest_location_start + 6, Quest.out_of_service, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + quest_location_start + 7, Quest.bunny_club, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + quest_location_start + 8, Quest.silky_slime, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + quest_location_start + 9, Quest.panty_raid, FlipwitchRegion.ghost_rose),
    create_location(LOCATION_CODE_START + quest_location_start + 10, Quest.unlucky_cat, FlipwitchRegion.jigoku),
    create_location(LOCATION_CODE_START + quest_location_start + 11, Quest.harvest_season, FlipwitchRegion.jigoku),
    create_location(LOCATION_CODE_START + quest_location_start + 12, Quest.long_distance, FlipwitchRegion.angelic_hallway),
    create_location(LOCATION_CODE_START + quest_location_start + 13, Quest.summoning_stones, FlipwitchRegion.slime_citadel),
    create_location(LOCATION_CODE_START + quest_location_start + 14, Quest.semen_with_a, FlipwitchRegion.umi_umi),
    create_location(LOCATION_CODE_START + quest_location_start + 15, Quest.cardio_day, FlipwitchRegion.shady_sewers),
    create_location(LOCATION_CODE_START + quest_location_start + 16, Quest.stop_democracy, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + quest_location_start + 17, Quest.medical_emergency, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + quest_location_start + 18, Quest.let_the_dog_out, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + quest_location_start + 19, Quest.rat_problem, FlipwitchRegion.cabaret_cafe),
    create_location(LOCATION_CODE_START + quest_location_start + 20, Quest.ghost_hunters, FlipwitchRegion.cabaret_cafe),
    create_location(LOCATION_CODE_START + quest_location_start + 21, Quest.haunted_bedroom, FlipwitchRegion.cabaret_cafe),
    create_location(LOCATION_CODE_START + quest_location_start + 22, Quest.ectogasm, FlipwitchRegion.cabaret_cafe),
    create_location(LOCATION_CODE_START + quest_location_start + 23, Quest.jelly_mushroom, FlipwitchRegion.cabaret_cafe),
    create_location(LOCATION_CODE_START + quest_location_start + 24, Quest.booze_bunny, FlipwitchRegion.cabaret_cafe),
    create_location(LOCATION_CODE_START + quest_location_start + 25, Quest.help_wanted, FlipwitchRegion.cabaret_cafe),
    create_location(LOCATION_CODE_START + quest_location_start + 26, Quest.deluxe_milkshake, FlipwitchRegion.cabaret_cafe),
    create_location(LOCATION_CODE_START + quest_location_start + 27, Quest.boned, FlipwitchRegion.cabaret_cafe),
    create_location(LOCATION_CODE_START + quest_location_start + 28, Quest.legendary_chewtoy, FlipwitchRegion.cabaret_cafe),
    create_location(LOCATION_CODE_START + quest_location_start + 29, Quest.tatils_tale, FlipwitchRegion.pig_mansion),
    create_location(LOCATION_CODE_START + quest_location_start + 30, Quest.signing_bonus, FlipwitchRegion.pig_mansion),
    create_location(LOCATION_CODE_START + quest_location_start + 31, Quest.emotional_baggage, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + quest_location_start + 32, Quest.dirty_debut, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + quest_location_start + 34, Quest.devilicious, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + quest_location_start + 35, Quest.daikon, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + quest_location_start + 36, Quest.alley_cat, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + quest_location_start + 37, Quest.whorus, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + quest_location_start + 38, Quest.priest, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + quest_location_start + 39, Quest.goblin_stud, FlipwitchRegion.witch_woods_lower)
]

gacha_location_start = 650
gacha_locations = [
    create_location(LOCATION_CODE_START + gacha_location_start + 1, Gacha.gacha_sp1, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + gacha_location_start + 2, Gacha.gacha_ag1, FlipwitchRegion.cabaret_cafe),
    create_location(LOCATION_CODE_START + gacha_location_start + 3, Gacha.gacha_ag2, FlipwitchRegion.cabaret_cafe),
    create_location(LOCATION_CODE_START + gacha_location_start + 4, Gacha.gacha_ag3, FlipwitchRegion.cabaret_cafe),
    create_location(LOCATION_CODE_START + gacha_location_start + 5, Gacha.gacha_ag4, FlipwitchRegion.cabaret_cafe),
    create_location(LOCATION_CODE_START + gacha_location_start + 6, Gacha.gacha_ag5, FlipwitchRegion.cabaret_cafe),
    create_location(LOCATION_CODE_START + gacha_location_start + 7, Gacha.gacha_ag6, FlipwitchRegion.cabaret_cafe),
    create_location(LOCATION_CODE_START + gacha_location_start + 8, Gacha.gacha_ag7, FlipwitchRegion.cabaret_cafe),
    create_location(LOCATION_CODE_START + gacha_location_start + 9, Gacha.gacha_ag8, FlipwitchRegion.cabaret_cafe),
    create_location(LOCATION_CODE_START + gacha_location_start + 10, Gacha.gacha_ag9, FlipwitchRegion.cabaret_cafe),
    create_location(LOCATION_CODE_START + gacha_location_start + 11, Gacha.gacha_ag0, FlipwitchRegion.cabaret_cafe),
    create_location(LOCATION_CODE_START + gacha_location_start + 12, Gacha.gacha_bg1, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + gacha_location_start + 13, Gacha.gacha_bg2, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + gacha_location_start + 14, Gacha.gacha_bg3, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + gacha_location_start + 15, Gacha.gacha_bg4, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + gacha_location_start + 16, Gacha.gacha_bg5, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + gacha_location_start + 17, Gacha.gacha_bg6, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + gacha_location_start + 18, Gacha.gacha_bg7, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + gacha_location_start + 19, Gacha.gacha_bg8, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + gacha_location_start + 20, Gacha.gacha_bg9, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + gacha_location_start + 21, Gacha.gacha_bg0, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + gacha_location_start + 22, Gacha.gacha_ad1, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + gacha_location_start + 23, Gacha.gacha_ad2, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + gacha_location_start + 24, Gacha.gacha_ad3, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + gacha_location_start + 25, Gacha.gacha_ad4, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + gacha_location_start + 26, Gacha.gacha_ad5, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + gacha_location_start + 27, Gacha.gacha_ad6, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + gacha_location_start + 28, Gacha.gacha_ad7, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + gacha_location_start + 29, Gacha.gacha_ad8, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + gacha_location_start + 30, Gacha.gacha_ad9, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + gacha_location_start + 31, Gacha.gacha_ad0, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + gacha_location_start + 32, Gacha.gacha_mg1, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + gacha_location_start + 33, Gacha.gacha_mg2, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + gacha_location_start + 34, Gacha.gacha_mg3, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + gacha_location_start + 35, Gacha.gacha_mg4, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + gacha_location_start + 36, Gacha.gacha_mg5, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + gacha_location_start + 37, Gacha.gacha_mg6, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + gacha_location_start + 38, Gacha.gacha_mg7, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + gacha_location_start + 39, Gacha.gacha_mg8, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + gacha_location_start + 40, Gacha.gacha_mg9, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + gacha_location_start + 41, Gacha.gacha_mg0, FlipwitchRegion.spirit_town),
]

crystal_panel_location_start = 700
crystal_panel_locations = [
    create_location(LOCATION_CODE_START + crystal_panel_location_start + 1, CrystalPanel.sensei, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + crystal_panel_location_start + 2, CrystalPanel.witchy, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + crystal_panel_location_start + 3, CrystalPanel.goblin, FlipwitchRegion.witch_woods_lower),
    create_location(LOCATION_CODE_START + crystal_panel_location_start + 4, CrystalPanel.spirit, FlipwitchRegion.spirit_town),
    create_location(LOCATION_CODE_START + crystal_panel_location_start + 5, CrystalPanel.shady, FlipwitchRegion.shady_sewers),
    create_location(LOCATION_CODE_START + crystal_panel_location_start + 6, CrystalPanel.ghost_entrance, FlipwitchRegion.early_ghost),
    create_location(LOCATION_CODE_START + crystal_panel_location_start + 7, CrystalPanel.ghost_castle, FlipwitchRegion.ghost_rose),
    create_location(LOCATION_CODE_START + crystal_panel_location_start + 8, CrystalPanel.jigoku, FlipwitchRegion.jigoku),
    create_location(LOCATION_CODE_START + crystal_panel_location_start + 9, CrystalPanel.club_demon, FlipwitchRegion.club_demon),
    create_location(LOCATION_CODE_START + crystal_panel_location_start + 10, CrystalPanel.tengoku, FlipwitchRegion.tengoku_upper),
    create_location(LOCATION_CODE_START + crystal_panel_location_start + 11, CrystalPanel.angelic_hallway, FlipwitchRegion.angelic_hallway),
    create_location(LOCATION_CODE_START + crystal_panel_location_start + 12, CrystalPanel.fungal_forest, FlipwitchRegion.fungal_forest),
    create_location(LOCATION_CODE_START + crystal_panel_location_start + 13, CrystalPanel.slime_citadel, FlipwitchRegion.slime_citadel),
    create_location(LOCATION_CODE_START + crystal_panel_location_start + 14, CrystalPanel.slimy_depths, FlipwitchRegion.slime_citadel),
    create_location(LOCATION_CODE_START + crystal_panel_location_start + 15, CrystalPanel.umi_umi, FlipwitchRegion.umi_umi),
    create_location(LOCATION_CODE_START + crystal_panel_location_start + 16, CrystalPanel.chaos_castle, FlipwitchRegion.chaos_castle),
]

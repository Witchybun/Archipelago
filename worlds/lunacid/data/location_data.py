from dataclasses import dataclass
from typing import Optional, List

from ..strings.locations import BaseLocation, ShopLocation, DropLocation
from ..strings.regions_entrances import LunacidRegion


@dataclass(frozen=True)
class LunacidLocation:
    location_id: Optional[int]
    name: str
    region: str


all_locations = []


# Some locations vary on multiple regions, so we default to Hollow Basin first.
def create_location(location_id: Optional[int], name: str, region: Optional[str] = LunacidRegion.hollow_basin):
    location = LunacidLocation(location_id, name, region)
    if location_id is not None:
        all_locations.append(location)
    return location


# Uses a structure of BASE LOCATION + type offset + pseudo value.  The base location ID will eventually be deprecated in favor of starting at 1.
LOCATION_CODE_START = 771111110
base_location_start = 0
wings_rest = [
    create_location(LOCATION_CODE_START + base_location_start + 1, BaseLocation.wings_rest_ocean_elixir, LunacidRegion.wings_rest),
    create_location(LOCATION_CODE_START + base_location_start + 2, BaseLocation.wings_rest_crystal_shard, LunacidRegion.wings_rest),
    create_location(LOCATION_CODE_START + base_location_start + 3, BaseLocation.wings_rest_clives_gift, LunacidRegion.wings_rest),
    create_location(LOCATION_CODE_START + base_location_start + 4, BaseLocation.wings_rest_demi_orb, LunacidRegion.wings_rest),
    create_location(LOCATION_CODE_START + base_location_start + 5, BaseLocation.wings_rest_demi_gift, LunacidRegion.wings_rest),
]

hollow_basin = [
    create_location(LOCATION_CODE_START + base_location_start + 9, BaseLocation.hollow_basin_starting_sword, LunacidRegion.hollow_basin),
    create_location(LOCATION_CODE_START + base_location_start + 10, BaseLocation.hollow_basin_right_water_right, LunacidRegion.hollow_basin),
    create_location(LOCATION_CODE_START + base_location_start + 11, BaseLocation.hollow_basin_right_water_left, LunacidRegion.hollow_basin),
    create_location(LOCATION_CODE_START + base_location_start + 12, BaseLocation.hollow_basin_left_water, LunacidRegion.hollow_basin),
    create_location(LOCATION_CODE_START + base_location_start + 13, BaseLocation.hollow_basin_demi_chest, LunacidRegion.hollow_basin),
    create_location(LOCATION_CODE_START + base_location_start + 14, BaseLocation.hollow_basin_enchanted_door, LunacidRegion.hollow_basin),
    create_location(LOCATION_CODE_START + base_location_start + 15, BaseLocation.hollow_basin_dark_item, LunacidRegion.hollow_basin),

    create_location(LOCATION_CODE_START + base_location_start + 16, BaseLocation.temple_fountain, LunacidRegion.temple_of_silence_entrance),
    create_location(LOCATION_CODE_START + base_location_start + 17, BaseLocation.temple_ritual_table, LunacidRegion.temple_of_silence_entrance),
    create_location(LOCATION_CODE_START + base_location_start + 18, BaseLocation.temple_altar_chest, LunacidRegion.temple_of_silence_entrance),
    create_location(LOCATION_CODE_START + base_location_start + 19, BaseLocation.temple_pillar_left, LunacidRegion.temple_of_silence_secret),
    create_location(LOCATION_CODE_START + base_location_start + 20, BaseLocation.temple_pillar_right, LunacidRegion.temple_of_silence_secret),
    create_location(LOCATION_CODE_START + base_location_start + 21, BaseLocation.temple_ritual_ring, LunacidRegion.temple_of_silence_interior),
    create_location(LOCATION_CODE_START + base_location_start + 22, BaseLocation.temple_small_pillar, LunacidRegion.temple_of_silence_interior),
    create_location(LOCATION_CODE_START + base_location_start + 23, BaseLocation.temple_pillar_room_left, LunacidRegion.temple_of_silence_secret),
    create_location(LOCATION_CODE_START + base_location_start + 24, BaseLocation.temple_pillar_room_back_left, LunacidRegion.temple_of_silence_secret),
    create_location(LOCATION_CODE_START + base_location_start + 25, BaseLocation.temple_pillar_room_back_right, LunacidRegion.temple_of_silence_secret),
    create_location(LOCATION_CODE_START + base_location_start + 26, BaseLocation.temple_pillar_room_hidden_room, LunacidRegion.temple_of_silence_secret),
    create_location(LOCATION_CODE_START + base_location_start + 27, BaseLocation.temple_hidden_room_in_sewer, LunacidRegion.temple_of_silence_secret),
    create_location(LOCATION_CODE_START + base_location_start + 28, BaseLocation.temple_table_in_sewer, LunacidRegion.temple_of_silence_interior),
    create_location(LOCATION_CODE_START + base_location_start + 29, BaseLocation.temple_sewer_puzzle, LunacidRegion.temple_of_silence_interior),
    create_location(LOCATION_CODE_START + base_location_start + 30, BaseLocation.temple_blood_altar, LunacidRegion.temple_of_silence_interior),
    create_location(LOCATION_CODE_START + base_location_start + 31, BaseLocation.temple_path_to_forest, LunacidRegion.temple_of_silence_interior),
]

the_fetid_mire = [
    create_location(LOCATION_CODE_START + base_location_start + 37, BaseLocation.mire_room_left_foyer, LunacidRegion.fetid_mire),
    create_location(LOCATION_CODE_START + base_location_start + 38, BaseLocation.mire_hidden_slime_chest, LunacidRegion.fetid_mire_secret),
    create_location(LOCATION_CODE_START + base_location_start + 39, BaseLocation.mire_upper_overlook_left, LunacidRegion.fetid_mire_secret),
    create_location(LOCATION_CODE_START + base_location_start + 40, BaseLocation.mire_upper_overlook_right, LunacidRegion.fetid_mire_secret),
    create_location(LOCATION_CODE_START + base_location_start + 41, BaseLocation.mire_bonenard_trash, LunacidRegion.fetid_mire),
    create_location(LOCATION_CODE_START + base_location_start + 42, BaseLocation.mire_rubble_bridge, LunacidRegion.fetid_mire),
    create_location(LOCATION_CODE_START + base_location_start + 43, BaseLocation.mire_skeleton_chest, LunacidRegion.fetid_mire),
    create_location(LOCATION_CODE_START + base_location_start + 44, BaseLocation.mire_jellisha_trash, LunacidRegion.fetid_mire_secret),
    create_location(LOCATION_CODE_START + base_location_start + 45, BaseLocation.mire_jellisha_reward, LunacidRegion.fetid_mire_secret),
    create_location(LOCATION_CODE_START + base_location_start + 46, BaseLocation.mire_path_to_sea_left, LunacidRegion.fetid_mire),
    create_location(LOCATION_CODE_START + base_location_start + 47, BaseLocation.mire_path_to_sea_right, LunacidRegion.fetid_mire),
    create_location(LOCATION_CODE_START + base_location_start + 48, BaseLocation.mire_hidden_chest_near_underworks, LunacidRegion.fetid_mire_secret),
    create_location(LOCATION_CODE_START + base_location_start + 49, BaseLocation.mire_rubble_near_illusory_wall, LunacidRegion.fetid_mire),
    create_location(LOCATION_CODE_START + base_location_start + 50, BaseLocation.mire_underwater_pipe, LunacidRegion.fetid_mire),
    create_location(LOCATION_CODE_START + base_location_start + 51, BaseLocation.mire_underworks_waterfall, LunacidRegion.fetid_mire),
    create_location(LOCATION_CODE_START + base_location_start + 52, BaseLocation.mire_underworks_skeleton, LunacidRegion.fetid_mire),
]

the_sanguine_sea = [
    create_location(LOCATION_CODE_START + base_location_start + 58, BaseLocation.sea_pillar, LunacidRegion.sanguine_sea),
    create_location(LOCATION_CODE_START + base_location_start + 59, BaseLocation.sea_underblood, LunacidRegion.sanguine_sea),
    create_location(LOCATION_CODE_START + base_location_start + 60, BaseLocation.sea_fairy_circle, LunacidRegion.sanguine_sea),
    create_location(LOCATION_CODE_START + base_location_start + 61, BaseLocation.sea_kill_jotunn, LunacidRegion.sanguine_sea)]

accursed_tomb = [
    create_location(LOCATION_CODE_START + base_location_start + 67, BaseLocation.catacombs_coffin_stairs, LunacidRegion.accursed_tomb),
    create_location(LOCATION_CODE_START + base_location_start + 68, BaseLocation.catacombs_coffin_blue_light, LunacidRegion.accursed_tomb),
    create_location(LOCATION_CODE_START + base_location_start + 69, BaseLocation.corrupted_room, LunacidRegion.accursed_tomb),
    create_location(LOCATION_CODE_START + base_location_start + 70, BaseLocation.catacombs_coffin_gate, LunacidRegion.accursed_tomb),
    create_location(LOCATION_CODE_START + base_location_start + 71, BaseLocation.catacombs_hidden_room, LunacidRegion.vampire_tomb),
    create_location(LOCATION_CODE_START + base_location_start + 72, BaseLocation.catacombs_deep_coffin_storage, LunacidRegion.vampire_tomb),
    create_location(LOCATION_CODE_START + base_location_start + 73, BaseLocation.catacombs_restore_vampire, LunacidRegion.vampire_tomb),

    create_location(LOCATION_CODE_START + base_location_start + 74, BaseLocation.mausoleum_hidden_chest, LunacidRegion.mausoleum),
    create_location(LOCATION_CODE_START + base_location_start + 75, BaseLocation.mausoleum_upper_table, LunacidRegion.mausoleum),
    create_location(LOCATION_CODE_START + base_location_start + 76, BaseLocation.mausoleum_maze_intro, LunacidRegion.mausoleum),
    create_location(LOCATION_CODE_START + base_location_start + 77, BaseLocation.mausoleum_maze_mid, LunacidRegion.mausoleum),
    create_location(LOCATION_CODE_START + base_location_start + 78, BaseLocation.mausoleum_center_right, LunacidRegion.mausoleum),
    create_location(LOCATION_CODE_START + base_location_start + 79, BaseLocation.mausoleum_center_left, LunacidRegion.mausoleum),
    create_location(LOCATION_CODE_START + base_location_start + 80, BaseLocation.mausoleum_center_back, LunacidRegion.mausoleum),
    create_location(LOCATION_CODE_START + base_location_start + 81, BaseLocation.mausoleum_center_left_path, LunacidRegion.mausoleum),
    create_location(LOCATION_CODE_START + base_location_start + 82, BaseLocation.mausoleum_center_right_path, LunacidRegion.mausoleum),
    create_location(LOCATION_CODE_START + base_location_start + 83, BaseLocation.mausoleum_kill_death, LunacidRegion.mausoleum),

    create_location(LOCATION_CODE_START + base_location_start + 84, BaseLocation.tomb_tomb_with_switch, LunacidRegion.accursed_tomb),
    create_location(LOCATION_CODE_START + base_location_start + 85, BaseLocation.tomb_tomb_with_corpse, LunacidRegion.accursed_tomb),
    create_location(LOCATION_CODE_START + base_location_start + 86, BaseLocation.tomb_demi_chest, LunacidRegion.accursed_tomb),
    create_location(LOCATION_CODE_START + base_location_start + 87, BaseLocation.tomb_near_light_switch, LunacidRegion.accursed_tomb),
    create_location(LOCATION_CODE_START + base_location_start + 88, BaseLocation.tomb_hidden_room, LunacidRegion.accursed_tomb),
    create_location(LOCATION_CODE_START + base_location_start + 89, BaseLocation.tomb_hidden_chest, LunacidRegion.accursed_tomb)
]

yosei_forest = [
    create_location(LOCATION_CODE_START + base_location_start + 94, BaseLocation.yosei_barrels, LunacidRegion.yosei_forest),
    create_location(LOCATION_CODE_START + base_location_start + 95, BaseLocation.yosei_blood_pool, LunacidRegion.yosei_forest),
    create_location(LOCATION_CODE_START + base_location_start + 96, BaseLocation.yosei_branch_in_tree, LunacidRegion.yosei_forest),
    create_location(LOCATION_CODE_START + base_location_start + 97, BaseLocation.yosei_chest_near_tree, LunacidRegion.yosei_forest),
    create_location(LOCATION_CODE_START + base_location_start + 98, BaseLocation.yosei_blood_plant_insides, LunacidRegion.yosei_forest),
    create_location(LOCATION_CODE_START + base_location_start + 99, BaseLocation.yosei_hanging_in_trees, LunacidRegion.yosei_forest),
    create_location(LOCATION_CODE_START + base_location_start + 100, BaseLocation.yosei_hidden_chest, LunacidRegion.yosei_lower),
    create_location(LOCATION_CODE_START + base_location_start + 101, BaseLocation.yosei_room_defended_by_blood_plant, LunacidRegion.yosei_lower),
    create_location(LOCATION_CODE_START + base_location_start + 102, BaseLocation.yosei_patchouli_key, LunacidRegion.yosei_lower),
    create_location(LOCATION_CODE_START + base_location_start + 103, BaseLocation.yosei_patchouli_quest, LunacidRegion.yosei_lower),
]

forest_canopy = [
    create_location(LOCATION_CODE_START + base_location_start + 109, BaseLocation.canopy_branch_edge, LunacidRegion.forest_canopy),
    create_location(LOCATION_CODE_START + base_location_start + 110, BaseLocation.branch_cave, LunacidRegion.forest_canopy),
    create_location(LOCATION_CODE_START + base_location_start + 111, BaseLocation.canopy_chest, LunacidRegion.forest_canopy),
    create_location(LOCATION_CODE_START + base_location_start + 112, BaseLocation.canopy_wooden_statue, LunacidRegion.forest_canopy),
    create_location(LOCATION_CODE_START + base_location_start + 113, BaseLocation.canopy_wooden_sitting, LunacidRegion.forest_canopy),
]

forbidden_archives = [
    create_location(LOCATION_CODE_START + base_location_start + 119, BaseLocation.archives_back_room_past_bridge, LunacidRegion.forbidden_archives_2),
    create_location(LOCATION_CODE_START + base_location_start + 120, BaseLocation.archives_strange_corpse, LunacidRegion.forbidden_archives_2),
    create_location(LOCATION_CODE_START + base_location_start + 121, BaseLocation.archives_against_wall_near_trees, LunacidRegion.forbidden_archives_1),
    create_location(LOCATION_CODE_START + base_location_start + 122, BaseLocation.archives_short_wall_near_trees, LunacidRegion.forbidden_archives_1),
    create_location(LOCATION_CODE_START + base_location_start + 123, BaseLocation.archives_snail_lectern_near, LunacidRegion.forbidden_archives_3),
    create_location(LOCATION_CODE_START + base_location_start + 124, BaseLocation.archives_snail_lectern_far, LunacidRegion.forbidden_archives_3),
    create_location(LOCATION_CODE_START + base_location_start + 125, BaseLocation.archives_rug_on_balcony, LunacidRegion.forbidden_archives_3),
    create_location(LOCATION_CODE_START + base_location_start + 126, BaseLocation.archives_rooftop, LunacidRegion.forbidden_archives_3),
    create_location(LOCATION_CODE_START + base_location_start + 127, BaseLocation.archives_hidden_room_upper, LunacidRegion.forbidden_archives_3),
    create_location(LOCATION_CODE_START + base_location_start + 128, BaseLocation.archives_hidden_room_lower, LunacidRegion.forbidden_archives_1b),
    create_location(LOCATION_CODE_START + base_location_start + 129, BaseLocation.archives_near_twisty_tree, LunacidRegion.forbidden_archives_1b),
    create_location(LOCATION_CODE_START + base_location_start + 130, BaseLocation.archives_uwu, LunacidRegion.forbidden_archives_1b),
    create_location(LOCATION_CODE_START + base_location_start + 131, BaseLocation.archives_daedalus_one, LunacidRegion.daedalus),
    create_location(LOCATION_CODE_START + base_location_start + 132, BaseLocation.archives_daedalus_two, LunacidRegion.daedalus),
    create_location(LOCATION_CODE_START + base_location_start + 133, BaseLocation.archives_daedalus_third, LunacidRegion.daedalus),
    create_location(LOCATION_CODE_START + base_location_start + 134, BaseLocation.archives_corner_near_daedalus, LunacidRegion.forbidden_archives_1b),
]

castle_le_fanu = [
    create_location(LOCATION_CODE_START + base_location_start + 140, BaseLocation.castle_outside_corner, LunacidRegion.castle_le_fanu),
    create_location(LOCATION_CODE_START + base_location_start + 141, BaseLocation.castle_cell_south, LunacidRegion.castle_le_fanu_red),
    create_location(LOCATION_CODE_START + base_location_start + 142, BaseLocation.castle_cell_west, LunacidRegion.castle_le_fanu_red),
    create_location(LOCATION_CODE_START + base_location_start + 143, BaseLocation.castle_cell_center, LunacidRegion.castle_le_fanu_red),
    create_location(LOCATION_CODE_START + base_location_start + 144, BaseLocation.castle_cell_north, LunacidRegion.castle_le_fanu_red),
    create_location(LOCATION_CODE_START + base_location_start + 145, BaseLocation.castle_hidden_cell, LunacidRegion.castle_le_fanu_red),

    create_location(LOCATION_CODE_START + base_location_start + 146, BaseLocation.castle_hallway_rubble_room, LunacidRegion.castle_le_fanu_white),
    create_location(LOCATION_CODE_START + base_location_start + 147, BaseLocation.castle_hallway_dining_room, LunacidRegion.castle_le_fanu_white),
    create_location(LOCATION_CODE_START + base_location_start + 148, BaseLocation.castle_garrat_resting_room_left, LunacidRegion.castle_le_fanu_white),
    create_location(LOCATION_CODE_START + base_location_start + 149, BaseLocation.castle_garrat_resting_room_back, LunacidRegion.castle_le_fanu_white),
    create_location(LOCATION_CODE_START + base_location_start + 150, BaseLocation.castle_hallway_deadend_before_door, LunacidRegion.castle_le_fanu_white),
    create_location(LOCATION_CODE_START + base_location_start + 151, BaseLocation.castle_upper_floor_coffin_small, LunacidRegion.castle_le_fanu_blue),
    create_location(LOCATION_CODE_START + base_location_start + 152, BaseLocation.castle_upper_floor_coffin_large, LunacidRegion.castle_le_fanu_blue),
    create_location(LOCATION_CODE_START + base_location_start + 153, BaseLocation.castle_upper_floor_coffin_double, LunacidRegion.castle_le_fanu_blue),
    create_location(LOCATION_CODE_START + base_location_start + 154, BaseLocation.castle_upper_floor_coffin_hallway, LunacidRegion.castle_le_fanu_blue),
]

sealed_ballroom = [
    create_location(LOCATION_CODE_START + base_location_start + 166, BaseLocation.ballroom_small_room_lounge, LunacidRegion.sealed_ballroom),
    create_location(LOCATION_CODE_START + base_location_start + 167, BaseLocation.ballroom_entry_hidden_couch_top, LunacidRegion.sealed_ballroom_secret),
    create_location(LOCATION_CODE_START + base_location_start + 168, BaseLocation.ballroom_entry_hidden_couch_bottom, LunacidRegion.sealed_ballroom_secret),
    create_location(LOCATION_CODE_START + base_location_start + 169, BaseLocation.ballroom_entry_hidden_cave_in_lounge, LunacidRegion.sealed_ballroom_secret),
    create_location(LOCATION_CODE_START + base_location_start + 170, BaseLocation.ballroom_entry_long_table, LunacidRegion.sealed_ballroom),
    create_location(LOCATION_CODE_START + base_location_start + 171, BaseLocation.ballroom_side_hidden_cave, LunacidRegion.sealed_ballroom_secret),
    create_location(LOCATION_CODE_START + base_location_start + 172, BaseLocation.ballroom_side_chest_near_switch, LunacidRegion.sealed_ballroom),
    create_location(LOCATION_CODE_START + base_location_start + 173, BaseLocation.ballroom_side_painting, LunacidRegion.sealed_ballroom),
    create_location(LOCATION_CODE_START + base_location_start + 174, BaseLocation.ballroom_side_hidden_casket_room, LunacidRegion.sealed_ballroom_secret),
    create_location(LOCATION_CODE_START + base_location_start + 175, BaseLocation.ballroom_side_xp_drain, LunacidRegion.sealed_ballroom),
]

laetus_chasm = [
    create_location(LOCATION_CODE_START + base_location_start + 181, BaseLocation.chasm_hidden_chest, LunacidRegion.laetus_chasm),
    create_location(LOCATION_CODE_START + base_location_start + 182, BaseLocation.chasm_invisible_cliffside, LunacidRegion.laetus_chasm)
]

great_well_surface = [
    create_location(LOCATION_CODE_START + base_location_start + 188, BaseLocation.surface_demi_gift, LunacidRegion.great_well_surface)
]

throne_room = [
    create_location(LOCATION_CODE_START + base_location_start + 194, BaseLocation.throne_book, LunacidRegion.throne_chamber)
]

boiling_grotto = [
    create_location(LOCATION_CODE_START + base_location_start + 200, BaseLocation.grotto_corpse_beneath_entrance, LunacidRegion.boiling_grotto),
    create_location(LOCATION_CODE_START + base_location_start + 201, BaseLocation.grotto_slab_of_bridge, LunacidRegion.boiling_grotto),
    create_location(LOCATION_CODE_START + base_location_start + 202, BaseLocation.grotto_hidden_chest, LunacidRegion.boiling_grotto),
    create_location(LOCATION_CODE_START + base_location_start + 203, BaseLocation.grotto_triple_secret_chest, LunacidRegion.boiling_grotto),
    create_location(LOCATION_CODE_START + base_location_start + 204, BaseLocation.grotto_rocks_near_lava_switch, LunacidRegion.boiling_grotto),
    create_location(LOCATION_CODE_START + base_location_start + 205, BaseLocation.grotto_through_switch_tunnel, LunacidRegion.boiling_grotto),

    create_location(LOCATION_CODE_START + base_location_start + 206, BaseLocation.sand_top_right_sarcophagus, LunacidRegion.sand_temple),
    create_location(LOCATION_CODE_START + base_location_start + 207, BaseLocation.sand_second_floor_snake, LunacidRegion.sand_temple),
    create_location(LOCATION_CODE_START + base_location_start + 208, BaseLocation.sand_basement_snake_pit, LunacidRegion.sand_temple),
    create_location(LOCATION_CODE_START + base_location_start + 209, BaseLocation.sand_room_buried_in_sand, LunacidRegion.sand_temple),
    create_location(LOCATION_CODE_START + base_location_start + 210, BaseLocation.sand_basement_rubble, LunacidRegion.sand_temple),
    create_location(LOCATION_CODE_START + base_location_start + 211, BaseLocation.sand_hidden_sarcophagus, LunacidRegion.sand_temple),
    create_location(LOCATION_CODE_START + base_location_start + 212, BaseLocation.sand_second_floor_dead_end, LunacidRegion.sand_temple),
    create_location(LOCATION_CODE_START + base_location_start + 213, BaseLocation.sand_lunacid_sandwich, LunacidRegion.sand_temple),
    create_location(LOCATION_CODE_START + base_location_start + 214, BaseLocation.sand_chest_near_switch, LunacidRegion.sand_temple),
    create_location(LOCATION_CODE_START + base_location_start + 215, BaseLocation.sand_chest_overlooking_crypt, LunacidRegion.sand_temple),
    create_location(LOCATION_CODE_START + base_location_start + 216, BaseLocation.sand_switch_maze, LunacidRegion.sand_temple),
    create_location(LOCATION_CODE_START + base_location_start + 217, BaseLocation.sand_triple_sarcophagus, LunacidRegion.sand_temple),
]

tower_of_abyss = [
    create_location(LOCATION_CODE_START + base_location_start + 222, BaseLocation.abyss_prize, LunacidRegion.tower_abyss),
    create_location(LOCATION_CODE_START + base_location_start + 223, BaseLocation.abyss_floor_5, LunacidRegion.tower_abyss),
    create_location(LOCATION_CODE_START + base_location_start + 224, BaseLocation.abyss_floor_10, LunacidRegion.tower_abyss),
    create_location(LOCATION_CODE_START + base_location_start + 225, BaseLocation.abyss_floor_15, LunacidRegion.tower_abyss),
    create_location(LOCATION_CODE_START + base_location_start + 226, BaseLocation.abyss_floor_20, LunacidRegion.tower_abyss),
    create_location(LOCATION_CODE_START + base_location_start + 227, BaseLocation.abyss_floor_25, LunacidRegion.tower_abyss),
    create_location(LOCATION_CODE_START + base_location_start + 228, BaseLocation.abyss_floor_30, LunacidRegion.tower_abyss),
    create_location(LOCATION_CODE_START + base_location_start + 229, BaseLocation.abyss_floor_35, LunacidRegion.tower_abyss),
    create_location(LOCATION_CODE_START + base_location_start + 230, BaseLocation.abyss_floor_40, LunacidRegion.tower_abyss),
    create_location(LOCATION_CODE_START + base_location_start + 231, BaseLocation.abyss_floor_45, LunacidRegion.tower_abyss),
    create_location(LOCATION_CODE_START + base_location_start + 232, BaseLocation.abyss_floor_50, LunacidRegion.tower_abyss),
]

terminus_prison = [
    create_location(LOCATION_CODE_START + base_location_start + 258, BaseLocation.prison_f3_locked_left, LunacidRegion.terminus_prison),
    create_location(LOCATION_CODE_START + base_location_start + 259, BaseLocation.prison_f3_locked_right, LunacidRegion.terminus_prison),
    create_location(LOCATION_CODE_START + base_location_start + 260, BaseLocation.prison_f3_locked_south, LunacidRegion.terminus_prison),
    create_location(LOCATION_CODE_START + base_location_start + 261, BaseLocation.prison_f3_bottomless_pit, LunacidRegion.terminus_prison_upstairs),
    create_location(LOCATION_CODE_START + base_location_start + 262, BaseLocation.prison_f2_broken_cell, LunacidRegion.terminus_prison_dark),
    create_location(LOCATION_CODE_START + base_location_start + 263, BaseLocation.prison_f2_jailer_table, LunacidRegion.terminus_prison_dark),
    create_location(LOCATION_CODE_START + base_location_start + 264, BaseLocation.prison_f1_hidden_cell, LunacidRegion.terminus_prison_dark),
    create_location(LOCATION_CODE_START + base_location_start + 265, BaseLocation.prison_f1_hidden_debris_room, LunacidRegion.terminus_prison_dark),
    create_location(LOCATION_CODE_START + base_location_start + 266, BaseLocation.prison_f1_remains, LunacidRegion.terminus_prison_dark),
    create_location(LOCATION_CODE_START + base_location_start + 267, BaseLocation.prison_b2_guarded_corner_one, LunacidRegion.terminus_prison_dark),
    create_location(LOCATION_CODE_START + base_location_start + 268, BaseLocation.prison_b2_guarded_corner_two, LunacidRegion.terminus_prison_dark),
    create_location(LOCATION_CODE_START + base_location_start + 269, BaseLocation.prison_b2_deep_alcove, LunacidRegion.terminus_prison_dark),
    create_location(LOCATION_CODE_START + base_location_start + 270, BaseLocation.prison_b2_bone_pit, LunacidRegion.terminus_prison_dark),
    create_location(LOCATION_CODE_START + base_location_start + 271, BaseLocation.prison_f4_hanging, LunacidRegion.terminus_prison_upstairs),
    create_location(LOCATION_CODE_START + base_location_start + 272, BaseLocation.prison_f4_maledictus_secret, LunacidRegion.terminus_prison_upstairs),
    create_location(LOCATION_CODE_START + base_location_start + 273, BaseLocation.prison_f4_hidden_beds, LunacidRegion.terminus_prison_upstairs),
    create_location(LOCATION_CODE_START + base_location_start + 274, BaseLocation.prison_f4_jailer_break_room, LunacidRegion.terminus_prison_upstairs),
    create_location(LOCATION_CODE_START + base_location_start + 275, BaseLocation.prison_f4_monk_room_one, LunacidRegion.terminus_prison_upstairs),
    create_location(LOCATION_CODE_START + base_location_start + 276, BaseLocation.prison_f4_monk_room_two, LunacidRegion.terminus_prison_upstairs),
    create_location(LOCATION_CODE_START + base_location_start + 277, BaseLocation.prison_f4_monk_room_three, LunacidRegion.terminus_prison_upstairs),
    create_location(LOCATION_CODE_START + base_location_start + 278, BaseLocation.prison_f4_collapsed_tunnel, LunacidRegion.terminus_prison_upstairs),
    create_location(LOCATION_CODE_START + base_location_start + 279, BaseLocation.prison_b2_egg_resting_place, LunacidRegion.terminus_prison_dark),
]

forlorn_arena = [
    create_location(LOCATION_CODE_START + base_location_start + 284, BaseLocation.arena_broken_sword, LunacidRegion.forlorn_arena),
    create_location(LOCATION_CODE_START + base_location_start + 285, BaseLocation.arena_rock_parkour, LunacidRegion.forlorn_arena),
    create_location(LOCATION_CODE_START + base_location_start + 286, BaseLocation.arena_earth_hidden_plant_haven, LunacidRegion.earth_temple_secret),
    create_location(LOCATION_CODE_START + base_location_start + 287, BaseLocation.arena_earth_hidden_room, LunacidRegion.earth_temple_secret),
    create_location(LOCATION_CODE_START + base_location_start + 288, BaseLocation.arena_earth_earthen_temple, LunacidRegion.forlorn_arena),
    create_location(LOCATION_CODE_START + base_location_start + 289, BaseLocation.arena_earth_chest_near_switch, LunacidRegion.forlorn_arena),
    create_location(LOCATION_CODE_START + base_location_start + 290, BaseLocation.arena_water_room_near_water, LunacidRegion.forlorn_arena),
    create_location(LOCATION_CODE_START + base_location_start + 291, BaseLocation.arena_water_dead_end_near_water, LunacidRegion.forlorn_arena),
    create_location(LOCATION_CODE_START + base_location_start + 292, BaseLocation.arena_water_collapsed_end_near_balcony, LunacidRegion.forlorn_arena),
    create_location(LOCATION_CODE_START + base_location_start + 293, BaseLocation.arena_water_hidden_basement_left, LunacidRegion.forlorn_arena),
    create_location(LOCATION_CODE_START + base_location_start + 294, BaseLocation.arena_water_hidden_basement_right, LunacidRegion.forlorn_arena),
    create_location(LOCATION_CODE_START + base_location_start + 295, BaseLocation.arena_water_hidden_laser_room, LunacidRegion.forlorn_arena),
    create_location(LOCATION_CODE_START + base_location_start + 296, BaseLocation.arena_water_hidden_alcove_before, LunacidRegion.forlorn_arena),
    create_location(LOCATION_CODE_START + base_location_start + 297, BaseLocation.arena_water_hidden_alcove_left, LunacidRegion.forlorn_arena),
    create_location(LOCATION_CODE_START + base_location_start + 298, BaseLocation.arena_water_hidden_alcove_right, LunacidRegion.forlorn_arena),
    create_location(LOCATION_CODE_START + base_location_start + 299, BaseLocation.arena_water_hidden_alcove_before_switch, LunacidRegion.forlorn_arena),
    create_location(LOCATION_CODE_START + base_location_start + 300, BaseLocation.arena_water_underwater_temple, LunacidRegion.forlorn_arena),
    create_location(LOCATION_CODE_START + base_location_start + 301, BaseLocation.arena_water_chest_near_switch, LunacidRegion.forlorn_arena),
]

labyrinth_of_ash = [
    create_location(LOCATION_CODE_START + base_location_start + 307, BaseLocation.ash_entry_coffin, LunacidRegion.labyrinth_of_ash),
    create_location(LOCATION_CODE_START + base_location_start + 308, BaseLocation.ash_giant_remains, LunacidRegion.labyrinth_of_ash),
    create_location(LOCATION_CODE_START + base_location_start + 309, BaseLocation.ash_cetea_statue, LunacidRegion.labyrinth_of_ash),
    create_location(LOCATION_CODE_START + base_location_start + 310, BaseLocation.ash_rocks_near_switch, LunacidRegion.labyrinth_of_ash),
    create_location(LOCATION_CODE_START + base_location_start + 311, BaseLocation.ash_forbidden_light_chest, LunacidRegion.labyrinth_of_ash),
    create_location(LOCATION_CODE_START + base_location_start + 312, BaseLocation.ash_hidden_chest, LunacidRegion.labyrinth_of_ash),
    create_location(LOCATION_CODE_START + base_location_start + 313, BaseLocation.ash_path_maze, LunacidRegion.labyrinth_of_ash),
]

chamber_of_fate = [
    create_location(LOCATION_CODE_START + base_location_start + 319, BaseLocation.fate_lucid_blade, LunacidRegion.chamber_of_fate)
]

base_locations = wings_rest + hollow_basin + great_well_surface + the_fetid_mire + the_sanguine_sea + accursed_tomb + yosei_forest + \
                 forest_canopy + forbidden_archives + castle_le_fanu + sealed_ballroom + laetus_chasm + throne_room + boiling_grotto + \
                 tower_of_abyss + terminus_prison + forlorn_arena + labyrinth_of_ash + chamber_of_fate
base_items: List[str] = []

shop_location_start = 350
shop_locations = [
    create_location(LOCATION_CODE_START + shop_location_start + 1, ShopLocation.buy_rapier, LunacidRegion.sheryl_the_crow),
    create_location(LOCATION_CODE_START + shop_location_start + 2, ShopLocation.buy_crossbow, LunacidRegion.sheryl_the_crow),
    create_location(LOCATION_CODE_START + shop_location_start + 3, ShopLocation.buy_oil_lantern, LunacidRegion.sheryl_the_crow),
    create_location(LOCATION_CODE_START + shop_location_start + 4, ShopLocation.buy_enchanted_key, LunacidRegion.sheryl_the_crow),
    create_location(LOCATION_CODE_START + shop_location_start + 5, ShopLocation.buy_jotunn_slayer, LunacidRegion.sheryl_the_crow),
    create_location(LOCATION_CODE_START + shop_location_start + 6, ShopLocation.buy_privateer_musket, LunacidRegion.sheryl_the_crow),
    create_location(LOCATION_CODE_START + shop_location_start + 7, ShopLocation.buy_steel_needle, LunacidRegion.sheryl_the_crow),
    create_location(LOCATION_CODE_START + shop_location_start + 8, ShopLocation.buy_ocean_elixir_sheryl, LunacidRegion.sheryl_the_crow),
    create_location(LOCATION_CODE_START + shop_location_start + 9, ShopLocation.buy_ocean_elixir_patchouli, LunacidRegion.patchouli),
]

unique_drop_location_start = 400
unique_drop_locations = [
    create_location(LOCATION_CODE_START + unique_drop_location_start + 1, DropLocation.snail),
    create_location(LOCATION_CODE_START + unique_drop_location_start + 2, DropLocation.mummy_knight),
    create_location(LOCATION_CODE_START + unique_drop_location_start + 3, DropLocation.kodama_drop),
    create_location(LOCATION_CODE_START + unique_drop_location_start + 4, DropLocation.chimera_drop),
    create_location(LOCATION_CODE_START + unique_drop_location_start + 5, DropLocation.milk_snail),
    create_location(LOCATION_CODE_START + unique_drop_location_start + 6, DropLocation.skeleton_weapon),
    create_location(LOCATION_CODE_START + unique_drop_location_start + 7, DropLocation.skeleton_spell),
    create_location(LOCATION_CODE_START + unique_drop_location_start + 8, DropLocation.phantom),
    create_location(LOCATION_CODE_START + unique_drop_location_start + 9, DropLocation.obsidian_skeleton_drop_1),
    create_location(LOCATION_CODE_START + unique_drop_location_start + 10, DropLocation.obsidian_skeleton_drop_2),
    create_location(LOCATION_CODE_START + unique_drop_location_start + 11, DropLocation.anpu_drop_1),
    create_location(LOCATION_CODE_START + unique_drop_location_start + 12, DropLocation.anpu_drop_2),
    create_location(LOCATION_CODE_START + unique_drop_location_start + 13, DropLocation.horse_drop),
    create_location(LOCATION_CODE_START + unique_drop_location_start + 14, DropLocation.jailor_drop),
    create_location(LOCATION_CODE_START + unique_drop_location_start + 15, DropLocation.vampire_drop),
    create_location(LOCATION_CODE_START + unique_drop_location_start + 16, DropLocation.sucsarian_drop_1),
    create_location(LOCATION_CODE_START + unique_drop_location_start + 17, DropLocation.sucsarian_drop_2),
    create_location(LOCATION_CODE_START + unique_drop_location_start + 18, DropLocation.giant_spell),
    create_location(LOCATION_CODE_START + unique_drop_location_start + 19, DropLocation.cetea_drop),
    create_location(LOCATION_CODE_START + unique_drop_location_start + 20, DropLocation.sea_demon),
]

other_drop_location_start = 450
other_drop_locations = [
    create_location(LOCATION_CODE_START + other_drop_location_start + 1, DropLocation.snail_2c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 2, DropLocation.snail_10c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 3, DropLocation.snail_ocean),
    create_location(LOCATION_CODE_START + other_drop_location_start + 4, DropLocation.milk_5c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 5, DropLocation.milk_10c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 6, DropLocation.milk_ocean),
    create_location(LOCATION_CODE_START + other_drop_location_start + 7, DropLocation.shulker_obsidian),
    create_location(LOCATION_CODE_START + other_drop_location_start + 8, DropLocation.shulker_onyx),
    create_location(LOCATION_CODE_START + other_drop_location_start + 9, DropLocation.mummy_mana_vial),
    create_location(LOCATION_CODE_START + other_drop_location_start + 10, DropLocation.mummy_onyx),
    create_location(LOCATION_CODE_START + other_drop_location_start + 11, DropLocation.mummy_2c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 12, DropLocation.mummy_10c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 13, DropLocation.necronomicon_fire_opal),
    create_location(LOCATION_CODE_START + other_drop_location_start + 14, DropLocation.necronomicon_5c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 15, DropLocation.necronomicon_10c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 16, DropLocation.necronomicon_mana_vial),
    create_location(LOCATION_CODE_START + other_drop_location_start + 17, DropLocation.chimera_light_urn),
    create_location(LOCATION_CODE_START + other_drop_location_start + 18, DropLocation.chimera_holy_water),
    create_location(LOCATION_CODE_START + other_drop_location_start + 19, DropLocation.enlightened_mana_vial),
    create_location(LOCATION_CODE_START + other_drop_location_start + 20, DropLocation.enlightened_ocean_bone_shell),
    create_location(LOCATION_CODE_START + other_drop_location_start + 21, DropLocation.slime_skeleton),
    create_location(LOCATION_CODE_START + other_drop_location_start + 22, DropLocation.skeleton_10c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 23, DropLocation.skeleton_mana_vial),
    create_location(LOCATION_CODE_START + other_drop_location_start + 24, DropLocation.skeleton_onyx),
    create_location(LOCATION_CODE_START + other_drop_location_start + 25, DropLocation.skeleton_bones),
    create_location(LOCATION_CODE_START + other_drop_location_start + 26, DropLocation.rat_king_10c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 27, DropLocation.rat_king_lotus_seed),
    create_location(LOCATION_CODE_START + other_drop_location_start + 28, DropLocation.rat),
    create_location(LOCATION_CODE_START + other_drop_location_start + 29, DropLocation.kodama_2c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 30, DropLocation.kodama_10c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 31, DropLocation.kodama_opal),
    create_location(LOCATION_CODE_START + other_drop_location_start + 32, DropLocation.yakul_10c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 33, DropLocation.yakul_fire_opal),
    create_location(LOCATION_CODE_START + other_drop_location_start + 34, DropLocation.yakul_opal),
    create_location(LOCATION_CODE_START + other_drop_location_start + 35, DropLocation.yakul_health_vial),
    create_location(LOCATION_CODE_START + other_drop_location_start + 36, DropLocation.venus_10c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 37, DropLocation.venus_yellow_morel),
    create_location(LOCATION_CODE_START + other_drop_location_start + 38, DropLocation.venus_dest_angel),
    create_location(LOCATION_CODE_START + other_drop_location_start + 39, DropLocation.neptune_10c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 40, DropLocation.neptune_yellow_morel),
    create_location(LOCATION_CODE_START + other_drop_location_start + 41, DropLocation.neptune_dest_angel),
    create_location(LOCATION_CODE_START + other_drop_location_start + 42, DropLocation.unilateralis_10c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 43, DropLocation.unilateralis_yellow_morel),
    create_location(LOCATION_CODE_START + other_drop_location_start + 44, DropLocation.unilateralis_dest_angel),
    create_location(LOCATION_CODE_START + other_drop_location_start + 45, DropLocation.hemalith_health_vial),
    create_location(LOCATION_CODE_START + other_drop_location_start + 46, DropLocation.hemalith_shrimp),
    create_location(LOCATION_CODE_START + other_drop_location_start + 47, DropLocation.hemallith_bloodweed),
    create_location(LOCATION_CODE_START + other_drop_location_start + 48, DropLocation.mi_go_ocean_bone_shell),
    create_location(LOCATION_CODE_START + other_drop_location_start + 49, DropLocation.mi_go_10c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 50, DropLocation.mi_go_snowflake_obsidian),
    create_location(LOCATION_CODE_START + other_drop_location_start + 51, DropLocation.mare_10c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 52, DropLocation.mare_obsidian),
    create_location(LOCATION_CODE_START + other_drop_location_start + 53, DropLocation.mare_onyx),
    create_location(LOCATION_CODE_START + other_drop_location_start + 54, DropLocation.painting_fire_opal),
    create_location(LOCATION_CODE_START + other_drop_location_start + 55, DropLocation.painting_10c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 56, DropLocation.painting_mana_vial),
    create_location(LOCATION_CODE_START + other_drop_location_start + 57, DropLocation.painting_20c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 58, DropLocation.phantom_10c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 59, DropLocation.phantom_holy_water),
    create_location(LOCATION_CODE_START + other_drop_location_start + 60, DropLocation.phantom_moon_vial),
    create_location(LOCATION_CODE_START + other_drop_location_start + 61, DropLocation.phantom_ectoplasm),
    create_location(LOCATION_CODE_START + other_drop_location_start + 62, DropLocation.vampire_5c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 63, DropLocation.vampire_vampiric_ashes),
    create_location(LOCATION_CODE_START + other_drop_location_start + 64, DropLocation.vampire_bandage),
    create_location(LOCATION_CODE_START + other_drop_location_start + 65, DropLocation.vampire_page_ashes),
    create_location(LOCATION_CODE_START + other_drop_location_start + 66, DropLocation.vampire_page_20c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 67, DropLocation.malformed_vampiric_ashes),
    create_location(LOCATION_CODE_START + other_drop_location_start + 68, DropLocation.great_bat_health_vial),
    create_location(LOCATION_CODE_START + other_drop_location_start + 69, DropLocation.great_bat_obsidian),
    create_location(LOCATION_CODE_START + other_drop_location_start + 70, DropLocation.great_bat_10c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 71, DropLocation.poltergeist_10c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 72, DropLocation.poltergeist_ectoplasm),
    create_location(LOCATION_CODE_START + other_drop_location_start + 73, DropLocation.horse_10c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 74, DropLocation.horse_mana_vial),
    create_location(LOCATION_CODE_START + other_drop_location_start + 75, DropLocation.hallowed_husk_10c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 76, DropLocation.hallowed_husk_bones),
    create_location(LOCATION_CODE_START + other_drop_location_start + 77, DropLocation.hallowed_husk_bandage),
    create_location(LOCATION_CODE_START + other_drop_location_start + 78, DropLocation.hallowed_husk_light_urn),
    create_location(LOCATION_CODE_START + other_drop_location_start + 79, DropLocation.hallowed_husk_goldeness),
    create_location(LOCATION_CODE_START + other_drop_location_start + 80, DropLocation.hallowed_husk_holy_water),
    create_location(LOCATION_CODE_START + other_drop_location_start + 81, DropLocation.ikkurilb_root),
    create_location(LOCATION_CODE_START + other_drop_location_start + 82, DropLocation.ikkurilb_10c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 83, DropLocation.ikkurilb_snowflake_obsidian),
    create_location(LOCATION_CODE_START + other_drop_location_start + 84, DropLocation.mimic_moon_vial),
    create_location(LOCATION_CODE_START + other_drop_location_start + 85, DropLocation.mimic_obsidian),
    create_location(LOCATION_CODE_START + other_drop_location_start + 86, DropLocation.mimic_fools_gold),
    create_location(LOCATION_CODE_START + other_drop_location_start + 87, DropLocation.obsidian_skeleton_10c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 88, DropLocation.obsidian_skeleton_bones),
    create_location(LOCATION_CODE_START + other_drop_location_start + 89, DropLocation.obsidian_skeleton_mana_vial),
    create_location(LOCATION_CODE_START + other_drop_location_start + 90, DropLocation.obsidian_skeleton_obsidian),
    create_location(LOCATION_CODE_START + other_drop_location_start + 91, DropLocation.anpu_10c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 92, DropLocation.anpu_fire_opal),
    create_location(LOCATION_CODE_START + other_drop_location_start + 93, DropLocation.serpent_antidote),
    create_location(LOCATION_CODE_START + other_drop_location_start + 94, DropLocation.serpent_5c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 95, DropLocation.embalmed_bandage),
    create_location(LOCATION_CODE_START + other_drop_location_start + 96, DropLocation.embalmed_ashes),
    create_location(LOCATION_CODE_START + other_drop_location_start + 97, DropLocation.embalmed_bones),
    create_location(LOCATION_CODE_START + other_drop_location_start + 98, DropLocation.jailor_10c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 99, DropLocation.jailor_candle),
    create_location(LOCATION_CODE_START + other_drop_location_start + 100, DropLocation.jailor_bandage),
    create_location(LOCATION_CODE_START + other_drop_location_start + 101, DropLocation.jailor_health_vial),
    create_location(LOCATION_CODE_START + other_drop_location_start + 102, DropLocation.jailor_angel),
    create_location(LOCATION_CODE_START + other_drop_location_start + 103, DropLocation.lunam_ectoplasm),
    create_location(LOCATION_CODE_START + other_drop_location_start + 104, DropLocation.lunam_10c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 105, DropLocation.lunam_snowflake_obsidian),
    create_location(LOCATION_CODE_START + other_drop_location_start + 106, DropLocation.giant_dark_urn),
    create_location(LOCATION_CODE_START + other_drop_location_start + 107, DropLocation.giant_bones),
    create_location(LOCATION_CODE_START + other_drop_location_start + 108, DropLocation.giant_mana_vial),
    create_location(LOCATION_CODE_START + other_drop_location_start + 109, DropLocation.giant_onyx),
    create_location(LOCATION_CODE_START + other_drop_location_start + 110, DropLocation.sucsarian_10c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 111, DropLocation.sucsarian_obsidian),
    create_location(LOCATION_CODE_START + other_drop_location_start + 112, DropLocation.sucsarian_snowflake_obsidian),
    create_location(LOCATION_CODE_START + other_drop_location_start + 113, DropLocation.sucsarian_throwing_knife),
    create_location(LOCATION_CODE_START + other_drop_location_start + 114, DropLocation.vesta_fairy_moss),
    create_location(LOCATION_CODE_START + other_drop_location_start + 115, DropLocation.vesta_yellow_morel),
    create_location(LOCATION_CODE_START + other_drop_location_start + 116, DropLocation.vesta_dest_angel),
    create_location(LOCATION_CODE_START + other_drop_location_start + 117, DropLocation.ceres_fairy_moss),
    create_location(LOCATION_CODE_START + other_drop_location_start + 118, DropLocation.ceres_yellow_morel),
    create_location(LOCATION_CODE_START + other_drop_location_start + 119, DropLocation.ceres_dest_angel),
    create_location(LOCATION_CODE_START + other_drop_location_start + 120, DropLocation.gloom_fairy_moss),
    create_location(LOCATION_CODE_START + other_drop_location_start + 121, DropLocation.gloom_health_vial),
    create_location(LOCATION_CODE_START + other_drop_location_start + 122, DropLocation.gloom_dest_angel),
    create_location(LOCATION_CODE_START + other_drop_location_start + 123, DropLocation.cetea_10c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 124, DropLocation.cetea_ocean_bone_shell),
    create_location(LOCATION_CODE_START + other_drop_location_start + 125, DropLocation.mummy_knight_onyx),
    create_location(LOCATION_CODE_START + other_drop_location_start + 126, DropLocation.mummy_knight_10c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 127, DropLocation.mummy_knight_5c),
    create_location(LOCATION_CODE_START + other_drop_location_start + 128, DropLocation.sanguis_book),
]




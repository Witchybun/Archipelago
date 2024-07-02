from dataclasses import dataclass
from typing import Optional, List

from ..strings.locations import BaseLocation, ShopLocation, DropLocation
from ..strings.regions_entrances import LunacidRegion


@dataclass(frozen=True)
class LunacidLocation:
    location_id: Optional[int]
    name: str
    region: str


LOCATION_CODE_START = 771111110
all_locations = []


# Some locations vary on multiple regions, so we default to Hollow Basin first.
def create_location(location_id: Optional[int], name: str, region: Optional[str] = LunacidRegion.hollow_basin):
    location = LunacidLocation(location_id, name, region)
    if location_id is not None:
        all_locations.append(location)
    return location


wings_rest = [
    create_location(1, BaseLocation.wings_rest_ocean_elixir, LunacidRegion.wings_rest),
    create_location(2, BaseLocation.wings_rest_crystal_shard, LunacidRegion.wings_rest),
    create_location(3, BaseLocation.wings_rest_clives_gift, LunacidRegion.wings_rest),
    create_location(4, BaseLocation.wings_rest_demi_orb, LunacidRegion.wings_rest),
    create_location(5, BaseLocation.wings_rest_demi_gift, LunacidRegion.wings_rest),
]

hollow_basin = [
    create_location(9, BaseLocation.hollow_basin_starting_sword, LunacidRegion.hollow_basin),
    create_location(10, BaseLocation.hollow_basin_right_water_right, LunacidRegion.hollow_basin),
    create_location(11, BaseLocation.hollow_basin_right_water_left, LunacidRegion.hollow_basin),
    create_location(12, BaseLocation.hollow_basin_left_water, LunacidRegion.hollow_basin),
    create_location(13, BaseLocation.hollow_basin_demi_chest, LunacidRegion.hollow_basin),
    create_location(14, BaseLocation.hollow_basin_enchanted_door, LunacidRegion.hollow_basin),
    create_location(15, BaseLocation.hollow_basin_dark_item, LunacidRegion.hollow_basin),

    create_location(16, BaseLocation.temple_fountain, LunacidRegion.temple_of_silence_entrance),
    create_location(17, BaseLocation.temple_ritual_table, LunacidRegion.temple_of_silence_entrance),
    create_location(18, BaseLocation.temple_altar_chest, LunacidRegion.temple_of_silence_entrance),
    create_location(19, BaseLocation.temple_pillar_left, LunacidRegion.temple_of_silence_secret),
    create_location(20, BaseLocation.temple_pillar_right, LunacidRegion.temple_of_silence_secret),
    create_location(21, BaseLocation.temple_ritual_ring, LunacidRegion.temple_of_silence_interior),
    create_location(22, BaseLocation.temple_small_pillar, LunacidRegion.temple_of_silence_interior),
    create_location(23, BaseLocation.temple_pillar_room_left, LunacidRegion.temple_of_silence_secret),
    create_location(24, BaseLocation.temple_pillar_room_back_left, LunacidRegion.temple_of_silence_secret),
    create_location(25, BaseLocation.temple_pillar_room_back_right, LunacidRegion.temple_of_silence_secret),
    create_location(26, BaseLocation.temple_pillar_room_hidden_room, LunacidRegion.temple_of_silence_secret),
    create_location(27, BaseLocation.temple_hidden_room_in_sewer, LunacidRegion.temple_of_silence_secret),
    create_location(28, BaseLocation.temple_table_in_sewer, LunacidRegion.temple_of_silence_interior),
    create_location(29, BaseLocation.temple_sewer_puzzle, LunacidRegion.temple_of_silence_interior),
    create_location(30, BaseLocation.temple_blood_altar, LunacidRegion.temple_of_silence_interior),
    create_location(31, BaseLocation.temple_path_to_forest, LunacidRegion.temple_of_silence_interior),
]

the_fetid_mire = [
    create_location(37, BaseLocation.mire_room_left_foyer, LunacidRegion.fetid_mire),
    create_location(38, BaseLocation.mire_hidden_slime_chest, LunacidRegion.fetid_mire_secret),
    create_location(39, BaseLocation.mire_upper_overlook_left, LunacidRegion.fetid_mire_secret),
    create_location(40, BaseLocation.mire_upper_overlook_right, LunacidRegion.fetid_mire_secret),
    create_location(41, BaseLocation.mire_bonenard_trash, LunacidRegion.fetid_mire),
    create_location(42, BaseLocation.mire_rubble_bridge, LunacidRegion.fetid_mire),
    create_location(43, BaseLocation.mire_skeleton_chest, LunacidRegion.fetid_mire),
    create_location(44, BaseLocation.mire_jellisha_trash, LunacidRegion.fetid_mire_secret),
    create_location(45, BaseLocation.mire_jellisha_reward, LunacidRegion.fetid_mire_secret),
    create_location(46, BaseLocation.mire_path_to_sea_left, LunacidRegion.fetid_mire),
    create_location(47, BaseLocation.mire_path_to_sea_right, LunacidRegion.fetid_mire),
    create_location(48, BaseLocation.mire_hidden_chest_near_underworks, LunacidRegion.fetid_mire_secret),
    create_location(49, BaseLocation.mire_rubble_near_illusory_wall, LunacidRegion.fetid_mire),
    create_location(50, BaseLocation.mire_underwater_pipe, LunacidRegion.fetid_mire),
    create_location(51, BaseLocation.mire_underworks_waterfall, LunacidRegion.fetid_mire),
    create_location(52, BaseLocation.mire_underworks_skeleton, LunacidRegion.fetid_mire),
]

the_sacrosant_sea = [
    create_location(58, BaseLocation.sea_pillar, LunacidRegion.sanguine_sea),
    create_location(59, BaseLocation.sea_underblood, LunacidRegion.sanguine_sea),
    create_location(60, BaseLocation.sea_fairy_circle, LunacidRegion.sanguine_sea),
    create_location(61, BaseLocation.sea_kill_jotunn, LunacidRegion.sanguine_sea)]

accursed_tomb = [
    create_location(67, BaseLocation.catacombs_coffin_stairs, LunacidRegion.accursed_tomb),
    create_location(68, BaseLocation.catacombs_coffin_blue_light, LunacidRegion.accursed_tomb),
    create_location(69, BaseLocation.corrupted_room, LunacidRegion.accursed_tomb),
    create_location(70, BaseLocation.catacombs_coffin_gate, LunacidRegion.accursed_tomb),
    create_location(71, BaseLocation.catacombs_hidden_room, LunacidRegion.vampire_tomb),
    create_location(72, BaseLocation.catacombs_deep_coffin_storage, LunacidRegion.vampire_tomb),
    create_location(73, BaseLocation.catacombs_restore_vampire, LunacidRegion.vampire_tomb),

    create_location(74, BaseLocation.mausoleum_hidden_chest, LunacidRegion.mausoleum),
    create_location(75, BaseLocation.mausoleum_upper_table, LunacidRegion.mausoleum),
    create_location(76, BaseLocation.mausoleum_maze_intro, LunacidRegion.mausoleum),
    create_location(77, BaseLocation.mausoleum_maze_mid, LunacidRegion.mausoleum),
    create_location(78, BaseLocation.mausoleum_center_right, LunacidRegion.mausoleum),
    create_location(79, BaseLocation.mausoleum_center_left, LunacidRegion.mausoleum),
    create_location(80, BaseLocation.mausoleum_center_back, LunacidRegion.mausoleum),
    create_location(81, BaseLocation.mausoleum_center_left_path, LunacidRegion.mausoleum),
    create_location(82, BaseLocation.mausoleum_center_right_path, LunacidRegion.mausoleum),
    create_location(83, BaseLocation.mausoleum_kill_death, LunacidRegion.mausoleum),

    create_location(84, BaseLocation.tomb_tomb_with_switch, LunacidRegion.accursed_tomb),
    create_location(85, BaseLocation.tomb_tomb_with_corpse, LunacidRegion.accursed_tomb),
    create_location(86, BaseLocation.tomb_demi_chest, LunacidRegion.accursed_tomb),
    create_location(87, BaseLocation.tomb_near_light_switch, LunacidRegion.accursed_tomb),
    create_location(88, BaseLocation.tomb_hidden_room, LunacidRegion.accursed_tomb),
    create_location(89, BaseLocation.tomb_hidden_chest, LunacidRegion.accursed_tomb)
]

yosei_forest = [
    create_location(94, BaseLocation.yosei_barrels, LunacidRegion.yosei_forest),
    create_location(95, BaseLocation.yosei_blood_pool, LunacidRegion.yosei_forest),
    create_location(96, BaseLocation.yosei_branch_in_tree, LunacidRegion.yosei_forest),
    create_location(97, BaseLocation.yosei_chest_near_tree, LunacidRegion.yosei_forest),
    create_location(98, BaseLocation.yosei_blood_plant_insides, LunacidRegion.yosei_forest),
    create_location(99, BaseLocation.yosei_hanging_in_trees, LunacidRegion.yosei_forest),
    create_location(100, BaseLocation.yosei_hidden_chest, LunacidRegion.yosei_lower),
    create_location(101, BaseLocation.yosei_room_defended_by_blood_plant, LunacidRegion.yosei_lower),
    create_location(102, BaseLocation.yosei_patchouli_key, LunacidRegion.yosei_lower),
    create_location(103, BaseLocation.yosei_patchouli_quest, LunacidRegion.yosei_lower),
]

forest_canopy = [
    create_location(109, BaseLocation.canopy_branch_edge, LunacidRegion.forest_canopy),
    create_location(110, BaseLocation.branch_cave, LunacidRegion.forest_canopy),
    create_location(111, BaseLocation.canopy_chest, LunacidRegion.forest_canopy),
    create_location(112, BaseLocation.canopy_wooden_statue, LunacidRegion.forest_canopy),
    create_location(113, BaseLocation.canopy_wooden_sitting, LunacidRegion.forest_canopy),
]

forbidden_archives = [
    create_location(119, BaseLocation.archives_back_room_past_bridge, LunacidRegion.forbidden_archives_2),
    create_location(120, BaseLocation.archives_strange_corpse, LunacidRegion.forbidden_archives_2),
    create_location(121, BaseLocation.archives_against_wall_near_trees, LunacidRegion.forbidden_archives_1),
    create_location(122, BaseLocation.archives_short_wall_near_trees, LunacidRegion.forbidden_archives_1),
    create_location(123, BaseLocation.archives_snail_lectern_near, LunacidRegion.forbidden_archives_3),
    create_location(124, BaseLocation.archives_snail_lectern_far, LunacidRegion.forbidden_archives_3),
    create_location(125, BaseLocation.archives_rug_on_balcony, LunacidRegion.forbidden_archives_3),
    create_location(126, BaseLocation.archives_rooftop, LunacidRegion.forbidden_archives_3),
    create_location(127, BaseLocation.archives_hidden_room_upper, LunacidRegion.forbidden_archives_3),
    create_location(128, BaseLocation.archives_hidden_room_lower, LunacidRegion.forbidden_archives_1b),
    create_location(129, BaseLocation.archives_near_twisty_tree, LunacidRegion.forbidden_archives_1b),
    create_location(130, BaseLocation.archives_uwu, LunacidRegion.forbidden_archives_1b),
    create_location(131, BaseLocation.archives_daedalus_one, LunacidRegion.daedalus),
    create_location(132, BaseLocation.archives_daedalus_two, LunacidRegion.daedalus),
    create_location(133, BaseLocation.archives_daedalus_third, LunacidRegion.daedalus),
    create_location(134, BaseLocation.archives_corner_near_daedalus, LunacidRegion.forbidden_archives_1b),
]

castle_le_fanu = [
    create_location(140, BaseLocation.castle_outside_corner, LunacidRegion.castle_le_fanu),
    create_location(141, BaseLocation.castle_cell_south, LunacidRegion.castle_le_fanu_red),
    create_location(142, BaseLocation.castle_cell_west, LunacidRegion.castle_le_fanu_red),
    create_location(143, BaseLocation.castle_cell_center, LunacidRegion.castle_le_fanu_red),
    create_location(144, BaseLocation.castle_cell_north, LunacidRegion.castle_le_fanu_red),
    create_location(145, BaseLocation.castle_hidden_cell, LunacidRegion.castle_le_fanu_red),

    create_location(146, BaseLocation.castle_hallway_rubble_room, LunacidRegion.castle_le_fanu_white),
    create_location(147, BaseLocation.castle_hallway_dining_room, LunacidRegion.castle_le_fanu_white),
    create_location(148, BaseLocation.castle_garrat_resting_room_left, LunacidRegion.castle_le_fanu_white),
    create_location(149, BaseLocation.castle_garrat_resting_room_back, LunacidRegion.castle_le_fanu_white),
    create_location(150, BaseLocation.castle_hallway_deadend_before_door, LunacidRegion.castle_le_fanu_white),
    create_location(151, BaseLocation.castle_upper_floor_coffin_small, LunacidRegion.castle_le_fanu_blue),
    create_location(152, BaseLocation.castle_upper_floor_coffin_large, LunacidRegion.castle_le_fanu_blue),
    create_location(153, BaseLocation.castle_upper_floor_coffin_double, LunacidRegion.castle_le_fanu_blue),
    create_location(154, BaseLocation.castle_upper_floor_coffin_hallway, LunacidRegion.castle_le_fanu_blue),
]

sealed_ballroom = [
    create_location(166, BaseLocation.ballroom_small_room_lounge, LunacidRegion.sealed_ballroom),
    create_location(167, BaseLocation.ballroom_entry_hidden_couch_top, LunacidRegion.sealed_ballroom_secret),
    create_location(168, BaseLocation.ballroom_entry_hidden_couch_bottom, LunacidRegion.sealed_ballroom_secret),
    create_location(169, BaseLocation.ballroom_entry_hidden_cave_in_lounge, LunacidRegion.sealed_ballroom_secret),
    create_location(170, BaseLocation.ballroom_entry_long_table, LunacidRegion.sealed_ballroom),
    create_location(171, BaseLocation.ballroom_side_hidden_cave, LunacidRegion.sealed_ballroom_secret),
    create_location(172, BaseLocation.ballroom_side_chest_near_switch, LunacidRegion.sealed_ballroom),
    create_location(173, BaseLocation.ballroom_side_painting, LunacidRegion.sealed_ballroom),
    create_location(174, BaseLocation.ballroom_side_hidden_casket_room, LunacidRegion.sealed_ballroom_secret),
    create_location(175, BaseLocation.ballroom_side_xp_drain, LunacidRegion.sealed_ballroom),
]

laetus_chasm = [
    create_location(181, BaseLocation.chasm_hidden_chest, LunacidRegion.laetus_chasm),
    create_location(182, BaseLocation.chasm_invisible_cliffside, LunacidRegion.laetus_chasm)
]

great_well_surface = [
    create_location(188, BaseLocation.surface_demi_gift, LunacidRegion.great_well_surface)
]

throne_room = [
    create_location(194, BaseLocation.throne_book, LunacidRegion.throne_chamber)
]

boiling_grotto = [
    create_location(200, BaseLocation.grotto_corpse_beneath_entrance, LunacidRegion.boiling_grotto),
    create_location(201, BaseLocation.grotto_slab_of_bridge, LunacidRegion.boiling_grotto),
    create_location(202, BaseLocation.grotto_hidden_chest, LunacidRegion.boiling_grotto),
    create_location(203, BaseLocation.grotto_triple_secret_chest, LunacidRegion.boiling_grotto),
    create_location(204, BaseLocation.grotto_rocks_near_lava_switch, LunacidRegion.boiling_grotto),
    create_location(205, BaseLocation.grotto_through_switch_tunnel, LunacidRegion.boiling_grotto),

    create_location(206, BaseLocation.sand_top_right_sarcophagus, LunacidRegion.sand_temple),
    create_location(207, BaseLocation.sand_second_floor_snake, LunacidRegion.sand_temple),
    create_location(208, BaseLocation.sand_basement_snake_pit, LunacidRegion.sand_temple),
    create_location(209, BaseLocation.sand_room_buried_in_sand, LunacidRegion.sand_temple),
    create_location(210, BaseLocation.sand_basement_rubble, LunacidRegion.sand_temple),
    create_location(211, BaseLocation.sand_hidden_sarcophagus, LunacidRegion.sand_temple),
    create_location(212, BaseLocation.sand_second_floor_dead_end, LunacidRegion.sand_temple),
    create_location(213, BaseLocation.sand_lunacid_sandwich, LunacidRegion.sand_temple),
    create_location(214, BaseLocation.sand_chest_near_switch, LunacidRegion.sand_temple),
    create_location(215, BaseLocation.sand_chest_overlooking_crypt, LunacidRegion.sand_temple),
    create_location(216, BaseLocation.sand_switch_maze, LunacidRegion.sand_temple),
    create_location(217, BaseLocation.sand_triple_sarcophagus, LunacidRegion.sand_temple),
]

tower_of_abyss = [
    create_location(222, BaseLocation.abyss_prize, LunacidRegion.tower_abyss),
    create_location(223, BaseLocation.abyss_floor_5, LunacidRegion.tower_abyss),
    create_location(224, BaseLocation.abyss_floor_10, LunacidRegion.tower_abyss),
    create_location(225, BaseLocation.abyss_floor_15, LunacidRegion.tower_abyss),
    create_location(226, BaseLocation.abyss_floor_20, LunacidRegion.tower_abyss),
    create_location(227, BaseLocation.abyss_floor_25, LunacidRegion.tower_abyss),
    create_location(228, BaseLocation.abyss_floor_30, LunacidRegion.tower_abyss),
    create_location(229, BaseLocation.abyss_floor_35, LunacidRegion.tower_abyss),
    create_location(230, BaseLocation.abyss_floor_40, LunacidRegion.tower_abyss),
    create_location(231, BaseLocation.abyss_floor_45, LunacidRegion.tower_abyss),
    create_location(232, BaseLocation.abyss_floor_50, LunacidRegion.tower_abyss),
]

terminus_prison = [
    create_location(258, BaseLocation.prison_f3_locked_left, LunacidRegion.terminus_prison),
    create_location(259, BaseLocation.prison_f3_locked_right, LunacidRegion.terminus_prison),
    create_location(260, BaseLocation.prison_f3_locked_south, LunacidRegion.terminus_prison),
    create_location(261, BaseLocation.prison_f3_bottomless_pit, LunacidRegion.terminus_prison_upstairs),
    create_location(262, BaseLocation.prison_f2_broken_cell, LunacidRegion.terminus_prison_dark),
    create_location(263, BaseLocation.prison_f2_jailer_table, LunacidRegion.terminus_prison_dark),
    create_location(264, BaseLocation.prison_f1_hidden_cell, LunacidRegion.terminus_prison_dark),
    create_location(265, BaseLocation.prison_f1_hidden_debris_room, LunacidRegion.terminus_prison_dark),
    create_location(266, BaseLocation.prison_f1_remains, LunacidRegion.terminus_prison_dark),
    create_location(267, BaseLocation.prison_b2_guarded_corner_one, LunacidRegion.terminus_prison_dark),
    create_location(268, BaseLocation.prison_b2_guarded_corner_two, LunacidRegion.terminus_prison_dark),
    create_location(269, BaseLocation.prison_b2_deep_alcove, LunacidRegion.terminus_prison_dark),
    create_location(270, BaseLocation.prison_b2_bone_pit, LunacidRegion.terminus_prison_dark),
    create_location(271, BaseLocation.prison_f4_hanging, LunacidRegion.terminus_prison_upstairs),
    create_location(272, BaseLocation.prison_f4_maledictus_secret, LunacidRegion.terminus_prison_upstairs),
    create_location(273, BaseLocation.prison_f4_hidden_beds, LunacidRegion.terminus_prison_upstairs),
    create_location(274, BaseLocation.prison_f4_jailer_break_room, LunacidRegion.terminus_prison_upstairs),
    create_location(275, BaseLocation.prison_f4_monk_room_one, LunacidRegion.terminus_prison_upstairs),
    create_location(276, BaseLocation.prison_f4_monk_room_two, LunacidRegion.terminus_prison_upstairs),
    create_location(277, BaseLocation.prison_f4_monk_room_three, LunacidRegion.terminus_prison_upstairs),
    create_location(278, BaseLocation.prison_f4_collapsed_tunnel, LunacidRegion.terminus_prison_upstairs),
    create_location(279, BaseLocation.prison_b2_egg_resting_place, LunacidRegion.terminus_prison_dark),
]

forlorn_arena = [
    create_location(284, BaseLocation.arena_broken_sword, LunacidRegion.forlorn_arena),
    create_location(285, BaseLocation.arena_rock_parkour, LunacidRegion.forlorn_arena),
    create_location(286, BaseLocation.arena_earth_hidden_plant_haven, LunacidRegion.earth_temple_secret),
    create_location(287, BaseLocation.arena_earth_hidden_room, LunacidRegion.earth_temple_secret),
    create_location(288, BaseLocation.arena_earth_earthen_temple, LunacidRegion.forlorn_arena),
    create_location(289, BaseLocation.arena_earth_chest_near_switch, LunacidRegion.forlorn_arena),
    create_location(290, BaseLocation.arena_water_room_near_water, LunacidRegion.forlorn_arena),
    create_location(291, BaseLocation.arena_water_dead_end_near_water, LunacidRegion.forlorn_arena),
    create_location(292, BaseLocation.arena_water_collapsed_end_near_balcony, LunacidRegion.forlorn_arena),
    create_location(293, BaseLocation.arena_water_hidden_basement_left, LunacidRegion.forlorn_arena),
    create_location(294, BaseLocation.arena_water_hidden_basement_right, LunacidRegion.forlorn_arena),
    create_location(295, BaseLocation.arena_water_hidden_laser_room, LunacidRegion.forlorn_arena),
    create_location(296, BaseLocation.arena_water_hidden_alcove_before, LunacidRegion.forlorn_arena),
    create_location(297, BaseLocation.arena_water_hidden_alcove_left, LunacidRegion.forlorn_arena),
    create_location(298, BaseLocation.arena_water_hidden_alcove_right, LunacidRegion.forlorn_arena),
    create_location(299, BaseLocation.arena_water_hidden_alcove_before_switch, LunacidRegion.forlorn_arena),
    create_location(300, BaseLocation.arena_water_underwater_temple, LunacidRegion.forlorn_arena),
    create_location(301, BaseLocation.arena_water_chest_near_switch, LunacidRegion.forlorn_arena),
]

labyrinth_of_ash = [
    create_location(307, BaseLocation.ash_entry_coffin, LunacidRegion.labyrinth_of_ash),
    create_location(308, BaseLocation.ash_giant_remains, LunacidRegion.labyrinth_of_ash),
    create_location(309, BaseLocation.ash_cetea_statue, LunacidRegion.labyrinth_of_ash),
    create_location(310, BaseLocation.ash_rocks_near_switch, LunacidRegion.labyrinth_of_ash),
    create_location(311, BaseLocation.ash_forbidden_light_chest, LunacidRegion.labyrinth_of_ash),
    create_location(312, BaseLocation.ash_hidden_chest, LunacidRegion.labyrinth_of_ash),
    create_location(313, BaseLocation.ash_path_maze, LunacidRegion.labyrinth_of_ash),
]

chamber_of_fate = [
    create_location(319, BaseLocation.fate_lucid_blade, LunacidRegion.chamber_of_fate)
]

base_locations = wings_rest + hollow_basin + great_well_surface + the_fetid_mire + the_sacrosant_sea + accursed_tomb + yosei_forest + \
                 forest_canopy + forbidden_archives + castle_le_fanu + sealed_ballroom + laetus_chasm + throne_room + boiling_grotto + \
                 tower_of_abyss + terminus_prison + forlorn_arena + labyrinth_of_ash + chamber_of_fate
base_items: List[str] = []

shop_locations = [
    create_location(360, ShopLocation.buy_rapier, LunacidRegion.sheryl_the_crow),
    create_location(361, ShopLocation.buy_crossbow, LunacidRegion.sheryl_the_crow),
    create_location(362, ShopLocation.buy_oil_lantern, LunacidRegion.sheryl_the_crow),
    create_location(363, ShopLocation.buy_enchanted_key, LunacidRegion.sheryl_the_crow),
    create_location(364, ShopLocation.buy_jotunn_slayer, LunacidRegion.sheryl_the_crow),
    create_location(365, ShopLocation.buy_privateer_musket, LunacidRegion.sheryl_the_crow),
    create_location(366, ShopLocation.buy_steel_needle, LunacidRegion.sheryl_the_crow),
    create_location(367, ShopLocation.buy_ocean_elixir_sheryl, LunacidRegion.sheryl_the_crow),
    create_location(368, ShopLocation.buy_ocean_elixir_patchouli, LunacidRegion.patchouli),
]

unique_drop_locations = [
    create_location(409, DropLocation.snail),
    create_location(410, DropLocation.mummy_knight),
    create_location(411, DropLocation.kodama_drop),
    create_location(412, DropLocation.chimera_drop),
    create_location(413, DropLocation.milk_snail),
    create_location(414, DropLocation.skeleton_weapon),
    create_location(415, DropLocation.skeleton_spell),
    create_location(416, DropLocation.phantom),
    create_location(417, DropLocation.obsidian_skeleton_drop_1),
    create_location(418, DropLocation.obsidian_skeleton_drop_2),
    create_location(419, DropLocation.anpu_drop_1),
    create_location(420, DropLocation.anpu_drop_2),
    create_location(421, DropLocation.horse_drop),
    create_location(422, DropLocation.jailor_drop),
    create_location(423, DropLocation.vampire_drop),
    create_location(424, DropLocation.sucsarian_drop_1),
    create_location(425, DropLocation.sucsarian_drop_2),
    create_location(426, DropLocation.giant_spell),
    create_location(427, DropLocation.cetea_drop),
    create_location(428, DropLocation.sea_demon),
]


other_drop_locations = [  # The regions and drops are wrong, but are assigned elsewhere
    create_location(440, DropLocation.snail_2c),
    create_location(441, DropLocation.snail_10c),
    create_location(442, DropLocation.snail_ocean),
    create_location(443, DropLocation.milk_5c),
    create_location(444, DropLocation.milk_10c),
    create_location(445, DropLocation.milk_ocean),
    create_location(446, DropLocation.shulker_obsidian),
    create_location(447, DropLocation.shulker_onyx),
    create_location(448, DropLocation.mummy_mana_vial),
    create_location(449, DropLocation.mummy_onyx),
    create_location(450, DropLocation.mummy_2c),
    create_location(451, DropLocation.mummy_10c),
    create_location(452, DropLocation.necronomicon_fire_opal),
    create_location(453, DropLocation.necronomicon_5c),
    create_location(454, DropLocation.necronomicon_10c),
    create_location(455, DropLocation.necronomicon_mana_vial),
    create_location(456, DropLocation.chimera_light_urn),
    create_location(457, DropLocation.chimera_holy_water),
    create_location(458, DropLocation.enlightened_mana_vial),
    create_location(459, DropLocation.enlightened_ocean_bone_shell),
    create_location(460, DropLocation.slime_skeleton),
    create_location(461, DropLocation.skeleton_10c),
    create_location(462, DropLocation.skeleton_mana_vial),
    create_location(463, DropLocation.skeleton_onyx),
    create_location(464, DropLocation.skeleton_bones),
    create_location(465, DropLocation.rat_king_10c),
    create_location(466, DropLocation.rat_king_lotus_seed),
    create_location(467, DropLocation.rat),
    create_location(468, DropLocation.kodama_2c),
    create_location(469, DropLocation.kodama_10c),
    create_location(470, DropLocation.kodama_opal),
    create_location(471, DropLocation.yakul_10c),
    create_location(472, DropLocation.yakul_fire_opal),
    create_location(473, DropLocation.yakul_opal),
    create_location(474, DropLocation.yakul_health_vial),
    create_location(475, DropLocation.venus_10c),
    create_location(476, DropLocation.venus_yellow_morel),
    create_location(477, DropLocation.venus_dest_angel),
    create_location(478, DropLocation.neptune_10c),
    create_location(479, DropLocation.neptune_yellow_morel),
    create_location(480, DropLocation.neptune_dest_angel),
    create_location(481, DropLocation.unilateralis_10c),
    create_location(482, DropLocation.unilateralis_yellow_morel),
    create_location(483, DropLocation.unilateralis_dest_angel),
    create_location(484, DropLocation.hemalith_health_vial),
    create_location(485, DropLocation.hemalith_shrimp),
    create_location(486, DropLocation.hemallith_bloodweed),
    create_location(487, DropLocation.mi_go_ocean_bone_shell),
    create_location(488, DropLocation.mi_go_10c),
    create_location(489, DropLocation.mi_go_snowflake_obsidian),
    create_location(490, DropLocation.mare_10c),
    create_location(491, DropLocation.mare_obsidian),
    create_location(492, DropLocation.mare_onyx),
    create_location(493, DropLocation.painting_fire_opal),
    create_location(494, DropLocation.painting_10c),
    create_location(495, DropLocation.painting_mana_vial),
    create_location(496, DropLocation.painting_20c),
    create_location(497, DropLocation.phantom_10c),
    create_location(498, DropLocation.phantom_holy_water),
    create_location(499, DropLocation.phantom_moon_vial),
    create_location(500, DropLocation.phantom_ectoplasm),
    create_location(501, DropLocation.vampire_5c),
    create_location(502, DropLocation.vampire_vampiric_ashes),
    create_location(503, DropLocation.vampire_bandage),
    create_location(504, DropLocation.vampire_page_ashes),
    create_location(505, DropLocation.vampire_page_20c),
    create_location(506, DropLocation.malformed_vampiric_ashes),
    create_location(507, DropLocation.great_bat_health_vial),
    create_location(508, DropLocation.great_bat_obsidian),
    create_location(509, DropLocation.great_bat_10c),
    create_location(510, DropLocation.poltergeist_10c),
    create_location(511, DropLocation.poltergeist_ectoplasm),
    create_location(512, DropLocation.horse_10c),
    create_location(513, DropLocation.horse_mana_vial),
    create_location(514, DropLocation.hallowed_husk_10c),
    create_location(515, DropLocation.hallowed_husk_bones),
    create_location(516, DropLocation.hallowed_husk_bandage),
    create_location(517, DropLocation.hallowed_husk_light_urn),
    create_location(518, DropLocation.hallowed_husk_goldeness),
    create_location(519, DropLocation.hallowed_husk_holy_water),
    create_location(520, DropLocation.ikkurilb_root),
    create_location(521, DropLocation.ikkurilb_10c),
    create_location(522, DropLocation.ikkurilb_snowflake_obsidian),
    create_location(523, DropLocation.mimic_moon_vial),
    create_location(524, DropLocation.mimic_obsidian),
    create_location(525, DropLocation.mimic_fools_gold),
    create_location(526, DropLocation.obsidian_skeleton_10c),
    create_location(527, DropLocation.obsidian_skeleton_bones),
    create_location(528, DropLocation.obsidian_skeleton_mana_vial),
    create_location(529, DropLocation.obsidian_skeleton_obsidian),
    create_location(530, DropLocation.anpu_10c),
    create_location(531, DropLocation.anpu_fire_opal),
    create_location(532, DropLocation.serpent_antidote),
    create_location(533, DropLocation.serpent_5c),
    create_location(534, DropLocation.embalmed_bandage),
    create_location(535, DropLocation.embalmed_ashes),
    create_location(536, DropLocation.embalmed_bones),
    create_location(537, DropLocation.jailor_10c),
    create_location(538, DropLocation.jailor_candle),
    create_location(539, DropLocation.jailor_bandage),
    create_location(540, DropLocation.jailor_health_vial),
    create_location(541, DropLocation.jailor_angel),
    create_location(542, DropLocation.lunam_ectoplasm),
    create_location(543, DropLocation.lunam_10c),
    create_location(544, DropLocation.lunam_snowflake_obsidian),
    create_location(545, DropLocation.giant_dark_urn),
    create_location(546, DropLocation.giant_bones),
    create_location(547, DropLocation.giant_mana_vial),
    create_location(548, DropLocation.giant_onyx),
    create_location(549, DropLocation.sucsarian_10c),
    create_location(550, DropLocation.sucsarian_obsidian),
    create_location(551, DropLocation.sucsarian_snowflake_obsidian),
    create_location(552, DropLocation.sucsarian_throwing_knife),
    create_location(553, DropLocation.vesta_fairy_moss),
    create_location(554, DropLocation.vesta_yellow_morel),
    create_location(555, DropLocation.vesta_dest_angel),
    create_location(556, DropLocation.ceres_fairy_moss),
    create_location(557, DropLocation.ceres_yellow_morel),
    create_location(558, DropLocation.ceres_dest_angel),
    create_location(559, DropLocation.gloom_fairy_moss),
    create_location(560, DropLocation.gloom_health_vial),
    create_location(561, DropLocation.gloom_dest_angel),
    create_location(562, DropLocation.cetea_10c),
    create_location(563, DropLocation.cetea_ocean_bone_shell),
    create_location(564, DropLocation.mummy_knight_onyx),
    create_location(565, DropLocation.mummy_knight_10c),
    create_location(566, DropLocation.mummy_knight_5c),
    create_location(567, DropLocation.sanguis_book),
]




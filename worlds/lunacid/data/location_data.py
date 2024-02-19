from dataclasses import dataclass
from typing import Optional, List

from ..strings.locations import BaseLocation, ShopLocation, DropLocation
from ..strings.regions_entrances import LunacidRegion
from ..strings.weapons import Weapon
from ..strings.spells import Spell, MobSpell
from ..strings.items import UniqueItem, GenericItem, Coins, Alchemy, Creation, Switch, Progressives


@dataclass(frozen=True)
class LocationData:
    id: Optional[int]
    name: str
    region: str
    original_item: Optional[str]


events = [
    LocationData(None, "Wake the Dreamer", LunacidRegion.grave_of_the_sleeper, None),
    LocationData(None, "Defeat Prince Crilall Fanu", LunacidRegion.throne_chamber, None),
    LocationData(None, "Look Into The Abyss", LunacidRegion.grave_of_the_sleeper, None)
]

wings_rest = [
    LocationData(1, BaseLocation.wings_rest_ocean_elixir, LunacidRegion.wings_rest, UniqueItem.ocean_elixir),
    LocationData(2, BaseLocation.wings_rest_crystal_shard, LunacidRegion.wings_rest, Creation.crystal_shard),
    LocationData(3, BaseLocation.wings_rest_clives_gift, LunacidRegion.wings_rest, Creation.health_vial),
]

hollow_basin = [
    LocationData(9, BaseLocation.hollow_basin_starting_sword, LunacidRegion.hollow_basin, Weapon.replica_sword),
    LocationData(10, BaseLocation.hollow_basin_right_water_right, LunacidRegion.hollow_basin, Creation.mana_vial),
    LocationData(11, BaseLocation.hollow_basin_right_water_left, LunacidRegion.hollow_basin, Spell.ghost_light),
    LocationData(12, BaseLocation.hollow_basin_left_water, LunacidRegion.hollow_basin, Creation.health_vial),
    LocationData(13, BaseLocation.hollow_basin_demi_chest, LunacidRegion.hollow_basin, Spell.flame_spear),
    LocationData(14, BaseLocation.hollow_basin_enchanted_door, LunacidRegion.hollow_basin, Creation.health_vial),
    LocationData(15, BaseLocation.hollow_basin_dark_item, LunacidRegion.hollow_basin, Weapon.torch),

    LocationData(16, BaseLocation.temple_fountain, LunacidRegion.temple_of_silence, Creation.health_vial),
    LocationData(17, BaseLocation.temple_ritual_table, LunacidRegion.temple_of_silence, Weapon.ritual_dagger),
    LocationData(18, BaseLocation.temple_altar_chest, LunacidRegion.temple_of_silence, Spell.lithomancy),
    LocationData(19, BaseLocation.temple_pillar_left, LunacidRegion.temple_of_silence, Creation.health_vial),
    LocationData(20, BaseLocation.temple_pillar_right, LunacidRegion.temple_of_silence, Creation.health_vial),
    LocationData(21, BaseLocation.temple_ritual_ring, LunacidRegion.temple_of_silence, Spell.flame_flare),
    LocationData(22, BaseLocation.temple_small_pillar, LunacidRegion.temple_of_silence, Creation.health_vial),
    LocationData(23, BaseLocation.temple_pillar_room_left, LunacidRegion.temple_of_silence, Creation.crystal_shard),
    LocationData(24, BaseLocation.temple_pillar_room_back_left, LunacidRegion.temple_of_silence, Weapon.wooden_shield),
    LocationData(25, BaseLocation.temple_pillar_room_back_right, LunacidRegion.temple_of_silence, GenericItem.blood_wine),
    LocationData(26, BaseLocation.temple_pillar_room_hidden_room, LunacidRegion.temple_of_silence, Spell.blood_strike),
    LocationData(27, BaseLocation.temple_hidden_room_in_sewer, LunacidRegion.temple_of_silence, UniqueItem.vhs_tape),
    LocationData(28, BaseLocation.temple_table_in_sewer, LunacidRegion.temple_of_silence, Weapon.stone_club),
    LocationData(29, BaseLocation.temple_sewer_puzzle, LunacidRegion.temple_of_silence, UniqueItem.corrupted_key),
    LocationData(30, BaseLocation.temple_blood_altar, LunacidRegion.temple_of_silence, Coins.strange_coin),
    LocationData(31, BaseLocation.temple_path_to_forest, LunacidRegion.temple_of_silence, Weapon.steel_spear),
]

the_fetid_mire = [
    LocationData(37, BaseLocation.mire_room_left_foyer, LunacidRegion.fetid_mire, Creation.antidote),
    LocationData(38, BaseLocation.mire_hidden_slime_chest, LunacidRegion.fetid_mire, Spell.ice_spear),
    LocationData(39, BaseLocation.mire_upper_overlook_left, LunacidRegion.fetid_mire, Creation.crystal_shard),
    LocationData(40, BaseLocation.mire_upper_overlook_right, LunacidRegion.fetid_mire, UniqueItem.ocean_elixir),
    LocationData(41, BaseLocation.mire_bonerard_trash, LunacidRegion.fetid_mire, Creation.antidote),
    LocationData(42, BaseLocation.mire_rubble_bridge, LunacidRegion.fetid_mire, Creation.antidote),
    LocationData(43, BaseLocation.mire_skeleton_chest, LunacidRegion.fetid_mire, Spell.barrier),
    LocationData(44, BaseLocation.mire_jellisha_trash, LunacidRegion.fetid_mire, Creation.mana_vial),
    LocationData(45, BaseLocation.mire_jellisha_reward, LunacidRegion.fetid_mire, Spell.slime_orb),
    LocationData(46, BaseLocation.mire_path_to_sea_left, LunacidRegion.fetid_mire, Weapon.battle_axe),
    LocationData(47, BaseLocation.mire_path_to_sea_right, LunacidRegion.fetid_mire, Creation.health_vial),
    LocationData(48, BaseLocation.mire_hidden_chest_near_underworks, LunacidRegion.fetid_mire, UniqueItem.earth_elixir),
    LocationData(49, BaseLocation.mire_rubble_near_illusory_wall, LunacidRegion.fetid_mire, Spell.wind_dash),
    LocationData(50, BaseLocation.mire_underwater_pipe, LunacidRegion.fetid_mire, Creation.poison_throwing_knife),
    LocationData(51, BaseLocation.mire_underworks_waterfall, LunacidRegion.fetid_mire, Creation.antidote),
    LocationData(52, BaseLocation.mire_underworks_skeleton, LunacidRegion.fetid_mire, Weapon.broken_hilt),
]

the_sacrosant_sea = [
    LocationData(58, BaseLocation.sea_pillar, LunacidRegion.sanguine_sea, Weapon.corrupted_dagger),
    LocationData(59, BaseLocation.sea_underblood, LunacidRegion.sanguine_sea, Weapon.dark_rapier),
    LocationData(60, BaseLocation.sea_blood_island, LunacidRegion.sanguine_sea, Spell.summon_fairy),
    LocationData(61, BaseLocation.sea_kill_jotunn, LunacidRegion.sanguine_sea, Coins.strange_coin)]

accursed_tomb = [
    LocationData(67, BaseLocation.catacombs_coffin_stairs, LunacidRegion.accursed_tomb, Creation.health_vial),
    LocationData(68, BaseLocation.catacombs_coffin_blue_light, LunacidRegion.accursed_tomb, Spell.coffin),
    LocationData(69, BaseLocation.corrupted_room, LunacidRegion.accursed_tomb, UniqueItem.white_tape),
    LocationData(70, BaseLocation.catacombs_coffin_gate, LunacidRegion.accursed_tomb, UniqueItem.ocean_elixir),
    LocationData(71, BaseLocation.catacombs_hidden_room, LunacidRegion.accursed_tomb, UniqueItem.ocean_elixir),
    LocationData(72, BaseLocation.catacombs_deep_coffin_storage, LunacidRegion.accursed_tomb, Weapon.halberd),
    LocationData(73, BaseLocation.catacombs_restore_vampire, LunacidRegion.accursed_tomb, Weapon.blade_of_jusztina),

    LocationData(74, BaseLocation.mausoleum_hidden_chest, LunacidRegion.accursed_tomb, Weapon.twisted_staff),
    LocationData(75, BaseLocation.mausoleum_upper_table, LunacidRegion.accursed_tomb, UniqueItem.black_book),
    LocationData(76, BaseLocation.mausoleum_maze_intro, LunacidRegion.accursed_tomb, Creation.holy_water),
    LocationData(77, BaseLocation.mausoleum_maze_mid, LunacidRegion.accursed_tomb, Creation.health_vial),
    LocationData(78, BaseLocation.mausoleum_center_right, LunacidRegion.accursed_tomb, Creation.health_vial),
    LocationData(79, BaseLocation.mausoleum_center_left, LunacidRegion.accursed_tomb, Creation.holy_water),
    LocationData(80, BaseLocation.mausoleum_center_back, LunacidRegion.accursed_tomb, UniqueItem.earth_elixir),
    LocationData(81, BaseLocation.mausoleum_center_left_path, LunacidRegion.accursed_tomb, Creation.health_vial),
    LocationData(82, BaseLocation.mausoleum_center_right_path, LunacidRegion.accursed_tomb, UniqueItem.ocean_elixir),
    LocationData(83, BaseLocation.mausoleum_kill_death, LunacidRegion.accursed_tomb, Coins.strange_coin),

    LocationData(83, BaseLocation.tomb_tomb_with_switch, LunacidRegion.accursed_tomb, Weapon.vampire_hunter_sword),
    LocationData(84, BaseLocation.tomb_tomb_with_corpse, LunacidRegion.accursed_tomb, UniqueItem.survey_banner),
    LocationData(85, BaseLocation.tomb_demi_chest, LunacidRegion.accursed_tomb, Spell.lightning),
    LocationData(86, BaseLocation.tomb_near_light_switch, LunacidRegion.accursed_tomb, Creation.crystal_shard),
    LocationData(87, BaseLocation.tomb_hidden_room, LunacidRegion.accursed_tomb, UniqueItem.earth_elixir),
    LocationData(88, BaseLocation.tomb_hidden_chest, LunacidRegion.accursed_tomb, Coins.silver_100)
]

yosei_forest = [
    LocationData(94, BaseLocation.yosei_barrels, LunacidRegion.yosei_forest, Creation.health_vial),
    LocationData(95, BaseLocation.yosei_blood_pool, LunacidRegion.yosei_forest, Spell.blood_drain),
    LocationData(96, BaseLocation.yosei_branch_in_tree, LunacidRegion.yosei_forest, Spell.holy_warmth),
    LocationData(97, BaseLocation.yosei_chest_near_tree, LunacidRegion.yosei_forest, Weapon.elfen_bow),
    LocationData(98, BaseLocation.yosei_blood_plant_insides, LunacidRegion.yosei_forest, Creation.health_vial),
    LocationData(99, BaseLocation.yosei_hanging_in_trees, LunacidRegion.yosei_forest, Weapon.elfen_sword),
    LocationData(100, BaseLocation.yosei_hidden_chest, LunacidRegion.yosei_lower, Spell.light_reveal),
    LocationData(101, BaseLocation.yosei_room_defended_by_blood_plant, LunacidRegion.yosei_lower, Spell.earth_strike),
    LocationData(102, BaseLocation.yosei_patchouli_key, LunacidRegion.yosei_lower, UniqueItem.enchanted_key),
    LocationData(103, BaseLocation.yosei_patchouli_quest, LunacidRegion.yosei_lower, UniqueItem.earth_elixir),
]

forest_canopy = [
    LocationData(109, BaseLocation.canopy_branch_edge, LunacidRegion.forest_canopy, Creation.crystal_shard),
    LocationData(110, BaseLocation.branch_cave, LunacidRegion.forest_canopy, Creation.fairy_moss),
    LocationData(111, BaseLocation.canopy_chest, LunacidRegion.forest_canopy, Spell.poison_mist),
    LocationData(112, BaseLocation.canopy_wooden_statue, LunacidRegion.forest_canopy, UniqueItem.skull_of_josiah),
    LocationData(113, BaseLocation.canopy_wooden_sitting, LunacidRegion.forest_canopy, Spell.wind_slicer),
]

forbidden_archives = [
    LocationData(119, BaseLocation.archives_back_room_past_bridge, LunacidRegion.forbidden_archives, UniqueItem.ocean_elixir),
    LocationData(120, BaseLocation.archives_strange_corpse, LunacidRegion.forbidden_archives, Spell.corpse_transformation),
    LocationData(121, BaseLocation.archives_against_wall_near_trees, LunacidRegion.forbidden_archives, GenericItem.light_urn),
    LocationData(122, BaseLocation.archives_short_wall_near_trees, LunacidRegion.forbidden_archives, Creation.health_vial),
    LocationData(123, BaseLocation.archives_snail_lectern_near, LunacidRegion.forbidden_archives, Spell.light_reveal),
    LocationData(124, BaseLocation.archives_snail_lectern_far, LunacidRegion.forbidden_archives, Spell.blood_drain),
    LocationData(125, BaseLocation.archives_rug_on_balcony, LunacidRegion.forbidden_archives, Creation.mana_vial),
    LocationData(126, BaseLocation.archives_rooftop, LunacidRegion.forbidden_archives, UniqueItem.earth_elixir),
    LocationData(127, BaseLocation.archives_hidden_room_upper, LunacidRegion.forbidden_archives, Weapon.wolfram_greatsword),
    LocationData(128, BaseLocation.archives_hidden_room_lower, LunacidRegion.forbidden_archives, Creation.crystal_shard),
    LocationData(129, BaseLocation.archives_near_twisty_tree, LunacidRegion.forbidden_archives, Creation.fairy_moss),
    LocationData(130, BaseLocation.archives_uwu, LunacidRegion.forbidden_archives, Weapon.axe_of_harming),
    LocationData(131, BaseLocation.archives_daedalus_one, LunacidRegion.daedalus, Spell.fire_worm),
    LocationData(132, BaseLocation.archives_daedalus_two, LunacidRegion.daedalus, Spell.bestial_communion),
    LocationData(133, BaseLocation.archives_daedalus_third, LunacidRegion.daedalus, Spell.moon_beam),
    LocationData(134, BaseLocation.archives_corner_near_daedalus, LunacidRegion.forbidden_archives, Creation.health_vial),
]

castle_le_fanu = [
    LocationData(140, BaseLocation.castle_outside_corner, LunacidRegion.castle_le_fanu, Creation.mana_vial),
    LocationData(141, BaseLocation.castle_cell_south, LunacidRegion.castle_le_fanu_red, Creation.spectral_candle),
    LocationData(142, BaseLocation.castle_cell_west, LunacidRegion.castle_le_fanu_red, Creation.health_vial),
    LocationData(143, BaseLocation.castle_cell_center, LunacidRegion.castle_le_fanu_red, Spell.summon_ice_sword),
    LocationData(144, BaseLocation.castle_cell_north, LunacidRegion.castle_le_fanu_red, Progressives.vampiric_symbol),
    LocationData(145, BaseLocation.castle_hidden_cell, LunacidRegion.castle_le_fanu_red, Weapon.wand_of_power),

    LocationData(146, BaseLocation.castle_hallway_rubble_room, LunacidRegion.castle_le_fanu_white, GenericItem.light_urn),
    LocationData(147, BaseLocation.castle_hallway_dining_room, LunacidRegion.castle_le_fanu_white, GenericItem.blood_wine),
    LocationData(148, BaseLocation.castle_garrat_resting_room_left, LunacidRegion.castle_le_fanu_white, Creation.holy_water),
    LocationData(149, BaseLocation.castle_garrat_resting_room_back, LunacidRegion.castle_le_fanu_white, Weapon.crossbow),
    LocationData(150, BaseLocation.castle_hallway_deadend_before_door, LunacidRegion.castle_le_fanu_white, Progressives.vampiric_symbol),
    LocationData(151, BaseLocation.castle_upper_floor_coffin_small, LunacidRegion.castle_le_fanu_blue, UniqueItem.earth_elixir),
    LocationData(152, BaseLocation.castle_upper_floor_coffin_large, LunacidRegion.castle_le_fanu_blue, UniqueItem.ocean_elixir),
    LocationData(153, BaseLocation.castle_upper_floor_coffin_double, LunacidRegion.castle_le_fanu_blue, Weapon.blade_of_ophelia),
    LocationData(154, BaseLocation.castle_upper_floor_coffin_hallway, LunacidRegion.castle_le_fanu_blue, Progressives.vampiric_symbol),
]

holy_battlefield = [
    LocationData(160, BaseLocation.battlefield_book, LunacidRegion.holy_battleground, UniqueItem.black_book),
]

sealed_ballroom = [
    LocationData(166, BaseLocation.ballroom_small_room_lounge, LunacidRegion.sealed_ballroom, GenericItem.blood_wine),
    LocationData(167, BaseLocation.ballroom_entry_hidden_couch_top, LunacidRegion.sealed_ballroom, Weapon.steel_needle),
    LocationData(168, BaseLocation.ballroom_entry_hidden_couch_bottom, LunacidRegion.sealed_ballroom, Creation.health_vial),
    LocationData(169, BaseLocation.ballroom_entry_hidden_cave_in_lounge, LunacidRegion.sealed_ballroom, Creation.spectral_candle),
    LocationData(170, BaseLocation.ballroom_entry_long_table, LunacidRegion.sealed_ballroom, Creation.health_vial),
    LocationData(171, BaseLocation.ballroom_side_hidden_cave, LunacidRegion.sealed_ballroom, Creation.crystal_shard),
    LocationData(172, BaseLocation.ballroom_side_chest_near_switch, LunacidRegion.sealed_ballroom, Spell.earth_thorn),
    LocationData(173, BaseLocation.ballroom_side_painting, LunacidRegion.sealed_ballroom, UniqueItem.ocean_elixir),
    LocationData(174, BaseLocation.ballroom_side_hidden_casket_room, LunacidRegion.sealed_ballroom, Creation.health_vial),
    LocationData(175, BaseLocation.ballroom_side_xp_drain, LunacidRegion.sealed_ballroom, Weapon.flail),
]

laetus_chasm = [
    LocationData(181, BaseLocation.chasm_hidden_chest, LunacidRegion.laetus_chasm, Spell.ice_tear),
    LocationData(182, BaseLocation.chasm_invisible_cliffside, LunacidRegion.laetus_chasm, Weapon.blessed_wind)
]

great_well_surface = [
    LocationData(188, BaseLocation.surface_demi_gift, LunacidRegion.great_well_surface, Creation.crystal_shard)
]

throne_room = [
    LocationData(194, BaseLocation.throne_book, LunacidRegion.throne_chamber, UniqueItem.black_book)
]

boiling_grotto = [
    LocationData(200, BaseLocation.grotto_corpse_beneath_entrance, LunacidRegion.boiling_grotto, Coins.silver_5),
    LocationData(201, BaseLocation.grotto_slab_of_bridge, LunacidRegion.boiling_grotto, Creation.crystal_shard),
    LocationData(202, BaseLocation.grotto_hidden_chest, LunacidRegion.boiling_grotto, Coins.silver_50),
    LocationData(203, BaseLocation.grotto_triple_secret_chest, LunacidRegion.boiling_grotto, Alchemy.ashes),
    LocationData(204, BaseLocation.grotto_rocks_near_lava_switch, LunacidRegion.boiling_grotto, Spell.rock_bridge),
    LocationData(205, BaseLocation.grotto_through_switch_tunnel, LunacidRegion.boiling_grotto, Creation.mana_vial),

    LocationData(206, BaseLocation.sand_top_right_sarcophagus, LunacidRegion.sand_temple, GenericItem.cloth_bandage),
    LocationData(207, BaseLocation.sand_second_floor_snake, LunacidRegion.sand_temple, Creation.health_vial),
    LocationData(208, BaseLocation.sand_basement_snake_pit, LunacidRegion.sand_temple, Creation.staff_of_osiris),
    LocationData(209, BaseLocation.sand_room_buried_in_sand, LunacidRegion.sand_temple, Creation.staff_of_osiris),
    LocationData(210, BaseLocation.sand_basement_rubble, LunacidRegion.sand_temple, Creation.mana_vial),
    LocationData(211, BaseLocation.sand_hidden_sarcophagus, LunacidRegion.sand_temple, GenericItem.cloth_bandage),
    LocationData(212, BaseLocation.sand_second_floor_dead_end, LunacidRegion.sand_temple, Creation.health_vial),
    LocationData(213, BaseLocation.sand_lunacid_sandwich, LunacidRegion.sand_temple, Weapon.iron_claw),
    LocationData(214, BaseLocation.sand_chest_near_switch, LunacidRegion.sand_temple, Spell.ignis_calor),
    LocationData(215, BaseLocation.sand_chest_overlooking_crypt, LunacidRegion.sand_temple, UniqueItem.ocean_elixir),
    LocationData(216, BaseLocation.sand_switch_maze, LunacidRegion.sand_temple, Creation.moonlight_vial),
]

tower_of_abyss = [
    LocationData(222, BaseLocation.abyss_prize, LunacidRegion.tower_abyss, Weapon.moonlight),
    LocationData(223, BaseLocation.abyss_floor_5, LunacidRegion.tower_abyss, Creation.mana_vial),
    LocationData(224, BaseLocation.abyss_health_5, LunacidRegion.tower_abyss, Creation.health_vial),
    LocationData(225, BaseLocation.abyss_crystal_5, LunacidRegion.tower_abyss, Creation.crystal_shard),
    LocationData(226, BaseLocation.abyss_floor_10, LunacidRegion.tower_abyss, Creation.antidote),
    LocationData(227, BaseLocation.abyss_health_10, LunacidRegion.tower_abyss, Creation.health_vial),
    LocationData(228, BaseLocation.abyss_crystal_10, LunacidRegion.tower_abyss, Creation.crystal_shard),
    LocationData(229, BaseLocation.abyss_floor_15, LunacidRegion.tower_abyss, Creation.fairy_moss),
    LocationData(230, BaseLocation.abyss_health_15, LunacidRegion.tower_abyss, Creation.health_vial),
    LocationData(231, BaseLocation.abyss_crystal_15, LunacidRegion.tower_abyss, Creation.crystal_shard),
    LocationData(232, BaseLocation.abyss_floor_20, LunacidRegion.tower_abyss, Creation.spectral_candle),
    LocationData(233, BaseLocation.abyss_health_20, LunacidRegion.tower_abyss, Creation.health_vial),
    LocationData(234, BaseLocation.abyss_crystal_20, LunacidRegion.tower_abyss, Creation.crystal_shard),
    LocationData(235, BaseLocation.abyss_floor_25, LunacidRegion.tower_abyss, Creation.health_vial),
    LocationData(236, BaseLocation.abyss_health_25, LunacidRegion.tower_abyss, Creation.health_vial),
    LocationData(237, BaseLocation.abyss_crystal_25, LunacidRegion.tower_abyss, Creation.crystal_shard),
    LocationData(238, BaseLocation.abyss_floor_30, LunacidRegion.tower_abyss, UniqueItem.crystal_lantern),
    LocationData(239, BaseLocation.abyss_health_30, LunacidRegion.tower_abyss, Creation.health_vial),
    LocationData(240, BaseLocation.abyss_crystal_30, LunacidRegion.tower_abyss, Creation.crystal_shard),
    LocationData(241, BaseLocation.abyss_floor_35, LunacidRegion.tower_abyss, Coins.silver_5),
    LocationData(242, BaseLocation.abyss_health_35, LunacidRegion.tower_abyss, Creation.health_vial),
    LocationData(243, BaseLocation.abyss_crystal_35, LunacidRegion.tower_abyss, Creation.crystal_shard),
    LocationData(244, BaseLocation.abyss_floor_40, LunacidRegion.tower_abyss, Creation.spectral_candle),
    LocationData(245, BaseLocation.abyss_health_40, LunacidRegion.tower_abyss, Creation.health_vial),
    LocationData(246, BaseLocation.abyss_crystal_40, LunacidRegion.tower_abyss, Creation.crystal_shard),
    LocationData(247, BaseLocation.abyss_floor_45, LunacidRegion.tower_abyss, UniqueItem.earth_elixir),
    LocationData(248, BaseLocation.abyss_health_45, LunacidRegion.tower_abyss, Creation.health_vial),
    LocationData(249, BaseLocation.abyss_crystal_45, LunacidRegion.tower_abyss, Creation.crystal_shard),
    LocationData(250, BaseLocation.abyss_floor_50, LunacidRegion.tower_abyss, UniqueItem.ocean_elixir),
    LocationData(251, BaseLocation.abyss_health_50, LunacidRegion.tower_abyss, Creation.health_vial),
    LocationData(252, BaseLocation.abyss_crystal_50, LunacidRegion.tower_abyss, Creation.crystal_shard),
]

terminus_prison = [
    LocationData(258, BaseLocation.prison_f3_locked_left, LunacidRegion.terminus_prison, GenericItem.cloth_bandage),
    LocationData(259, BaseLocation.prison_f3_locked_right, LunacidRegion.terminus_prison, Alchemy.ashes),
    LocationData(260, BaseLocation.prison_f3_locked_south, LunacidRegion.terminus_prison, Weapon.broken_lance),
    LocationData(261, BaseLocation.prison_f3_bottomless_pit, LunacidRegion.terminus_prison, Spell.icarian_flight),
    LocationData(262, BaseLocation.prison_f2_broken_cell, LunacidRegion.terminus_prison_dark, GenericItem.cloth_bandage),
    LocationData(263, BaseLocation.prison_f2_jailer_table, LunacidRegion.terminus_prison_dark, UniqueItem.terminus_prison_key),
    LocationData(264, BaseLocation.prison_f1_hidden_cell, LunacidRegion.terminus_prison_dark, Creation.holy_water),
    LocationData(265, BaseLocation.prison_f1_hidden_debris_room, LunacidRegion.terminus_prison_dark, GenericItem.light_urn),
    LocationData(266, BaseLocation.prison_f1_remains, LunacidRegion.terminus_prison_dark, Weapon.fishing_spear),
    LocationData(267, BaseLocation.prison_b2_guarded_corner_one, LunacidRegion.terminus_prison_dark, Creation.moonlight_vial),
    LocationData(268, BaseLocation.prison_b2_guarded_corner_two, LunacidRegion.terminus_prison_dark, Creation.moonlight_vial),
    LocationData(269, BaseLocation.prison_b2_deep_alcove, LunacidRegion.terminus_prison_dark, UniqueItem.earth_elixir),
    LocationData(270, BaseLocation.prison_b2_bone_pit, LunacidRegion.terminus_prison_dark, Creation.health_vial),
    LocationData(271, BaseLocation.prison_f4_hanging, LunacidRegion.terminus_prison, Creation.health_vial),
    LocationData(272, BaseLocation.prison_f4_maledictus_secret, LunacidRegion.terminus_prison, Spell.blue_flame_arc),
    LocationData(273, BaseLocation.prison_f4_hidden_beds, LunacidRegion.terminus_prison, Creation.holy_water),
    LocationData(274, BaseLocation.prison_f4_jailer_break_room, LunacidRegion.terminus_prison, Creation.mana_vial),
    LocationData(275, BaseLocation.prison_f4_monk_room_one, LunacidRegion.terminus_prison, Alchemy.ectoplasm),
    LocationData(276, BaseLocation.prison_f4_monk_room_two, LunacidRegion.terminus_prison, Alchemy.snowflake_obsidian),
    LocationData(277, BaseLocation.prison_f4_monk_room_three, LunacidRegion.terminus_prison, Alchemy.moon_petal),
    LocationData(278, BaseLocation.prison_f4_collapsed_tunnel, LunacidRegion.terminus_prison, Weapon.hammer_of_cruelty),
]

forlorn_arena = [
    LocationData(284, BaseLocation.arena_broken_sword, LunacidRegion.forlorn_arena, Alchemy.broken_sword),
    LocationData(285, BaseLocation.arena_rock_parkour, LunacidRegion.forlorn_arena, Creation.health_vial),
    LocationData(286, BaseLocation.arena_earth_hidden_plant_haven, LunacidRegion.forlorn_arena, Weapon.shadow_blade),
    LocationData(287, BaseLocation.arena_earth_hidden_room, LunacidRegion.forlorn_arena, UniqueItem.earth_elixir),
    LocationData(288, BaseLocation.arena_earth_earthen_temple, LunacidRegion.forlorn_arena, Alchemy.fractured_life),
    LocationData(289, BaseLocation.arena_earth_chest_near_switch, LunacidRegion.forlorn_arena, UniqueItem.earth_talisman),
    LocationData(290, BaseLocation.arena_water_room_near_water, LunacidRegion.forlorn_arena, Creation.fairy_moss),
    LocationData(291, BaseLocation.arena_water_dead_end_near_water, LunacidRegion.forlorn_arena, Creation.antidote),
    LocationData(292, BaseLocation.arena_water_collapsed_end_near_balcony, LunacidRegion.forlorn_arena, Creation.health_vial),
    LocationData(293, BaseLocation.arena_water_hidden_basement_left, LunacidRegion.forlorn_arena, Creation.antidote),
    LocationData(294, BaseLocation.arena_water_hidden_basement_right, LunacidRegion.forlorn_arena, Creation.antidote),
    LocationData(295, BaseLocation.arena_water_hidden_laser_room, LunacidRegion.forlorn_arena, Weapon.obsidian_seal),
    LocationData(296, BaseLocation.arena_water_hidden_alcove_before, LunacidRegion.forlorn_arena, Creation.health_vial),
    LocationData(297, BaseLocation.arena_water_hidden_alcove_left, LunacidRegion.forlorn_arena, Creation.wisp_heart),
    LocationData(298, BaseLocation.arena_water_hidden_alcove_right, LunacidRegion.forlorn_arena, Creation.wisp_heart),
    LocationData(299, BaseLocation.arena_water_hidden_alcove_before_switch, LunacidRegion.forlorn_arena, UniqueItem.ocean_elixir),
    LocationData(300, BaseLocation.arena_water_underwater_temple, LunacidRegion.forlorn_arena, Alchemy.fractured_death),
    LocationData(301, BaseLocation.arena_water_chest_near_switch, LunacidRegion.forlorn_arena, UniqueItem.water_talisman),
]

labyrinth_of_ash = [
    LocationData(307, BaseLocation.ash_entry_coffin, LunacidRegion.labyrinth_of_ash, Creation.mana_vial),
    LocationData(308, BaseLocation.ash_jotunn_remains, LunacidRegion.labyrinth_of_ash, Creation.health_vial),
    LocationData(309, BaseLocation.ash_cetea_statue, LunacidRegion.labyrinth_of_ash, Creation.wisp_heart),
    LocationData(310, BaseLocation.ash_rocks_near_switch, LunacidRegion.labyrinth_of_ash, Spell.lava_chasm),
    LocationData(311, BaseLocation.ash_forbidden_light_chest, LunacidRegion.labyrinth_of_ash, Spell.spirit_warp),
    LocationData(312, BaseLocation.ash_hidden_chest, LunacidRegion.labyrinth_of_ash, GenericItem.dark_urn),
    LocationData(313, BaseLocation.ash_path_maze, LunacidRegion.labyrinth_of_ash, Weapon.serpent_fang),
]

chamber_of_fate = [
    LocationData(319, BaseLocation.fate_lucid_blade, LunacidRegion.chamber_of_fate, Weapon.lucid_blade)
]

base_locations = wings_rest + hollow_basin + great_well_surface + the_fetid_mire + the_sacrosant_sea + accursed_tomb + yosei_forest + \
                 forest_canopy + forbidden_archives + castle_le_fanu + holy_battlefield + sealed_ballroom + laetus_chasm + throne_room + boiling_grotto + \
                 terminus_prison + forlorn_arena + labyrinth_of_ash + chamber_of_fate
base_items: List[str] = []
[base_items.append(location.original_item) for location in base_locations if location.original_item not in base_items]

shop_locations = [
    LocationData(360, ShopLocation.buy_rapier, LunacidRegion.sheryl_the_crow, Weapon.rapier),
    LocationData(361, ShopLocation.buy_crossbow, LunacidRegion.sheryl_the_crow, Weapon.crossbow),
    LocationData(362, ShopLocation.buy_oil_lantern, LunacidRegion.sheryl_the_crow, UniqueItem.oil_lantern),
    LocationData(363, ShopLocation.buy_enchanted_key, LunacidRegion.sheryl_the_crow, UniqueItem.enchanted_key),
    LocationData(364, ShopLocation.buy_jotunn_slayer, LunacidRegion.sheryl_the_crow, Weapon.jotunn_slayer),
    LocationData(365, ShopLocation.buy_privateer_musket, LunacidRegion.sheryl_the_crow, Weapon.privateer_musket),
    LocationData(366, ShopLocation.buy_steel_needle, LunacidRegion.sheryl_the_crow, Weapon.steel_needle),
    LocationData(367, ShopLocation.buy_ocean_elixir_sheryl, LunacidRegion.sheryl_the_crow, UniqueItem.ocean_elixir),
    LocationData(368, ShopLocation.buy_ocean_elixir_patchouli, LunacidRegion.patchouli, UniqueItem.ocean_elixir),
]
shop_items: List[str] = []
[shop_items.append(location.original_item) for location in shop_locations if location.original_item not in shop_items]

mob_drop_locations = [
    LocationData(409, DropLocation.snail_drop, LunacidRegion.hollow_basin, MobSpell.summon_snail),
    LocationData(410, DropLocation.mummy_drop, LunacidRegion.temple_of_silence, Weapon.rusted_sword),
    LocationData(411, DropLocation.kodama_drop, LunacidRegion.yosei_forest, MobSpell.summon_kodama),
    LocationData(412, DropLocation.chimera_drop, LunacidRegion.forbidden_archives, MobSpell.quick_stride),
    LocationData(413, DropLocation.milk_snail_drop, LunacidRegion.hollow_basin, Weapon.ice_sickle),
    LocationData(414, DropLocation.skeleon_weapon_drop, LunacidRegion.fetid_mire, Weapon.skeleton_axe),
    LocationData(415, DropLocation.skeleton_spell_drop, LunacidRegion.fetid_mire, MobSpell.dark_skull),
    LocationData(416, DropLocation.phantom_drop, LunacidRegion.accursed_tomb, Weapon.cursed_blade),
    LocationData(417, DropLocation.obsidian_skeleton_drop_1, LunacidRegion.boiling_grotto, Weapon.obsidian_cursebrand),
    LocationData(418, DropLocation.obsidian_skeleton_drop_2, LunacidRegion.boiling_grotto, Weapon.obsidian_poisonguard),
    LocationData(419, DropLocation.anpu_drop_1, LunacidRegion.sand_temple, Weapon.golden_kopesh),
    LocationData(420, DropLocation.anpu_drop_2, LunacidRegion.sand_temple, Weapon.golden_sickle),
    LocationData(421, DropLocation.horse_drop, LunacidRegion.sealed_ballroom, Weapon.brittle_arming_sword),
    LocationData(422, DropLocation.jailor_drop, LunacidRegion.terminus_prison, Weapon.jailor_candle),
    LocationData(423, DropLocation.vampire_drop, LunacidRegion.castle_le_fanu_red, Weapon.lyrian_longsword),
    LocationData(424, DropLocation.sucsarian_drop_1, LunacidRegion.forlorn_arena, Weapon.sucsarian_spear),
    LocationData(425, DropLocation.sucsarian_drop_2, LunacidRegion.forlorn_arena, Weapon.sucsarian_dagger),
    LocationData(426, DropLocation.cetea_drop, LunacidRegion.labyrinth_of_ash, MobSpell.tornado),
    LocationData(427, DropLocation.sea_demon, LunacidRegion.sanguine_sea, UniqueItem.ocean_elixir),
]

drop_items: List[str] = []
[drop_items.append(location.original_item) for location in mob_drop_locations if location.original_item not in drop_items]

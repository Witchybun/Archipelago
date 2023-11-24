from dataclasses import dataclass
from typing import Optional

from ..strings.locations import BaseLocation, ShopLocation
from ..strings.regions_entrances import LunacidRegion
from ..strings.weapons import Weapon
from ..strings.spells import Spell
from ..strings.items import UniqueItem, GenericItem, Coins, Alchemy, Creation


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
]

hollow_basin = [
    LocationData(3, BaseLocation.hollow_basin_dark_item, LunacidRegion.hollow_basin, Weapon.torch),
    LocationData(4, BaseLocation.hollow_basin_demi_chest, LunacidRegion.hollow_basin, Spell.flame_spear),
    LocationData(5, BaseLocation.hollow_basin_enchanted_door, LunacidRegion.hollow_basin, Creation.health_vial),
    LocationData(6, BaseLocation.hollow_basin_left_water, LunacidRegion.hollow_basin, Creation.health_vial),
    LocationData(7, BaseLocation.hollow_basin_starting_sword, LunacidRegion.hollow_basin, Weapon.replica_sword),
    LocationData(8, BaseLocation.hollow_basin_right_water_left, LunacidRegion.hollow_basin, Spell.ghost_light),
    LocationData(9, BaseLocation.hollow_basin_right_water_right, LunacidRegion.hollow_basin, Creation.mana_vial),
    LocationData(10, BaseLocation.temple_fountain, LunacidRegion.temple_of_silence, Creation.health_vial),
    LocationData(11, BaseLocation.temple_ritual_table, LunacidRegion.temple_of_silence, Weapon.ritual_dagger),
    LocationData(12, BaseLocation.temple_altar_chest, LunacidRegion.temple_of_silence, Spell.lithomancy),
    LocationData(13, BaseLocation.temple_small_pillar, LunacidRegion.temple_of_silence, Creation.health_vial),
    LocationData(14, BaseLocation.temple_ritual_ring, LunacidRegion.temple_of_silence, Spell.flame_flare),
    LocationData(15, BaseLocation.temple_pillar_room_back_left, LunacidRegion.temple_of_silence, Creation.health_vial),
    LocationData(16, BaseLocation.temple_pillar_room_back_right, LunacidRegion.temple_of_silence, Creation.health_vial),
    LocationData(17, BaseLocation.temple_pillar_room_left, LunacidRegion.temple_of_silence, Creation.crystal_shard),
    LocationData(18, BaseLocation.temple_pillar_room_back_left, LunacidRegion.temple_of_silence, Weapon.wooden_shield),
    LocationData(19, BaseLocation.temple_pillar_room_back_right, LunacidRegion.temple_of_silence, GenericItem.blood_wine),
    LocationData(20, BaseLocation.temple_pillar_room_hidden_room, LunacidRegion.temple_of_silence, Spell.blood_strike),
    LocationData(21, BaseLocation.temple_hidden_room_in_sewer, LunacidRegion.temple_of_silence, UniqueItem.vhs_tape),
    LocationData(22, BaseLocation.temple_table_in_sewer, LunacidRegion.temple_of_silence, Weapon.stone_club),
    LocationData(23, BaseLocation.temple_sewer_puzzle, LunacidRegion.temple_of_silence, UniqueItem.corrupted_key),
    LocationData(24, BaseLocation.temple_blood_altar, LunacidRegion.temple_of_silence, Coins.strange_coin)
]

the_fetid_mire = [
    LocationData(25, BaseLocation.mire_bonerard_trash, LunacidRegion.fetid_mire, Creation.antidote),
    LocationData(26, BaseLocation.mire_jellisha_reward, LunacidRegion.fetid_mire, Spell.slime_orb),
    LocationData(27, BaseLocation.mire_jellisha_trash, LunacidRegion.fetid_mire, Creation.mana_vial),
    LocationData(28, BaseLocation.mire_rubble_bridge, LunacidRegion.fetid_mire, Creation.antidote),
    LocationData(29, BaseLocation.mire_skeleton_chest, LunacidRegion.fetid_mire, Spell.barrier),
    LocationData(30, BaseLocation.mire_hidden_chest_near_underworks, LunacidRegion.fetid_mire, UniqueItem.earth_elixir),
    LocationData(31, BaseLocation.mire_hidden_slime_chest, LunacidRegion.fetid_mire, Spell.ice_spear),
    LocationData(32, BaseLocation.mire_room_left_foyer, LunacidRegion.fetid_mire, Creation.antidote),
    LocationData(33, BaseLocation.mire_rubble_near_illusory_wall, LunacidRegion.fetid_mire, Spell.wind_dash),
    LocationData(34, BaseLocation.mire_underwater_pipe, LunacidRegion.fetid_mire, Creation.poison_throwing_knife),
    LocationData(35, BaseLocation.mire_underworks_skeleton, LunacidRegion.fetid_mire, Weapon.broken_hilt),
    LocationData(36, BaseLocation.mire_underworks_waterfall, LunacidRegion.fetid_mire, Creation.antidote),
    LocationData(37, BaseLocation.mire_upper_overlook_left, LunacidRegion.fetid_mire, Creation.crystal_shard),
    LocationData(38, BaseLocation.mire_upper_overlook_right, LunacidRegion.fetid_mire, UniqueItem.ocean_elixir),
]

the_sacrosant_sea = [
    LocationData(39, BaseLocation.sea_demon, LunacidRegion.sanguine_sea, UniqueItem.ocean_elixir),
    LocationData(40, BaseLocation.sea_pillar, LunacidRegion.sanguine_sea, Weapon.corrupted_dagger),
    LocationData(41, BaseLocation.sea_underblood, LunacidRegion.sanguine_sea, Weapon.dark_rapier),
    LocationData(42, BaseLocation.sea_blood_island, LunacidRegion.sanguine_sea, Spell.summon_fairy),
    LocationData(43, BaseLocation.sea_kill_jotunn, LunacidRegion.sanguine_sea, Coins.strange_coin)]

accursed_tomb = [
    LocationData(44, BaseLocation.catacombs_coffin_stairs, LunacidRegion.accursed_tomb, Creation.health_vial),
    LocationData(45, BaseLocation.catacombs_hidden_room, LunacidRegion.accursed_tomb, UniqueItem.ocean_elixir),
    LocationData(46, BaseLocation.corrupted_room, LunacidRegion.accursed_tomb, UniqueItem.white_tape),
    LocationData(47, BaseLocation.catacombs_restore_vampire, LunacidRegion.accursed_tomb, Weapon.blade_of_jusztina),
    LocationData(48, BaseLocation.catacombs_coffin_blue_light, LunacidRegion.accursed_tomb, Spell.coffin),
    LocationData(49, BaseLocation.catacombs_coffin_gate, LunacidRegion.accursed_tomb, UniqueItem.ocean_elixir),
    LocationData(50, BaseLocation.catacombs_deep_coffin_storage, LunacidRegion.accursed_tomb, Weapon.halberd),
    LocationData(51, BaseLocation.mausoleum_hidden_chest, LunacidRegion.accursed_tomb, Weapon.twisted_staff),
    LocationData(52, BaseLocation.mausoleum_maze_intro, LunacidRegion.accursed_tomb, Creation.holy_water),
    LocationData(53, BaseLocation.mausoleum_upper_table, LunacidRegion.accursed_tomb, UniqueItem.black_book),
    LocationData(54, BaseLocation.mausoleum_maze_mid, LunacidRegion.accursed_tomb, Creation.health_vial),
    LocationData(55, BaseLocation.mausoleum_center_back, LunacidRegion.accursed_tomb, UniqueItem.earth_elixir),
    LocationData(56, BaseLocation.mausoleum_center_right, LunacidRegion.accursed_tomb, Creation.health_vial),
    LocationData(57, BaseLocation.mausoleum_center_left, LunacidRegion.accursed_tomb, Creation.holy_water),
    LocationData(58, BaseLocation.mausoleum_center_left_path, LunacidRegion.accursed_tomb, Creation.health_vial),
    LocationData(59, BaseLocation.mausoleum_center_right_path, LunacidRegion.accursed_tomb, UniqueItem.ocean_elixir),
    LocationData(60, BaseLocation.tomb_demi_chest, LunacidRegion.accursed_tomb, Spell.lightning),
    LocationData(61, BaseLocation.tomb_hidden_room, LunacidRegion.accursed_tomb, UniqueItem.earth_elixir),
    LocationData(62, BaseLocation.tomb_tomb_with_corpse, LunacidRegion.accursed_tomb, UniqueItem.survey_banner),
    LocationData(63, BaseLocation.tomb_tomb_with_switch, LunacidRegion.accursed_tomb, Weapon.vampire_hunter_sword),
    LocationData(64, BaseLocation.tomb_near_light_switch, LunacidRegion.accursed_tomb, Creation.crystal_shard),
    LocationData(65, BaseLocation.tomb_hidden_chest, LunacidRegion.accursed_tomb, Coins.silver_100)
]

yosei_forest = [
    LocationData(66, BaseLocation.yosei_patchouli_key, LunacidRegion.yosei_lower, UniqueItem.enchanted_key),
    LocationData(67, BaseLocation.yosei_barrels, LunacidRegion.yosei_forest, Creation.health_vial),
    LocationData(68, BaseLocation.yosei_blood_pool, LunacidRegion.yosei_forest, Spell.blood_drain),
    LocationData(69, BaseLocation.yosei_branch_in_tree, LunacidRegion.yosei_forest, Spell.holy_warmth),
    LocationData(70, BaseLocation.yosei_chest_near_tree, LunacidRegion.yosei_forest, Weapon.elfen_bow),
    LocationData(71, BaseLocation.yosei_blood_plant_insides, LunacidRegion.yosei_forest, Creation.health_vial),
    LocationData(72, BaseLocation.yosei_hanging_in_trees, LunacidRegion.yosei_forest, Weapon.elfen_sword),
    LocationData(73, BaseLocation.yosei_hidden_chest, LunacidRegion.yosei_lower, Spell.light_reveal),
    LocationData(74, BaseLocation.yosei_room_defended_by_blood_plant, LunacidRegion.yosei_lower, Spell.earth_strike),
    LocationData(75, BaseLocation.yosei_patchouli_quest, LunacidRegion.yosei_lower, UniqueItem.earth_elixir),
]

forest_canopy = [
    LocationData(76, BaseLocation.canopy_branch_edge, LunacidRegion.forest_canopy, Creation.crystal_shard),
    LocationData(77, BaseLocation.canopy_chest, LunacidRegion.forest_canopy, Spell.poison_mist),
    LocationData(78, BaseLocation.canopy_wooden_statue, LunacidRegion.forest_canopy, UniqueItem.skull_of_josiah),
    LocationData(79, BaseLocation.canopy_wooden_sitting, LunacidRegion.forest_canopy, Spell.wind_slicer),
]

forbidden_archives = [
    LocationData(80, BaseLocation.archives_snail_lectern_near, LunacidRegion.forbidden_archives, Spell.light_reveal),
    LocationData(81, BaseLocation.archives_snail_lectern_far, LunacidRegion.forbidden_archives, Spell.blood_drain),
    LocationData(82, BaseLocation.archives_back_room_past_bridge, LunacidRegion.forbidden_archives, UniqueItem.ocean_elixir),
    LocationData(83, BaseLocation.archives_strange_corpse, LunacidRegion.forbidden_archives, Spell.corpse_transformation),
    LocationData(84, BaseLocation.archives_short_wall_near_trees, LunacidRegion.forbidden_archives, Creation.health_vial),
    LocationData(85, BaseLocation.archives_against_wall_near_trees, LunacidRegion.forbidden_archives, GenericItem.light_urn),
    LocationData(86, BaseLocation.archives_hidden_room_upper, LunacidRegion.forbidden_archives, Weapon.wolfram_greatsword),
    LocationData(87, BaseLocation.archives_rooftop, LunacidRegion.forbidden_archives, UniqueItem.earth_elixir),
    LocationData(88, BaseLocation.archives_rug_on_balcony, LunacidRegion.forbidden_archives, Creation.mana_vial),
    LocationData(89, BaseLocation.archives_hidden_room_lower, LunacidRegion.forbidden_archives, Creation.crystal_shard),
    LocationData(90, BaseLocation.archives_near_twisty_tree, LunacidRegion.forbidden_archives, Creation.fairy_moss),
    LocationData(91, BaseLocation.archives_daedalus_one, LunacidRegion.daedalus, Spell.fire_worm),
    LocationData(92, BaseLocation.archives_daedalus_two, LunacidRegion.daedalus, Spell.bestial_communion),
    LocationData(93, BaseLocation.archives_daedalus_third, LunacidRegion.daedalus, Spell.moon_beam),
]

castle_le_fanu = [
    LocationData(94, BaseLocation.castle_outside_corner, LunacidRegion.castle_le_fanu, Creation.mana_vial),
    LocationData(95, BaseLocation.castle_cell_south, LunacidRegion.castle_le_fanu_red, Creation.spectral_candle),
    LocationData(96, BaseLocation.castle_cell_west, LunacidRegion.castle_le_fanu_red, Creation.health_vial),
    LocationData(97, BaseLocation.castle_cell_center, LunacidRegion.castle_le_fanu_red, Spell.summon_ice_sword),
    LocationData(98, BaseLocation.castle_cell_north, LunacidRegion.castle_le_fanu_red, UniqueItem.vampiric_symbol_w),
    LocationData(99, BaseLocation.castle_hidden_cell, LunacidRegion.castle_le_fanu_red, Weapon.wand_of_power),
    LocationData(100, BaseLocation.castle_hallway_rubble_room, LunacidRegion.castle_le_fanu_white, GenericItem.light_urn),
    LocationData(101, BaseLocation.castle_hallway_dining_room, LunacidRegion.castle_le_fanu_white, GenericItem.blood_wine),
    LocationData(102, BaseLocation.castle_garrat_resting_room_left, LunacidRegion.castle_le_fanu_white, Creation.holy_water),
    LocationData(103, BaseLocation.castle_garrat_resting_room_back, LunacidRegion.castle_le_fanu_white, Weapon.crossbow),
    LocationData(104, BaseLocation.castle_hallway_deadend_before_door, LunacidRegion.castle_le_fanu_white, UniqueItem.vampiric_symbol_a),
    LocationData(105, BaseLocation.castle_upper_floor_coffin_small, LunacidRegion.castle_le_fanu_blue, UniqueItem.earth_elixir),
    LocationData(106, BaseLocation.castle_upper_floor_coffin_large, LunacidRegion.castle_le_fanu_blue, UniqueItem.ocean_elixir),
    LocationData(107, BaseLocation.castle_upper_floor_coffin_double, LunacidRegion.castle_le_fanu_blue, Weapon.blade_of_ophelia),
    LocationData(108, BaseLocation.castle_upper_floor_coffin_hallway, LunacidRegion.castle_le_fanu_blue, UniqueItem.vampiric_symbol_e),
]

holy_battlefield = [
    LocationData(109, BaseLocation.battlefield_book, LunacidRegion.holy_battleground, UniqueItem.black_book),
]

sealed_ballroom = [
    LocationData(110, BaseLocation.ballroom_entry_hidden_cave_in_lounge, LunacidRegion.sealed_ballroom, Creation.spectral_candle),
    LocationData(111, BaseLocation.ballroom_small_room_lounge, LunacidRegion.sealed_ballroom, GenericItem.blood_wine),
    LocationData(112, BaseLocation.ballroom_entry_long_table, LunacidRegion.sealed_ballroom, Creation.health_vial),
    LocationData(113, BaseLocation.ballroom_entry_hidden_couch_top, LunacidRegion.sealed_ballroom, Weapon.steel_needle),
    LocationData(114, BaseLocation.ballroom_entry_hidden_couch_bottom, LunacidRegion.sealed_ballroom, Creation.health_vial),
    LocationData(115, BaseLocation.ballroom_side_chest_near_switch, LunacidRegion.sealed_ballroom, Spell.earth_thorn),
    LocationData(116, BaseLocation.ballroom_side_hidden_casket_room, LunacidRegion.sealed_ballroom, Creation.health_vial),
    LocationData(117, BaseLocation.ballroom_side_hidden_cave, LunacidRegion.sealed_ballroom, Creation.crystal_shard),
    LocationData(118, BaseLocation.ballroom_side_painting, LunacidRegion.sealed_ballroom, UniqueItem.ocean_elixir),
    LocationData(119, BaseLocation.ballroom_side_xp_drain, LunacidRegion.sealed_ballroom, Weapon.flail),
]

laetus_chasm = [
    LocationData(120, BaseLocation.chasm_hidden_chest, LunacidRegion.laetus_chasm, Spell.ice_tear),
    LocationData(121, BaseLocation.chasm_invisible_cliffside, LunacidRegion.laetus_chasm, Weapon.blessed_wind)
]

great_well_surface = [
    LocationData(122, BaseLocation.surface_demi_gift, LunacidRegion.great_well_surface, Creation.crystal_shard)
]

throne_room = [
    LocationData(123, BaseLocation.throne_book, LunacidRegion.throne_chamber, UniqueItem.black_book)
]

boiling_grotto = [
    LocationData(124, BaseLocation.grotto_slab_of_bridge, LunacidRegion.boiling_grotto, Creation.crystal_shard),
    LocationData(125, BaseLocation.grotto_triple_secret_chest, LunacidRegion.boiling_grotto, Alchemy.ashes),
    LocationData(126, BaseLocation.grotto_hidden_chest, LunacidRegion.boiling_grotto, Creation.moonlight_vial),
    LocationData(127, BaseLocation.grotto_rocks_near_lava_switch, LunacidRegion.boiling_grotto, Spell.rock_bridge),
    LocationData(128, BaseLocation.grotto_through_switch_tunnel, LunacidRegion.boiling_grotto, Creation.mana_vial),
    LocationData(129, BaseLocation.sand_room_buried_in_sand, LunacidRegion.sand_temple, Creation.health_vial),
    LocationData(130, BaseLocation.sand_lunacid_sandwich, LunacidRegion.sand_temple, Weapon.iron_claw),
    LocationData(131, BaseLocation.sand_hidden_sarcophagus, LunacidRegion.sand_temple, GenericItem.cloth_bandage),
    LocationData(132, BaseLocation.sand_switch_maze, LunacidRegion.sand_temple, Coins.silver_2),
    LocationData(133, BaseLocation.sand_triple_sarcophagus, LunacidRegion.sand_temple, Coins.silver_5),
    LocationData(134, BaseLocation.sand_chest_near_switch, LunacidRegion.sand_temple, Spell.ignis_calor),
    LocationData(135, BaseLocation.sand_chest_overlooking_crypt, LunacidRegion.sand_temple, UniqueItem.ocean_elixir),
    LocationData(136, BaseLocation.sand_second_floor_dead_end, LunacidRegion.sand_temple, Creation.health_vial),
]

tower_of_abyss = [
    LocationData(137, BaseLocation.abyss_prize, LunacidRegion.tower_abyss, Weapon.moonlight),
    LocationData(138, BaseLocation.abyss_floor_5, LunacidRegion.tower_abyss, Creation.mana_vial),
    LocationData(139, BaseLocation.abyss_floor_10, LunacidRegion.tower_abyss, Creation.antidote),
    LocationData(140, BaseLocation.abyss_floor_15, LunacidRegion.tower_abyss, Creation.fairy_moss),
    LocationData(141, BaseLocation.abyss_floor_20, LunacidRegion.tower_abyss, Creation.spectral_candle),
    LocationData(142, BaseLocation.abyss_floor_25, LunacidRegion.tower_abyss, Creation.health_vial),
    LocationData(143, BaseLocation.abyss_floor_30, LunacidRegion.tower_abyss, UniqueItem.crystal_lantern),
    LocationData(144, BaseLocation.abyss_floor_35, LunacidRegion.tower_abyss, Coins.silver_5),
    LocationData(145, BaseLocation.abyss_floor_40, LunacidRegion.tower_abyss, Creation.spectral_candle),
    LocationData(146, BaseLocation.abyss_floor_45, LunacidRegion.tower_abyss, UniqueItem.earth_elixir),
    LocationData(147, BaseLocation.abyss_floor_50, LunacidRegion.tower_abyss, UniqueItem.ocean_elixir)
]

terminus_prison = [
    LocationData(148, BaseLocation.prison_f3_locked_left, LunacidRegion.terminus_prison, GenericItem.cloth_bandage),
    LocationData(149, BaseLocation.prison_f3_locked_right, LunacidRegion.terminus_prison, Alchemy.ashes),
    LocationData(150, BaseLocation.prison_f3_locked_south, LunacidRegion.terminus_prison, Weapon.broken_lance),
    LocationData(151, BaseLocation.prison_f3_bottomless_pit, LunacidRegion.terminus_prison, Spell.icarian_flight),
    LocationData(152, BaseLocation.prison_f2_broken_cell, LunacidRegion.terminus_prison_dark, GenericItem.cloth_bandage),
    LocationData(153, BaseLocation.prison_f2_jailer_table, LunacidRegion.terminus_prison_dark, Alchemy.ashes),
    LocationData(154, BaseLocation.prison_f1_hidden_debris_room, LunacidRegion.terminus_prison_dark, GenericItem.light_urn),
    LocationData(155, BaseLocation.prison_f1_remains, LunacidRegion.terminus_prison_dark, Weapon.fishing_spear),
    LocationData(156, BaseLocation.prison_f1_hidden_cell, LunacidRegion.terminus_prison_dark, Creation.health_vial),
    LocationData(157, BaseLocation.prison_f4_hanging, LunacidRegion.terminus_prison, Creation.health_vial),
    LocationData(158, BaseLocation.prison_f4_monk_room_one, LunacidRegion.terminus_prison, Alchemy.ectoplasm),
    LocationData(159, BaseLocation.prison_f4_monk_room_two, LunacidRegion.terminus_prison, Alchemy.snowflake_obsidian),
    LocationData(160, BaseLocation.prison_f4_monk_room_three, LunacidRegion.terminus_prison, Alchemy.moon_petal),
    LocationData(161, BaseLocation.prison_f4_jailer_break_room, LunacidRegion.terminus_prison, Creation.mana_vial),
    LocationData(162, BaseLocation.prison_f4_hidden_beds, LunacidRegion.terminus_prison, Creation.holy_water),
    LocationData(163, BaseLocation.prison_f4_maledictus_secret, LunacidRegion.terminus_prison, Spell.blue_flame_arc),
    LocationData(164, BaseLocation.prison_f4_collapsed_tunnel, LunacidRegion.terminus_prison, Weapon.hammer_of_cruelty),
    LocationData(165, BaseLocation.prison_b2_bone_pit, LunacidRegion.terminus_prison_dark, Creation.health_vial),
    LocationData(166, BaseLocation.prison_b2_deep_alcove, LunacidRegion.terminus_prison_dark, UniqueItem.earth_elixir),
    LocationData(167, BaseLocation.prison_b2_guarded_corner_one, LunacidRegion.terminus_prison_dark, Creation.moonlight_vial),
    LocationData(168, BaseLocation.prison_b2_guarded_corner_two, LunacidRegion.terminus_prison_dark, Creation.moonlight_vial),
]

forlorn_arena = [
    LocationData(169, BaseLocation.arena_rock_parkour, LunacidRegion.forlorn_arena, Creation.health_vial),
    LocationData(170, BaseLocation.arena_water_room_near_water, LunacidRegion.forlorn_arena, Creation.fairy_moss),
    LocationData(171, BaseLocation.arena_water_dead_end_near_water, LunacidRegion.forlorn_arena, Creation.antidote),
    LocationData(172, BaseLocation.arena_water_collapsed_end_near_balcony, LunacidRegion.forlorn_arena, Creation.health_vial),
    LocationData(173, BaseLocation.arena_water_hidden_alcove_before, LunacidRegion.forlorn_arena, Creation.health_vial),
    LocationData(174, BaseLocation.arena_water_hidden_alcove_after, LunacidRegion.forlorn_arena, UniqueItem.ocean_elixir),
    LocationData(175, BaseLocation.arena_water_underwater_temple, LunacidRegion.forlorn_arena, Alchemy.fractured_death),
    LocationData(176, BaseLocation.arena_water_chest_near_switch, LunacidRegion.forlorn_arena, UniqueItem.water_talisman),
    LocationData(177, BaseLocation.arena_earth_hidden_room, LunacidRegion.forlorn_arena, UniqueItem.earth_elixir),
    LocationData(178, BaseLocation.arena_earth_hidden_plant_haven, LunacidRegion.forlorn_arena, Weapon.shadow_blade),
    LocationData(179, BaseLocation.arena_earth_earthen_temple, LunacidRegion.forlorn_arena, Alchemy.fractured_life),
    LocationData(180, BaseLocation.arena_earth_hidden_room, LunacidRegion.forlorn_arena, UniqueItem.earth_talisman)
]

labyrinth_of_ash = [
    LocationData(181, BaseLocation.ash_entry_coffin, LunacidRegion.labyrinth_of_ash, Creation.mana_vial),
    LocationData(182, BaseLocation.ash_jotunn_remains, LunacidRegion.labyrinth_of_ash, Creation.health_vial),
    LocationData(183, BaseLocation.ash_cetea_statue, LunacidRegion.labyrinth_of_ash, Creation.wisp_heart),
    LocationData(184, BaseLocation.ash_rocks_near_switch, LunacidRegion.labyrinth_of_ash, Spell.lava_chasm),
    LocationData(185, BaseLocation.ash_forbidden_light_chest, LunacidRegion.labyrinth_of_ash, Spell.spirit_warp),
    LocationData(186, BaseLocation.ash_hidden_chest, LunacidRegion.labyrinth_of_ash, GenericItem.dark_urn)
]

chamber_of_fate = [
    LocationData(187, BaseLocation.fate_lucid_blade, LunacidRegion.chamber_of_fate, Weapon.lucid_blade)
]


base_locations = wings_rest + hollow_basin + great_well_surface + the_fetid_mire + the_sacrosant_sea + accursed_tomb + yosei_forest + \
                 forest_canopy + forbidden_archives + castle_le_fanu + holy_battlefield + sealed_ballroom + laetus_chasm + throne_room + boiling_grotto + \
                 terminus_prison + forlorn_arena + labyrinth_of_ash + chamber_of_fate

switch_locations = []

shop_locations = [
    LocationData(188, ShopLocation.buy_rapier, LunacidRegion.sheryl_the_crow, Weapon.rapier),
    LocationData(189, ShopLocation.buy_crossbow, LunacidRegion.sheryl_the_crow, Weapon.crossbow),
    LocationData(190, ShopLocation.buy_oil_lantern, LunacidRegion.sheryl_the_crow, UniqueItem.oil_lantern),
    LocationData(191, ShopLocation.buy_enchanted_key, LunacidRegion.sheryl_the_crow, UniqueItem.enchanted_key),
    LocationData(192, ShopLocation.buy_jotunn_slayer, LunacidRegion.sheryl_the_crow, Weapon.jotunn_slayer),
    LocationData(193, ShopLocation.buy_privateer_musket, LunacidRegion.sheryl_the_crow, Weapon.privateer_musket),
    LocationData(194, ShopLocation.buy_steel_needle, LunacidRegion.sheryl_the_crow, Weapon.steel_needle),
    LocationData(195, ShopLocation.buy_ocean_elixir, LunacidRegion.sheryl_the_crow, UniqueItem.ocean_elixir)
]

mob_drop_locations = []

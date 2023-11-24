from dataclasses import dataclass
from typing import List, TypedDict

from ..strings.locations import Location
from ..strings.regions_entrances import Region
from ..strings.weapons import Weapon
from ..strings.spells import Spell
from ..strings.items import UniqueItem, GenericItem, Coins, Alchemy


@dataclass(frozen=True)
class LocationData:
    name: str
    region: str
    original_item: str


wings_rest = [
    LocationData(Location.wings_rest_ocean_elixir, Region.wings_rest, UniqueItem.ocean_elixir),
    LocationData(Location.wings_rest_crystal_shard, Region.wings_rest, GenericItem.crystal_shard),
]

hollow_basin = [
    LocationData(Location.hollow_basin_dark_item, Region.hollow_basin, Weapon.torch),
    LocationData(Location.hollow_basin_demi_chest, Region.hollow_basin, Spell.flame_spear),
    LocationData(Location.hollow_basin_enchanted_door, Region.hollow_basin, GenericItem.health_vial),
    LocationData(Location.hollow_basin_left_water, Region.hollow_basin, GenericItem.health_vial),
    LocationData(Location.hollow_basin_starting_sword, Region.hollow_basin, Weapon.replica_sword),
    LocationData(Location.hollow_basin_right_water_left, Region.hollow_basin, Spell.ghost_light),
    LocationData(Location.hollow_basin_right_water_right, Region.hollow_basin, GenericItem.mana_vial),
    LocationData(Location.temple_fountain, Region.temple_of_silence, GenericItem.health_vial),
    LocationData(Location.temple_ritual_table, Region.temple_of_silence, Weapon.ritual_dagger),
    LocationData(Location.temple_altar_chest, Region.temple_of_silence, Spell.lithomancy),
    LocationData(Location.temple_small_pillar, Region.temple_of_silence, GenericItem.health_vial),
    LocationData(Location.temple_ritual_ring, Region.temple_of_silence, Spell.flame_flare),
    LocationData(Location.temple_pillar_room_back_left, Region.temple_of_silence, GenericItem.health_vial),
    LocationData(Location.temple_pillar_room_back_right, Region.temple_of_silence, GenericItem.health_vial),
    LocationData(Location.temple_pillar_room_left, Region.temple_of_silence, GenericItem.crystal_shard),
    LocationData(Location.temple_pillar_room_back_left, Region.temple_of_silence, Weapon.wooden_shield),
    LocationData(Location.temple_pillar_room_back_right, Region.temple_of_silence, GenericItem.blood_wine),
    LocationData(Location.temple_pillar_room_hidden_room, Region.temple_of_silence, Spell.blood_strike),
    LocationData(Location.temple_hidden_room_in_sewer, Region.temple_of_silence, UniqueItem.vhs_tape),
    LocationData(Location.temple_table_in_sewer, Region.temple_of_silence, Weapon.stone_club),
    LocationData(Location.temple_sewer_puzzle, Region.temple_of_silence, UniqueItem.corrupted_key),
]

the_fetid_mire = [
    LocationData(Location.mire_bonerard_trash, Region.fetid_mire, GenericItem.antidote),
    LocationData(Location.mire_jellisha_reward, Region.fetid_mire, Spell.slime_orb),
    LocationData(Location.mire_jellisha_trash, Region.fetid_mire, GenericItem.mana_vial),
    LocationData(Location.mire_rubble_bridge, Region.fetid_mire, GenericItem.antidote),
    LocationData(Location.mire_skeleton_chest, Region.fetid_mire, Spell.barrier),
    LocationData(Location.mire_hidden_chest_near_underworks, Region.fetid_mire, UniqueItem.earth_elixir),
    LocationData(Location.mire_hidden_slime_chest, Region.fetid_mire, Spell.ice_spear),
    LocationData(Location.mire_room_left_foyer, Region.fetid_mire, GenericItem.antidote),
    LocationData(Location.mire_rubble_near_illusory_wall, Region.fetid_mire, Spell.wind_dash),
    LocationData(Location.mire_underwater_pipe, Region.fetid_mire, GenericItem.poison_throwing_knife),
    LocationData(Location.mire_underworks_skeleton, Region.fetid_mire, Weapon.broken_hilt),
    LocationData(Location.mire_underworks_waterfall, Region.fetid_mire, GenericItem.antidote),
    LocationData(Location.mire_upper_overlook_left, Region.fetid_mire, GenericItem.crystal_shard),
    LocationData(Location.mire_upper_overlook_right, Region.fetid_mire, UniqueItem.ocean_elixir),
]

the_sacrosant_sea = [
    LocationData(Location.sea_demon, Region.sanguine_sea, UniqueItem.ocean_elixir),
    LocationData(Location.sea_pillar, Region.sanguine_sea, Weapon.corrupted_dagger),
    LocationData(Location.sea_underblood, Region.sanguine_sea, Weapon.dark_rapier),
    LocationData(Location.sea_blood_island, Region.sanguine_sea, Spell.summon_fairy),]

accursed_tomb = [
    LocationData(Location.catacombs_coffin_stairs, Region.accursed_tomb, GenericItem.health_vial),
    LocationData(Location.catacombs_hidden_room, Region.accursed_tomb, UniqueItem.ocean_elixir),
    LocationData(Location.corrupted_room, Region.accursed_tomb, UniqueItem.white_tape),
    LocationData(Location.catacombs_restore_vampire, Region.accursed_tomb, Weapon.blade_of_jusztina),
    LocationData(Location.catacombs_coffin_blue_light, Region.accursed_tomb, Spell.coffin),
    LocationData(Location.catacombs_coffin_gate, Region.accursed_tomb, UniqueItem.ocean_elixir),
    LocationData(Location.catacombs_deep_coffin_storage, Region.accursed_tomb, Weapon.halberd),
    LocationData(Location.mausoleum_hidden_chest, Region.accursed_tomb, Weapon.twisted_staff),
    LocationData(Location.mausoleum_maze_intro, Region.accursed_tomb, GenericItem.holy_water),
    LocationData(Location.mausoleum_upper_table, Region.accursed_tomb, UniqueItem.black_book),
    LocationData(Location.mausoleum_maze_mid, Region.accursed_tomb, GenericItem.health_vial),
    LocationData(Location.mausoleum_center_back, Region.accursed_tomb, UniqueItem.earth_elixir),
    LocationData(Location.mausoleum_center_right, Region.accursed_tomb, GenericItem.health_vial),
    LocationData(Location.mausoleum_center_left, Region.accursed_tomb, GenericItem.holy_water),
    LocationData(Location.mausoleum_center_left_path, Region.accursed_tomb, GenericItem.health_vial),
    LocationData(Location.mausoleum_center_right_path, Region.accursed_tomb, UniqueItem.ocean_elixir),
    LocationData(Location.tomb_demi_chest, Region.accursed_tomb, Spell.lightning),
    LocationData(Location.tomb_hidden_room, Region.accursed_tomb, UniqueItem.earth_elixir),
    LocationData(Location.tomb_tomb_with_corpse, Region.accursed_tomb, UniqueItem.survey_banner),
    LocationData(Location.tomb_tomb_with_switch, Region.accursed_tomb, Weapon.vampire_hunter_sword),
    LocationData(Location.tomb_near_light_switch, Region.accursed_tomb, GenericItem.crystal_shard),
    LocationData(Location.tomb_hidden_chest, Region.accursed_tomb, Coins.silver_100)
]

yosei_forest = [
    LocationData(Location.yosei_patchouli_key, Region.yosei_lower, UniqueItem.enchanted_key),
    LocationData(Location.yosei_barrels, Region.yosei_forest, GenericItem.health_vial),
    LocationData(Location.yosei_blood_pool, Region.yosei_forest, Spell.blood_drain),
    LocationData(Location.yosei_branch_in_tree, Region.yosei_forest, Spell.holy_warmth),
    LocationData(Location.yosei_chest_near_tree, Region.yosei_forest, Weapon.elfen_bow),
    LocationData(Location.yosei_blood_plant_insides, Region.yosei_forest, GenericItem.health_vial),
    LocationData(Location.yosei_hanging_in_trees, Region.yosei_forest, Weapon.elfen_sword),
    LocationData(Location.yosei_hidden_chest, Region.yosei_lower, Spell.light_reveal),
    LocationData(Location.yosei_room_defended_by_blood_plant, Region.yosei_lower, Spell.earth_strike),
    LocationData(Location.yosei_patchouli_quest, Region.yosei_lower, UniqueItem.earth_elixir),
]

forest_canopy = [
    LocationData(Location.canopy_branch_edge, Region.forest_canopy, GenericItem.crystal_shard),
    LocationData(Location.canopy_chest, Region.forest_canopy, Spell.poison_mist),
    LocationData(Location.canopy_wooden_statue, Region.forest_canopy, UniqueItem.skull_of_josiah),
    LocationData(Location.canopy_wooden_sitting, Region.forest_canopy, Spell.wind_slicer),
]

forbidden_archives = [
    LocationData(Location.archives_snail_lectern_near, Region.forbidden_archives, Spell.light_reveal),
    LocationData(Location.archives_snail_lectern_far, Region.forbidden_archives, Spell.blood_drain),
    LocationData(Location.archives_back_room_past_bridge, Region.forbidden_archives, UniqueItem.ocean_elixir),
    LocationData(Location.archives_strange_corpse, Region.forbidden_archives, Spell.corpse_transformation),
    LocationData(Location.archives_short_wall_near_trees, Region.forbidden_archives, GenericItem.health_vial),
    LocationData(Location.archives_against_wall_near_trees, Region.forbidden_archives, GenericItem.light_urn),
    LocationData(Location.archives_hidden_room_upper, Region.forbidden_archives, Weapon.wolfram_greatsword),
    LocationData(Location.archives_rooftop, Region.forbidden_archives, UniqueItem.earth_elixir),
    LocationData(Location.archives_rug_on_balcony, Region.forbidden_archives, GenericItem.mana_vial),
    LocationData(Location.archives_hidden_room_lower, Region.forbidden_archives, GenericItem.crystal_shard),
    LocationData(Location.archives_near_twisty_tree, Region.forbidden_archives, GenericItem.fairy_moss),
    LocationData(Location.archives_daedalus_one, Region.daedalus, Spell.fire_worm),
    LocationData(Location.archives_daedalus_two, Region.daedalus, Spell.bestial_communion),
    LocationData(Location.archives_daedalus_third, Region.daedalus, Spell.moon_beam),
]

castle_le_fanu = [
    LocationData(Location.castle_outside_corner, Region.castle_le_fanu, GenericItem.mana_vial),
    LocationData(Location.castle_cell_south, Region.castle_le_fanu_red, GenericItem.spectral_candle),
    LocationData(Location.castle_cell_west, Region.castle_le_fanu_red, GenericItem.health_vial),
    LocationData(Location.castle_cell_center, Region.castle_le_fanu_red, Spell.summon_ice_sword),
    LocationData(Location.castle_cell_north, Region.castle_le_fanu_red, UniqueItem.vampiric_symbol_w),
    LocationData(Location.castle_hidden_cell, Region.castle_le_fanu_red, Weapon.wand_of_power),
    LocationData(Location.castle_hallway_rubble_room, Region.castle_le_fanu_white, GenericItem.light_urn),
    LocationData(Location.castle_hallway_dining_room, Region.castle_le_fanu_white, GenericItem.blood_wine),
    LocationData(Location.castle_garrat_resting_room_left, Region.castle_le_fanu_white, GenericItem.holy_water),
    LocationData(Location.castle_garrat_resting_room_back, Region.castle_le_fanu_white, Weapon.crossbow),
    LocationData(Location.castle_hallway_deadend_before_door, Region.castle_le_fanu_white, UniqueItem.vampiric_symbol_a),
    LocationData(Location.castle_upper_floor_coffin_small, Region.castle_le_fanu_blue, UniqueItem.earth_elixir),
    LocationData(Location.castle_upper_floor_coffin_large, Region.castle_le_fanu_blue, UniqueItem.ocean_elixir),
    LocationData(Location.castle_upper_floor_coffin_double, Region.castle_le_fanu_blue, Weapon.blade_of_ophelia),
    LocationData(Location.castle_upper_floor_coffin_hallway, Region.castle_le_fanu_blue, UniqueItem.vampiric_symbol_e),
]

holy_battlefield = [
    LocationData(Location.battlefield_book, Region.holy_battleground, UniqueItem.black_book),
]

sealed_ballroom = [
    LocationData(Location.ballroom_entry_hidden_cave_in_lounge, Region.sealed_ballroom, GenericItem.spectral_candle),
    LocationData(Location.ballroom_small_room_lounge, Region.sealed_ballroom, GenericItem.blood_wine),
    LocationData(Location.ballroom_entry_long_table, Region.sealed_ballroom, GenericItem.health_vial),
    LocationData(Location.ballroom_entry_hidden_couch_top, Region.sealed_ballroom, Weapon.steel_needle),
    LocationData(Location.ballroom_entry_hidden_couch_bottom, Region.sealed_ballroom, GenericItem.health_vial),
    LocationData(Location.ballroom_side_chest_near_switch, Region.sealed_ballroom, Spell.earth_thorn),
    LocationData(Location.ballroom_side_hidden_casket_room, Region.sealed_ballroom, GenericItem.health_vial),
    LocationData(Location.ballroom_side_hidden_cave, Region.sealed_ballroom, GenericItem.crystal_shard),
    LocationData(Location.ballroom_side_painting, Region.sealed_ballroom, UniqueItem.ocean_elixir),
    LocationData(Location.ballroom_side_xp_drain, Region.sealed_ballroom, Weapon.flail),
]

laetus_chasm = [
    LocationData(Location.chasm_hidden_chest, Region.laetus_chasm, Spell.ice_tear),
    LocationData(Location.chasm_invisible_cliffside, Region.laetus_chasm, Weapon.blessed_wind)
]

great_well_surface = [
    LocationData(Location.surface_demi_gift, Region.great_well_surface, GenericItem.crystal_shard)
]

throne_room = [
    LocationData(Location.throne_book, Region.throne_chamber, UniqueItem.black_book)
]

boiling_grotto = [
    LocationData(Location.grotto_slab_of_bridge, Region.boiling_grotto, GenericItem.crystal_shard),
    LocationData(Location.grotto_triple_secret_chest, Region.boiling_grotto, GenericItem.ashes),
    LocationData(Location.grotto_hidden_chest, Region.boiling_grotto, GenericItem.moonlight_vial),
    LocationData(Location.grotto_rocks_near_lava_switch, Region.boiling_grotto, Spell.rock_bridge),
    LocationData(Location.grotto_through_switch_tunnel, Region.boiling_grotto, GenericItem.mana_vial),
    LocationData(Location.sand_room_buried_in_sand, Region.sand_temple, GenericItem.health_vial),
    LocationData(Location.sand_lunacid_sandwich, Region.sand_temple, Weapon.iron_claw),
    LocationData(Location.sand_hidden_sarcophagus, Region.sand_temple, GenericItem.cloth_bandage),
    LocationData(Location.sand_switch_maze, Region.sand_temple, Coins.silver_2),
    LocationData(Location.sand_triple_sarcophagus, Region.sand_temple, Coins.silver_5),
    LocationData(Location.sand_chest_near_switch, Region.sand_temple, Spell.ignis_calor),
    LocationData(Location.sand_chest_overlooking_crypt, Region.sand_temple, UniqueItem.ocean_elixir),
    LocationData(Location.sand_second_floor_dead_end, Region.sand_temple, GenericItem.health_vial),
]

tower_of_abyss = [
    LocationData(Location.abyss_prize, Region.tower_abyss, Weapon.moonlight),
    LocationData(Location.abyss_floor_5, Region.tower_abyss, GenericItem.mana_vial),
    LocationData(Location.abyss_floor_10, Region.tower_abyss, GenericItem.antidote),
    LocationData(Location.abyss_floor_15, Region.tower_abyss, GenericItem.fairy_moss),
    LocationData(Location.abyss_floor_20, Region.tower_abyss, GenericItem.spectral_candle),
    LocationData(Location.abyss_floor_25, Region.tower_abyss, GenericItem.health_vial),
    LocationData(Location.abyss_floor_30, Region.tower_abyss, UniqueItem.crystal_lantern),
    LocationData(Location.abyss_floor_35, Region.tower_abyss, Coins.silver_5),
    LocationData(Location.abyss_floor_40, Region.tower_abyss, GenericItem.spectral_candle),
    LocationData(Location.abyss_floor_45, Region.tower_abyss, UniqueItem.earth_elixir),
    LocationData(Location.abyss_floor_50, Region.tower_abyss, UniqueItem.ocean_elixir)
]

terminus_prison = [
    LocationData(Location.prison_f3_locked_left, Region.terminus_prison, GenericItem.cloth_bandage),
    LocationData(Location.prison_f3_locked_right, Region.terminus_prison, GenericItem.ashes),
    LocationData(Location.prison_f3_locked_south, Region.terminus_prison, Weapon.broken_lance),
    LocationData(Location.prison_f3_bottomless_pit, Region.terminus_prison, Spell.icarian_flight),
    LocationData(Location.prison_f2_broken_cell, Region.terminus_prison_dark, GenericItem.cloth_bandage),
    LocationData(Location.prison_f2_jailer_table, Region.terminus_prison_dark, GenericItem.ashes),
    LocationData(Location.prison_f1_hidden_debris_room, Region.terminus_prison_dark, GenericItem.light_urn),
    LocationData(Location.prison_f1_remains, Region.terminus_prison_dark, Weapon.fishing_spear),
    LocationData(Location.prison_f1_hidden_cell, Region.terminus_prison_dark, GenericItem.health_vial),
    LocationData(Location.prison_f4_hanging, Region.terminus_prison, GenericItem.health_vial),
    LocationData(Location.prison_f4_monk_room_one, Region.terminus_prison, Alchemy.ectoplasm),
    LocationData(Location.prison_f4_monk_room_two, Region.terminus_prison, Alchemy.snowflake_obsidian),
    LocationData(Location.prison_f4_monk_room_three, Region.terminus_prison, Alchemy.moonpetal),
    LocationData(Location.prison_f4_jailer_break_room, Region.terminus_prison, GenericItem.mana_vial),
    LocationData(Location.prison_f4_hidden_beds, Region.terminus_prison, GenericItem.holy_water),
    LocationData(Location.prison_f4_maledictus_secret, Region.terminus_prison, Spell.blue_flame_arc),
    LocationData(Location.prison_f4_collapsed_tunnel, Region.terminus_prison, Weapon.hammer_of_cruelty),
    LocationData(Location.prison_b2_bone_pit, Region.terminus_prison_dark, GenericItem.health_vial),
    LocationData(Location.prison_b2_deep_alcove, Region.terminus_prison_dark, UniqueItem.earth_elixir),
    LocationData(Location.prison_b2_guarded_corner_one, Region.terminus_prison_dark, GenericItem.moonlight_vial),
    LocationData(Location.prison_b2_guarded_corner_two, Region.terminus_prison_dark, GenericItem.moonlight_vial),
]

forlorn_arena = [
    LocationData(Location.arena_water_hidden_alcove_before)
]

labyrinth_of_ash = [

]

chamber_of_fate = [

]


base_locations = wings_rest + hollow_basin + great_well_surface + the_fetid_mire + the_sacrosant_sea + accursed_tomb + yosei_forest + \
                 forest_canopy + forbidden_archives + castle_le_fanu + holy_battlefield + sealed_ballroom + laetus_chasm + throne_room + boiling_grotto + \
                 terminus_prison + forlorn_arena + labyrinth_of_ash

switch_locations = []

shop_locations = []

mob_drop_locations = []

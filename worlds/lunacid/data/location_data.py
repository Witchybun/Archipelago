from dataclasses import dataclass
from typing import Optional, List

from ..strings.locations import BaseLocation, ShopLocation, SwitchLocation, DropLocation
from ..strings.regions_entrances import LunacidRegion
from ..strings.weapons import Weapon
from ..strings.spells import Spell, MobSpell
from ..strings.items import UniqueItem, GenericItem, Coins, Alchemy, Creation, Switch


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

location_id = 1


def loc_id(init: Optional[int] = -1):
    global location_id
    if init != -1:
        location_id = 1
    location_id += 1
    return location_id - 1


wings_rest = [
    LocationData(loc_id(1), BaseLocation.wings_rest_ocean_elixir, LunacidRegion.wings_rest, UniqueItem.ocean_elixir),
    LocationData(loc_id(), BaseLocation.wings_rest_crystal_shard, LunacidRegion.wings_rest, Creation.crystal_shard),
]

hollow_basin = [
    LocationData(loc_id(), BaseLocation.hollow_basin_dark_item, LunacidRegion.hollow_basin, Weapon.torch),
    LocationData(loc_id(), BaseLocation.hollow_basin_demi_chest, LunacidRegion.hollow_basin, Spell.flame_spear),
    LocationData(loc_id(), BaseLocation.hollow_basin_enchanted_door, LunacidRegion.hollow_basin, Creation.health_vial),
    LocationData(loc_id(), BaseLocation.hollow_basin_left_water, LunacidRegion.hollow_basin, Creation.health_vial),
    LocationData(loc_id(), BaseLocation.hollow_basin_starting_sword, LunacidRegion.hollow_basin, Weapon.replica_sword),
    LocationData(loc_id(), BaseLocation.hollow_basin_right_water_left, LunacidRegion.hollow_basin, Spell.ghost_light),
    LocationData(loc_id(), BaseLocation.hollow_basin_right_water_right, LunacidRegion.hollow_basin, Creation.mana_vial),
    LocationData(loc_id(), BaseLocation.temple_fountain, LunacidRegion.temple_of_silence, Creation.health_vial),
    LocationData(loc_id(), BaseLocation.temple_ritual_table, LunacidRegion.temple_of_silence, Weapon.ritual_dagger),
    LocationData(loc_id(), BaseLocation.temple_altar_chest, LunacidRegion.temple_of_silence, Spell.lithomancy),
    LocationData(loc_id(), BaseLocation.temple_small_pillar, LunacidRegion.temple_of_silence, Creation.health_vial),
    LocationData(loc_id(), BaseLocation.temple_ritual_ring, LunacidRegion.temple_of_silence, Spell.flame_flare),
    LocationData(loc_id(), BaseLocation.temple_pillar_room_back_left, LunacidRegion.temple_of_silence, Creation.health_vial),
    LocationData(loc_id(), BaseLocation.temple_pillar_room_back_right, LunacidRegion.temple_of_silence, Creation.health_vial),
    LocationData(loc_id(), BaseLocation.temple_pillar_room_left, LunacidRegion.temple_of_silence, Creation.crystal_shard),
    LocationData(loc_id(), BaseLocation.temple_pillar_room_back_left, LunacidRegion.temple_of_silence, Weapon.wooden_shield),
    LocationData(loc_id(), BaseLocation.temple_pillar_room_back_right, LunacidRegion.temple_of_silence, GenericItem.blood_wine),
    LocationData(loc_id(), BaseLocation.temple_pillar_room_hidden_room, LunacidRegion.temple_of_silence, Spell.blood_strike),
    LocationData(loc_id(), BaseLocation.temple_hidden_room_in_sewer, LunacidRegion.temple_of_silence, UniqueItem.vhs_tape),
    LocationData(loc_id(), BaseLocation.temple_table_in_sewer, LunacidRegion.temple_of_silence, Weapon.stone_club),
    LocationData(loc_id(), BaseLocation.temple_sewer_puzzle, LunacidRegion.temple_of_silence, UniqueItem.corrupted_key),
    LocationData(loc_id(), BaseLocation.temple_blood_altar, LunacidRegion.temple_of_silence, Coins.strange_coin)
]

the_fetid_mire = [
    LocationData(loc_id(), BaseLocation.mire_bonerard_trash, LunacidRegion.fetid_mire, Creation.antidote),
    LocationData(loc_id(), BaseLocation.mire_jellisha_reward, LunacidRegion.fetid_mire, Spell.slime_orb),
    LocationData(loc_id(), BaseLocation.mire_jellisha_trash, LunacidRegion.fetid_mire, Creation.mana_vial),
    LocationData(loc_id(), BaseLocation.mire_rubble_bridge, LunacidRegion.fetid_mire, Creation.antidote),
    LocationData(loc_id(), BaseLocation.mire_skeleton_chest, LunacidRegion.fetid_mire, Spell.barrier),
    LocationData(loc_id(), BaseLocation.mire_hidden_chest_near_underworks, LunacidRegion.fetid_mire, UniqueItem.earth_elixir),
    LocationData(loc_id(), BaseLocation.mire_hidden_slime_chest, LunacidRegion.fetid_mire, Spell.ice_spear),
    LocationData(loc_id(), BaseLocation.mire_room_left_foyer, LunacidRegion.fetid_mire, Creation.antidote),
    LocationData(loc_id(), BaseLocation.mire_rubble_near_illusory_wall, LunacidRegion.fetid_mire, Spell.wind_dash),
    LocationData(loc_id(), BaseLocation.mire_underwater_pipe, LunacidRegion.fetid_mire, Creation.poison_throwing_knife),
    LocationData(loc_id(), BaseLocation.mire_underworks_skeleton, LunacidRegion.fetid_mire, Weapon.broken_hilt),
    LocationData(loc_id(), BaseLocation.mire_underworks_waterfall, LunacidRegion.fetid_mire, Creation.antidote),
    LocationData(loc_id(), BaseLocation.mire_upper_overlook_left, LunacidRegion.fetid_mire, Creation.crystal_shard),
    LocationData(loc_id(), BaseLocation.mire_upper_overlook_right, LunacidRegion.fetid_mire, UniqueItem.ocean_elixir),
]

the_sacrosant_sea = [
    LocationData(loc_id(), BaseLocation.sea_demon, LunacidRegion.sanguine_sea, UniqueItem.ocean_elixir),
    LocationData(loc_id(), BaseLocation.sea_pillar, LunacidRegion.sanguine_sea, Weapon.corrupted_dagger),
    LocationData(loc_id(), BaseLocation.sea_underblood, LunacidRegion.sanguine_sea, Weapon.dark_rapier),
    LocationData(loc_id(), BaseLocation.sea_blood_island, LunacidRegion.sanguine_sea, Spell.summon_fairy),
    LocationData(loc_id(), BaseLocation.sea_kill_jotunn, LunacidRegion.sanguine_sea, Coins.strange_coin)]

accursed_tomb = [
    LocationData(loc_id(), BaseLocation.catacombs_coffin_stairs, LunacidRegion.accursed_tomb, Creation.health_vial),
    LocationData(loc_id(), BaseLocation.catacombs_hidden_room, LunacidRegion.accursed_tomb, UniqueItem.ocean_elixir),
    LocationData(loc_id(), BaseLocation.corrupted_room, LunacidRegion.accursed_tomb, UniqueItem.white_tape),
    LocationData(loc_id(), BaseLocation.catacombs_restore_vampire, LunacidRegion.accursed_tomb, Weapon.blade_of_jusztina),
    LocationData(loc_id(), BaseLocation.catacombs_coffin_blue_light, LunacidRegion.accursed_tomb, Spell.coffin),
    LocationData(loc_id(), BaseLocation.catacombs_coffin_gate, LunacidRegion.accursed_tomb, UniqueItem.ocean_elixir),
    LocationData(loc_id(), BaseLocation.catacombs_deep_coffin_storage, LunacidRegion.accursed_tomb, Weapon.halberd),
    LocationData(loc_id(), BaseLocation.mausoleum_hidden_chest, LunacidRegion.accursed_tomb, Weapon.twisted_staff),
    LocationData(loc_id(), BaseLocation.mausoleum_maze_intro, LunacidRegion.accursed_tomb, Creation.holy_water),
    LocationData(loc_id(), BaseLocation.mausoleum_upper_table, LunacidRegion.accursed_tomb, UniqueItem.black_book),
    LocationData(loc_id(), BaseLocation.mausoleum_maze_mid, LunacidRegion.accursed_tomb, Creation.health_vial),
    LocationData(loc_id(), BaseLocation.mausoleum_center_back, LunacidRegion.accursed_tomb, UniqueItem.earth_elixir),
    LocationData(loc_id(), BaseLocation.mausoleum_center_right, LunacidRegion.accursed_tomb, Creation.health_vial),
    LocationData(loc_id(), BaseLocation.mausoleum_center_left, LunacidRegion.accursed_tomb, Creation.holy_water),
    LocationData(loc_id(), BaseLocation.mausoleum_center_left_path, LunacidRegion.accursed_tomb, Creation.health_vial),
    LocationData(loc_id(), BaseLocation.mausoleum_center_right_path, LunacidRegion.accursed_tomb, UniqueItem.ocean_elixir),
    LocationData(loc_id(), BaseLocation.tomb_demi_chest, LunacidRegion.accursed_tomb, Spell.lightning),
    LocationData(loc_id(), BaseLocation.tomb_hidden_room, LunacidRegion.accursed_tomb, UniqueItem.earth_elixir),
    LocationData(loc_id(), BaseLocation.tomb_tomb_with_corpse, LunacidRegion.accursed_tomb, UniqueItem.survey_banner),
    LocationData(loc_id(), BaseLocation.tomb_tomb_with_switch, LunacidRegion.accursed_tomb, Weapon.vampire_hunter_sword),
    LocationData(loc_id(), BaseLocation.tomb_near_light_switch, LunacidRegion.accursed_tomb, Creation.crystal_shard),
    LocationData(loc_id(), BaseLocation.tomb_hidden_chest, LunacidRegion.accursed_tomb, Coins.silver_100)
]

yosei_forest = [
    LocationData(loc_id(), BaseLocation.yosei_patchouli_key, LunacidRegion.yosei_lower, UniqueItem.enchanted_key),
    LocationData(loc_id(), BaseLocation.yosei_barrels, LunacidRegion.yosei_forest, Creation.health_vial),
    LocationData(loc_id(), BaseLocation.yosei_blood_pool, LunacidRegion.yosei_forest, Spell.blood_drain),
    LocationData(loc_id(), BaseLocation.yosei_branch_in_tree, LunacidRegion.yosei_forest, Spell.holy_warmth),
    LocationData(loc_id(), BaseLocation.yosei_chest_near_tree, LunacidRegion.yosei_forest, Weapon.elfen_bow),
    LocationData(loc_id(), BaseLocation.yosei_blood_plant_insides, LunacidRegion.yosei_forest, Creation.health_vial),
    LocationData(loc_id(), BaseLocation.yosei_hanging_in_trees, LunacidRegion.yosei_forest, Weapon.elfen_sword),
    LocationData(loc_id(), BaseLocation.yosei_hidden_chest, LunacidRegion.yosei_lower, Spell.light_reveal),
    LocationData(loc_id(), BaseLocation.yosei_room_defended_by_blood_plant, LunacidRegion.yosei_lower, Spell.earth_strike),
    LocationData(loc_id(), BaseLocation.yosei_patchouli_quest, LunacidRegion.yosei_lower, UniqueItem.earth_elixir),
]

forest_canopy = [
    LocationData(loc_id(), BaseLocation.canopy_branch_edge, LunacidRegion.forest_canopy, Creation.crystal_shard),
    LocationData(loc_id(), BaseLocation.canopy_chest, LunacidRegion.forest_canopy, Spell.poison_mist),
    LocationData(loc_id(), BaseLocation.canopy_wooden_statue, LunacidRegion.forest_canopy, UniqueItem.skull_of_josiah),
    LocationData(loc_id(), BaseLocation.canopy_wooden_sitting, LunacidRegion.forest_canopy, Spell.wind_slicer),
]

forbidden_archives = [
    LocationData(loc_id(), BaseLocation.archives_snail_lectern_near, LunacidRegion.forbidden_archives, Spell.light_reveal),
    LocationData(loc_id(), BaseLocation.archives_snail_lectern_far, LunacidRegion.forbidden_archives, Spell.blood_drain),
    LocationData(loc_id(), BaseLocation.archives_back_room_past_bridge, LunacidRegion.forbidden_archives, UniqueItem.ocean_elixir),
    LocationData(loc_id(), BaseLocation.archives_strange_corpse, LunacidRegion.forbidden_archives, Spell.corpse_transformation),
    LocationData(loc_id(), BaseLocation.archives_short_wall_near_trees, LunacidRegion.forbidden_archives, Creation.health_vial),
    LocationData(loc_id(), BaseLocation.archives_against_wall_near_trees, LunacidRegion.forbidden_archives, GenericItem.light_urn),
    LocationData(loc_id(), BaseLocation.archives_hidden_room_upper, LunacidRegion.forbidden_archives, Weapon.wolfram_greatsword),
    LocationData(loc_id(), BaseLocation.archives_rooftop, LunacidRegion.forbidden_archives, UniqueItem.earth_elixir),
    LocationData(loc_id(), BaseLocation.archives_rug_on_balcony, LunacidRegion.forbidden_archives, Creation.mana_vial),
    LocationData(loc_id(), BaseLocation.archives_hidden_room_lower, LunacidRegion.forbidden_archives, Creation.crystal_shard),
    LocationData(loc_id(), BaseLocation.archives_near_twisty_tree, LunacidRegion.forbidden_archives, Creation.fairy_moss),
    LocationData(loc_id(), BaseLocation.archives_daedalus_one, LunacidRegion.daedalus, Spell.fire_worm),
    LocationData(loc_id(), BaseLocation.archives_daedalus_two, LunacidRegion.daedalus, Spell.bestial_communion),
    LocationData(loc_id(), BaseLocation.archives_daedalus_third, LunacidRegion.daedalus, Spell.moon_beam),
]

castle_le_fanu = [
    LocationData(loc_id(), BaseLocation.castle_outside_corner, LunacidRegion.castle_le_fanu, Creation.mana_vial),
    LocationData(loc_id(), BaseLocation.castle_cell_south, LunacidRegion.castle_le_fanu_red, Creation.spectral_candle),
    LocationData(loc_id(), BaseLocation.castle_cell_west, LunacidRegion.castle_le_fanu_red, Creation.health_vial),
    LocationData(loc_id(), BaseLocation.castle_cell_center, LunacidRegion.castle_le_fanu_red, Spell.summon_ice_sword),
    LocationData(loc_id(), BaseLocation.castle_cell_north, LunacidRegion.castle_le_fanu_red, UniqueItem.vampiric_symbol_w),
    LocationData(loc_id(), BaseLocation.castle_hidden_cell, LunacidRegion.castle_le_fanu_red, Weapon.wand_of_power),
    LocationData(loc_id(), BaseLocation.castle_hallway_rubble_room, LunacidRegion.castle_le_fanu_white, GenericItem.light_urn),
    LocationData(loc_id(), BaseLocation.castle_hallway_dining_room, LunacidRegion.castle_le_fanu_white, GenericItem.blood_wine),
    LocationData(loc_id(), BaseLocation.castle_garrat_resting_room_left, LunacidRegion.castle_le_fanu_white, Creation.holy_water),
    LocationData(loc_id(), BaseLocation.castle_garrat_resting_room_back, LunacidRegion.castle_le_fanu_white, Weapon.crossbow),
    LocationData(loc_id(), BaseLocation.castle_hallway_deadend_before_door, LunacidRegion.castle_le_fanu_white, UniqueItem.vampiric_symbol_a),
    LocationData(loc_id(), BaseLocation.castle_upper_floor_coffin_small, LunacidRegion.castle_le_fanu_blue, UniqueItem.earth_elixir),
    LocationData(loc_id(), BaseLocation.castle_upper_floor_coffin_large, LunacidRegion.castle_le_fanu_blue, UniqueItem.ocean_elixir),
    LocationData(loc_id(), BaseLocation.castle_upper_floor_coffin_double, LunacidRegion.castle_le_fanu_blue, Weapon.blade_of_ophelia),
    LocationData(loc_id(), BaseLocation.castle_upper_floor_coffin_hallway, LunacidRegion.castle_le_fanu_blue, UniqueItem.vampiric_symbol_e),
]

holy_battlefield = [
    LocationData(loc_id(), BaseLocation.battlefield_book, LunacidRegion.holy_battleground, UniqueItem.black_book),
]

sealed_ballroom = [
    LocationData(loc_id(), BaseLocation.ballroom_entry_hidden_cave_in_lounge, LunacidRegion.sealed_ballroom, Creation.spectral_candle),
    LocationData(loc_id(), BaseLocation.ballroom_small_room_lounge, LunacidRegion.sealed_ballroom, GenericItem.blood_wine),
    LocationData(loc_id(), BaseLocation.ballroom_entry_long_table, LunacidRegion.sealed_ballroom, Creation.health_vial),
    LocationData(loc_id(), BaseLocation.ballroom_entry_hidden_couch_top, LunacidRegion.sealed_ballroom, Weapon.steel_needle),
    LocationData(loc_id(), BaseLocation.ballroom_entry_hidden_couch_bottom, LunacidRegion.sealed_ballroom, Creation.health_vial),
    LocationData(loc_id(), BaseLocation.ballroom_side_chest_near_switch, LunacidRegion.sealed_ballroom, Spell.earth_thorn),
    LocationData(loc_id(), BaseLocation.ballroom_side_hidden_casket_room, LunacidRegion.sealed_ballroom, Creation.health_vial),
    LocationData(loc_id(), BaseLocation.ballroom_side_hidden_cave, LunacidRegion.sealed_ballroom, Creation.crystal_shard),
    LocationData(loc_id(), BaseLocation.ballroom_side_painting, LunacidRegion.sealed_ballroom, UniqueItem.ocean_elixir),
    LocationData(loc_id(), BaseLocation.ballroom_side_xp_drain, LunacidRegion.sealed_ballroom, Weapon.flail),
]

laetus_chasm = [
    LocationData(loc_id(), BaseLocation.chasm_hidden_chest, LunacidRegion.laetus_chasm, Spell.ice_tear),
    LocationData(loc_id(), BaseLocation.chasm_invisible_cliffside, LunacidRegion.laetus_chasm, Weapon.blessed_wind)
]

great_well_surface = [
    LocationData(loc_id(), BaseLocation.surface_demi_gift, LunacidRegion.great_well_surface, Creation.crystal_shard)
]

throne_room = [
    LocationData(loc_id(), BaseLocation.throne_book, LunacidRegion.throne_chamber, UniqueItem.black_book)
]

boiling_grotto = [
    LocationData(loc_id(), BaseLocation.grotto_slab_of_bridge, LunacidRegion.boiling_grotto, Creation.crystal_shard),
    LocationData(loc_id(), BaseLocation.grotto_triple_secret_chest, LunacidRegion.boiling_grotto, Alchemy.ashes),
    LocationData(loc_id(), BaseLocation.grotto_hidden_chest, LunacidRegion.boiling_grotto, Creation.moonlight_vial),
    LocationData(loc_id(), BaseLocation.grotto_rocks_near_lava_switch, LunacidRegion.boiling_grotto, Spell.rock_bridge),
    LocationData(loc_id(), BaseLocation.grotto_through_switch_tunnel, LunacidRegion.boiling_grotto, Creation.mana_vial),
    LocationData(loc_id(), BaseLocation.sand_room_buried_in_sand, LunacidRegion.sand_temple, Creation.health_vial),
    LocationData(loc_id(), BaseLocation.sand_lunacid_sandwich, LunacidRegion.sand_temple, Weapon.iron_claw),
    LocationData(loc_id(), BaseLocation.sand_hidden_sarcophagus, LunacidRegion.sand_temple, GenericItem.cloth_bandage),
    LocationData(loc_id(), BaseLocation.sand_switch_maze, LunacidRegion.sand_temple, Coins.silver_2),
    LocationData(loc_id(), BaseLocation.sand_triple_sarcophagus, LunacidRegion.sand_temple, Coins.silver_5),
    LocationData(loc_id(), BaseLocation.sand_chest_near_switch, LunacidRegion.sand_temple, Spell.ignis_calor),
    LocationData(loc_id(), BaseLocation.sand_chest_overlooking_crypt, LunacidRegion.sand_temple, UniqueItem.ocean_elixir),
    LocationData(loc_id(), BaseLocation.sand_second_floor_dead_end, LunacidRegion.sand_temple, Creation.health_vial),
]

tower_of_abyss = [
    LocationData(loc_id(), BaseLocation.abyss_prize, LunacidRegion.tower_abyss, Weapon.moonlight),
    LocationData(loc_id(), BaseLocation.abyss_floor_5, LunacidRegion.tower_abyss, Creation.mana_vial),
    LocationData(loc_id(), BaseLocation.abyss_floor_10, LunacidRegion.tower_abyss, Creation.antidote),
    LocationData(loc_id(), BaseLocation.abyss_floor_15, LunacidRegion.tower_abyss, Creation.fairy_moss),
    LocationData(loc_id(), BaseLocation.abyss_floor_20, LunacidRegion.tower_abyss, Creation.spectral_candle),
    LocationData(loc_id(), BaseLocation.abyss_floor_25, LunacidRegion.tower_abyss, Creation.health_vial),
    LocationData(loc_id(), BaseLocation.abyss_floor_30, LunacidRegion.tower_abyss, UniqueItem.crystal_lantern),
    LocationData(loc_id(), BaseLocation.abyss_floor_35, LunacidRegion.tower_abyss, Coins.silver_5),
    LocationData(loc_id(), BaseLocation.abyss_floor_40, LunacidRegion.tower_abyss, Creation.spectral_candle),
    LocationData(loc_id(), BaseLocation.abyss_floor_45, LunacidRegion.tower_abyss, UniqueItem.earth_elixir),
    LocationData(loc_id(), BaseLocation.abyss_floor_50, LunacidRegion.tower_abyss, UniqueItem.ocean_elixir)
]

terminus_prison = [
    LocationData(loc_id(), BaseLocation.prison_f3_locked_left, LunacidRegion.terminus_prison, GenericItem.cloth_bandage),
    LocationData(loc_id(), BaseLocation.prison_f3_locked_right, LunacidRegion.terminus_prison, Alchemy.ashes),
    LocationData(loc_id(), BaseLocation.prison_f3_locked_south, LunacidRegion.terminus_prison, Weapon.broken_lance),
    LocationData(loc_id(), BaseLocation.prison_f3_bottomless_pit, LunacidRegion.terminus_prison, Spell.icarian_flight),
    LocationData(loc_id(), BaseLocation.prison_f2_broken_cell, LunacidRegion.terminus_prison_dark, GenericItem.cloth_bandage),
    LocationData(loc_id(), BaseLocation.prison_f2_jailer_table, LunacidRegion.terminus_prison_dark, UniqueItem.terminus_prison_key),
    LocationData(loc_id(), BaseLocation.prison_f1_hidden_debris_room, LunacidRegion.terminus_prison_dark, GenericItem.light_urn),
    LocationData(loc_id(), BaseLocation.prison_f1_remains, LunacidRegion.terminus_prison_dark, Weapon.fishing_spear),
    LocationData(loc_id(), BaseLocation.prison_f1_hidden_cell, LunacidRegion.terminus_prison_dark, Creation.health_vial),
    LocationData(loc_id(), BaseLocation.prison_f4_hanging, LunacidRegion.terminus_prison, Creation.health_vial),
    LocationData(loc_id(), BaseLocation.prison_f4_monk_room_one, LunacidRegion.terminus_prison, Alchemy.ectoplasm),
    LocationData(loc_id(), BaseLocation.prison_f4_monk_room_two, LunacidRegion.terminus_prison, Alchemy.snowflake_obsidian),
    LocationData(loc_id(), BaseLocation.prison_f4_monk_room_three, LunacidRegion.terminus_prison, Alchemy.moon_petal),
    LocationData(loc_id(), BaseLocation.prison_f4_jailer_break_room, LunacidRegion.terminus_prison, Creation.mana_vial),
    LocationData(loc_id(), BaseLocation.prison_f4_hidden_beds, LunacidRegion.terminus_prison, Creation.holy_water),
    LocationData(loc_id(), BaseLocation.prison_f4_maledictus_secret, LunacidRegion.terminus_prison, Spell.blue_flame_arc),
    LocationData(loc_id(), BaseLocation.prison_f4_collapsed_tunnel, LunacidRegion.terminus_prison, Weapon.hammer_of_cruelty),
    LocationData(loc_id(), BaseLocation.prison_b2_bone_pit, LunacidRegion.terminus_prison_dark, Creation.health_vial),
    LocationData(loc_id(), BaseLocation.prison_b2_deep_alcove, LunacidRegion.terminus_prison_dark, UniqueItem.earth_elixir),
    LocationData(loc_id(), BaseLocation.prison_b2_guarded_corner_one, LunacidRegion.terminus_prison_dark, Creation.moonlight_vial),
    LocationData(loc_id(), BaseLocation.prison_b2_guarded_corner_two, LunacidRegion.terminus_prison_dark, Creation.moonlight_vial),
]

forlorn_arena = [
    LocationData(loc_id(), BaseLocation.arena_rock_parkour, LunacidRegion.forlorn_arena, Creation.health_vial),
    LocationData(loc_id(), BaseLocation.arena_water_room_near_water, LunacidRegion.forlorn_arena, Creation.fairy_moss),
    LocationData(loc_id(), BaseLocation.arena_water_dead_end_near_water, LunacidRegion.forlorn_arena, Creation.antidote),
    LocationData(loc_id(), BaseLocation.arena_water_collapsed_end_near_balcony, LunacidRegion.forlorn_arena, Creation.health_vial),
    LocationData(loc_id(), BaseLocation.arena_water_hidden_alcove_before, LunacidRegion.forlorn_arena, Creation.health_vial),
    LocationData(loc_id(), BaseLocation.arena_water_hidden_alcove_after, LunacidRegion.forlorn_arena, UniqueItem.ocean_elixir),
    LocationData(loc_id(), BaseLocation.arena_water_underwater_temple, LunacidRegion.forlorn_arena, Alchemy.fractured_death),
    LocationData(loc_id(), BaseLocation.arena_water_chest_near_switch, LunacidRegion.forlorn_arena, UniqueItem.water_talisman),
    LocationData(loc_id(), BaseLocation.arena_earth_hidden_room, LunacidRegion.forlorn_arena, UniqueItem.earth_elixir),
    LocationData(loc_id(), BaseLocation.arena_earth_hidden_plant_haven, LunacidRegion.forlorn_arena, Weapon.shadow_blade),
    LocationData(loc_id(), BaseLocation.arena_earth_earthen_temple, LunacidRegion.forlorn_arena, Alchemy.fractured_life),
    LocationData(loc_id(), BaseLocation.arena_earth_hidden_room, LunacidRegion.forlorn_arena, UniqueItem.earth_talisman),
    LocationData(loc_id(), BaseLocation.arena_broken_sword, LunacidRegion.forlorn_arena, Alchemy.broken_sword)
]

labyrinth_of_ash = [
    LocationData(loc_id(), BaseLocation.ash_entry_coffin, LunacidRegion.labyrinth_of_ash, Creation.mana_vial),
    LocationData(loc_id(), BaseLocation.ash_jotunn_remains, LunacidRegion.labyrinth_of_ash, Creation.health_vial),
    LocationData(loc_id(), BaseLocation.ash_cetea_statue, LunacidRegion.labyrinth_of_ash, Creation.wisp_heart),
    LocationData(loc_id(), BaseLocation.ash_rocks_near_switch, LunacidRegion.labyrinth_of_ash, Spell.lava_chasm),
    LocationData(loc_id(), BaseLocation.ash_forbidden_light_chest, LunacidRegion.labyrinth_of_ash, Spell.spirit_warp),
    LocationData(loc_id(), BaseLocation.ash_hidden_chest, LunacidRegion.labyrinth_of_ash, GenericItem.dark_urn)
]

chamber_of_fate = [
    LocationData(loc_id(), BaseLocation.fate_lucid_blade, LunacidRegion.chamber_of_fate, Weapon.lucid_blade)
]

base_locations = wings_rest + hollow_basin + great_well_surface + the_fetid_mire + the_sacrosant_sea + accursed_tomb + yosei_forest + \
                 forest_canopy + forbidden_archives + castle_le_fanu + holy_battlefield + sealed_ballroom + laetus_chasm + throne_room + boiling_grotto + \
                 terminus_prison + forlorn_arena + labyrinth_of_ash + chamber_of_fate
base_items: List[str] = []
[base_items.append(location.original_item) for location in base_locations if location.original_item not in base_items]

shop_locations = [
    LocationData(loc_id(), ShopLocation.buy_rapier, LunacidRegion.sheryl_the_crow, Weapon.rapier),
    LocationData(loc_id(), ShopLocation.buy_crossbow, LunacidRegion.sheryl_the_crow, Weapon.crossbow),
    LocationData(loc_id(), ShopLocation.buy_oil_lantern, LunacidRegion.sheryl_the_crow, UniqueItem.oil_lantern),
    LocationData(loc_id(), ShopLocation.buy_enchanted_key, LunacidRegion.sheryl_the_crow, UniqueItem.enchanted_key),
    LocationData(loc_id(), ShopLocation.buy_jotunn_slayer, LunacidRegion.sheryl_the_crow, Weapon.jotunn_slayer),
    LocationData(loc_id(), ShopLocation.buy_privateer_musket, LunacidRegion.sheryl_the_crow, Weapon.privateer_musket),
    LocationData(loc_id(), ShopLocation.buy_steel_needle, LunacidRegion.sheryl_the_crow, Weapon.steel_needle),
    LocationData(loc_id(), ShopLocation.buy_ocean_elixir, LunacidRegion.sheryl_the_crow, UniqueItem.ocean_elixir)
]
shop_items: List[str] = []
[shop_items.append(location.original_item) for location in shop_locations if location.original_item not in shop_items]

switch_locations = [
    LocationData(loc_id(), SwitchLocation.hollow_basin_switch_near_demi, LunacidRegion.hollow_basin, Switch.hollow_basin_switch_near_demi),
    LocationData(loc_id(), SwitchLocation.temple_switch, LunacidRegion.temple_of_silence, Switch.temple_switch),
    LocationData(loc_id(), SwitchLocation.fetid_mire_switch, LunacidRegion.fetid_mire, Switch.fetid_mire_switch),
    LocationData(loc_id(), SwitchLocation.archives_switch, LunacidRegion.forbidden_archives, Switch.archives_switch),
    LocationData(loc_id(), SwitchLocation.tomb_shortcut_switch, LunacidRegion.accursed_tomb, Switch.tomb_shortcut_switch),
    LocationData(loc_id(), SwitchLocation.tomb_crypt_switch, LunacidRegion.accursed_tomb, Switch.tomb_crypt_switch),
    LocationData(loc_id(), SwitchLocation.grotto_temple_switch, LunacidRegion.boiling_grotto, Switch.grotto_temple_switch),
    LocationData(loc_id(), SwitchLocation.grotto_calor_switch, LunacidRegion.sand_temple, Switch.grotto_calor_switch),
    LocationData(loc_id(), SwitchLocation.ballroom_switch, LunacidRegion.sealed_ballroom, Switch.ballroom_switch),
    LocationData(loc_id(), SwitchLocation.prison_shortcut_switch, LunacidRegion.terminus_prison_dark, Switch.prison_shortcut_switch),
    LocationData(loc_id(), SwitchLocation.prison_arena_switch, LunacidRegion.terminus_prison, Switch.prison_arena_switch),
    LocationData(loc_id(), SwitchLocation.ash_switch, LunacidRegion.labyrinth_of_ash, Switch.ash_switch),
    LocationData(loc_id(), SwitchLocation.arena_earth_switch, LunacidRegion.forlorn_arena, Switch.arena_earth_switch),
    LocationData(loc_id(), SwitchLocation.arena_water_switch, LunacidRegion.forlorn_arena, Switch.arena_water_switch)
]

switch_items: List[str] = []
[switch_items.append(location.original_item) for location in switch_locations if location.original_item not in switch_items]

mob_drop_locations = [
    LocationData(loc_id(), DropLocation.snail_drop, LunacidRegion.hollow_basin, MobSpell.summon_snail),
    LocationData(loc_id(), DropLocation.mummy_drop, LunacidRegion.temple_of_silence, Weapon.rusted_sword),
    LocationData(loc_id(), DropLocation.kodama_drop, LunacidRegion.yosei_forest, MobSpell.summon_kodama),
    LocationData(loc_id(), DropLocation.chimera_drop, LunacidRegion.forbidden_archives, MobSpell.quick_stride),
    LocationData(loc_id(), DropLocation.milk_snail_drop, LunacidRegion.hollow_basin, Weapon.ice_sickle),
    LocationData(loc_id(), DropLocation.skeleon_weapon_drop, LunacidRegion.fetid_mire, Weapon.skeleton_axe),
    LocationData(loc_id(), DropLocation.skeleton_spell_drop, LunacidRegion.fetid_mire, MobSpell.dark_skull),
    LocationData(loc_id(), DropLocation.phantom_drop, LunacidRegion.accursed_tomb, Weapon.cursed_blade),
    LocationData(loc_id(), DropLocation.obsidian_skeleton_drop_1, LunacidRegion.boiling_grotto, Weapon.obsidian_cursebrand),
    LocationData(loc_id(), DropLocation.obsidian_skeleton_drop_2, LunacidRegion.boiling_grotto, Weapon.obsidian_poisonguard),
    LocationData(loc_id(), DropLocation.anpu_drop_1, LunacidRegion.sand_temple, Weapon.golden_kopesh),
    LocationData(loc_id(), DropLocation.anpu_drop_2, LunacidRegion.sand_temple, Weapon.golden_sickle),
    LocationData(loc_id(), DropLocation.horse_drop, LunacidRegion.sealed_ballroom, Weapon.brittle_arming_sword),
    LocationData(loc_id(), DropLocation.jailor_drop, LunacidRegion.terminus_prison, Weapon.jailor_candle),
    LocationData(loc_id(), DropLocation.vampire_drop, LunacidRegion.castle_le_fanu_red, Weapon.lyrian_longsword),
    LocationData(loc_id(), DropLocation.sucsarian_drop_1, LunacidRegion.forlorn_arena, Weapon.sucsarian_spear),
    LocationData(loc_id(), DropLocation.sucsarian_drop_2, LunacidRegion.forlorn_arena, Weapon.sucsarian_dagger),
    LocationData(loc_id(), DropLocation.cetea_drop, LunacidRegion.labyrinth_of_ash, MobSpell.tornado),
]

drop_items: List[str] = []
[drop_items.append(location.original_item) for location in mob_drop_locations if location.original_item not in drop_items]

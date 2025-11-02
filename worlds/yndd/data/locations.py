from dataclasses import dataclass
from typing import Optional

from ..strings.locations import Nasu, RealBedroom, Streets, Wilderness, Docks, Mall, School, Blocks, Snow, Sewer, \
    Apartment, AoOni, WitchAdventure
from ..strings.regions_entrances import DreamRegions


@dataclass(frozen=True)
class DreamLocation:
    location_id: Optional[int]
    name: str
    region: str


all_locations = []
base_locations = []


def create_location(location_id: Optional[int], name: str, region: Optional[str] = DreamRegions.real_bedroom):
    location = DreamLocation(location_id, name, region)
    if location_id is not None:
        all_locations.append(location)
    if location_id < 200:
        base_locations.append(location)
    return location


real_bedroom_location_start = 0
real_bedroom = [
    create_location(real_bedroom_location_start + 1, RealBedroom.nasu),
]

streets_location_start = 10
streets = [
    create_location(streets_location_start + 1, Streets.diary_1, DreamRegions.streets),
    create_location(streets_location_start + 2, Streets.diary_2, DreamRegions.streets),
    create_location(streets_location_start + 3, Streets.diary_3, DreamRegions.streets),
    create_location(streets_location_start + 4, Streets.knife, DreamRegions.butcher_front),
    create_location(streets_location_start + 5, Streets.diary_secret, DreamRegions.butcher_front),
    create_location(streets_location_start + 6, Streets.egg, DreamRegions.road),
    create_location(streets_location_start + 7, Streets.diary_monoko_1, DreamRegions.bed_maze),
    create_location(streets_location_start + 8, Streets.diary_monoko_2, DreamRegions.bed_maze),
    create_location(streets_location_start + 9, Streets.diary_monoko_3, DreamRegions.bed_maze),
    create_location(streets_location_start + 10, Streets.jellyfish, DreamRegions.initial_street),
]

wilderness_location_start = 30
wilderness = [
    create_location(wilderness_location_start + 1, Wilderness.red_eye, DreamRegions.temple_base),
    create_location(wilderness_location_start + 2, Wilderness.death_glyph, DreamRegions.temple_base),
    create_location(wilderness_location_start + 3, Wilderness.diary_train, DreamRegions.train_4),
    create_location(wilderness_location_start + 4, Wilderness.diary_town_box, DreamRegions.wilderness_town),
    create_location(wilderness_location_start + 5, Wilderness.diary_toriningen, DreamRegions.temple_base),
    create_location(wilderness_location_start + 6, Wilderness.war_glyph, DreamRegions.wilderness_town_interior),
    create_location(wilderness_location_start + 7, Wilderness.kite, DreamRegions.wilderness_night),
    create_location(wilderness_location_start + 8, Wilderness.moon_glyph, DreamRegions.wilderness_night),
    create_location(wilderness_location_start + 9, Wilderness.kalimba, DreamRegions.train_2),
    create_location(wilderness_location_start + 10, Wilderness.diary_piori, DreamRegions.wilderness_town_interior),
    create_location(wilderness_location_start + 11, Wilderness.sun_glyph, DreamRegions.wilderness_town_interior),
    create_location(wilderness_location_start + 12, Wilderness.diary_endless, DreamRegions.endless_wilderness),
    create_location(wilderness_location_start + 13, Wilderness.umbrella, DreamRegions.sky_garden),
    create_location(wilderness_location_start + 14, Wilderness.diary_bench, DreamRegions.sky_garden),
    create_location(wilderness_location_start + 15, Wilderness.diary_lookout, DreamRegions.sky_garden),
    create_location(wilderness_location_start + 16, Wilderness.egg, DreamRegions.sky_garden),
    create_location(wilderness_location_start + 17, Wilderness.jellyfish, DreamRegions.wilderness_town_interior),
]

docks_location_start = 50
docks = [
    create_location(docks_location_start + 1, Docks.yen_1, DreamRegions.dock_train),
    create_location(docks_location_start + 2, Docks.yen_2, DreamRegions.dock_train),
    create_location(docks_location_start + 3, Docks.yen_3, DreamRegions.dock_fisher),
    create_location(docks_location_start + 4, Docks.yen_4, DreamRegions.dock_vending),
    create_location(docks_location_start + 5, Docks.yen_5, DreamRegions.docks_crate),
    create_location(docks_location_start + 6, Docks.yen_6, DreamRegions.docks_crate),
    create_location(docks_location_start + 7, Docks.yen_7, DreamRegions.docks_scale),
    create_location(docks_location_start + 8, Docks.yen_8, DreamRegions.docks_two_story),
    create_location(docks_location_start + 9, Docks.yen_9, DreamRegions.docks_two_story),
    create_location(docks_location_start + 10, Docks.yen_10, DreamRegions.dock_w_room),
    create_location(docks_location_start + 11, Docks.hamsa, DreamRegions.dock_train),
    create_location(docks_location_start + 12, Docks.planks, DreamRegions.dock_train),
    create_location(docks_location_start + 13, Docks.boarded_art, DreamRegions.dock_train),
    create_location(docks_location_start + 14, Docks.diary_strober, DreamRegions.dock_train),
    create_location(docks_location_start + 15, Docks.blood_bag, DreamRegions.dock_vending),
    create_location(docks_location_start + 16, Docks.sad_fish, DreamRegions.dock_fisher),
    create_location(docks_location_start + 17, Docks.diary_forest_tree, DreamRegions.docks_lighthouse),
    create_location(docks_location_start + 18, Docks.dirty_game_cartridge, DreamRegions.docks_lighthouse),
    create_location(docks_location_start + 19, Docks.diary_pink_sea, DreamRegions.pink_sea),
    create_location(docks_location_start + 20, Docks.egg, DreamRegions.poniko_room),
    create_location(docks_location_start + 21, Docks.mask_of_fear, DreamRegions.poniko_room),
    create_location(docks_location_start + 22, Docks.jellyfish, DreamRegions.dock_fisher),
]

mall_location_start = 80
malls = [
    create_location(mall_location_start + 1, Mall.hidden_storage, DreamRegions.storage_room),
    create_location(mall_location_start + 2, Mall.flute, DreamRegions.music_room),
    create_location(mall_location_start + 3, Mall.diary_flute, DreamRegions.music_room),
    create_location(mall_location_start + 4, Mall.diary_plant, DreamRegions.mall),
    create_location(mall_location_start + 5, Mall.valve, DreamRegions.storage_room_upper),
    create_location(mall_location_start + 6, Mall.egg, DreamRegions.box_room),
    create_location(mall_location_start + 8, Mall.rooftop_key, DreamRegions.box_room),
    create_location(mall_location_start + 9, Mall.diary_upper_boxes, DreamRegions.box_room),
    create_location(mall_location_start + 10, Mall.mysterious_cartridge, DreamRegions.mall_roof),
    create_location(mall_location_start + 11, Mall.jellyfish, DreamRegions.mall_roof),
]

school_location_start = 100
schools = [
    create_location(school_location_start + 1, School.picture_1, DreamRegions.school_first),
    create_location(school_location_start + 2, School.diary_bathroom, DreamRegions.school_first),
    create_location(school_location_start + 3, School.books, DreamRegions.school_second),
    create_location(school_location_start + 4, School.brush, DreamRegions.school_book_room),
    create_location(school_location_start + 5, School.triangle, DreamRegions.school_third_class),
    create_location(school_location_start + 6, School.diary_triangle, DreamRegions.school_third_class),
    create_location(school_location_start + 7, School.picture_2, DreamRegions.school_band_room),
    create_location(school_location_start + 8, School.picture_3, DreamRegions.school_second),
    create_location(school_location_start + 9, School.picture_4, DreamRegions.school_third_class),
    create_location(school_location_start + 10, School.lever, DreamRegions.school_storm_interior_front),
    create_location(school_location_start + 11, School.toilet_key, DreamRegions.school_storm_interior_front),
    create_location(school_location_start + 12, School.lantern, DreamRegions.school_storm_interior_front_past_switch),
    create_location(school_location_start + 13, School.diary_cabinet, DreamRegions.school_storm_interior_front_past_switch),
    create_location(school_location_start + 14, School.diary_switch, DreamRegions.school_storm_interior_front_past_switch),
    create_location(school_location_start + 15, School.diary_zipper, DreamRegions.school_storm_interior_back),
    create_location(school_location_start + 16, School.egg, DreamRegions.school_storm_interior_back),
    create_location(school_location_start + 17, School.diary_kyuukyuu, DreamRegions.school_storm_interior_back),
    create_location(school_location_start + 18, School.jellyfish, DreamRegions.school_locked_bathroom),
]

sewers_location_start = 120
sewers = [
    create_location(sewers_location_start + 1, Blocks.girl_1, DreamRegions.blocks),
    create_location(sewers_location_start + 2, Blocks.girl_2, DreamRegions.blocks),
    create_location(sewers_location_start + 3, Blocks.girl_3, DreamRegions.blocks),
    create_location(sewers_location_start + 4, Blocks.girl_4, DreamRegions.blocks),
    create_location(sewers_location_start + 5, Blocks.girl_5, DreamRegions.blocks),
    create_location(sewers_location_start + 6, Blocks.girl_6, DreamRegions.blocks),
    create_location(sewers_location_start + 7, Blocks.diary_blocks, DreamRegions.blocks),
    create_location(sewers_location_start + 8, Snow.hat_and_scarf, DreamRegions.snow),
    create_location(sewers_location_start + 9, Snow.diary_snowman, DreamRegions.snow),
    create_location(sewers_location_start + 10, Snow.egg, DreamRegions.snow),
    create_location(sewers_location_start + 11, Sewer.diary_pool, DreamRegions.sewers),
    create_location(sewers_location_start + 12, Sewer.jellyfish, DreamRegions.sewers),
]

apartment_location_start = 140
apartments = [
    create_location(apartment_location_start + 1, Apartment.diary_lone_bed, DreamRegions.apartment_bottom_floor),
    create_location(apartment_location_start + 2, Apartment.diary_open_box, DreamRegions.apartment_bottom_floor),
    create_location(apartment_location_start + 3, Apartment.rusty_key, DreamRegions.apartment_top_floor),
    create_location(apartment_location_start + 4, Apartment.diary_outside, DreamRegions.apartment_roof),
]

nasu_location_start = 200
nasu_locations = [
    create_location(nasu_location_start + 1, Nasu.nasu_points_1, DreamRegions.nasu_game),
    create_location(nasu_location_start + 2, Nasu.nasu_points_2, DreamRegions.nasu_game),
    create_location(nasu_location_start + 3, Nasu.nasu_points_3, DreamRegions.nasu_game),
    create_location(nasu_location_start + 4, Nasu.nasu_points_4, DreamRegions.nasu_game),
    create_location(nasu_location_start + 5, Nasu.nasu_points_5, DreamRegions.nasu_game),
    create_location(nasu_location_start + 6, Nasu.nasu_points_6, DreamRegions.nasu_game),
]

ao_oni_location_start = 230
ao_oni_locations = [
    create_location(ao_oni_location_start + 1, AoOni.floor_1_key, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 2, AoOni.floor_1_mansion_key, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 3, AoOni.floor_1_poniko, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 4, AoOni.floor_1_monoe, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 5, AoOni.floor_1_monoko, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 6, AoOni.floor_1_bonus_1, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 7, AoOni.floor_1_bonus_2, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 8, AoOni.floor_1_bonus_3, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 9, AoOni.floor_2_key, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 10, AoOni.floor_2_mansion_key, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 11, AoOni.floor_2_poniko, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 12, AoOni.floor_2_monoe, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 13, AoOni.floor_2_monoko, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 14, AoOni.floor_2_bonus_1, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 15, AoOni.floor_2_bonus_2, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 16, AoOni.floor_2_bonus_3, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 17, AoOni.floor_3_key, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 18, AoOni.floor_3_mansion_key, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 19, AoOni.floor_3_poniko, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 20, AoOni.floor_3_monoe, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 21, AoOni.floor_3_monoko, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 22, AoOni.floor_3_bonus_1, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 23, AoOni.floor_3_bonus_2, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 24, AoOni.floor_3_bonus_3, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 25, AoOni.floor_4_key, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 26, AoOni.floor_4_mansion_key, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 27, AoOni.floor_4_poniko, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 28, AoOni.floor_4_monoe, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 29, AoOni.floor_4_monoko, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 30, AoOni.floor_4_bonus_1, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 31, AoOni.floor_4_bonus_2, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 32, AoOni.floor_4_bonus_3, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 33, AoOni.floor_5_key, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 34, AoOni.floor_5_mansion_key, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 35, AoOni.floor_5_poniko, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 36, AoOni.floor_5_monoe, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 37, AoOni.floor_5_monoko, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 38, AoOni.floor_5_bonus_1, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 39, AoOni.floor_5_bonus_2, DreamRegions.ao_oni_game),
    create_location(ao_oni_location_start + 40, AoOni.floor_5_bonus_3, DreamRegions.ao_oni_game),
]

witch_adventure_location_start = 300
witch_adventure_locations = [
    create_location(witch_adventure_location_start + 1, WitchAdventure.boss_1, DreamRegions.witch_game),
    create_location(witch_adventure_location_start + 2, WitchAdventure.boss_2, DreamRegions.witch_game),
    create_location(witch_adventure_location_start + 3, WitchAdventure.boss_3, DreamRegions.witch_game),
    create_location(witch_adventure_location_start + 4, WitchAdventure.boss_4, DreamRegions.witch_game),
    create_location(witch_adventure_location_start + 5, WitchAdventure.boss_5, DreamRegions.witch_game),
]
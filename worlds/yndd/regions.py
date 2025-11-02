from entrance_rando import EntranceType
from dataclasses import dataclass, field
from typing import List, Tuple, Dict, Optional, Protocol, Iterable, Set

from BaseClasses import MultiWorld, Region, Entrance

from .strings.regions_entrances import DreamRegions, DreamEntrances


class RegionFactory(Protocol):
    def __call__(self, name: str, regions: Iterable[str]) -> Region:
        raise NotImplementedError


@dataclass(frozen=True)
class RegionData:
    name: str
    exits: List[str] = field(default_factory=list)


@dataclass(frozen=True)
class EntranceData:
    entrance_name: str
    region_exit: Optional[str] = None
    randomized: bool = False
    type: EntranceType = EntranceType.ONE_WAY


yume_nikki_regions = [
    RegionData(DreamRegions.menu, [DreamEntrances.begin_day]),
    RegionData(DreamRegions.real_bedroom, [DreamEntrances.nasu_game_path, DreamEntrances.sleep]),
    RegionData(DreamRegions.dream_bedroom, [DreamEntrances.ao_oni_game_path, DreamEntrances.witch_game_path,
                                            DreamEntrances.leave_dream_room]),
    RegionData(DreamRegions.nexus, [DreamEntrances.nexus_to_streets, DreamEntrances.nexus_to_wilderness,
                                    DreamEntrances.nexus_to_docks, DreamEntrances.nexus_to_school,
                                    DreamEntrances.nexus_to_mall, DreamEntrances.nexus_to_sewers,
                                    DreamEntrances.nexus_to_apartment]),

    RegionData(DreamRegions.nasu_game),

    RegionData(DreamRegions.witch_game),

    RegionData(DreamRegions.ao_oni_game, [DreamEntrances.ao_oni_1_to_2]),
    RegionData(DreamRegions.ao_oni_2, [DreamEntrances.ao_oni_2_to_3]),
    RegionData(DreamRegions.ao_oni_3, [DreamEntrances.ao_oni_3_to_4]),
    RegionData(DreamRegions.ao_oni_4, [DreamEntrances.ao_oni_4_to_5]),
    RegionData(DreamRegions.ao_oni_5),

    RegionData(DreamRegions.initial_street, [DreamEntrances.initial_streets_to_streets]),
    RegionData(DreamRegions.streets, [DreamEntrances.streets_to_sewers, DreamEntrances.streets_to_butcher_front]),
    RegionData(DreamRegions.butcher_front, [DreamEntrances.butcher_front_to_butcher_back]),
    RegionData(DreamRegions.butcher_feeding, [DreamEntrances.butcher_feeding_to_road]),
    RegionData(DreamRegions.road, [DreamEntrances.road_to_monoe]),
    RegionData(DreamRegions.bed_maze),

    RegionData(DreamRegions.temple_base, [DreamEntrances.hamsa_path, DreamEntrances.first_train, DreamEntrances.temple_base_to_garden]),
    RegionData(DreamRegions.endless_wilderness),
    RegionData(DreamRegions.train_1, [DreamEntrances.first_train_off]),
    RegionData(DreamRegions.wilderness_town, [DreamEntrances.second_train, DreamEntrances.wilderness_town_to_sewers,
                                              DreamEntrances.wilderness_homes_doors]),
    RegionData(DreamRegions.wilderness_town_interior),
    RegionData(DreamRegions.train_2, [DreamEntrances.second_train_off]),
    RegionData(DreamRegions.wilderness_night, [DreamEntrances.third_train]),
    RegionData(DreamRegions.train_3, [DreamEntrances.third_train_off, DreamEntrances.third_train_to_fourth]),
    RegionData(DreamRegions.train_4, [DreamEntrances.fourth_train_off]),
    RegionData(DreamRegions.sky_garden),

    RegionData(DreamRegions.mall, [DreamEntrances.mall_to_storage, DreamEntrances.enter_mannequin_room, DreamEntrances.mall_to_music]),
    RegionData(DreamRegions.storage_room, [DreamEntrances.storage_to_upper_storage, DreamEntrances.storage_to_sewers]),
    RegionData(DreamRegions.storage_room_upper, [DreamEntrances.upper_storage_to_roof]),
    RegionData(DreamRegions.mall_roof),
    RegionData(DreamRegions.music_room),
    RegionData(DreamRegions.mannequin_room, [DreamEntrances.enter_box_room]),
    RegionData(DreamRegions.box_room),

    RegionData(DreamRegions.school_front, [DreamEntrances.school_front_to_first]),
    RegionData(DreamRegions.school_first, [DreamEntrances.school_first_to_book, DreamEntrances.school_first_to_second]),
    RegionData(DreamRegions.school_book_room),
    RegionData(DreamRegions.school_second, [DreamEntrances.school_second_to_music, DreamEntrances.school_second_to_third]),
    RegionData(DreamRegions.school_band_room),
    RegionData(DreamRegions.school_third, [DreamEntrances.school_third_to_class, DreamEntrances.school_third_to_bathroom,
                                           DreamEntrances.school_third_to_storm]),
    RegionData(DreamRegions.school_third_class),
    RegionData(DreamRegions.school_locked_bathroom),
    RegionData(DreamRegions.school_outside_storm, [DreamEntrances.school_storm_to_front]),
    RegionData(DreamRegions.school_storm_interior_front, [DreamEntrances.school_storm_front_to_lever]),
    RegionData(DreamRegions.school_storm_interior_front_past_switch, [DreamEntrances.school_storm_front_to_back]),
    RegionData(DreamRegions.school_storm_interior_back),

    RegionData(DreamRegions.dock_fisher, [DreamEntrances.fisher_to_w]),
    RegionData(DreamRegions.dock_w_room, [DreamEntrances.w_to_vending]),
    RegionData(DreamRegions.dock_vending, [DreamEntrances.vending_to_crate]),
    RegionData(DreamRegions.docks_crate, [DreamEntrances.crate_to_scale]),
    RegionData(DreamRegions.docks_scale, [DreamEntrances.scale_to_two_story]),
    RegionData(DreamRegions.docks_two_story, [DreamEntrances.two_story_to_train]),
    RegionData(DreamRegions.dock_train, [DreamEntrances.dock_train_to_lighthouse, DreamEntrances.fourth_train]),
    RegionData(DreamRegions.docks_lighthouse, [DreamEntrances.lighthouse_to_igloo]),
    RegionData(DreamRegions.igloo, [DreamEntrances.igloo_to_pink_sea]),
    RegionData(DreamRegions.pink_sea, [DreamEntrances.pink_sea_to_poniko]),
    RegionData(DreamRegions.poniko_room),

    RegionData(DreamRegions.sewers, [DreamEntrances.sewers_to_storage, DreamEntrances.sewers_to_blocks,
                                     DreamEntrances.sewers_to_streets, DreamEntrances.sewers_to_wilderness_town]),
    RegionData(DreamRegions.blocks, [DreamEntrances.blocks_to_snow]),
    RegionData(DreamRegions.snow, [DreamEntrances.snow_to_igloo]),

    RegionData(DreamRegions.apartment_bottom_floor, [DreamEntrances.apartment_bottom_to_top]),
    RegionData(DreamRegions.apartment_top_floor, [DreamEntrances.apartment_top_to_roof]),
    RegionData(DreamRegions.apartment_roof, [DreamEntrances.apartment_roof_to_ufo, DreamEntrances.to_normal_end]),
    RegionData(DreamRegions.normal_end),
    RegionData(DreamRegions.apartment_ufo, [DreamEntrances.to_secret_end]),
    RegionData(DreamRegions.secret_end),
]

yume_nikki_entrances =  [
    EntranceData(DreamEntrances.begin_day, DreamRegions.real_bedroom),
    EntranceData(DreamEntrances.nasu_game_path, DreamRegions.nasu_game),
    EntranceData(DreamEntrances.witch_game_path, DreamRegions.witch_game),
    EntranceData(DreamEntrances.sleep, DreamRegions.dream_bedroom),
    EntranceData(DreamEntrances.leave_dream_room, DreamRegions.nexus),

    EntranceData(DreamEntrances.ao_oni_game_path, DreamRegions.ao_oni_game),
    EntranceData(DreamEntrances.ao_oni_1_to_2, DreamRegions.ao_oni_2),
    EntranceData(DreamEntrances.ao_oni_2_to_3, DreamRegions.ao_oni_3),
    EntranceData(DreamEntrances.ao_oni_3_to_4, DreamRegions.ao_oni_4),
    EntranceData(DreamEntrances.ao_oni_4_to_5, DreamRegions.ao_oni_5),

    EntranceData(DreamEntrances.nexus_to_streets, DreamRegions.initial_street),
    EntranceData(DreamEntrances.initial_streets_to_streets, DreamRegions.streets),
    EntranceData(DreamEntrances.streets_to_sewers, DreamRegions.sewers, True, EntranceType.TWO_WAY),
    EntranceData(DreamEntrances.sewers_to_streets, DreamRegions.streets, True, EntranceType.TWO_WAY),
    EntranceData(DreamEntrances.streets_to_butcher_front, DreamRegions.butcher_front),
    EntranceData(DreamEntrances.butcher_front_to_butcher_back, DreamRegions.butcher_feeding),
    EntranceData(DreamEntrances.butcher_feeding_to_road, DreamRegions.road),
    EntranceData(DreamEntrances.road_to_monoe, DreamRegions.bed_maze),

    EntranceData(DreamEntrances.nexus_to_wilderness, DreamRegions.temple_base),
    EntranceData(DreamEntrances.hamsa_path, DreamRegions.endless_wilderness),
    EntranceData(DreamEntrances.first_train, DreamRegions.train_1),
    EntranceData(DreamEntrances.first_train_off, DreamRegions.wilderness_town),
    EntranceData(DreamEntrances.wilderness_homes_doors, DreamRegions.wilderness_town_interior),
    EntranceData(DreamEntrances.wilderness_town_to_sewers, DreamRegions.sewers, True, EntranceType.TWO_WAY),
    EntranceData(DreamEntrances.sewers_to_wilderness_town, DreamRegions.wilderness_town, True, EntranceType.TWO_WAY),
    EntranceData(DreamEntrances.second_train, DreamRegions.train_2),
    EntranceData(DreamEntrances.second_train_off, DreamRegions.wilderness_night),
    EntranceData(DreamEntrances.third_train, DreamRegions.train_3),
    EntranceData(DreamEntrances.third_train_off, DreamRegions.dock_train, True, EntranceType.TWO_WAY),
    EntranceData(DreamEntrances.fourth_train, DreamRegions.train_3, True, EntranceType.TWO_WAY),
    EntranceData(DreamEntrances.third_train_to_fourth, DreamRegions.train_4),
    EntranceData(DreamEntrances.fourth_train_off, DreamRegions.temple_base),
    EntranceData(DreamEntrances.temple_base_to_garden, DreamRegions.sky_garden),

    EntranceData(DreamEntrances.nexus_to_mall, DreamRegions.mall),
    EntranceData(DreamEntrances.mall_to_storage, DreamRegions.storage_room),
    EntranceData(DreamEntrances.upper_storage_to_roof, DreamRegions.mall_roof),
    EntranceData(DreamEntrances.storage_to_sewers, DreamRegions.sewers, True, EntranceType.TWO_WAY),
    EntranceData(DreamEntrances.sewers_to_storage, DreamRegions.storage_room, True, EntranceType.TWO_WAY),
    EntranceData(DreamEntrances.storage_to_upper_storage, DreamRegions.storage_room_upper),
    EntranceData(DreamEntrances.enter_mannequin_room, DreamRegions.mannequin_room),
    EntranceData(DreamEntrances.enter_box_room, DreamRegions.box_room),
    EntranceData(DreamEntrances.mall_to_music, DreamRegions.music_room),

    EntranceData(DreamEntrances.nexus_to_school, DreamRegions.school_front),
    EntranceData(DreamEntrances.school_front_to_first, DreamRegions.school_first),
    EntranceData(DreamEntrances.school_first_to_book, DreamRegions.school_book_room),
    EntranceData(DreamEntrances.school_first_to_second, DreamRegions.school_second),
    EntranceData(DreamEntrances.school_second_to_music, DreamRegions.school_band_room),
    EntranceData(DreamEntrances.school_second_to_third, DreamRegions.school_third),
    EntranceData(DreamEntrances.school_third_to_class, DreamRegions.school_third_class),
    EntranceData(DreamEntrances.school_third_to_bathroom, DreamRegions.school_locked_bathroom),
    EntranceData(DreamEntrances.school_third_to_storm, DreamRegions.school_outside_storm),
    EntranceData(DreamEntrances.school_storm_to_front, DreamRegions.school_storm_interior_front),
    EntranceData(DreamEntrances.school_storm_front_to_lever, DreamRegions.school_storm_interior_front_past_switch),
    EntranceData(DreamEntrances.school_storm_front_to_back, DreamRegions.school_storm_interior_back),

    EntranceData(DreamEntrances.nexus_to_docks, DreamRegions.dock_fisher),
    EntranceData(DreamEntrances.fisher_to_w, DreamRegions.dock_w_room),
    EntranceData(DreamEntrances.w_to_vending, DreamRegions.dock_vending),
    EntranceData(DreamEntrances.vending_to_crate, DreamRegions.docks_crate),
    EntranceData(DreamEntrances.crate_to_scale, DreamRegions.docks_scale),
    EntranceData(DreamEntrances.scale_to_two_story, DreamRegions.docks_two_story),
    EntranceData(DreamEntrances.two_story_to_train, DreamRegions.dock_train),
    EntranceData(DreamEntrances.dock_train_to_lighthouse, DreamRegions.docks_lighthouse),
    EntranceData(DreamEntrances.lighthouse_to_igloo, DreamRegions.igloo),
    EntranceData(DreamEntrances.igloo_to_pink_sea, DreamRegions.pink_sea),
    EntranceData(DreamEntrances.pink_sea_to_poniko, DreamRegions.poniko_room),

    EntranceData(DreamEntrances.nexus_to_sewers, DreamRegions.sewers),
    EntranceData(DreamEntrances.sewers_to_blocks, DreamRegions.blocks),
    EntranceData(DreamEntrances.blocks_to_snow, DreamRegions.snow),
    EntranceData(DreamEntrances.snow_to_igloo, DreamRegions.igloo),

    EntranceData(DreamEntrances.nexus_to_apartment, DreamRegions.apartment_bottom_floor),
    EntranceData(DreamEntrances.apartment_bottom_to_top, DreamRegions.apartment_top_floor),
    EntranceData(DreamEntrances.apartment_top_to_roof, DreamRegions.apartment_roof),
    EntranceData(DreamEntrances.apartment_roof_to_ufo, DreamRegions.apartment_ufo),
    EntranceData(DreamEntrances.to_normal_end, DreamRegions.normal_end),
    EntranceData(DreamEntrances.to_secret_end, DreamRegions.secret_end),
]

randomized_entrance_names = [entrance.entrance_name for entrance in yume_nikki_entrances if entrance.randomized]


def create_regions(region_factory: RegionFactory, multiworld: MultiWorld) -> Tuple[Dict[str, Region], Dict[str, Entrance]]:
    final_regions = yume_nikki_regions.copy()
    regions: Dict[str: Region] = {region.name: region_factory(region.name, region.exits) for region in
                                  final_regions}
    entrances: Dict[str: Entrance] = {}
    for region in regions.values():
        for entrance in region.exits:
            multiworld.register_indirect_condition(region, entrance)
            entrances[entrance.name] = entrance

    for connection in yume_nikki_entrances:
        if connection.entrance_name in entrances:
            entrances[connection.entrance_name].randomization_type = connection.type
            entrances[connection.entrance_name].connect(regions[connection.region_exit])
    return regions, entrances

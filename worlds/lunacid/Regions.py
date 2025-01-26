from dataclasses import dataclass, field
from enum import IntFlag
from random import Random
from typing import List, Tuple, Dict, Optional, Protocol, Iterable, Set

from BaseClasses import MultiWorld, Region, Entrance

from worlds.lunacid.strings.regions_entrances import LunacidRegion, LunacidEntrance


class RegionFactory(Protocol):
    def __call__(self, name: str, regions: Iterable[str]) -> Region:
        raise NotImplementedError


connector_keyword = " to "


def link_lunacid_areas(world: MultiWorld, player: int):
    for (entrance, region) in consistent_entrances:
        world.get_entrance(entrance, player).connect(world.get_region(region, player))


def REVERSE(connection: str):
    connection_array = connection.split(" to ")
    return connection_array[1] + " to " + connection_array[0]


@dataclass(frozen=True)
class RegionData:
    name: str
    exits: List[str] = field(default_factory=list)

    def get_merged_with(self, exits: List[str]):
        merged_exits = []
        merged_exits.extend(self.exits)
        if exits is not None:
            merged_exits.extend(exits)
        merged_exits = list(set(merged_exits))
        return RegionData(self.name, merged_exits)

    def get_clone(self):
        return self.get_merged_with(None)


class RandomizationFlag(IntFlag):
    NOT_RANDOMIZED = 0b0
    RANDOMIZED = 0b1


@dataclass(frozen=True)
class ConnectionData:
    name: str
    destination: str
    origin: Optional[str] = None
    reverse: Optional[str] = None
    flag: RandomizationFlag = RandomizationFlag.NOT_RANDOMIZED

    def __post_init__(self):
        if connector_keyword in self.name:
            origin, destination = self.name.split(connector_keyword)
            if self.reverse is None:
                super().__setattr__("reverse", f"{destination}{connector_keyword}{origin}")


consistent_regions = [
    RegionData(LunacidRegion.temple_of_silence_secret),
    RegionData(LunacidRegion.wings_rest, [LunacidEntrance.wings_to_surface, LunacidEntrance.sheryl]),
    RegionData(LunacidRegion.sheryl_the_crow),
    RegionData(LunacidRegion.forbidden_archives_1),
    RegionData(LunacidRegion.forbidden_archives_1b, [LunacidEntrance.archives_to_daedalus]),
    RegionData(LunacidRegion.daedalus),
    RegionData(LunacidRegion.forest_canopy),
    RegionData(LunacidRegion.yosei_lower, [LunacidEntrance.yosei_lower_to_tomb_upper_lobby, LunacidEntrance.yosei_lower_to_patchouli]),
    RegionData(LunacidRegion.accursed_tomb_upper_lobby, [LunacidEntrance.tomb_upper_to_tomb]),
    RegionData(LunacidRegion.patchouli),
    RegionData(LunacidRegion.great_well_surface),
    RegionData(LunacidRegion.sanguine_sea, [LunacidEntrance.sea_to_castle, LunacidEntrance.sea_to_tomb_lobby]),
    RegionData(LunacidRegion.accursed_tomb_lobby, [LunacidEntrance.tomb_lobby_to_tomb]),
    RegionData(LunacidRegion.accursed_tomb, [LunacidEntrance.tomb_to_vampire, LunacidEntrance.tomb_to_mausoleum, LunacidEntrance.tomb_to_tomb_platform]),
    RegionData(LunacidRegion.vampire_tomb),
    RegionData(LunacidRegion.accursed_tomb_platform),
    RegionData(LunacidRegion.mausoleum),
    RegionData(LunacidRegion.holy_battleground),
    RegionData(LunacidRegion.sealed_ballroom, [LunacidEntrance.ballroom_to_doors, LunacidEntrance.ballroom_to_secret]),
    RegionData(LunacidRegion.sealed_ballroom_doors),
    RegionData(LunacidRegion.sealed_ballroom_secret),
    RegionData(LunacidRegion.tower_abyss, [LunacidEntrance.tower_abyss_to_5]),
    RegionData(LunacidRegion.tower_abyss_5, [LunacidEntrance.tower_abyss_5_to_10]),
    RegionData(LunacidRegion.tower_abyss_10, [LunacidEntrance.tower_abyss_10_to_15]),
    RegionData(LunacidRegion.tower_abyss_15, [LunacidEntrance.tower_abyss_15_to_20]),
    RegionData(LunacidRegion.tower_abyss_20, [LunacidEntrance.tower_abyss_20_to_25]),
    RegionData(LunacidRegion.tower_abyss_25, [LunacidEntrance.tower_abyss_25_to_30]),
    RegionData(LunacidRegion.tower_abyss_30, [LunacidEntrance.tower_abyss_30_to_35]),
    RegionData(LunacidRegion.tower_abyss_35, [LunacidEntrance.tower_abyss_35_to_40]),
    RegionData(LunacidRegion.tower_abyss_40, [LunacidEntrance.tower_abyss_40_to_45]),
    RegionData(LunacidRegion.tower_abyss_45, [LunacidEntrance.tower_abyss_45_to_50]),
    RegionData(LunacidRegion.tower_abyss_50, [LunacidEntrance.tower_abyss_50_to_top]),
    RegionData(LunacidRegion.tower_abyss_top),
    RegionData(LunacidRegion.sand_temple, [LunacidEntrance.sand_to_deep_snake, LunacidEntrance.sand_to_secret_snake, LunacidEntrance.sand_to_sand_secret]),
    RegionData(LunacidRegion.sand_temple_secret),
    RegionData(LunacidRegion.deep_snake_pit),
    RegionData(LunacidRegion.secret_snake_pit),
    RegionData(LunacidRegion.terminus_prison_upstairs),
    RegionData(LunacidRegion.terminus_prison_dark, [LunacidEntrance.prison_to_ash_entrance, LunacidEntrance.prison_to_arena]),
    RegionData(LunacidRegion.labyrinth_of_ash_entrance, [LunacidEntrance.ash_entrance_to_ash]),
    RegionData(LunacidRegion.labyrinth_of_ash, [LunacidEntrance.labyrinth_of_ash_to_holy_seat_of_gold]),
    RegionData(LunacidRegion.holy_seat_of_gold),
    RegionData(LunacidRegion.forlorn_arena, [LunacidEntrance.arena_to_fate, LunacidEntrance.arena_to_earth_secret, LunacidEntrance.arena_to_water]),
    RegionData(LunacidRegion.water_temple, [LunacidEntrance.water_to_deep]),
    RegionData(LunacidRegion.water_temple_lower, [LunacidEntrance.water_to_secret]),
    RegionData(LunacidRegion.water_temple_secret),
    RegionData(LunacidRegion.chamber_of_fate, [LunacidEntrance.fate_to_sleeper]),
    RegionData(LunacidRegion.grave_of_the_sleeper),

    RegionData(LunacidRegion.menu, [LunacidEntrance.menu_to_basin]),
    RegionData(LunacidRegion.hollow_basin, [LunacidEntrance.basin_to_wings_rest, LunacidEntrance.basin_to_archives, LunacidEntrance.basin_to_surface,
                                            LunacidEntrance.basin_to_temple]),
    RegionData(LunacidRegion.temple_of_silence_entrance, [LunacidEntrance.temple_entrance_to_temple_interior]),
    RegionData(LunacidRegion.temple_of_silence_interior, [LunacidEntrance.temple_to_mire, LunacidEntrance.temple_to_forest,
                                                          LunacidEntrance.temple_interior_to_temple_secret]),
    RegionData(LunacidRegion.fetid_mire, [LunacidEntrance.mire_to_sea, LunacidEntrance.mire_to_secret]),
    RegionData(LunacidRegion.fetid_mire_secret),
    RegionData(LunacidRegion.forbidden_archives_2, [LunacidEntrance.archives_2_to_archives_1, LunacidEntrance.archives_2_to_archives_3]),
    RegionData(LunacidRegion.forbidden_archives_3, [LunacidEntrance.archives_3_to_archives_1b, LunacidEntrance.archives_to_chasm]),
    RegionData(LunacidRegion.laetus_chasm, [LunacidEntrance.chasm_to_surface]),
    RegionData(LunacidRegion.yosei_forest, [LunacidEntrance.yosei_to_yosei_lower, LunacidEntrance.yosei_to_canopy]),

    RegionData(LunacidRegion.castle_le_fanu, [LunacidEntrance.castle_to_red, LunacidEntrance.castle_to_white, LunacidEntrance.castle_to_battleground]),
    RegionData(LunacidRegion.castle_le_fanu_red, [LunacidEntrance.red_to_red_deep]),
    RegionData(LunacidRegion.castle_le_fanu_red_deep, [LunacidEntrance.red_deep_to_red_secret]),
    RegionData(LunacidRegion.castle_le_fanu_red_secret),
    RegionData(LunacidRegion.castle_le_fanu_white, [LunacidEntrance.white_to_blue, LunacidEntrance.white_to_throne]),
    RegionData(LunacidRegion.castle_le_fanu_blue, [LunacidEntrance.castle_to_grotto, LunacidEntrance.castle_to_ballroom]),
    RegionData(LunacidRegion.boiling_grotto, [LunacidEntrance.grotto_to_tower, LunacidEntrance.grotto_to_secret, LunacidEntrance.grotto_to_sand]),
    RegionData(LunacidRegion.boiling_grotto_secret),
    RegionData(LunacidRegion.throne_chamber, [LunacidEntrance.throne_to_prison]),
    RegionData(LunacidRegion.terminus_prison, [LunacidEntrance.prison_to_prison_upstairs, LunacidEntrance.prison_to_prison_dark]),
    RegionData(LunacidRegion.earth_temple_secret)
]

consistent_entrances = [
    ConnectionData(LunacidEntrance.basin_to_wings_rest, LunacidRegion.wings_rest),
    ConnectionData(LunacidEntrance.sheryl, LunacidRegion.sheryl_the_crow),
    ConnectionData(LunacidEntrance.temple_interior_to_temple_secret, LunacidRegion.temple_of_silence_secret),
    ConnectionData(LunacidEntrance.mire_to_secret, LunacidRegion.fetid_mire_secret),
    ConnectionData(LunacidEntrance.prison_to_arena, LunacidRegion.forlorn_arena, flag=RandomizationFlag.RANDOMIZED),
    ConnectionData(LunacidEntrance.prison_to_ash_entrance, LunacidRegion.labyrinth_of_ash_entrance, flag=RandomizationFlag.RANDOMIZED),
    ConnectionData(LunacidEntrance.ash_entrance_to_ash, LunacidRegion.labyrinth_of_ash),
    ConnectionData(LunacidEntrance.sea_to_tomb_lobby, LunacidRegion.accursed_tomb_lobby, flag=RandomizationFlag.RANDOMIZED),
    ConnectionData(LunacidEntrance.tomb_lobby_to_tomb, LunacidRegion.accursed_tomb),
    ConnectionData(LunacidEntrance.chasm_to_surface, LunacidRegion.great_well_surface, flag=RandomizationFlag.RANDOMIZED),
    ConnectionData(LunacidEntrance.yosei_to_canopy, LunacidRegion.forest_canopy, flag=RandomizationFlag.RANDOMIZED),
    ConnectionData(LunacidEntrance.yosei_to_yosei_lower, LunacidRegion.yosei_lower),
    ConnectionData(LunacidEntrance.yosei_lower_to_tomb_upper_lobby, LunacidRegion.accursed_tomb_upper_lobby, flag=RandomizationFlag.RANDOMIZED),
    ConnectionData(LunacidEntrance.tomb_upper_to_tomb, LunacidRegion.accursed_tomb),
    ConnectionData(LunacidEntrance.tomb_to_tomb_platform, LunacidRegion.accursed_tomb_platform),
    ConnectionData(LunacidEntrance.tomb_to_vampire, LunacidRegion.vampire_tomb),
    ConnectionData(LunacidEntrance.tomb_to_mausoleum, LunacidRegion.mausoleum),
    ConnectionData(LunacidEntrance.arena_to_fate, LunacidRegion.chamber_of_fate),
    ConnectionData(LunacidEntrance.fate_to_sleeper, LunacidRegion.grave_of_the_sleeper),
    ConnectionData(LunacidEntrance.archives_to_daedalus, LunacidRegion.daedalus),
    ConnectionData(LunacidEntrance.grotto_to_tower, LunacidRegion.tower_abyss, flag=RandomizationFlag.RANDOMIZED),
    ConnectionData(LunacidEntrance.tower_abyss_to_5, LunacidRegion.tower_abyss_5),
    ConnectionData(LunacidEntrance.tower_abyss_5_to_10, LunacidRegion.tower_abyss_10),
    ConnectionData(LunacidEntrance.tower_abyss_10_to_15, LunacidRegion.tower_abyss_15),
    ConnectionData(LunacidEntrance.tower_abyss_15_to_20, LunacidRegion.tower_abyss_20),
    ConnectionData(LunacidEntrance.tower_abyss_20_to_25, LunacidRegion.tower_abyss_25),
    ConnectionData(LunacidEntrance.tower_abyss_25_to_30, LunacidRegion.tower_abyss_30),
    ConnectionData(LunacidEntrance.tower_abyss_30_to_35, LunacidRegion.tower_abyss_35),
    ConnectionData(LunacidEntrance.tower_abyss_35_to_40, LunacidRegion.tower_abyss_40),
    ConnectionData(LunacidEntrance.tower_abyss_40_to_45, LunacidRegion.tower_abyss_45),
    ConnectionData(LunacidEntrance.tower_abyss_45_to_50, LunacidRegion.tower_abyss_50),
    ConnectionData(LunacidEntrance.tower_abyss_50_to_top, LunacidRegion.tower_abyss_top),
    ConnectionData(LunacidEntrance.grotto_to_sand, LunacidRegion.sand_temple),
    ConnectionData(LunacidEntrance.prison_to_prison_dark, LunacidRegion.terminus_prison_dark),
    ConnectionData(LunacidEntrance.yosei_lower_to_patchouli, LunacidRegion.patchouli),
    ConnectionData(LunacidEntrance.wings_to_surface, LunacidRegion.great_well_surface),
    ConnectionData(LunacidEntrance.prison_to_prison_upstairs, LunacidRegion.terminus_prison_upstairs),
    ConnectionData(LunacidEntrance.menu_to_basin, LunacidRegion.hollow_basin),
    ConnectionData(LunacidEntrance.basin_to_archives, LunacidRegion.forbidden_archives_2, flag=RandomizationFlag.RANDOMIZED),
    ConnectionData(LunacidEntrance.basin_to_surface, LunacidRegion.great_well_surface, flag=RandomizationFlag.RANDOMIZED),
    ConnectionData(LunacidEntrance.basin_to_temple, LunacidRegion.temple_of_silence_entrance),
    ConnectionData(LunacidEntrance.temple_entrance_to_temple_interior, LunacidRegion.temple_of_silence_interior),
    ConnectionData(LunacidEntrance.temple_to_mire, LunacidRegion.fetid_mire, flag=RandomizationFlag.RANDOMIZED),
    ConnectionData(LunacidEntrance.temple_to_forest, LunacidRegion.yosei_forest, flag=RandomizationFlag.RANDOMIZED),
    ConnectionData(LunacidEntrance.mire_to_sea, LunacidRegion.sanguine_sea, flag=RandomizationFlag.RANDOMIZED),
    ConnectionData(LunacidEntrance.archives_2_to_archives_1, LunacidRegion.forbidden_archives_1),
    ConnectionData(LunacidEntrance.archives_2_to_archives_3, LunacidRegion.forbidden_archives_3),
    ConnectionData(LunacidEntrance.archives_3_to_archives_1b, LunacidRegion.forbidden_archives_1b),
    ConnectionData(LunacidEntrance.archives_to_chasm, LunacidRegion.laetus_chasm, flag=RandomizationFlag.RANDOMIZED),
    ConnectionData(LunacidEntrance.sea_to_castle, LunacidRegion.castle_le_fanu, flag=RandomizationFlag.RANDOMIZED),
    ConnectionData(LunacidEntrance.castle_to_red, LunacidRegion.castle_le_fanu_red),
    ConnectionData(LunacidEntrance.red_to_red_deep, LunacidRegion.castle_le_fanu_red_deep),
    ConnectionData(LunacidEntrance.red_deep_to_red_secret, LunacidRegion.castle_le_fanu_red_secret),
    ConnectionData(LunacidEntrance.castle_to_white, LunacidRegion.castle_le_fanu_white),
    ConnectionData(LunacidEntrance.castle_to_battleground, LunacidRegion.holy_battleground, flag=RandomizationFlag.RANDOMIZED),
    ConnectionData(LunacidEntrance.ballroom_to_doors, LunacidRegion.sealed_ballroom_doors),
    ConnectionData(LunacidEntrance.ballroom_to_secret, LunacidRegion.sealed_ballroom_secret),
    ConnectionData(LunacidEntrance.white_to_throne, LunacidRegion.throne_chamber, flag=RandomizationFlag.RANDOMIZED),
    ConnectionData(LunacidEntrance.white_to_blue, LunacidRegion.castle_le_fanu_blue),
    ConnectionData(LunacidEntrance.castle_to_ballroom, LunacidRegion.sealed_ballroom, flag=RandomizationFlag.RANDOMIZED),
    ConnectionData(LunacidEntrance.castle_to_grotto, LunacidRegion.boiling_grotto, flag=RandomizationFlag.RANDOMIZED),
    ConnectionData(LunacidEntrance.throne_to_prison, LunacidRegion.terminus_prison, flag=RandomizationFlag.RANDOMIZED),
    ConnectionData(LunacidEntrance.labyrinth_of_ash_to_holy_seat_of_gold, LunacidRegion.holy_seat_of_gold),
    ConnectionData(LunacidEntrance.grotto_to_secret, LunacidRegion.boiling_grotto_secret),
    ConnectionData(LunacidEntrance.arena_to_earth_secret, LunacidRegion.earth_temple_secret),
    ConnectionData(LunacidEntrance.arena_to_water, LunacidRegion.water_temple),
    ConnectionData(LunacidEntrance.water_to_deep, LunacidRegion.water_temple_lower),
    ConnectionData(LunacidEntrance.water_to_secret, LunacidRegion.water_temple_secret),
    ConnectionData(LunacidEntrance.sand_to_secret_snake, LunacidRegion.secret_snake_pit),
    ConnectionData(LunacidEntrance.sand_to_deep_snake, LunacidRegion.deep_snake_pit),
    ConnectionData(LunacidEntrance.sand_to_sand_secret, LunacidRegion.sand_temple_secret)
]


def reconstruct_connection_list(randomized_data: dict[str, str]):
    reconstructed_list: Dict[ConnectionData, ConnectionData] = {}
    for connection in randomized_data:
        starting_position = find_suitable_connection_data(connection)
        if starting_position is None:
            continue
        final_position = find_suitable_connection_data(randomized_data[connection])
        reconstructed_list[starting_position] = final_position
    return reconstructed_list


def find_suitable_connection_data(connection_name: str):
    for connection in consistent_entrances:
        if connection.name != connection_name:
            continue
        return connection
    return None


def create_regions(region_factory: RegionFactory, random: Random, options, established_randomized_data: Dict[str, str] = None) -> Tuple[Dict[str, Region], Dict[str, str]]:
    final_regions = consistent_regions
    regions: Dict[str: Region] = {region.name: region_factory(region.name, region.exits) for region in
                                  final_regions}
    entrances: Dict[str: Entrance] = {entrance.name: entrance
                                      for region in regions.values()
                                      for entrance in region.exits}

    regions_by_name: Dict[str, RegionData] = {region.name: region for region in final_regions}
    if established_randomized_data is None:
        connections, randomized_data = randomize_connections(random, options, regions_by_name)
    else:
        connections = collect_connections_to_randomize(options)
        randomized_data = reconstruct_connection_list(established_randomized_data)

    for connection in connections:
        if connection.name in entrances:
            entrances[connection.name].connect(regions[connection.destination])

    return regions, randomized_data


def collect_connections_to_randomize(options):
    connections_to_randomize = []
    final_connections = consistent_entrances
    if options.entrance_randomization == options.entrance_randomization.option_true:
        connections_to_randomize = [connection for connection in final_connections if
                                    RandomizationFlag.RANDOMIZED in connection.flag]
    return connections_to_randomize


def randomize_connections(random: Random, options, regions_by_name) -> Tuple[List[ConnectionData], Dict[str, str]]:
    final_connections = consistent_entrances
    connections_by_name: Dict[str, ConnectionData] = {connection.name: connection for connection in final_connections}
    connections_to_randomize = collect_connections_to_randomize(options)

    random.shuffle(connections_to_randomize)
    destination_pool = list(connections_to_randomize)
    random.shuffle(destination_pool)

    randomized_connections = randomize_chosen_connections(connections_to_randomize, destination_pool)
    add_non_randomized_connections(final_connections, connections_to_randomize, randomized_connections)

    swap_connections_until_valid(regions_by_name, connections_by_name, randomized_connections, connections_to_randomize, random)

    return package_connections(connections_to_randomize, randomized_connections)


def package_connections(connections_to_randomize: List[ConnectionData], randomized_connections: Dict[ConnectionData, ConnectionData]):
    randomized_connections_for_generation = create_connections_for_generation(randomized_connections)
    randomized_data_for_mod = create_data_for_mod(randomized_connections, connections_to_randomize)
    return randomized_connections_for_generation, randomized_data_for_mod


def randomize_chosen_connections(connections_to_randomize: List[ConnectionData],
                                 destination_pool: List[ConnectionData]) -> Dict[ConnectionData, ConnectionData]:
    randomized_connections = {}
    for connection in connections_to_randomize:
        destination = destination_pool.pop()
        randomized_connections[connection] = destination
    return randomized_connections


def create_connections_for_generation(randomized_connections: Dict[ConnectionData, ConnectionData]) -> List[ConnectionData]:
    connections = []
    for connection in randomized_connections:
        destination = randomized_connections[connection]
        connections.append(ConnectionData(connection.name, destination.destination, destination.reverse))
    return connections


def create_data_for_mod(randomized_connections: Dict[ConnectionData, ConnectionData],
                        connections_to_randomize: List[ConnectionData]) -> Dict[str, str]:
    randomized_data_for_mod = {}
    for connection in randomized_connections:
        if connection not in connections_to_randomize:
            continue
        destination = randomized_connections[connection]
        add_to_mod_data(connection, destination, randomized_data_for_mod)
    return randomized_data_for_mod


def add_to_mod_data(connection: ConnectionData, destination: ConnectionData, randomized_data_for_mod: Dict[str, str]):
    randomized_data_for_mod[connection.name] = destination.name
    randomized_data_for_mod[destination.reverse] = connection.reverse


def add_non_randomized_connections(connections, connections_to_randomize: List[ConnectionData],
                                   randomized_connections: Dict[ConnectionData, ConnectionData]):
    for connection in connections:
        if connection in connections_to_randomize:
            continue
        randomized_connections[connection] = connection


def swap_connections_until_valid(regions_by_name, connections_by_name, randomized_connections: Dict[ConnectionData, ConnectionData],
                                 connections_to_randomize: List[ConnectionData], random: Random):
    while True:
        reachable_regions, unreachable_regions = find_reachable_regions(regions_by_name, connections_by_name, randomized_connections)
        if not unreachable_regions:
            return randomized_connections
        swap_one_connection(regions_by_name, connections_by_name, randomized_connections, reachable_regions,
                            unreachable_regions, connections_to_randomize, random)


def find_reachable_regions(regions_by_name, connections_by_name,
                           randomized_connections: Dict[ConnectionData, ConnectionData]):
    reachable_regions = {LunacidRegion.menu}
    unreachable_regions = {region for region in regions_by_name.keys()}
    unreachable_regions.remove(LunacidRegion.menu)
    exits_to_explore = list(regions_by_name[LunacidRegion.menu].exits)
    while exits_to_explore:
        exit_name = exits_to_explore.pop()
        exit_connection = connections_by_name[exit_name]
        replaced_connection = randomized_connections[exit_connection]
        target_region_name = replaced_connection.destination
        if target_region_name in reachable_regions:
            continue

        target_region = regions_by_name[target_region_name]
        reachable_regions.add(target_region_name)
        unreachable_regions.remove(target_region_name)
        exits_to_explore.extend(target_region.exits)
    return reachable_regions, unreachable_regions


def swap_one_connection(regions_by_name, connections_by_name, randomized_connections: Dict[ConnectionData, ConnectionData],
                        reachable_regions: Set[str], unreachable_regions: Set[str],
                        connections_to_randomize: List[ConnectionData], random: Random):
    randomized_connections_already_shuffled = {connection: randomized_connections[connection]
                                               for connection in randomized_connections
                                               if connection != randomized_connections[connection]}
    unreachable_regions_names_leading_somewhere = tuple([region for region in unreachable_regions
                                                         if len(regions_by_name[region].exits) > 0])
    unreachable_regions_leading_somewhere = [regions_by_name[region_name] for region_name in unreachable_regions_names_leading_somewhere]
    unreachable_regions_exits_names = [exit_name for region in unreachable_regions_leading_somewhere for exit_name in region.exits]
    unreachable_connections = [connections_by_name[exit_name] for exit_name in unreachable_regions_exits_names]
    unreachable_connections_that_can_be_randomized = [connection for connection in unreachable_connections if connection in connections_to_randomize]

    chosen_unreachable_entrance = random.choice(unreachable_connections_that_can_be_randomized)

    chosen_reachable_entrance = None
    while chosen_reachable_entrance is None or chosen_reachable_entrance not in randomized_connections_already_shuffled:
        chosen_reachable_region_name = random.choice(sorted(reachable_regions))
        chosen_reachable_region = regions_by_name[chosen_reachable_region_name]
        if not any(chosen_reachable_region.exits):
            continue
        chosen_reachable_entrance_name = random.choice(chosen_reachable_region.exits)
        chosen_reachable_entrance = connections_by_name[chosen_reachable_entrance_name]

    reachable_destination = randomized_connections[chosen_reachable_entrance]
    unreachable_destination = randomized_connections[chosen_unreachable_entrance]
    randomized_connections[chosen_reachable_entrance] = unreachable_destination
    randomized_connections[chosen_unreachable_entrance] = reachable_destination

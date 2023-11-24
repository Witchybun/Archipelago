from random import Random
from BaseClasses import Region
from typing import Protocol, Iterable, Tuple, Dict

from worlds.lunacid.strings.regions_entrances import LunacidRegion, LunacidEntrance
from .RegionClasses import RegionData, ConnectionData
from .Options import LunacidOptions


class RegionFactory(Protocol):
    def __call__(self, name: str, regions: Iterable[str]) -> Region:
        raise NotImplementedError


lunacid_regions = [
    RegionData(LunacidRegion.menu, [LunacidEntrance.menu_to_basin]),
    RegionData(LunacidRegion.hollow_basin, [LunacidEntrance.to_wings_rest, LunacidEntrance.basin_to_archives, LunacidEntrance.basin_to_surface, LunacidEntrance.basin_to_temple]),
    RegionData(LunacidRegion.temple_of_silence, [LunacidEntrance.temple_to_mire, LunacidEntrance.temple_to_forest]),
    RegionData(LunacidRegion.wings_rest, [LunacidEntrance.wings_to_surface, LunacidEntrance.sheryl]),
    RegionData(LunacidRegion.fetid_mire, [LunacidEntrance.mire_to_sea]),
    RegionData(LunacidRegion.forbidden_archives, [LunacidEntrance.archives_to_chasm]),
    RegionData(LunacidRegion.laetus_chasm, [LunacidEntrance.chasm_to_surface]),
    RegionData(LunacidRegion.great_well_surface),
    RegionData(LunacidRegion.yosei_forest, [LunacidEntrance.yosei_to_yosei_lower, LunacidEntrance.yosei_to_canopy]),
    RegionData(LunacidRegion.forest_canopy),
    RegionData(LunacidRegion.yosei_lower, [LunacidEntrance.yosei_lower_to_tomb]),
    RegionData(LunacidRegion.sanguine_sea, [LunacidEntrance.sea_to_castle, LunacidEntrance.sea_to_tomb]),
    RegionData(LunacidRegion.accursed_tomb, [LunacidEntrance.tomb_to_mausoleum]),
    RegionData(LunacidRegion.mausoleum),
    RegionData(LunacidRegion.castle_le_fanu, [LunacidEntrance.castle_to_red, LunacidEntrance.castle_to_white, LunacidEntrance.castle_to_battleground]),
    RegionData(LunacidRegion.castle_le_fanu_red),
    RegionData(LunacidRegion.holy_battleground),
    RegionData(LunacidRegion.castle_le_fanu_white, [LunacidEntrance.white_to_blue, LunacidEntrance.white_to_throne]),
    RegionData(LunacidRegion.castle_le_fanu_blue, [LunacidEntrance.castle_to_grotto, LunacidEntrance.castle_to_ballroom]),
    RegionData(LunacidRegion.sealed_ballroom),
    RegionData(LunacidRegion.boiling_grotto, [LunacidEntrance.grotto_to_tower, LunacidEntrance.grotto_to_sand]),
    RegionData(LunacidRegion.tower_abyss),
    RegionData(LunacidRegion.sand_temple),
    RegionData(LunacidRegion.throne_chamber, [LunacidEntrance.throne_to_prison]),
    RegionData(LunacidRegion.terminus_prison, [LunacidEntrance.prison_to_prison_dark]),
    RegionData(LunacidRegion.terminus_prison_dark, [LunacidEntrance.prison_to_ash, LunacidEntrance.prison_to_arena]),
    RegionData(LunacidRegion.labyrinth_of_ash),
    RegionData(LunacidRegion.forlorn_arena, [LunacidEntrance.arena_to_fate]),
    RegionData(LunacidRegion.chamber_of_fate, [LunacidEntrance.fate_to_sleeper]),
    RegionData(LunacidRegion.grave_of_the_sleeper),
]

lunacid_entrances = [
    ConnectionData(LunacidEntrance.menu_to_basin, LunacidRegion.hollow_basin),
    ConnectionData(LunacidEntrance.to_wings_rest, LunacidRegion.wings_rest),
    ConnectionData(LunacidEntrance.sheryl, LunacidRegion.sheryl_the_crow),
    ConnectionData(LunacidEntrance.basin_to_archives, LunacidRegion.forbidden_archives),
    ConnectionData(LunacidEntrance.basin_to_surface, LunacidRegion.great_well_surface),
    ConnectionData(LunacidEntrance.basin_to_temple, LunacidRegion.temple_of_silence),
    ConnectionData(LunacidEntrance.temple_to_mire, LunacidRegion.fetid_mire),
    ConnectionData(LunacidEntrance.temple_to_forest, LunacidRegion.yosei_forest),
    ConnectionData(LunacidEntrance.wings_to_surface, LunacidRegion.great_well_surface),
    ConnectionData(LunacidEntrance.mire_to_sea, LunacidRegion.sanguine_sea),
    ConnectionData(LunacidEntrance.archives_to_chasm, LunacidRegion.laetus_chasm),
    ConnectionData(LunacidEntrance.chasm_to_surface, LunacidRegion.great_well_surface),
    ConnectionData(LunacidEntrance.yosei_to_canopy, LunacidRegion.forest_canopy),
    ConnectionData(LunacidEntrance.yosei_to_yosei_lower, LunacidRegion.yosei_lower),
    ConnectionData(LunacidEntrance.yosei_lower_to_tomb, LunacidRegion.accursed_tomb),
    ConnectionData(LunacidEntrance.sea_to_castle, LunacidRegion.castle_le_fanu),
    ConnectionData(LunacidEntrance.sea_to_tomb, LunacidRegion.accursed_tomb),
    ConnectionData(LunacidEntrance.tomb_to_mausoleum, LunacidRegion.mausoleum),
    ConnectionData(LunacidEntrance.castle_to_red, LunacidRegion.castle_le_fanu_red),
    ConnectionData(LunacidEntrance.castle_to_white, LunacidRegion.castle_le_fanu_white),
    ConnectionData(LunacidEntrance.castle_to_battleground, LunacidRegion.holy_battleground),
    ConnectionData(LunacidEntrance.white_to_throne, LunacidRegion.throne_chamber),
    ConnectionData(LunacidEntrance.white_to_blue, LunacidRegion.castle_le_fanu_blue),
    ConnectionData(LunacidEntrance.castle_to_ballroom, LunacidRegion.sealed_ballroom),
    ConnectionData(LunacidEntrance.castle_to_grotto, LunacidRegion.boiling_grotto),
    ConnectionData(LunacidEntrance.grotto_to_tower, LunacidRegion.tower_abyss),
    ConnectionData(LunacidEntrance.throne_to_prison, LunacidRegion.terminus_prison),
    ConnectionData(LunacidEntrance.prison_to_arena, LunacidRegion.forlorn_arena),
    ConnectionData(LunacidEntrance.prison_to_ash, LunacidRegion.labyrinth_of_ash),
    ConnectionData(LunacidEntrance.arena_to_fate, LunacidRegion.chamber_of_fate),
    ConnectionData(LunacidEntrance.fate_to_sleeper, LunacidRegion.grave_of_the_sleeper),
    ConnectionData(LunacidEntrance.grotto_to_sand, LunacidRegion.sand_temple),
    ConnectionData(LunacidEntrance.prison_to_prison_dark, LunacidRegion.terminus_prison_dark)
]


def create_regions(region_factory: RegionFactory) -> Dict[str, Region]:
    final_regions = lunacid_regions
    regions: Dict[str: LunacidRegion] = {region.name: region_factory(region.name, region.exits) for region in final_regions}
    entrances: Dict[str: LunacidEntrance] = {entrance.name: entrance for region in regions.values() for entrance in region.exits}

    connections = lunacid_entrances
    for connection in connections:
        if connection.name in entrances:
            entrances[connection.name].connect(regions[connection.destination])
    return regions

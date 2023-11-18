from worlds.lunacid.strings.regions_entrances import Region, Entrance
from .RegionClasses import RegionData

lunacid_regions = [
    RegionData(Region.menu, [Entrance.menu_to_basin]),
    RegionData(Region.hollow_basin, [Entrance.to_wings_rest, Entrance.basin_to_archives, Entrance.basin_to_surface, Entrance.basin_to_mire]),
    RegionData(Region.wings_rest, [Entrance.wings_to_surface]),
    RegionData(Region.fetid_mire, [Entrance.mire_to_sea]),
    RegionData(Region.forbidden_archives, [Entrance.archives_to_chasm]),
    RegionData(Region.laetus_chasm, [Entrance.chasm_to_surface]),
    RegionData(Region.great_well_surface),
    RegionData(Region.yosei_forest, [Entrance.yosei_to_tomb, Entrance.yosei_to_canopy]),
    RegionData(Region.forest_canopy),
    RegionData(Region.sanguine_sea, [Entrance.sea_to_castle, Entrance.sea_to_tomb]),

]

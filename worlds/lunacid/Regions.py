from BaseClasses import MultiWorld

from worlds.lunacid.strings.regions_entrances import LunacidRegion, LunacidEntrance


def link_lunacid_areas(world: MultiWorld, player: int):
    for (entrance, region) in lunacid_entrances:
        world.get_entrance(entrance, player).connect(world.get_region(region, player))


lunacid_regions = [
    (LunacidRegion.menu, [LunacidEntrance.menu_to_basin]),
    (LunacidRegion.hollow_basin, [LunacidEntrance.to_wings_rest, LunacidEntrance.basin_to_archives, LunacidEntrance.basin_to_surface,
                                  LunacidEntrance.basin_to_temple]),
    (LunacidRegion.temple_of_silence, [LunacidEntrance.temple_to_mire, LunacidEntrance.temple_to_forest]),
    (LunacidRegion.wings_rest, [LunacidEntrance.wings_to_surface, LunacidEntrance.sheryl]),
    (LunacidRegion.sheryl_the_crow, []),
    (LunacidRegion.fetid_mire, [LunacidEntrance.mire_to_sea]),
    (LunacidRegion.forbidden_archives, [LunacidEntrance.archives_to_chasm, LunacidEntrance.archives_to_daedalus]),
    (LunacidRegion.daedalus, []),
    (LunacidRegion.laetus_chasm, [LunacidEntrance.chasm_to_surface]),
    (LunacidRegion.great_well_surface, []),
    (LunacidRegion.yosei_forest, [LunacidEntrance.yosei_to_yosei_lower, LunacidEntrance.yosei_to_canopy]),
    (LunacidRegion.forest_canopy, []),
    (LunacidRegion.yosei_lower, [LunacidEntrance.yosei_lower_to_tomb, LunacidEntrance.yosei_lower_to_patchouli]),
    (LunacidRegion.patchouli, []),
    (LunacidRegion.sanguine_sea, [LunacidEntrance.sea_to_castle, LunacidEntrance.sea_to_tomb]),
    (LunacidRegion.accursed_tomb, [LunacidEntrance.tomb_to_mausoleum]),
    (LunacidRegion.mausoleum, []),
    (LunacidRegion.castle_le_fanu, [LunacidEntrance.castle_to_red, LunacidEntrance.castle_to_white, LunacidEntrance.castle_to_battleground]),
    (LunacidRegion.castle_le_fanu_red, []),
    (LunacidRegion.holy_battleground, []),
    (LunacidRegion.castle_le_fanu_white, [LunacidEntrance.white_to_blue, LunacidEntrance.white_to_throne]),
    (LunacidRegion.castle_le_fanu_blue, [LunacidEntrance.castle_to_grotto, LunacidEntrance.castle_to_ballroom]),
    (LunacidRegion.sealed_ballroom, []),
    (LunacidRegion.boiling_grotto, [LunacidEntrance.grotto_to_tower, LunacidEntrance.grotto_to_sand]),
    (LunacidRegion.tower_abyss, []),
    (LunacidRegion.sand_temple, []),
    (LunacidRegion.throne_chamber, [LunacidEntrance.throne_to_prison]),
    (LunacidRegion.terminus_prison, [LunacidEntrance.prison_to_prison_dark]),
    (LunacidRegion.terminus_prison_dark, [LunacidEntrance.prison_to_ash, LunacidEntrance.prison_to_arena]),
    (LunacidRegion.labyrinth_of_ash, []),
    (LunacidRegion.forlorn_arena, [LunacidEntrance.arena_to_fate]),
    (LunacidRegion.chamber_of_fate, [LunacidEntrance.fate_to_sleeper]),
    (LunacidRegion.grave_of_the_sleeper, []),
]

lunacid_entrances = [
    (LunacidEntrance.menu_to_basin, LunacidRegion.hollow_basin),
    (LunacidEntrance.to_wings_rest, LunacidRegion.wings_rest),
    (LunacidEntrance.sheryl, LunacidRegion.sheryl_the_crow),
    (LunacidEntrance.basin_to_archives, LunacidRegion.forbidden_archives),
    (LunacidEntrance.basin_to_surface, LunacidRegion.great_well_surface),
    (LunacidEntrance.basin_to_temple, LunacidRegion.temple_of_silence),
    (LunacidEntrance.temple_to_mire, LunacidRegion.fetid_mire),
    (LunacidEntrance.temple_to_forest, LunacidRegion.yosei_forest),
    (LunacidEntrance.wings_to_surface, LunacidRegion.great_well_surface),
    (LunacidEntrance.mire_to_sea, LunacidRegion.sanguine_sea),
    (LunacidEntrance.archives_to_chasm, LunacidRegion.laetus_chasm),
    (LunacidEntrance.archives_to_daedalus, LunacidRegion.daedalus),
    (LunacidEntrance.chasm_to_surface, LunacidRegion.great_well_surface),
    (LunacidEntrance.yosei_to_canopy, LunacidRegion.forest_canopy),
    (LunacidEntrance.yosei_to_yosei_lower, LunacidRegion.yosei_lower),
    (LunacidEntrance.yosei_lower_to_tomb, LunacidRegion.accursed_tomb),
    (LunacidEntrance.sea_to_castle, LunacidRegion.castle_le_fanu),
    (LunacidEntrance.sea_to_tomb, LunacidRegion.accursed_tomb),
    (LunacidEntrance.tomb_to_mausoleum, LunacidRegion.mausoleum),
    (LunacidEntrance.castle_to_red, LunacidRegion.castle_le_fanu_red),
    (LunacidEntrance.castle_to_white, LunacidRegion.castle_le_fanu_white),
    (LunacidEntrance.castle_to_battleground, LunacidRegion.holy_battleground),
    (LunacidEntrance.white_to_throne, LunacidRegion.throne_chamber),
    (LunacidEntrance.white_to_blue, LunacidRegion.castle_le_fanu_blue),
    (LunacidEntrance.castle_to_ballroom, LunacidRegion.sealed_ballroom),
    (LunacidEntrance.castle_to_grotto, LunacidRegion.boiling_grotto),
    (LunacidEntrance.grotto_to_tower, LunacidRegion.tower_abyss),
    (LunacidEntrance.throne_to_prison, LunacidRegion.terminus_prison),
    (LunacidEntrance.prison_to_arena, LunacidRegion.forlorn_arena),
    (LunacidEntrance.prison_to_ash, LunacidRegion.labyrinth_of_ash),
    (LunacidEntrance.arena_to_fate, LunacidRegion.chamber_of_fate),
    (LunacidEntrance.fate_to_sleeper, LunacidRegion.grave_of_the_sleeper),
    (LunacidEntrance.grotto_to_sand, LunacidRegion.sand_temple),
    (LunacidEntrance.prison_to_prison_dark, LunacidRegion.terminus_prison_dark),
    (LunacidEntrance.yosei_lower_to_patchouli, LunacidRegion.patchouli)
]

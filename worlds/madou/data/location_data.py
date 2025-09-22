from dataclasses import dataclass
from typing import Optional, Tuple, Dict

from worlds.madou.strings.locations import Spell, MagicTown, School, BuildingBlockMaze, ForestOfLight, LookoutMountain, LightGarden, HarpyPath, AncientRuins, DarkForest, \
    SatanVilla, AncientVillage, SageMountain, Bazaar, DragonAreas, FlightSpots, Bestiary, ShadyWell, Shop
from worlds.madou.strings.region_entrances import MadouRegion


@dataclass(frozen=True)
class MadouLocation:
    location_id: Optional[int]
    name: str
    region: str
    hex_address: int
    value: int


all_locations = []
hex_by_location: Dict[int, Tuple[int, int]] = {}


def create_location(location_id: Optional[int], name: str, region: str, hex_address: int, value: int):
    location = MadouLocation(location_id, name, region, hex_address, value)
    if location_id is not None:
        all_locations.append(location)
    hex_by_location[location_id] = (hex_address, value)
    return location


#  The address should just be a part of the intro that we skip.
starting_spell_location_start = 0
starting_spell_locations = [
    create_location(starting_spell_location_start + 1, Spell.healing_start, MadouRegion.arle_house, 0x001379, 0x01),
    create_location(starting_spell_location_start + 2, Spell.fire_start, MadouRegion.arle_house, 0x001379, 0x01),
    create_location(starting_spell_location_start + 3, Spell.ice_storm_start, MadouRegion.arle_house, 0x001379, 0x01),
    create_location(starting_spell_location_start + 4, Spell.thunder_start, MadouRegion.arle_house, 0x001379, 0x01),
]

spell_location_start = 10
spell_locations = [
    create_location(spell_location_start + 1, Spell.bayohihihiii, MadouRegion.library, 0x00137B, 0x08),
    create_location(spell_location_start + 2, Spell.braindumbed, MadouRegion.library, 0x00137B, 0x04),
    create_location(spell_location_start + 3, Spell.bayoen, MadouRegion.library, 0x00137B, 0x02),
    create_location(spell_location_start + 4, Spell.heedon, MadouRegion.death_valley, 0x001386, 0x08),
    create_location(spell_location_start + 5, Spell.jugem, MadouRegion.magic_village, 0x00138C, 0x04),
    create_location(spell_location_start + 6, Spell.revia, MadouRegion.smoky_cave_right, 0x00138c, 0x01),
    create_location(spell_location_start + 7, Spell.fire_school, MadouRegion.library, 0x00137b, 0x10),
    create_location(spell_location_start + 8, Spell.fire_northwestern, MadouRegion.northwest_cave, 0x001385, 0x04),
    create_location(spell_location_start + 9, Spell.fire_library, MadouRegion.library_secret, 0x00139c, 0x02),
    create_location(spell_location_start + 10, Spell.ice_storm_wolf, MadouRegion.wolf_town, 0x001385, 0x08),
    create_location(spell_location_start + 11, Spell.ice_storm_underground, MadouRegion.smoky_cave_left, 0x00137b, 0x20),
    create_location(spell_location_start + 12, Spell.ice_storm_library, MadouRegion.library_secret, 0x00139c, 0x04),
    create_location(spell_location_start + 13, Spell.thunder_northwestern, MadouRegion.northwest_cave, 0x00137b, 0x40),
    create_location(spell_location_start + 14, Spell.thunder_dark_forest, MadouRegion.dark_forest, 0x001385, 0x10),
    create_location(spell_location_start + 15, Spell.thunder_library, MadouRegion.library_secret, 0x00139c, 0x08),
    create_location(spell_location_start + 16, Spell.diacute_ruins, MadouRegion.ancient_ruins, 0x001386, 0x01),
    create_location(spell_location_start + 17, Spell.diacute_dark_forest, MadouRegion.dark_forest, 0x001386, 0x02),
    create_location(spell_location_start + 18, Spell.diacute_library, MadouRegion.library_secret, 0x00138c, 0x08),
    create_location(spell_location_start + 19, Spell.diacute_underground, MadouRegion.smoky_cave_left, 0x001386, 0x04),
    create_location(spell_location_start + 20, Spell.healing_ruins, MadouRegion.ruins_town, 0x001385, 0x20),
    create_location(spell_location_start + 21, Spell.healing_underground, MadouRegion.smoky_cave_left, 0x001385, 0x40),
    create_location(spell_location_start + 22, Spell.healing_temple, MadouRegion.dragon_temple, 0x001385, 0x80),
]

magic_village_start = 40
magic_village_locations = [
    create_location(magic_village_start + 1, MagicTown.magic_bracelet, MadouRegion.magic_village, 0x00137c, 0x80),
    create_location(magic_village_start + 2, MagicTown.white_gem, MadouRegion.arle_house, 0x001388, 0x02),
    create_location(magic_village_start + 3, MagicTown.suketoudara, MadouRegion.magic_village, 0x001386, 0x40),
    create_location(magic_village_start + 4, LookoutMountain.red_gem, MadouRegion.lookout_mountain, 0x001387, 0x08),
    create_location(magic_village_start + 5, LookoutMountain.carbuncle, MadouRegion.lookout_mountain, 0x001386, 0x20),
]

school_location_start = 50
school_locations = [
    # The address for dictionary is actually right before you talk to the headmaster about the dictionary.
    create_location(school_location_start + 1, School.magical_dictionary, MadouRegion.headmaster_office, 0x001388, 0x10),
    create_location(school_location_start + 2, School.mandrake_leaf, MadouRegion.school, 0x001383, 0x10),
    create_location(school_location_start + 3, BuildingBlockMaze.magic_crystal, MadouRegion.school_maze, 0x0013a7, 0x01),
    create_location(school_location_start + 4, BuildingBlockMaze.dragon_meat, MadouRegion.school_maze, 0x0013a7, 0x04),
    create_location(school_location_start + 5, BuildingBlockMaze.cotton_ball, MadouRegion.school_maze, 0x0013a7, 0x08),
    create_location(school_location_start + 6, BuildingBlockMaze.soy_veggies, MadouRegion.school_maze, 0x0013a7, 0x02),
]

light_forest_location_start = 60
light_forest_locations = [
    create_location(light_forest_location_start + 1, ForestOfLight.ribbit_boots, MadouRegion.frog_swamp, 0x00137c, 0x20),
    create_location(light_forest_location_start + 2, ForestOfLight.sukiyapodes_1, MadouRegion.frog_swamp, 0x00137c, 0x10),
    create_location(light_forest_location_start + 3, ForestOfLight.sukiyapodes_2, MadouRegion.forest_of_light, 0x00139d, 0x80),
    create_location(light_forest_location_start + 4, ForestOfLight.orb, MadouRegion.forest_of_light, 0x00137d, 0x10),
]

ruins_location_start = 70
ruins_locations = [
    create_location(ruins_location_start + 1, LightGarden.bouquet, MadouRegion.fairy_cove, 0x001382, 0x40),
    create_location(ruins_location_start + 2, LightGarden.purple_orb, MadouRegion.fairy_cove, 0x001387, 0x80),
    create_location(ruins_location_start + 3, HarpyPath.bag, MadouRegion.harpy_mountain, 0x00137e, 0x01),
    create_location(ruins_location_start + 4, AncientRuins.elephant_head, MadouRegion.ancient_ruins, 0x001379, 0x10),
    create_location(ruins_location_start + 5, AncientRuins.zoh_daimaoh, MadouRegion.zoh_daimaoh_room, 0x00137a, 0x20),
]

dark_forest_location_start = 80
dark_forest_locations = [
    create_location(dark_forest_location_start + 1, DarkForest.flute, MadouRegion.dark_orb_clearing, 0x00137d, 0x04),
    create_location(dark_forest_location_start + 2, DarkForest.dark_flower, MadouRegion.dark_forest, 0x001383, 0x08),
    create_location(dark_forest_location_start + 3, DarkForest.green_gem, MadouRegion.dark_forest, 0x001387, 0x20),
    create_location(dark_forest_location_start + 4, DarkForest.orb, MadouRegion.dark_orb_clearing, 0x00137d, 0x01),
    create_location(dark_forest_location_start + 5, DarkForest.rele, MadouRegion.dark_maze, 0x0013a4, 0x02),
    create_location(dark_forest_location_start + 6, DarkForest.ribbon, MadouRegion.dark_maze, 0x001389, 0x04),
    create_location(dark_forest_location_start + 7, SatanVilla.satan, MadouRegion.satan_mansion, 0x00137b, 0x80),
    create_location(dark_forest_location_start + 8, SageMountain.cyan_orb, MadouRegion.sage_mountain, 0x001388, 0x01),
]

well_location_start = 90
well_locations = [
    create_location(well_location_start + 1, ShadyWell.yellow_gem, MadouRegion.well, 0x001387, 0x40),  # 139d was set to 20 at the end.  Which one?
    create_location(well_location_start + 2, ShadyWell.lofu, MadouRegion.well, 0x0013a4, 0x04),
    create_location(well_location_start + 3, ShadyWell.ripe_cucumber, MadouRegion.well, 0x001380, 0x02),
    create_location(well_location_start + 4, ShadyWell.rotten_cucumber_1, MadouRegion.well, 0x001380, 0x40),
    create_location(well_location_start + 5, ShadyWell.rotten_cucumber_2, MadouRegion.well, 0x001381, 0x01),
    create_location(well_location_start + 6, ShadyWell.rotten_cucumber_3, MadouRegion.well, 0x001380, 0x01),
    create_location(well_location_start + 7, ShadyWell.rotten_cucumber_4, MadouRegion.well, 0x001380, 0x80),
    create_location(well_location_start + 8, ShadyWell.rotten_cucumber_5, MadouRegion.well, 0x001381, 0x02),
    create_location(well_location_start + 9, ShadyWell.rotten_cucumber_6, MadouRegion.well, 0x001381, 0x04),
    create_location(well_location_start + 10, ShadyWell.rotten_cucumber_7, MadouRegion.well, 0x001381, 0x08),
    create_location(well_location_start + 11, ShadyWell.rotten_cucumber_8, MadouRegion.well, 0x001381, 0x10),
    create_location(well_location_start + 12, ShadyWell.rotten_cucumber_9, MadouRegion.well, 0x001381, 0x20),
    create_location(well_location_start + 13, ShadyWell.arachne, MadouRegion.well, 0x001380, 0x20),
]

ancient_village_location_start = 110
ancient_village_locations = [
    create_location(ancient_village_location_start + 1, AncientVillage.villager_1, MadouRegion.ancient_village, 0x00138a, 0x01),
    create_location(ancient_village_location_start + 2, AncientVillage.villager_2, MadouRegion.ancient_village, 0x001389, 0x08),
    create_location(ancient_village_location_start + 3, AncientVillage.villager_3, MadouRegion.ancient_village, 0x001389, 0x80),
    create_location(ancient_village_location_start + 4, AncientVillage.villager_4, MadouRegion.ancient_village, 0x001389, 0x20),
    create_location(ancient_village_location_start + 5, AncientVillage.villager_5, MadouRegion.ancient_village, 0x001389, 0x10),
    create_location(ancient_village_location_start + 6, AncientVillage.villager_6, MadouRegion.ancient_village, 0x001389, 0x40),
    create_location(ancient_village_location_start + 7, AncientVillage.elder, MadouRegion.ancient_village, 0x00137f, 0x01),
]

bazaar_location_start = 120
bazaar_locations = [
    create_location(bazaar_location_start + 1, Bazaar.bazaar_pass, MadouRegion.bazaar, 0x001384, 0x10),
    create_location(bazaar_location_start + 2, Bazaar.elephant, MadouRegion.bazaar, 0x001384, 0x08),
    create_location(bazaar_location_start + 3, Bazaar.blue_gem, MadouRegion.bazaar, 0x001387, 0x10),
    create_location(bazaar_location_start + 4, Bazaar.firefly_egg, MadouRegion.bazaar, 0x001384, 0x40),
    create_location(bazaar_location_start + 5, DragonAreas.firefly_egg, MadouRegion.dragon_graveyard, 0x001382, 0x10),
    create_location(bazaar_location_start + 6, DragonAreas.stone, MadouRegion.dragon_temple, 0x001382, 0x02),
]

base_locations = (spell_locations + magic_village_locations + school_locations + ruins_locations + light_forest_locations +
                  dark_forest_locations + well_locations + ancient_village_locations + bazaar_locations)

#  For these hex addresses we don't need to scrub the  flip here, just read; mama does an inventory check, not a flag check.
souvenir_location_start = 130
souvenir_locations = [
    create_location(souvenir_location_start + 1, Shop.ruins_town_souvenir_1, MadouRegion.ruins_town, 0x0013A4, 0x10),
    create_location(souvenir_location_start + 2, Shop.ruins_town_souvenir_2, MadouRegion.ruins_town, 0x0013A4, 0x20),
    create_location(souvenir_location_start + 3, Shop.ruins_town_souvenir_3, MadouRegion.ruins_town, 0x0013A4, 0x40),
    create_location(souvenir_location_start + 4, Shop.ruins_town_souvenir_4, MadouRegion.ruins_town, 0x0013A4, 0x80),
    create_location(souvenir_location_start + 5, Shop.wolf_town_item_7, MadouRegion.wolf_town, 0x0013A5, 0x04),
    create_location(souvenir_location_start + 6, Shop.wolf_town_item_8, MadouRegion.wolf_town, 0x0013A5, 0x02),
    create_location(souvenir_location_start + 7, Shop.bazaar_item_7, MadouRegion.bazaar, 0x001384, 0x20),
    create_location(souvenir_location_start + 8, Shop.bazaar_item_8, MadouRegion.bazaar, 0x0013a5, 0x01)
]

#  The question is...what makes these calls?
flight_location_start = 140
flight_locations = [
    create_location(flight_location_start + 1, FlightSpots.ruins_flight, MadouRegion.ruins_town, 0x001392, 0x80),
    create_location(flight_location_start + 2, FlightSpots.wolf_flight, MadouRegion.wolf_town, 0x001392, 0x01),
    create_location(flight_location_start + 3, FlightSpots.ancient_flight, MadouRegion.ancient_village, 0x001392, 0x02),
    create_location(flight_location_start + 4, FlightSpots.sage_flight, MadouRegion.sage_mountain, 0x001392, 0x04),
    create_location(flight_location_start + 5, FlightSpots.magic_flight, MadouRegion.magic_village, 0x001392, 0x40)
]

# The values assigned to the address are just what page its on.  If its bigger than zero its been added.
bestiary_location_start = 150
bestiary_locations = [
    create_location(bestiary_location_start + 1, Bestiary.green_puyo, MadouRegion.forest_of_light, 0x0014A9, 0x00),
    create_location(bestiary_location_start + 2, Bestiary.cait_sith, MadouRegion.forest_of_light, 0x0014C8, 0x00),
    create_location(bestiary_location_start + 3, Bestiary.sukiyapodes, MadouRegion.frog_swamp, 0x0014A8, 0x00),
    create_location(bestiary_location_start + 4, Bestiary.mini_zombie, MadouRegion.magic_village, 0x0014BA, 0x00),
    create_location(bestiary_location_start + 5, Bestiary.mummy, MadouRegion.ancient_ruins, 0x0014C2, 0x00),
    create_location(bestiary_location_start + 6, Bestiary.zombie, MadouRegion.ancient_ruins, 0x0014B4, 0x00),
    create_location(bestiary_location_start + 7, Bestiary.zoh, MadouRegion.zoh_daimaoh_room, 0x0014BE, 0x00),
    create_location(bestiary_location_start + 8, Bestiary.red_puyo, MadouRegion.dark_forest, 0x0014AA, 0x00),
    create_location(bestiary_location_start + 9, Bestiary.draco, MadouRegion.dark_forest, 0x0014B0, 0x00),
    create_location(bestiary_location_start + 10, Bestiary.mellow, MadouRegion.well, 0x0014B6, 0x00),
    create_location(bestiary_location_start + 11, Bestiary.blue_puyo, MadouRegion.well, 0x0014AB, 0x00),
    create_location(bestiary_location_start + 12, Bestiary.arachne, MadouRegion.well, 0x0014bd, 0x00),
    create_location(bestiary_location_start + 13, Bestiary.fakebuncle, MadouRegion.school_maze, 0x0014b3, 0x00),
    create_location(bestiary_location_start + 14, Bestiary.yellow_puyo, MadouRegion.school_maze, 0x0014ad, 0x00),
    create_location(bestiary_location_start + 15, Bestiary.headmaster, MadouRegion.school_maze, 0x0014c7, 0x00),
    create_location(bestiary_location_start + 16, Bestiary.banshee, MadouRegion.smoky_cave_left, 0x0014c5, 0x00),
    create_location(bestiary_location_start + 17, Bestiary.will_o_wisp, MadouRegion.smoky_cave_left, 0x0014b5, 0x00),
    create_location(bestiary_location_start + 18, Bestiary.baromet, MadouRegion.dark_maze, 0x0014b7, 0x00),
    create_location(bestiary_location_start + 19, Bestiary.purple_puyo, MadouRegion.dark_maze, 0x0014ac, 0x00),
    create_location(bestiary_location_start + 20, Bestiary.nasu_grave, MadouRegion.dark_maze, 0x0014b9, 0x00),
    create_location(bestiary_location_start + 21, Bestiary.wood_man, MadouRegion.ancient_village, 0x0014c1, 0x00),
    create_location(bestiary_location_start + 22, Bestiary.skeleton_d, MadouRegion.ancient_village, 0x0014bc, 0x00),
    create_location(bestiary_location_start + 23, Bestiary.witch, MadouRegion.sage_mountain, 0x0014b8, 0x00),
    create_location(bestiary_location_start + 24, Bestiary.scylla, MadouRegion.sage_mountain, 0x0014c3, 0x00),
    create_location(bestiary_location_start + 25, Bestiary.wraith, MadouRegion.harpy_mountain, 0x0014c0, 0x00),
    create_location(bestiary_location_start + 26, Bestiary.dullahan, MadouRegion.harpy_mountain, 0x0014c4, 0x00),
    create_location(bestiary_location_start + 27, Bestiary.harpy, MadouRegion.harpy_mountain, 0x0014ae, 0x00),
    create_location(bestiary_location_start + 28, Bestiary.flea, MadouRegion.fairy_cove, 0x0014cb, 0x00),
    create_location(bestiary_location_start + 29, Bestiary.skeleton_t, MadouRegion.dragon_graveyard, 0x0014bb, 0x00),
    create_location(bestiary_location_start + 30, Bestiary.leviathan, MadouRegion.dragon_temple, 0x0014bf, 0x00),
    create_location(bestiary_location_start + 31, Bestiary.owlbear, MadouRegion.dark_forest, 0x0014af, 0x00),
    create_location(bestiary_location_start + 32, Bestiary.devil, MadouRegion.headmaster_office, 0x0014c9, 0x00),
    create_location(bestiary_location_start + 33, Bestiary.giant_puyo, MadouRegion.magical_tower, 0x0014c6, 0x00),
]

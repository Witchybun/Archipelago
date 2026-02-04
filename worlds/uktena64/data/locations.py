from dataclasses import dataclass
from typing import Optional

from worlds.uktena64.strings.items import BaseItem, PhotoItem, MeatItem, JebItem, JeebItem
from worlds.uktena64.strings.locations import JebCabin, TurkeyCreek, FrigidValley, HowlingMarsh, BleedingGrove, JebLore, CabinCamera, TurkeyCamera, \
    FrigidCamera, HowlingCamera, BleedingCamera, TheBBQBasket, RitualRoad, LakeLinger, PallidPark, BurningGrove, JeebLore, BBQMeat, RitualMeat, \
    LakeMeat, PallidMeat, BurningMeat, Hyena
from worlds.uktena64.strings.regions import BaseRegion, JebRegion, JeebRegion


@dataclass(frozen=True)
class UktenaLocation:
    location_id: int
    name: str
    region: str
    forced_item: str


all_locations = []


# Some locations vary on multiple regions, so we default to Hollow Basin first.
def create_location(location_id: int, name: str, region: Optional[str] = BaseRegion.menu, forced_item: Optional[str] = BaseItem.nothing):
    location = UktenaLocation(location_id, name, region, forced_item)
    if location_id is not None:
        all_locations.append(location)
    return location


jeb_base_locations = [
    create_location(1, JebCabin.knife, JebRegion.cabin),
    create_location(2, JebCabin.camera, JebRegion.cabin, JebItem.camera),
    create_location(3, JebCabin.rifle, JebRegion.cabin),
    create_location(4, JebCabin.coffee, JebRegion.cabin),
    create_location(5, JebCabin.ammo, JebRegion.cabin),
    create_location(6, JebCabin.clear, JebRegion.cabin),

    create_location(7, TurkeyCreek.turkey_call, JebRegion.turkey),
    create_location(8, TurkeyCreek.hen_ammo, JebRegion.turkey),
    create_location(9, TurkeyCreek.hen_coffee, JebRegion.turkey),
    create_location(10, TurkeyCreek.house_ammo, JebRegion.turkey),
    create_location(11, TurkeyCreek.dark_spot_ammo, JebRegion.turkey),
    create_location(12, TurkeyCreek.house_coffee, JebRegion.turkey),
    create_location(13, TurkeyCreek.rock_coffee, JebRegion.turkey),
    create_location(14, TurkeyCreek.clear, JebRegion.turkey),

    create_location(15, FrigidValley.shack_ammo, JebRegion.frigid),
    create_location(16, FrigidValley.truck, JebRegion.frigid),
    create_location(17, FrigidValley.path_ammo, JebRegion.frigid),
    create_location(18, FrigidValley.second_ammo, JebRegion.frigid),
    create_location(19, FrigidValley.trailer_coffee, JebRegion.frigid),
    create_location(20, FrigidValley.trailer_ammo, JebRegion.frigid),
    create_location(21, FrigidValley.trailer_barrel_ammo, JebRegion.frigid),
    create_location(22, FrigidValley.trailer_tv_coffee, JebRegion.frigid),
    create_location(23, FrigidValley.final_shack_coffee, JebRegion.frigid),
    create_location(24, FrigidValley.final_shack_ammo, JebRegion.frigid),
    create_location(25, FrigidValley.late_path_ammo, JebRegion.frigid),
    create_location(26, FrigidValley.clear, JebRegion.frigid),

    create_location(27, HowlingMarsh.revolver, JebRegion.howling),
    create_location(28, HowlingMarsh.house_coffee, JebRegion.howling),
    create_location(29, HowlingMarsh.house_ammo, JebRegion.howling),
    create_location(30, HowlingMarsh.fence_house_ammo_1, JebRegion.howling),
    create_location(31, HowlingMarsh.fence_house_ammo_2, JebRegion.howling),
    create_location(32, HowlingMarsh.church_key, JebRegion.howling),
    create_location(33, HowlingMarsh.graveyard_ammo, JebRegion.howling),
    create_location(34, HowlingMarsh.greenhouse_ammo_1, JebRegion.howling),
    create_location(35, HowlingMarsh.greenhouse_ammo_2, JebRegion.howling),
    create_location(36, HowlingMarsh.trailer_coffee, JebRegion.howling),
    create_location(37, HowlingMarsh.clear, JebRegion.howling),

    create_location(38, BleedingGrove.bren, JebRegion.bleeding),
    create_location(39, BleedingGrove.clear, JebRegion.howling),
]

jeb_lore_code = 50
jeb_lore_locations = [
    create_location(jeb_lore_code + 1, JebLore.guide, JebRegion.cabin),
    create_location(jeb_lore_code + 2, JebLore.cdc, JebRegion.cabin),
    create_location(jeb_lore_code + 3, JebLore.hero_of_horned_snake, JebRegion.turkey),
    create_location(jeb_lore_code + 4, JebLore.ate_fish, JebRegion.turkey),
    create_location(jeb_lore_code + 5, JebLore.starved_chickens, JebRegion.turkey),
    create_location(jeb_lore_code + 6, JebLore.newfound_god, JebRegion.turkey),
    create_location(jeb_lore_code + 7, JebLore.the_turkeys, JebRegion.turkey),
    create_location(jeb_lore_code + 8, JebLore.the_uktena_1, JebRegion.frigid),
    create_location(jeb_lore_code + 9, JebLore.the_uktena_2, JebRegion.frigid),
    create_location(jeb_lore_code + 10, JebLore.loud_sound, JebRegion.frigid),
    create_location(jeb_lore_code + 11, JebLore.ringing, JebRegion.frigid),
    create_location(jeb_lore_code + 12, JebLore.nightmare, JebRegion.frigid),
    create_location(jeb_lore_code + 13, JebLore.church_note, JebRegion.howling),
    create_location(jeb_lore_code + 14, JebLore.trailer_day_1, JebRegion.howling),
    create_location(jeb_lore_code + 15, JebLore.trailer_day_5, JebRegion.howling),
    create_location(jeb_lore_code + 16, JebLore.more_than_one, JebRegion.bleeding),
    create_location(jeb_lore_code + 17, JebLore.the_uktena_3, JebRegion.bleeding),
    create_location(jeb_lore_code + 18, JebLore.the_hunger, JebRegion.bleeding),
    create_location(jeb_lore_code + 19, JebLore.no_food, JebRegion.bleeding),
]

jeb_photo_code = 80
jeb_photo_locations = [
    create_location(jeb_photo_code + 1, CabinCamera.squirrel, JebRegion.cabin, PhotoItem.cabin),

    create_location(jeb_photo_code + 2, TurkeyCamera.turkey_1, JebRegion.turkey, PhotoItem.turkey),
    create_location(jeb_photo_code + 3, TurkeyCamera.dark_linked_turkey_1, JebRegion.turkey, PhotoItem.turkey),
    create_location(jeb_photo_code + 4, TurkeyCamera.dark_linked_turkey_2, JebRegion.turkey, PhotoItem.turkey),
    create_location(jeb_photo_code + 5, TurkeyCamera.dark_linked_turkey_3, JebRegion.turkey, PhotoItem.turkey),
    create_location(jeb_photo_code + 6, TurkeyCamera.rock_linked_turkey_1, JebRegion.turkey, PhotoItem.turkey),
    create_location(jeb_photo_code + 7, TurkeyCamera.rock_linked_turkey_2, JebRegion.turkey, PhotoItem.turkey),
    create_location(jeb_photo_code + 8, TurkeyCamera.rock_linked_turkey_3, JebRegion.turkey, PhotoItem.turkey),
    create_location(jeb_photo_code + 9, TurkeyCamera.creek_dead_body, JebRegion.turkey, PhotoItem.turkey),
    create_location(jeb_photo_code + 10, TurkeyCamera.house_linked_turkey_1, JebRegion.turkey, PhotoItem.turkey),
    create_location(jeb_photo_code + 11, TurkeyCamera.house_linked_turkey_2, JebRegion.turkey, PhotoItem.turkey),
    create_location(jeb_photo_code + 12, TurkeyCamera.house_linked_turkey_3, JebRegion.turkey, PhotoItem.turkey),
    create_location(jeb_photo_code + 13, TurkeyCamera.turkey_3, JebRegion.turkey, PhotoItem.turkey),
    create_location(jeb_photo_code + 14, TurkeyCamera.headless_turkey, JebRegion.turkey, PhotoItem.turkey),

    create_location(jeb_photo_code + 15, FrigidCamera.early_wolf_1, JebRegion.frigid, PhotoItem.frigid_valley),
    create_location(jeb_photo_code + 16, FrigidCamera.early_wolf_2, JebRegion.frigid, PhotoItem.frigid_valley),
    create_location(jeb_photo_code + 17, FrigidCamera.early_wolf_3, JebRegion.frigid, PhotoItem.frigid_valley),
    create_location(jeb_photo_code + 18, FrigidCamera.second_wolf_1, JebRegion.frigid, PhotoItem.frigid_valley),
    create_location(jeb_photo_code + 19, FrigidCamera.second_wolf_2, JebRegion.frigid, PhotoItem.frigid_valley),
    create_location(jeb_photo_code + 20, FrigidCamera.second_wolf_3, JebRegion.frigid, PhotoItem.frigid_valley),
    create_location(jeb_photo_code + 21, FrigidCamera.second_wolf_4, JebRegion.frigid, PhotoItem.frigid_valley),
    create_location(jeb_photo_code + 22, FrigidCamera.open_wolf_1, JebRegion.frigid, PhotoItem.frigid_valley),
    create_location(jeb_photo_code + 23, FrigidCamera.open_wolf_2, JebRegion.frigid, PhotoItem.frigid_valley),
    create_location(jeb_photo_code + 24, FrigidCamera.circle_meat, JebRegion.frigid, PhotoItem.frigid_valley),
    create_location(jeb_photo_code + 25, FrigidCamera.trailer_dog, JebRegion.frigid, PhotoItem.frigid_valley),
    create_location(jeb_photo_code + 26, FrigidCamera.tree_dog_1, JebRegion.frigid, PhotoItem.frigid_valley),
    create_location(jeb_photo_code + 27, FrigidCamera.tree_dog_2, JebRegion.frigid, PhotoItem.frigid_valley),
    create_location(jeb_photo_code + 28, FrigidCamera.elk, JebRegion.frigid, PhotoItem.frigid_valley),
    create_location(jeb_photo_code + 29, FrigidCamera.skinned_return_1, JebRegion.frigid),
    create_location(jeb_photo_code + 30, FrigidCamera.skinned_return_2, JebRegion.frigid),
    create_location(jeb_photo_code + 31, FrigidCamera.skinned_return_3, JebRegion.frigid),
    create_location(jeb_photo_code + 32, FrigidCamera.skinned_return_4, JebRegion.frigid),
    create_location(jeb_photo_code + 33, FrigidCamera.skinned_return_5, JebRegion.frigid),
    create_location(jeb_photo_code + 34, FrigidCamera.skinned_return_6, JebRegion.frigid),
    create_location(jeb_photo_code + 35, FrigidCamera.skinned_return_7, JebRegion.frigid),
    create_location(jeb_photo_code + 36, FrigidCamera.snowman_skull, JebRegion.frigid),
    create_location(jeb_photo_code + 37, FrigidCamera.mountain_wolf, JebRegion.frigid),

    create_location(jeb_photo_code + 38, HowlingCamera.bear_1, JebRegion.howling, PhotoItem.howling_marsh),
    create_location(jeb_photo_code + 39, HowlingCamera.bear_2, JebRegion.howling, PhotoItem.howling_marsh),
    create_location(jeb_photo_code + 40, HowlingCamera.bear_3, JebRegion.howling, PhotoItem.howling_marsh),
    create_location(jeb_photo_code + 41, HowlingCamera.bear_4, JebRegion.howling, PhotoItem.howling_marsh),
    create_location(jeb_photo_code + 42, HowlingCamera.burned_corpses_1, JebRegion.howling, PhotoItem.howling_marsh),
    create_location(jeb_photo_code + 43, HowlingCamera.burned_corpses_2, JebRegion.howling, PhotoItem.howling_marsh),
    create_location(jeb_photo_code + 44, HowlingCamera.burned_corpses_3, JebRegion.howling, PhotoItem.howling_marsh),
    create_location(jeb_photo_code + 45, HowlingCamera.burned_corpses_4, JebRegion.howling, PhotoItem.howling_marsh),
    create_location(jeb_photo_code + 46, HowlingCamera.burned_corpses_5, JebRegion.howling, PhotoItem.howling_marsh),
    create_location(jeb_photo_code + 47, HowlingCamera.burned_corpses_6, JebRegion.howling, PhotoItem.howling_marsh),
    create_location(jeb_photo_code + 48, HowlingCamera.huge_bear, JebRegion.howling, PhotoItem.howling_marsh),

    create_location(jeb_photo_code + 49, BleedingCamera.starved, JebRegion.bleeding, PhotoItem.bleeding_grove),
]

jeeb_base_code = 150
jeeb_base_locations = [
    create_location(jeeb_base_code + 1, TheBBQBasket.butcher_knives, JeebRegion.bbq, JeebItem.butcher_knives),
    create_location(jeeb_base_code + 2, TheBBQBasket.binoculars, JeebRegion.bbq),
    create_location(jeeb_base_code + 3, TheBBQBasket.ruger, JeebRegion.bbq),
    create_location(jeeb_base_code + 4, TheBBQBasket.coffee, JeebRegion.bbq),
    create_location(jeeb_base_code + 5, TheBBQBasket.clear, JeebRegion.bbq),

    create_location(jeeb_base_code + 6, RitualRoad.bridge_ammo, JeebRegion.ritual),
    create_location(jeeb_base_code + 7, RitualRoad.outside_venereal_ammo, JeebRegion.ritual),
    create_location(jeeb_base_code + 8, RitualRoad.venereal_coffee, JeebRegion.ritual),
    create_location(jeeb_base_code + 9, RitualRoad.venereal_ammo, JeebRegion.ritual),
    create_location(jeeb_base_code + 10, RitualRoad.truck_ammo, JeebRegion.ritual),
    create_location(jeeb_base_code + 11, RitualRoad.tent_coffee, JeebRegion.ritual),
    create_location(jeeb_base_code + 12, RitualRoad.clear, JeebRegion.ritual),

    create_location(jeeb_base_code + 13, LakeLinger.starting_ammo, JeebRegion.lake),
    create_location(jeeb_base_code + 14, LakeLinger.boat_house_coffee, JeebRegion.lake),
    create_location(jeeb_base_code + 15, LakeLinger.island_coffee, JeebRegion.lake),
    create_location(jeeb_base_code + 16, LakeLinger.island_ammo, JeebRegion.lake),
    create_location(jeeb_base_code + 17, LakeLinger.dead_end_ammo, JeebRegion.lake),
    create_location(jeeb_base_code + 18, LakeLinger.two_story_coffee, JeebRegion.lake),
    create_location(jeeb_base_code + 19, LakeLinger.main_office_ammo, JeebRegion.lake),
    create_location(jeeb_base_code + 20, LakeLinger.main_office_trap, JeebRegion.lake),
    create_location(jeeb_base_code + 21, LakeLinger.north_house_trap, JeebRegion.lake),
    create_location(jeeb_base_code + 22, LakeLinger.coffee_trap_trap_1, JeebRegion.lake),
    create_location(jeeb_base_code + 23, LakeLinger.coffee_trap_trap_2, JeebRegion.lake),
    create_location(jeeb_base_code + 24, LakeLinger.coffee_trap_trap_3, JeebRegion.lake),
    create_location(jeeb_base_code + 25, LakeLinger.coffee_trap_coffee, JeebRegion.lake),
    create_location(jeeb_base_code + 26, LakeLinger.dam_ammo_1, JeebRegion.lake),
    create_location(jeeb_base_code + 27, LakeLinger.dam_ammo_2, JeebRegion.lake),
    create_location(jeeb_base_code + 28, LakeLinger.trapped_start_trap_1, JeebRegion.lake),
    create_location(jeeb_base_code + 29, LakeLinger.trapped_start_trap_2, JeebRegion.lake),
    create_location(jeeb_base_code + 30, LakeLinger.trapped_start_trap_3, JeebRegion.lake),
    create_location(jeeb_base_code + 31, LakeLinger.trapped_start_trap_4, JeebRegion.lake),
    create_location(jeeb_base_code + 32, LakeLinger.trapped_start_trap_5, JeebRegion.lake),
    create_location(jeeb_base_code + 33, LakeLinger.trapped_start_trap_6, JeebRegion.lake),
    create_location(jeeb_base_code + 34, LakeLinger.trapped_start_trap_7, JeebRegion.lake),
    create_location(jeeb_base_code + 35, LakeLinger.clear, JeebRegion.lake),

    create_location(jeeb_base_code + 36, PallidPark.chamber_ammo, JeebRegion.pallid),
    create_location(jeeb_base_code + 37, PallidPark.owner_ammo, JeebRegion.pallid),
    create_location(jeeb_base_code + 38, PallidPark.swamp_bridge_ammo, JeebRegion.pallid),
    create_location(jeeb_base_code + 39, PallidPark.crossbow, JeebRegion.pallid),
    create_location(jeeb_base_code + 40, PallidPark.north_coffee, JeebRegion.pallid),
    create_location(jeeb_base_code + 41, PallidPark.swamp_shack_ammo, JeebRegion.pallid),
    create_location(jeeb_base_code + 42, PallidPark.swamp_shack_bolts, JeebRegion.pallid),
    create_location(jeeb_base_code + 43, PallidPark.swamp_shack_coffee, JeebRegion.pallid),
    create_location(jeeb_base_code + 44, PallidPark.south_office_coffee, JeebRegion.pallid),
    create_location(jeeb_base_code + 45, PallidPark.south_office_ammo, JeebRegion.pallid),
    create_location(jeeb_base_code + 46, PallidPark.clear, JeebRegion.pallid),

    create_location(jeeb_base_code + 47, BurningGrove.banjo, JeebRegion.burning),
    create_location(jeeb_base_code + 48, BurningGrove.clear, JeebRegion.burning),
]

jeeb_lore_code = 200
jeeb_lore_locations = [
    create_location(jeeb_lore_code + 1, JeebLore.jeeb_diary, JeebRegion.bbq),
    create_location(jeeb_lore_code + 2, JeebLore.cia, JeebRegion.bbq),
    create_location(jeeb_lore_code + 3, JeebLore.tree, JeebRegion.bbq),
    create_location(jeeb_lore_code + 4, JeebLore.nothing_satisfies, JeebRegion.ritual),
    create_location(jeeb_lore_code + 5, JeebLore.black_spines, JeebRegion.ritual),
    create_location(jeeb_lore_code + 6, JeebLore.taste_that_flesh, JeebRegion.ritual),
    create_location(jeeb_lore_code + 7, JeebLore.elation, JeebRegion.ritual),
    create_location(jeeb_lore_code + 8, JeebLore.boat_diary, JeebRegion.lake),
    create_location(jeeb_lore_code + 9, JeebLore.the_deluge, JeebRegion.lake),
    create_location(jeeb_lore_code + 10, JeebLore.almighty_baya, JeebRegion.lake),
    create_location(jeeb_lore_code + 11, JeebLore.otter_warning, JeebRegion.lake),
    create_location(jeeb_lore_code + 12, JeebLore.juiced_baby, JeebRegion.pallid),
    create_location(jeeb_lore_code + 13, JeebLore.woke_gallows, JeebRegion.pallid),
    create_location(jeeb_lore_code + 14, JeebLore.great_leech, JeebRegion.pallid),
    create_location(jeeb_lore_code + 15, JeebLore.right_to_be_naked, JeebRegion.pallid),
    create_location(jeeb_lore_code + 16, JeebLore.what_magic, JeebRegion.burning),
    create_location(jeeb_lore_code + 17, JeebLore.partook_flesh, JeebRegion.burning),
    create_location(jeeb_lore_code + 18, JeebLore.feel_the_vines, JeebRegion.burning),
    create_location(jeeb_lore_code + 19, JeebLore.someday_peace, JeebRegion.burning),
    create_location(jeeb_lore_code + 20, JeebLore.nipple_yogurt, JeebRegion.pallid),
]

jeeb_meat_code = 230
jeeb_meat_locations = [
    create_location(jeeb_meat_code + 1, BBQMeat.squirrel, JeebRegion.bbq, MeatItem.bbq),

    create_location(jeeb_meat_code + 2, RitualMeat.bird_bridge_1, JeebRegion.ritual, MeatItem.ritual),
    create_location(jeeb_meat_code + 3, RitualMeat.bird_bridge_2, JeebRegion.ritual, MeatItem.ritual),
    create_location(jeeb_meat_code + 4, RitualMeat.bird_bridge_3, JeebRegion.ritual, MeatItem.ritual),
    create_location(jeeb_meat_code + 5, RitualMeat.roadkill_bridge_1, JeebRegion.ritual, MeatItem.ritual),
    create_location(jeeb_meat_code + 6, RitualMeat.roadkill_bridge_2, JeebRegion.ritual, MeatItem.ritual),
    create_location(jeeb_meat_code + 7, RitualMeat.dollar_bird_1, JeebRegion.ritual, MeatItem.ritual),
    create_location(jeeb_meat_code + 8, RitualMeat.dollar_bird_2, JeebRegion.ritual, MeatItem.ritual),
    create_location(jeeb_meat_code + 9, RitualMeat.dollar_bird_3, JeebRegion.ritual, MeatItem.ritual),
    create_location(jeeb_meat_code + 10, RitualMeat.tree_roadkill, JeebRegion.ritual, MeatItem.ritual),
    create_location(jeeb_meat_code + 11, RitualMeat.intersection_bird_1, JeebRegion.ritual, MeatItem.ritual),
    create_location(jeeb_meat_code + 12, RitualMeat.intersection_bird_2, JeebRegion.ritual, MeatItem.ritual),
    create_location(jeeb_meat_code + 13, RitualMeat.intersection_roadkill, JeebRegion.ritual, MeatItem.ritual),
    create_location(jeeb_meat_code + 14, RitualMeat.car_crash, JeebRegion.ritual, MeatItem.ritual),
    create_location(jeeb_meat_code + 15, RitualMeat.legless_deer, JeebRegion.ritual, MeatItem.ritual),
    create_location(jeeb_meat_code + 16, RitualMeat.your_truck, JeebRegion.ritual),

    create_location(jeeb_meat_code + 17, LakeMeat.dead_body, JeebRegion.lake, MeatItem.lake),
    create_location(jeeb_meat_code + 18, LakeMeat.hiding_otter_1, JeebRegion.lake, MeatItem.lake),
    create_location(jeeb_meat_code + 19, LakeMeat.hiding_otter_2, JeebRegion.lake, MeatItem.lake),
    create_location(jeeb_meat_code + 20, LakeMeat.hiding_otter_3, JeebRegion.lake, MeatItem.lake),
    create_location(jeeb_meat_code + 21, LakeMeat.covered_body, JeebRegion.lake, MeatItem.lake),
    create_location(jeeb_meat_code + 22, LakeMeat.north_house_otter_1, JeebRegion.lake, MeatItem.lake),
    create_location(jeeb_meat_code + 23, LakeMeat.north_house_otter_2, JeebRegion.lake, MeatItem.lake),
    create_location(jeeb_meat_code + 24, LakeMeat.north_house_otter_3, JeebRegion.lake, MeatItem.lake),
    create_location(jeeb_meat_code + 25, LakeMeat.north_house_otter_4, JeebRegion.lake, MeatItem.lake),
    create_location(jeeb_meat_code + 26, LakeMeat.north_house_otter_5, JeebRegion.lake, MeatItem.lake),
    create_location(jeeb_meat_code + 27, LakeMeat.north_house_otter_6, JeebRegion.lake, MeatItem.lake),
    create_location(jeeb_meat_code + 28, LakeMeat.north_house_otter_7, JeebRegion.lake, MeatItem.lake),
    create_location(jeeb_meat_code + 29, LakeMeat.coffee_trap_otter_1, JeebRegion.lake, MeatItem.lake),
    create_location(jeeb_meat_code + 30, LakeMeat.coffee_trap_otter_2, JeebRegion.lake, MeatItem.lake),
    create_location(jeeb_meat_code + 31, LakeMeat.coffee_trap_otter_3, JeebRegion.lake, MeatItem.lake),
    create_location(jeeb_meat_code + 32, LakeMeat.dam_otter_1, JeebRegion.lake, MeatItem.lake),
    create_location(jeeb_meat_code + 33, LakeMeat.dam_otter_2, JeebRegion.lake, MeatItem.lake),
    create_location(jeeb_meat_code + 34, LakeMeat.warning_otter_1, JeebRegion.lake, MeatItem.lake),
    create_location(jeeb_meat_code + 35, LakeMeat.warning_otter_2, JeebRegion.lake, MeatItem.lake),
    create_location(jeeb_meat_code + 36, LakeMeat.warning_otter_3, JeebRegion.lake, MeatItem.lake),
    create_location(jeeb_meat_code + 37, LakeMeat.warning_otter_4, JeebRegion.lake, MeatItem.lake),
    create_location(jeeb_meat_code + 38, LakeMeat.warning_otter_5, JeebRegion.lake, MeatItem.lake),
    create_location(jeeb_meat_code + 40, LakeMeat.trapped_start_1, JeebRegion.lake),
    create_location(jeeb_meat_code + 41, LakeMeat.trapped_start_2, JeebRegion.lake),
    create_location(jeeb_meat_code + 42, LakeMeat.trapped_start_3, JeebRegion.lake),
    create_location(jeeb_meat_code + 43, LakeMeat.trapped_start_4, JeebRegion.lake),


    create_location(jeeb_meat_code + 44, PallidMeat.dougie, JeebRegion.pallid, MeatItem.pallid),
    create_location(jeeb_meat_code + 45, PallidMeat.dead_owner, JeebRegion.pallid, MeatItem.pallid),
    create_location(jeeb_meat_code + 46, PallidMeat.north_leech_1, JeebRegion.pallid, MeatItem.pallid),
    create_location(jeeb_meat_code + 47, PallidMeat.north_leech_2, JeebRegion.pallid, MeatItem.pallid),
    create_location(jeeb_meat_code + 48, PallidMeat.north_leech_3, JeebRegion.pallid, MeatItem.pallid),
    create_location(jeeb_meat_code + 49, PallidMeat.north_leech_4, JeebRegion.pallid, MeatItem.pallid),
    create_location(jeeb_meat_code + 50, PallidMeat.south_leech_2, JeebRegion.pallid, MeatItem.pallid),
    create_location(jeeb_meat_code + 51, PallidMeat.south_leech_3, JeebRegion.pallid, MeatItem.pallid),
    create_location(jeeb_meat_code + 52, PallidMeat.south_leech_4, JeebRegion.pallid, MeatItem.pallid),
    create_location(jeeb_meat_code + 53, PallidMeat.ghost_1, JeebRegion.pallid, MeatItem.pallid),
    create_location(jeeb_meat_code + 54, PallidMeat.ghost_2, JeebRegion.pallid),

    create_location(jeeb_meat_code + 55, BurningMeat.burning_dog_1, JeebRegion.burning, MeatItem.burning),
    create_location(jeeb_meat_code + 56, BurningMeat.burning_dog_2, JeebRegion.burning, MeatItem.burning),
    create_location(jeeb_meat_code + 57, BurningMeat.burning_dog_3, JeebRegion.burning, MeatItem.burning),
    create_location(jeeb_meat_code + 58, BurningMeat.burning_dog_4, JeebRegion.burning, MeatItem.burning),
    create_location(jeeb_meat_code + 59, BurningMeat.burning_dog_5, JeebRegion.burning, MeatItem.burning),
    create_location(jeeb_meat_code + 60, BurningMeat.burning_dog_6, JeebRegion.burning, MeatItem.burning),
    create_location(jeeb_meat_code + 61, BurningMeat.rotting_corpse, JeebRegion.burning, MeatItem.burning),
]

hyena_code = 450
hyena_locations = [
    create_location(hyena_code + 1, Hyena.turkey_creek, JebRegion.turkey, BaseItem.hyena),
    create_location(hyena_code + 2, Hyena.frigid_valley, JebRegion.frigid, BaseItem.hyena),
    create_location(hyena_code + 3, Hyena.howling_marsh, JebRegion.howling, BaseItem.hyena),
    create_location(hyena_code + 4, Hyena.lake_linger, JeebRegion.lake, BaseItem.hyena),
    create_location(hyena_code + 5, Hyena.burning_grove, JeebRegion.burning, BaseItem.hyena),
]

jeb_clear_events = {
    JebRegion.cabin: JebCabin.clear,
    JebRegion.turkey: TurkeyCreek.clear,
    JebRegion.frigid: FrigidValley.clear,
    JebRegion.howling: HowlingMarsh.clear,
}

jeeb_clear_events = {
    JeebRegion.bbq: TheBBQBasket.clear,
    JeebRegion.ritual: RitualRoad.clear,
    JeebRegion.lake: LakeLinger.clear,
    JeebRegion.pallid: PallidPark.clear,
}

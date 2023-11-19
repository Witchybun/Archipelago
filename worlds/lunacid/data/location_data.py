from dataclasses import dataclass
from typing import List, TypedDict

from ..strings.locations import Location
from ..strings.regions_entrances import Region
from ..strings.weapons import Weapon
from ..strings.spells import Spell
from ..strings.items import UniqueItem, GenericItem


@dataclass(frozen=True)
class LocationData:
    name: str
    region: str
    original_item: str


base_locations = [
    LocationData(Location.wings_rest_ocean_elixir, Region.wings_rest, GenericItem.ocean_elixir),
    LocationData(Location.wings_rest_crystal_shard, Region.wings_rest, GenericItem.crystal_shard),
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
    LocationData(Location.mire_bonerard_trash, Region.fetid_mire, GenericItem.antidote),
    LocationData(Location.mire_jellisha_reward, Region.fetid_mire, Spell.slime_orb),
    LocationData(Location.mire_jellisha_trash, Region.fetid_mire, GenericItem.mana_vial),
    LocationData(Location.mire_rubble_bridge, Region.fetid_mire, GenericItem.antidote),
    LocationData(Location.mire_skeleton_chest, Region.fetid_mire, Spell.barrier),
    LocationData(Location.mire_hidden_chest_near_underworks, Region.fetid_mire, GenericItem.earth_elixir),
    LocationData(Location.mire_hidden_slime_chest, Region.fetid_mire, Spell.ice_spear),
    LocationData(Location.mire_room_left_foyer, Region.fetid_mire, GenericItem.antidote),
    LocationData(Location.mire_rubble_near_illusory_wall, Region.fetid_mire, Spell.wind_dash),
    LocationData(Location.mire_underwater_pipe, Region.fetid_mire, GenericItem.poison_throwing_knife),
    LocationData(Location.mire_underworks_skeleton, Region.fetid_mire, Weapon.broken_hilt),
    LocationData(Location.mire_underworks_waterfall, Region.fetid_mire, GenericItem.antidote),
    LocationData(Location.mire_upper_overlook_left, Region.fetid_mire, GenericItem.crystal_shard),
    LocationData(Location.mire_upper_overlook_right, Region.fetid_mire, GenericItem.ocean_elixir),
    LocationData(Location.sea_demon, Region.sanguine_sea, GenericItem.ocean_elixir),
    LocationData(Location.sea_pillar, Region.sanguine_sea, Weapon.corrupted_dagger),
    LocationData(Location.sea_underblood, Region.sanguine_sea, Weapon.dark_rapier),
    LocationData(Location.sea_blood_island, Region.sanguine_sea, Spell.summon_fairy),

]

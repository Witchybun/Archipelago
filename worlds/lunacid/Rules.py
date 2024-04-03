from BaseClasses import CollectionState
from typing import Dict, List, TYPE_CHECKING

from .Regions import REVERSE
from .data.item_count_data import base_spells
from .strings.properties import Elements
from ..generic.Rules import CollectionRule

from .data.spell_data import spell_light_sources, drop_spells, ranged_spells, blood_spells
from .data.weapon_data import ranged_weapons, weapon_light_sources
from .data.item_data import item_light_sources
from .Options import LunacidOptions
from .strings.regions_entrances import LunacidEntrance, LunacidRegion
from .strings.spells import Spell, MobSpell
from .strings.items import UniqueItem, Progressives, Switch, Alchemy, Door
from .strings.locations import BaseLocation, ShopLocation, DropLocation

if TYPE_CHECKING:
    from . import LunacidWorld, Weapon


class LunacidRules:
    player: int
    world: "LunacidWorld"
    region_rules: Dict[str, CollectionRule]
    entrance_rules: Dict[str, CollectionRule]
    location_rules: Dict[str, CollectionRule]
    elements: Dict[str, str]

    def __init__(self, world: "LunacidWorld") -> None:
        self.player = world.player
        self.world = world
        self.world.options = world.options

        self.region_rules = {
            LunacidRegion.temple_of_silence_entrance: lambda state: self.has_light_source(state),
            LunacidRegion.temple_of_silence_interior: lambda state: self.has_light_source(state),
            LunacidRegion.temple_of_silence_secret: lambda state: self.has_light_source(state),
            LunacidRegion.accursed_tomb: lambda state: self.has_light_source(state),
            LunacidRegion.fetid_mire_secret: lambda state: self.has_crystal_orb(state, self.world.options),
            LunacidRegion.castle_le_fanu_white: lambda state: state.has(Progressives.vampiric_symbol, self.player, 1),
            LunacidRegion.castle_le_fanu_blue: lambda state: state.has(Progressives.vampiric_symbol, self.player, 2),
            LunacidRegion.chamber_of_fate: lambda state: state.has_all({UniqueItem.earth_talisman, UniqueItem.water_talisman}, self.player),
            LunacidRegion.sealed_ballroom_secret: lambda state: self.has_crystal_orb(state, self.world.options),
            LunacidRegion.vampire_tomb: lambda state: self.has_element_access([Elements.light, Elements.dark_and_light], state),
            LunacidRegion.mausoleum: lambda state: self.has_element_access([Elements.light, Elements.dark_and_light], state),
            LunacidRegion.sand_temple: lambda state: self.has_key_to_switch(state, Switch.grotto_valves_switches, self.world.options),
            LunacidRegion.terminus_prison_dark: lambda state: self.has_light_source(state) and
                                                              (self.has_key_to_switch(state, Switch.prison_shortcut_switch, self.world.options) or
                                                               state.has(Spell.icarian_flight, self.player)),
            LunacidRegion.terminus_prison_upstairs: lambda state: state.has(UniqueItem.terminus_prison_key, self.player),
            LunacidRegion.throne_chamber: lambda state: self.can_defeat_the_prince(state),
            LunacidRegion.tower_abyss: lambda state: self.has_door_key(Door.tower_key, state, self.world.options),
        }

        self.entrance_rules = {
            LunacidEntrance.basin_to_temple: lambda state: self.has_keys_for_basin_door(state, self.world.options) and self.has_light_source(state),
            REVERSE(LunacidEntrance.basin_to_temple): lambda state: self.has_keys_for_basin_door(state, self.world.options),
            LunacidEntrance.temple_entrance_to_temple_interior: lambda state: self.has_key_to_switch(state, Switch.temple_switch, self.world.options),
            REVERSE(LunacidEntrance.temple_entrance_to_temple_interior): lambda state: self.has_key_to_switch(state, Switch.temple_switch, self.world.options),
            LunacidEntrance.temple_interior_to_temple_secret: lambda state: self.has_crystal_orb(state, self.world.options),
            LunacidEntrance.temple_to_mire: lambda state: self.has_door_key(Door.basin_temple_sewers, state, self.world.options),
            LunacidEntrance.temple_to_forest: lambda state: self.has_door_key(Door.basin_rickety_bridge, state, self.world.options),
            LunacidEntrance.basin_to_archives: lambda state: self.has_door_key(Door.basin_broken_steps, state, self.world.options),
            REVERSE(LunacidEntrance.temple_to_forest): lambda state: self.has_door_key(Door.basin_rickety_bridge, state, self.world.options),
            REVERSE(LunacidEntrance.basin_to_archives): lambda state: self.has_door_key(Door.basin_broken_steps, state, self.world.options),
            REVERSE(LunacidEntrance.temple_to_mire): lambda state: self.has_light_source(state) and self.has_door_key(Door.basin_temple_sewers, state,
                                                                                                                      self.world.options),
            LunacidEntrance.mire_to_sea: lambda state: self.has_door_key(Door.sea_westward, state, self.world.options),
            REVERSE(LunacidEntrance.mire_to_sea): lambda state: self.has_door_key(Door.sea_westward, state, self.world.options),
            LunacidEntrance.sea_to_tomb: lambda state: self.has_light_source(state) and self.has_door_key(Door.sea_eastward, state, self.world.options),
            LunacidEntrance.sea_to_castle: lambda state: self.has_door_key(Door.sea_double_doors, state, self.world.options),
            REVERSE(LunacidEntrance.sea_to_castle): lambda state: self.has_door_key(Door.sea_double_doors, state, self.world.options),
            LunacidEntrance.yosei_lower_to_tomb: lambda state: self.has_light_source(state) and self.has_door_key(Door.forest_patchouli, state,
                                                                                                                  self.world.options),
            LunacidEntrance.castle_to_ballroom: lambda state: self.has_door_key(Door.ballroom_key, state, self.world.options) and
            self.can_reach_region(state, LunacidRegion.castle_le_fanu) and (
                    self.has_ranged_element_access(
                        [Elements.dark, Elements.dark_and_fire, Elements.dark_and_light, Elements.poison, Elements.ice_and_poison], state) or
                    (self.has_element_access(
                        [Elements.dark, Elements.dark_and_fire, Elements.dark_and_light, Elements.poison,
                         Elements.ice_and_poison], state) and state.has(Spell.rock_bridge, self.player))),
            REVERSE(LunacidEntrance.castle_to_ballroom): lambda state: self.has_door_key(Door.ballroom_key, state, self.world.options) and
                                                                       self.can_reach_region(state, LunacidRegion.castle_le_fanu) and (
                    self.has_ranged_element_access(
                        [Elements.dark, Elements.dark_and_fire, Elements.dark_and_light, Elements.poison, Elements.ice_and_poison], state) or
                    (self.has_element_access([Elements.dark, Elements.dark_and_fire, Elements.dark_and_light, Elements.poison,
                                              Elements.ice_and_poison], state) and state.has(Spell.rock_bridge, self.player))),
            LunacidEntrance.white_to_throne: lambda state: state.has(Progressives.vampiric_symbol, self.player, 3) and
                                                           self.has_door_key(Door.throne_key, state, self.world.options),
            REVERSE(LunacidEntrance.white_to_throne): lambda state: state.has(Progressives.vampiric_symbol, self.player, 3) and
                                                                    self.has_door_key(Door.throne_key, state, self.world.options),
            LunacidEntrance.throne_to_prison: lambda state: self.has_door_key(Door.prison_key, state, self.world.options),
            LunacidEntrance.archives_to_chasm: lambda state: state.has(Progressives.vampiric_symbol, self.player, 2) and
                                                             self.can_jump_given_height(state, "Medium", self.world.options) and
                                                             self.has_door_key(Door.archives_sealed_door, state, self.world.options),
            REVERSE(LunacidEntrance.archives_to_chasm): lambda state: state.has(Progressives.vampiric_symbol, self.player, 2) and
                                                                      self.can_jump_given_height(state, "Medium", self.world.options) and
                                                                      self.has_door_key(Door.archives_sealed_door, state, self.world.options),
            LunacidEntrance.chasm_to_surface: lambda state: self.has_door_key(Door.chasm_surface_door, state, self.world.options),
            LunacidEntrance.wings_to_surface: lambda state: state.has(Spell.icarian_flight, self.player),
            LunacidEntrance.basin_to_surface: lambda state: state.has_all({Spell.icarian_flight, Spell.spirit_warp}, self.player) or
                                                            (state.has(Spell.icarian_flight, self.player) and state.can_reach(
                                                                LunacidRegion.temple_of_silence_interior, None, self.player)),
            LunacidEntrance.yosei_to_yosei_lower: lambda state: self.can_jump_given_height(state, "Medium", self.world.options) or self.has_blood_spell_access(
                state),
            LunacidEntrance.castle_to_red: self.has_blood_spell_access,
            LunacidEntrance.castle_to_grotto: lambda state: self.has_door_key(Door.burning_key, state, self.world.options),
            REVERSE(LunacidEntrance.castle_to_grotto): lambda state: self.has_door_key(Door.burning_key, state, self.world.options),
            LunacidEntrance.yosei_to_canopy: lambda state: self.has_keys_for_canopy(state, self.world.options) and
                                                           self.has_door_key(Door.forest_door_in_trees, state, self.world.options),
            LunacidEntrance.archives_3_to_archives_1b: lambda state: self.has_key_to_switch(state, Switch.archives_elevator_switches, self.world.options)
                                                                     or self.can_jump_given_height(state, "High", self.world.options),
            LunacidEntrance.archives_2_to_archives_3: lambda state: self.has_key_to_switch(state, Switch.archives_elevator_switches, self.world.options)
                                                                    or self.can_jump_given_height(state, "High", self.world.options),
            LunacidEntrance.grotto_to_tower: lambda state: self.has_crystal_orb(state, self.world.options),
            REVERSE(LunacidEntrance.grotto_to_tower): lambda state: self.has_crystal_orb(state, self.world.options),
            LunacidEntrance.prison_to_arena: lambda state: self.has_key_to_switch(state, Switch.prison_arena_switch, self.world.options)
                                                           and state.has(UniqueItem.terminus_prison_key, self.player) and
                                                           self.has_door_key(Door.forlorn_key, state, self.world.options),
            LunacidEntrance.prison_to_ash: lambda state: self.has_door_key(Door.ash_key, state, self.world.options),
            LunacidEntrance.arena_to_fate: lambda state: self.has_door_key(Door.sucs_key, state, self.world.options),
            LunacidEntrance.fate_to_sleeper: lambda state: self.has_door_key(Door.sleeper_key, state, self.world.options),
        }

        self.location_rules = {
            BaseLocation.wings_rest_demi_orb: lambda state: self.can_reach_region(state, LunacidRegion.grave_of_the_sleeper),
            BaseLocation.temple_blood_altar: self.has_blood_spell_access,
            BaseLocation.hollow_basin_dark_item: lambda state: state.has(UniqueItem.enchanted_key, self.player),
            BaseLocation.temple_sewer_puzzle: lambda state: state.has(UniqueItem.vhs_tape, self.player) and
                                                            self.can_reach_region(state, LunacidRegion.vampire_tomb) and
                                                            self.has_crystal_orb(state, self.world.options),
            BaseLocation.archives_strange_corpse: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.archives_hidden_room_lower: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.archives_hidden_room_upper: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.archives_daedalus_one: lambda state: state.has(UniqueItem.black_book, self.player),
            BaseLocation.archives_daedalus_two: lambda state: state.has(UniqueItem.black_book, self.player, 2),
            BaseLocation.archives_daedalus_third: lambda state: state.has(UniqueItem.black_book, self.player, 3),
            BaseLocation.sea_pillar: lambda state: state.has_any({Spell.icarian_flight, Spell.rock_bridge}, self.player),
            BaseLocation.tomb_demi_chest: lambda state: self.can_jump_given_height(state, "Medium", self.world.options),
            BaseLocation.chasm_hidden_chest: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.chasm_invisible_cliffside: lambda state: state.has_any([Spell.coffin, Spell.icarian_flight], self.player),
            BaseLocation.tomb_hidden_chest: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.tomb_hidden_room: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.catacombs_hidden_room: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.mausoleum_hidden_chest: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.mausoleum_upper_table: lambda state: self.can_jump_given_height(state, "Medium", self.world.options),
            BaseLocation.mausoleum_kill_death: lambda state: state.has_all({Alchemy.fractured_life, Alchemy.fractured_death, Alchemy.broken_sword},
                                                                           self.player),
            BaseLocation.corrupted_room: lambda state: state.has(UniqueItem.corrupted_key, self.player),
            BaseLocation.yosei_hanging_in_trees: lambda state: state.has_any(ranged_weapons, self.player),
            BaseLocation.yosei_hidden_chest: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.yosei_room_defended_by_blood_plant: lambda state: self.has_blood_spell_access(state),
            BaseLocation.yosei_blood_plant_insides: lambda state: self.has_blood_spell_access(state),
            BaseLocation.castle_cell_center: lambda state: self.has_element_access(Elements.fire, state),
            BaseLocation.castle_hidden_cell: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.castle_upper_floor_coffin_double: lambda state: state.has(Progressives.vampiric_symbol, self.player, 3) and
                                                                         self.has_crystal_orb(state, self.world.options),
            BaseLocation.ballroom_side_chest_near_switch: lambda state: self.has_door_key(Door.ballroom_rooms_key, state, self.world.options),
            BaseLocation.ballroom_side_xp_drain: lambda state: self.has_door_key(Door.ballroom_rooms_key, state, self.world.options),
            BaseLocation.ballroom_entry_long_table: lambda state: self.has_door_key(Door.ballroom_rooms_key, state, self.world.options),
            BaseLocation.ballroom_side_painting: lambda state: self.has_door_key(Door.ballroom_rooms_key, state, self.world.options),
            BaseLocation.ballroom_entry_hidden_cave_in_lounge: lambda state: self.has_door_key(Door.ballroom_rooms_key, state, self.world.options),
            BaseLocation.ballroom_entry_hidden_couch_bottom: lambda state: self.has_door_key(Door.ballroom_rooms_key, state, self.world.options),
            BaseLocation.ballroom_entry_hidden_couch_top: lambda state: self.has_door_key(Door.ballroom_rooms_key, state, self.world.options),
            BaseLocation.ballroom_small_room_lounge: lambda state: self.has_door_key(Door.ballroom_rooms_key, state, self.world.options),
            BaseLocation.prison_f3_bottomless_pit: lambda state: state.has_any({Spell.icarian_flight, Spell.spirit_warp}, self.player),
            BaseLocation.grotto_hidden_chest: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.grotto_triple_secret_chest: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.sand_basement_snake_pit: lambda state: self.can_jump_given_height(state, "High", self.world.options),
            BaseLocation.sand_hidden_sarcophagus: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.sand_second_floor_snake: lambda state: self.can_jump_given_height(state, "Medium", self.world.options),
            BaseLocation.sand_second_floor_dead_end: lambda state: self.can_jump_given_height(state, "Medium", self.world.options),
            BaseLocation.sand_chest_overlooking_crypt: lambda state: self.can_jump_given_height(state, "High", self.world.options),
            BaseLocation.sand_lunacid_sandwich: lambda state: state.has(Spell.spirit_warp, self.player),
            BaseLocation.arena_earth_hidden_room: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.arena_earth_hidden_plant_haven: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.arena_water_hidden_alcove_before: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.arena_water_hidden_alcove_right: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.arena_water_hidden_alcove_left: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.arena_water_hidden_basement_left: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.arena_water_hidden_basement_right: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.arena_water_hidden_laser_room: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.arena_water_underwater_temple: lambda state: self.can_jump_given_height(state, "High", self.world.options) and
                                                                      self.has_crystal_orb(state, self.world.options),
            BaseLocation.arena_earth_earthen_temple: lambda state: self.can_jump_given_height(state, "High", self.world.options) and
                                                                   self.has_crystal_orb(state, self.world.options),
            BaseLocation.prison_b2_egg_resting_place: lambda state: state.has(UniqueItem.skeleton_egg, self.player),
            BaseLocation.prison_f1_hidden_cell: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.prison_f1_hidden_debris_room: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.prison_f4_hidden_beds: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.prison_f4_maledictus_secret: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.prison_f3_locked_left: lambda state: state.has(UniqueItem.terminus_prison_key, self.player),
            BaseLocation.prison_f3_locked_right: lambda state: state.has(UniqueItem.terminus_prison_key, self.player),
            BaseLocation.prison_f3_locked_south: lambda state: state.has(UniqueItem.terminus_prison_key, self.player),
            "Free Sir Hicket": lambda state: state.has(Spell.ignis_calor, self.player),
            BaseLocation.ash_path_maze: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.ash_hidden_chest: lambda state: self.has_crystal_orb(state, self.world.options),
            ShopLocation.buy_steel_needle: lambda state: self.can_reach_region(state, LunacidRegion.sanguine_sea),  # Push out of sphere 0
            ShopLocation.buy_crossbow: lambda state: self.can_reach_region(state, LunacidRegion.sanguine_sea),  # Push out of sphere 0
            ShopLocation.buy_rapier: lambda state: self.can_reach_region(state, LunacidRegion.sanguine_sea),  # Push out of sphere 0
            ShopLocation.buy_ocean_elixir_sheryl: lambda state: self.can_purchase_item(state, self.world.options),
            ShopLocation.buy_privateer_musket: lambda state: self.can_purchase_item(state, self.world.options),
            ShopLocation.buy_oil_lantern: lambda state: self.can_purchase_item(state, self.world.options),
            ShopLocation.buy_jotunn_slayer: lambda state: self.can_reach_location(state, BaseLocation.fate_lucid_blade),
            DropLocation.sucsarian_drop_1: lambda state: self.can_reach_region(state, LunacidRegion.forlorn_arena),
            DropLocation.sucsarian_drop_2: lambda state: self.can_reach_region(state, LunacidRegion.forlorn_arena),
            DropLocation.jailor_drop: lambda state: self.can_reach_region(state, LunacidRegion.terminus_prison) and
                                                    state.has(UniqueItem.terminus_prison_key, self.player),
            DropLocation.cetea_drop: lambda state: self.can_reach_region(state, LunacidRegion.labyrinth_of_ash),
            DropLocation.vampire_drop: lambda state: self.can_reach_any_region(state, [LunacidRegion.castle_le_fanu_red,
                                                                                       LunacidRegion.castle_le_fanu_white]),
            DropLocation.horse_drop: lambda state: self.can_reach_region(state, LunacidRegion.sealed_ballroom),
            DropLocation.anpu_drop_1: lambda state: self.can_reach_region(state, LunacidRegion.sand_temple),
            DropLocation.anpu_drop_2: lambda state: self.can_reach_region(state, LunacidRegion.sand_temple),
            DropLocation.obsidian_skeleton_drop_1: lambda state: self.can_reach_any_region(state, [LunacidRegion.boiling_grotto,
                                                                                                   LunacidRegion.terminus_prison_dark]),
            DropLocation.obsidian_skeleton_drop_2: lambda state: self.can_reach_any_region(state, [LunacidRegion.boiling_grotto,
                                                                                                   LunacidRegion.terminus_prison_dark]),
            DropLocation.phantom_drop: lambda state: self.can_reach_any_region(state, [LunacidRegion.mausoleum, LunacidRegion.castle_le_fanu]),
            DropLocation.chimera_drop: lambda state: self.can_reach_any_region(state, [LunacidRegion.forbidden_archives_3,
                                                                                       LunacidRegion.forbidden_archives_1b]),
            DropLocation.skeleton_spell_drop: lambda state: self.can_reach_any_region(state, [LunacidRegion.fetid_mire, LunacidRegion.boiling_grotto,
                                                                                              LunacidRegion.terminus_prison_dark]),
            DropLocation.skeleton_weapon_drop: lambda state: self.can_reach_any_region(state, [LunacidRegion.fetid_mire, LunacidRegion.boiling_grotto,
                                                                                               LunacidRegion.terminus_prison_dark]),
            DropLocation.kodama_drop: lambda state: self.can_reach_region(state, LunacidRegion.yosei_forest),
            DropLocation.mummy_drop: lambda state: self.can_reach_region(state, LunacidRegion.temple_of_silence_interior),
            DropLocation.sea_demon: lambda state: self.can_reach_any_region(state, [LunacidRegion.sanguine_sea, LunacidRegion.mausoleum]),
            DropLocation.snail_drop: lambda state: self.can_reach_region(state, LunacidRegion.hollow_basin),
            DropLocation.milk_snail_drop: lambda state: self.can_reach_region(state, LunacidRegion.hollow_basin),
        }

    def can_reach_region(self, state: CollectionState, spot: str):
        return state.can_reach(spot, "Region", self.player)

    def can_reach_any_region(self, state: CollectionState, spots: List[str]):
        any_rule = False
        for spot in spots:
            any_rule = any_rule or self.can_reach_region(state, spot)
        return any_rule

    def can_reach_all_regions(self, state: CollectionState, spots: List[str]):
        all_rule = True
        for spot in spots:
            all_rule = all_rule and self.can_reach_region(state, spot)
        return all_rule

    def can_reach_location(self, state: CollectionState, spot: str):
        return state.can_reach(spot, "Location", self.player)

    def can_jump_given_height(self, state: CollectionState, height: str, options: LunacidOptions) -> bool:
        if height == "Low":
            return True
        elif height == "Medium":
            medium_spells = {Spell.barrier, Spell.icarian_flight, Spell.coffin, Spell.rock_bridge}
            if options.dropsanity == options.dropsanity.option_true:
                medium_spells.add(MobSpell.summon_snail)
            return state.has_any(medium_spells, self.player)
        else:
            high_spells = {Spell.barrier, Spell.rock_bridge, Spell.icarian_flight}
            return state.has_any(high_spells, self.player)

    def has_door_key(self, key: str, state: CollectionState, options: LunacidOptions) -> bool:
        if options.door_locks == options.door_locks.option_false:
            return True
        return state.has(key, self.player)

    def has_light_source(self, state: CollectionState) -> bool:
        sources = []
        sources.extend(source for source in spell_light_sources)
        sources.extend(source for source in weapon_light_sources)
        sources.extend(source for source in item_light_sources)
        return state.has_any(sources, self.player)

    def has_spell(self, spell: str, state: CollectionState):
        return state.has(spell, self.player)

    def has_all_spells(self, spells: List[str], state: CollectionState):
        return state.has_all(spells, self.player)

    def has_every_spell(self, state: CollectionState, options: LunacidOptions, starting_weapon: str = None) -> bool:
        every_spell = list(set.union(set(base_spells), set(drop_spells)))
        if starting_weapon is not None and starting_weapon in every_spell:
            every_spell.remove(starting_weapon)
        mob_spell_regions = [LunacidRegion.forlorn_arena, LunacidRegion.castle_le_fanu_red, LunacidRegion.castle_le_fanu_white,
                             LunacidRegion.terminus_prison_dark,
                             LunacidRegion.labyrinth_of_ash, LunacidRegion.boiling_grotto, LunacidRegion.forbidden_archives_3, LunacidRegion.sand_temple,
                             LunacidRegion.temple_of_silence_interior, LunacidRegion.sealed_ballroom]
        if options.dropsanity == options.dropsanity.option_false:
            every_spell = base_spells
            return self.has_all_spells(every_spell, state) & self.can_reach_all_regions(state, mob_spell_regions)
        else:
            return self.has_all_spells(every_spell, state)

    def can_purchase_item(self, state: CollectionState, options: LunacidOptions) -> bool:
        if options.shopsanity == options.shopsanity.option_false:
            return True
        return state.has("Sir Hicket's Freedom from Armor", self.player)

    def has_blood_spell_access(self, state: CollectionState) -> bool:
        return state.has_any(blood_spells, self.player)

    def has_keys_for_basin_door(self, state: CollectionState, options: LunacidOptions) -> bool:
        if options.shopsanity == options.shopsanity.option_false:
            return True
        return state.has(UniqueItem.enchanted_key, self.player)

    def has_keys_for_canopy(self, state: CollectionState, options: LunacidOptions) -> bool:
        if options.shopsanity == options.shopsanity.option_false:
            return state.has(UniqueItem.enchanted_key, self.player)
        return state.has(UniqueItem.enchanted_key, self.player, 2)

    def has_key_to_switch(self, state: CollectionState, key: str, options: LunacidOptions) -> bool:
        if options.switch_locks == options.switch_locks.option_false:
            return True
        return state.has(key, self.player)

    def has_all_keys_to_switch(self, state: CollectionState, keys: List[str], options: LunacidOptions) -> bool:
        rule = True
        for key in keys:
            rule = rule and self.has_key_to_switch(state, key, options)
        return rule

    def has_crystal_orb(self, state: CollectionState, options: LunacidOptions) -> bool:
        if options.secret_door_lock == options.secret_door_lock.option_false:
            return True
        return state.has(UniqueItem.dusty_crystal_orb, self.player)

    def has_element_access(self, element: str | List[str], state: CollectionState):
        if isinstance(element, str):
            element = [element]
        element_options = [item for item in self.elements if self.elements[item] in element]
        return state.has_any(element_options, self.player)

    def has_ranged_element_access(self, element: str | List[str], state: CollectionState):
        if isinstance(element, str):
            element = [element]
        ranged_options = [item for item in ranged_weapons]
        ranged_options.extend([item for item in ranged_spells])
        element_options = [item for item in self.elements if self.elements[item] in element and item in ranged_options]
        return state.has_any(element_options, self.player)

    def can_defeat_the_prince(self, state: CollectionState):
        return (self.has_element_access([Elements.light, Elements.dark_and_light], state) and
                self.can_reach_any_region(state, [LunacidRegion.castle_le_fanu_white, LunacidRegion.forbidden_archives_2, LunacidRegion.sealed_ballroom, LunacidRegion.boiling_grotto, LunacidRegion.forlorn_arena]))

    def set_lunacid_rules(self, world_elements: Dict[str, str]) -> None:
        multiworld = self.world.multiworld
        self.elements = world_elements
        for region in multiworld.get_regions(self.player):
            if region.name in self.region_rules:
                for entrance in region.entrances:
                    entrance.access_rule = self.region_rules[region.name]
                for location in region.locations:
                    location.access_rule = self.region_rules[region.name]
            for entrance in region.entrances:
                if entrance.name in self.entrance_rules:
                    entrance.access_rule = entrance.access_rule and self.entrance_rules[entrance.name]
            for loc in region.locations:
                if loc.name in self.location_rules:
                    loc.access_rule = loc.access_rule and self.location_rules[loc.name]

from BaseClasses import CollectionState
from typing import Dict, List, TYPE_CHECKING

from .Regions import REVERSE
from .data.enemy_positions import immovable_enemies
from .strings.enemies import Enemy
from .strings.properties import Elements
from worlds.generic.Rules import CollectionRule

from .data.spell_info import ranged_spells
from .data.weapon_info import ranged_weapons
from .data.item_data import base_light_sources, shop_light_sources, blood_spells
from .data.plant_data import all_alchemy_plant_data
from .Options import LunacidOptions
from .strings.regions_entrances import LunacidEntrance, LunacidRegion
from .strings.spells import Spell, MobSpell
from .strings.items import UniqueItem, Progressives, Switch, Alchemy, Door, Coins, Voucher
from .strings.locations import BaseLocation, ShopLocation, all_drops_by_enemy, DropLocation, Quench, AlchemyLocation
from .strings.weapons import Weapon

if TYPE_CHECKING:
    from . import LunacidWorld


class LunacidRules:
    player: int
    world: "LunacidWorld"
    region_rules: Dict[str, CollectionRule]
    entrance_rules: Dict[str, CollectionRule]
    location_rules: Dict[str, CollectionRule]
    elements: Dict[str, str]
    enemy_regions: Dict[str, List[str]]

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

            LunacidEntrance.castle_to_white: lambda state: state.has(Progressives.vampiric_symbol, self.player, 1) or self.is_vampire(self.world.options),
            LunacidEntrance.mire_to_sea: lambda state: self.has_door_key(Door.sea_westward, state, self.world.options),
            REVERSE(LunacidEntrance.mire_to_sea): lambda state: self.has_door_key(Door.sea_westward, state, self.world.options),
            LunacidEntrance.sea_to_tomb_lobby: lambda state: self.has_door_key(Door.sea_eastward, state, self.world.options),
            LunacidEntrance.tomb_upper_to_tomb: lambda state: self.has_light_source(state) and self.can_jump_given_height(state, "High", self.world.options),
            LunacidEntrance.tomb_lobby_to_tomb: lambda state: self.has_light_source(state),
            LunacidEntrance.tomb_to_tomb_platform: lambda state: self.can_jump_given_height(state, "Medium", self.world.options),
            LunacidEntrance.sea_to_castle: lambda state: self.has_door_key(Door.sea_double_doors, state, self.world.options),
            REVERSE(LunacidEntrance.sea_to_castle): lambda state: self.has_door_key(Door.sea_double_doors, state, self.world.options),
            LunacidEntrance.yosei_lower_to_tomb_upper_lobby: lambda state: self.has_door_key(Door.forest_patchouli, state, self.world.options),
            LunacidEntrance.castle_to_ballroom: lambda state: self.has_door_key(Door.ballroom_key, state, self.world.options) and
                                                              state.can_reach_region(LunacidRegion.castle_le_fanu, self.player) and (
                                                                      self.has_ranged_element_access(
                                                                          [Elements.dark, Elements.dark_and_fire, Elements.dark_and_light, Elements.poison,
                                                                           Elements.ice_and_poison], state) or
                                                                      (self.has_element_access(
                                                                          [Elements.dark, Elements.dark_and_fire, Elements.dark_and_light, Elements.poison,
                                                                           Elements.ice_and_poison], state) and state.has(Spell.rock_bridge, self.player))),
            REVERSE(LunacidEntrance.castle_to_ballroom): lambda state: self.has_door_key(Door.ballroom_key, state, self.world.options) and
                                                                       state.can_reach_region(LunacidRegion.castle_le_fanu, self.player) and (
                                                                               self.has_ranged_element_access(
                                                                                   [Elements.dark, Elements.dark_and_fire, Elements.dark_and_light,
                                                                                    Elements.poison, Elements.ice_and_poison], state) or
                                                                               (self.has_element_access(
                                                                                   [Elements.dark, Elements.dark_and_fire, Elements.dark_and_light,
                                                                                    Elements.poison,
                                                                                    Elements.ice_and_poison], state) and state.has(Spell.rock_bridge,
                                                                                                                                   self.player))),
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
            LunacidEntrance.castle_to_red: lambda state: self.has_blood_spell_access(state) or self.is_vampire(self.world.options) or
                                                         state.can_reach_region(LunacidRegion.castle_le_fanu_blue, self.player),
            LunacidEntrance.red_to_red_deep: lambda state: self.has_blood_spell_access(state) or self.is_vampire(self.world.options),
            LunacidEntrance.red_deep_to_red_secret: lambda state: self.has_crystal_orb(state, self.world.options),
            LunacidEntrance.castle_to_grotto: lambda state: self.has_door_key(Door.burning_key, state, self.world.options),
            REVERSE(LunacidEntrance.castle_to_grotto): lambda state: self.has_door_key(Door.burning_key, state, self.world.options),
            LunacidEntrance.yosei_to_canopy: lambda state: self.has_keys_for_canopy(state, self.world.options) and
                                                           self.has_door_key(Door.forest_door_in_trees, state, self.world.options),
            LunacidEntrance.archives_3_to_archives_1b: lambda state: self.has_key_to_switch(state, Switch.archives_elevator_switches, self.world.options)
                                                                     or self.can_jump_given_height(state, "High", self.world.options)
                                                                     or state.has(Spell.spirit_warp, self.player),
            LunacidEntrance.archives_2_to_archives_3: lambda state: self.has_key_to_switch(state, Switch.archives_elevator_switches, self.world.options)
                                                                    or self.can_jump_given_height(state, "High", self.world.options),
            LunacidEntrance.grotto_to_tower: lambda state: self.has_crystal_orb(state, self.world.options),
            REVERSE(LunacidEntrance.grotto_to_tower): lambda state: self.has_crystal_orb(state, self.world.options),
            LunacidEntrance.prison_to_arena: lambda state: self.has_key_to_switch(state, Switch.prison_arena_switch, self.world.options)
                                                           and state.has(UniqueItem.terminus_prison_key, self.player) and
                                                           self.has_door_key(Door.forlorn_key, state, self.world.options),
            LunacidEntrance.prison_to_ash_entrance: lambda state: self.has_door_key(Door.ash_key, state, self.world.options),
            LunacidEntrance.ash_entrance_to_ash: lambda state: self.has_door_key(Door.musical_key, state, self.world.options),
            LunacidEntrance.arena_to_fate: lambda state: state.has_all([UniqueItem.water_talisman, UniqueItem.earth_talisman], self.player) and
                                                         self.has_door_key(Door.sucsarian_key, state, self.world.options),
            LunacidEntrance.fate_to_sleeper: lambda state: self.has_door_key(Door.sleeper_key, state, self.world.options),
            LunacidEntrance.grotto_to_secret: lambda state: self.has_crystal_orb(state, self.world.options),
            LunacidEntrance.arena_to_earth_secret: lambda state: self.has_crystal_orb(state, self.world.options),
            LunacidEntrance.sand_to_deep_snake: lambda state: self.can_jump_given_height(state, "High", self.world.options),
            LunacidEntrance.sand_to_sand_secret: lambda state: self.has_crystal_orb(state, self.world.options),
            LunacidEntrance.sand_to_secret_snake: lambda state: self.can_jump_given_height(state, "High", self.world.options) or
                                                                self.has_crystal_orb(state, self.world.options) or state.has(Spell.spirit_warp, self.player),
            LunacidEntrance.ballroom_to_doors: lambda state: self.has_door_key(Door.ballroom_rooms_key, state, self.world.options),
            LunacidEntrance.arena_to_water: lambda state: self.can_jump_given_height(state, "Medium", self.world.options),
            LunacidEntrance.water_to_deep: lambda state: self.can_jump_given_height(state, "High", self.world.options) or
                                                         self.has_key_to_switch(state, Switch.arena_water_switch, self.world.options) or
                                                         state.has(Spell.spirit_warp, self.player),
            LunacidEntrance.water_to_secret: lambda state: self.has_crystal_orb(state, self.world.options),
            LunacidEntrance.labyrinth_of_ash_to_holy_seat_of_gold: lambda state: self.has_door_key(Door.musical_key, state, self.world.options),
        }

        self.location_rules = {
            "Throne of Prince Crilall Fanu": lambda state: self.has_element_access([Elements.light, Elements.dark_and_light, Elements.fire,
                                                                                    Elements.dark_and_fire, Elements.normal_and_fire], state) and
                                                           self.can_level_reasonably(state),
            BaseLocation.wings_rest_demi_orb: lambda state: state.can_reach_region(LunacidRegion.grave_of_the_sleeper, self.player),
            BaseLocation.temple_blood_altar: self.has_blood_spell_access,
            BaseLocation.hollow_basin_dark_item: lambda state: state.has(UniqueItem.enchanted_key, self.player),
            BaseLocation.temple_sewer_puzzle: lambda state: state.has(UniqueItem.vhs_tape, self.player) and
                                                            state.can_reach_region(LunacidRegion.vampire_tomb, self.player) and
                                                            self.has_crystal_orb(state, self.world.options),
            BaseLocation.archives_strange_corpse: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.archives_hidden_room_lower: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.archives_hidden_room_upper: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.archives_daedalus_one: lambda state: self.has_black_book_count(self.world.options, state, 1),
            BaseLocation.archives_daedalus_two: lambda state: self.has_black_book_count(self.world.options, state, 2),
            BaseLocation.archives_daedalus_third: lambda state: self.has_black_book_count(self.world.options, state, 3),
            BaseLocation.sea_pillar: lambda state: state.has_any({Spell.icarian_flight, Spell.rock_bridge}, self.player),
            BaseLocation.chasm_hidden_chest: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.chasm_invisible_cliffside: lambda state: state.has_any([Spell.coffin, Spell.icarian_flight], self.player),
            BaseLocation.tomb_hidden_chest: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.tomb_hidden_room: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.catacombs_hidden_room: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.catacombs_restore_vampire: lambda state: self.has_blood_spell_access(state),
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
            BaseLocation.sand_basement_snake_pit: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.sand_hidden_sarcophagus: lambda state: self.has_crystal_orb(state, self.world.options),
            BaseLocation.sand_chest_overlooking_crypt: lambda state: self.can_jump_given_height(state, "High", self.world.options),
            BaseLocation.sand_lunacid_sandwich: lambda state: state.has(Spell.spirit_warp, self.player),
            BaseLocation.arena_earth_earthen_temple: lambda state: self.can_jump_given_height(state, "High", self.world.options),
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
            BaseLocation.fate_lucid_blade: lambda state: state.has(Weapon.lucid_blade, self.player) or
                                                         self.world.multiworld.get_location(BaseLocation.fate_lucid_blade, self.player).item == Weapon.lucid_blade,

            # Shop Location Runes
            ShopLocation.buy_steel_needle: lambda state: state.has(Voucher.sheryl_initial_voucher, self.player),
            ShopLocation.buy_crossbow: lambda state: state.has(Voucher.sheryl_initial_voucher, self.player),
            ShopLocation.buy_rapier: lambda state: state.has(Voucher.sheryl_initial_voucher, self.player),
            ShopLocation.buy_privateer_musket: lambda state: self.can_purchase_item(state, self.world.options) and
                                                             state.has(Voucher.sheryl_golden_voucher, self.player),
            ShopLocation.buy_oil_lantern: lambda state: self.can_purchase_item(state, self.world.options) and
                                                        state.has(Voucher.sheryl_golden_voucher, self.player),
            ShopLocation.buy_jotunn_slayer: lambda state: self.can_reach_location(state, BaseLocation.fate_lucid_blade)
                                                          and state.has(Voucher.sheryl_dreamer_voucher, self.player),
            ShopLocation.buy_ocean_elixir_patchouli: lambda state: state.has(Voucher.patchouli_simp_discount, self.player),

            # All Drop Location Rules Yikes
            DropLocation.snail_2c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.snail]),
            DropLocation.snail_10c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.snail]),
            DropLocation.snail_ocean: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.snail]),
            DropLocation.snail: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.snail]),
            DropLocation.milk_5c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.milk_snail]),
            DropLocation.milk_10c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.milk_snail]),
            DropLocation.milk_ocean: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.milk_snail]),
            DropLocation.milk_snail: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.milk_snail]),
            DropLocation.shulker_obsidian: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.shulker]),
            DropLocation.shulker_onyx: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.shulker]),
            DropLocation.mummy_knight_onyx: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.mummy_knight]),
            DropLocation.mummy_knight_10c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.mummy_knight]),
            DropLocation.mummy_knight_5c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.mummy_knight]),
            DropLocation.mummy_knight: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.mummy_knight]),
            DropLocation.mummy_mana_vial: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.mummy]),
            DropLocation.mummy_onyx: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.mummy]),
            DropLocation.mummy_2c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.mummy]),
            DropLocation.mummy_10c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.mummy_knight]),
            DropLocation.necronomicon_fire_opal: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.necronomicon]),
            DropLocation.necronomicon_5c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.necronomicon]),
            DropLocation.necronomicon_10c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.necronomicon]),
            DropLocation.necronomicon_mana_vial: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.necronomicon]),
            DropLocation.chimera_light_urn: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.chimera]),
            DropLocation.chimera_holy_water: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.chimera]),
            DropLocation.chimera_drop: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.chimera]),
            DropLocation.enlightened_mana_vial: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.enlightened_one]),
            DropLocation.enlightened_ocean_bone_shell: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.enlightened_one]),
            DropLocation.slime_skeleton: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.slime_skeleton]),
            DropLocation.skeleton_10c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.skeleton] or
                                                                               self.can_reach_any_region(state, self.enemy_regions[Enemy.skeleton_weapon])),
            DropLocation.skeleton_mana_vial: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.skeleton] or
                                                                                     self.can_reach_any_region(state, self.enemy_regions[Enemy.skeleton_weapon])),
            DropLocation.skeleton_onyx: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.skeleton] or
                                                                                self.can_reach_any_region(state, self.enemy_regions[Enemy.skeleton_weapon])),
            DropLocation.skeleton_bones: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.skeleton] or
                                                                                 self.can_reach_any_region(state, self.enemy_regions[Enemy.skeleton_weapon])),
            DropLocation.skeleton_spell: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.skeleton_weapon]),
            DropLocation.skeleton_weapon: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.skeleton_weapon]),
            DropLocation.rat_king_10c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.rat_king]),
            DropLocation.rat_king_lotus_seed: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.rat_king]),
            DropLocation.rat: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.rat]),
            DropLocation.kodama_drop: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.kodama]),
            DropLocation.kodama_2c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.kodama]),
            DropLocation.kodama_10c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.kodama]),
            DropLocation.kodama_opal: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.kodama]),
            DropLocation.yakul_10c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.yakul]),
            DropLocation.yakul_fire_opal: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.yakul]),
            DropLocation.yakul_opal: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.yakul]),
            DropLocation.yakul_health_vial: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.yakul]),
            DropLocation.venus_10c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.venus]),
            DropLocation.venus_yellow_morel: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.venus]),
            DropLocation.venus_dest_angel: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.venus]),
            DropLocation.neptune_10c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.neptune]),
            DropLocation.neptune_yellow_morel: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.neptune]),
            DropLocation.neptune_dest_angel: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.neptune]),
            DropLocation.unilateralis_10c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.unilateralis]),
            DropLocation.unilateralis_yellow_morel: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.unilateralis]),
            DropLocation.unilateralis_dest_angel: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.unilateralis]),
            DropLocation.hemalith_health_vial: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.hemalith]),
            DropLocation.hemalith_shrimp: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.hemalith]),
            DropLocation.hemallith_bloodweed: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.hemalith]),
            DropLocation.mi_go_ocean_bone_shell: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.mi_go]),
            DropLocation.mi_go_10c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.mi_go]),
            DropLocation.mi_go_snowflake_obsidian: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.mi_go]),
            DropLocation.mare_10c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.mare]),
            DropLocation.mare_obsidian: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.mare]),
            DropLocation.mare_onyx: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.mare]),
            DropLocation.painting_fire_opal: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.cursed_painting]),
            DropLocation.painting_10c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.cursed_painting]),
            DropLocation.painting_mana_vial: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.cursed_painting]),
            DropLocation.painting_20c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.cursed_painting]),
            DropLocation.phantom_10c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.phantom]),
            DropLocation.phantom_holy_water: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.phantom]),
            DropLocation.phantom_moon_vial: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.phantom]),
            DropLocation.phantom: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.phantom]),
            DropLocation.phantom_ectoplasm: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.phantom]),
            DropLocation.vampire_5c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.vampire]),
            DropLocation.vampire_vampiric_ashes: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.vampire]),
            DropLocation.vampire_bandage: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.vampire]),
            DropLocation.vampire_page_ashes: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.vampire_page]),
            DropLocation.vampire_page_20c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.vampire_page]),
            DropLocation.vampire_drop: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.vampire_page]),
            DropLocation.malformed_vampiric_ashes: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.malformed]),
            DropLocation.great_bat_health_vial: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.great_bat]),
            DropLocation.great_bat_obsidian: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.great_bat]),
            DropLocation.great_bat_10c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.great_bat]),
            DropLocation.poltergeist_10c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.poltergeist]),
            DropLocation.poltergeist_ectoplasm: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.poltergeist]),
            DropLocation.horse_10c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.malformed_horse]),
            DropLocation.horse_mana_vial: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.malformed_horse]),
            DropLocation.horse_drop: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.malformed_horse]),
            DropLocation.hallowed_husk_10c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.hallowed_husk]),
            DropLocation.hallowed_husk_bones: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.hallowed_husk]),
            DropLocation.hallowed_husk_bandage: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.hallowed_husk]),
            DropLocation.hallowed_husk_light_urn: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.hallowed_husk]),
            DropLocation.hallowed_husk_goldeness: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.hallowed_husk]),
            DropLocation.hallowed_husk_holy_water: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.hallowed_husk]),
            DropLocation.ikkurilb_root: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.ikurrilb]),
            DropLocation.ikkurilb_10c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.ikurrilb]),
            DropLocation.ikkurilb_snowflake_obsidian: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.ikurrilb]),
            DropLocation.mimic_moon_vial: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.mimic]),
            DropLocation.mimic_obsidian: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.mimic]),
            DropLocation.mimic_fools_gold: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.mimic]),
            DropLocation.obsidian_skeleton_10c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.obsidian_skeleton]),
            DropLocation.obsidian_skeleton_bones: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.obsidian_skeleton]),
            DropLocation.obsidian_skeleton_mana_vial: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.obsidian_skeleton]),
            DropLocation.obsidian_skeleton_obsidian: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.obsidian_skeleton]),
            DropLocation.obsidian_skeleton_drop_1: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.obsidian_skeleton]),
            DropLocation.obsidian_skeleton_drop_2: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.obsidian_skeleton]),
            DropLocation.anpu_10c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.anpu]) or
                                                 self.can_reach_any_region(state, self.enemy_regions[Enemy.anpu_sword]),
            DropLocation.anpu_fire_opal: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.anpu]) or
                                                 self.can_reach_any_region(state, self.enemy_regions[Enemy.anpu_sword]),
            DropLocation.anpu_drop_1: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.anpu_sword]),
            DropLocation.anpu_drop_2: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.anpu]),
            DropLocation.serpent_antidote: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.serpent]),
            DropLocation.serpent_5c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.serpent]),
            DropLocation.embalmed_bandage: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.embalmed]),
            DropLocation.embalmed_ashes: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.embalmed]),
            DropLocation.embalmed_bones: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.embalmed]),
            DropLocation.jailor_drop: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.jailor]),
            DropLocation.jailor_10c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.jailor]),
            DropLocation.jailor_candle: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.jailor]),
            DropLocation.jailor_bandage: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.jailor]),
            DropLocation.jailor_health_vial: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.jailor]),
            DropLocation.jailor_angel: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.jailor]),
            DropLocation.lunam_ectoplasm: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.lunam]),
            DropLocation.lunam_10c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.lunam]),
            DropLocation.lunam_snowflake_obsidian: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.lunam]),
            DropLocation.giant_spell: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.giant_skeleton]),
            DropLocation.giant_dark_urn: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.giant_skeleton]),
            DropLocation.giant_bones: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.giant_skeleton]),
            DropLocation.giant_mana_vial: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.giant_skeleton]),
            DropLocation.giant_onyx: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.giant_skeleton]),
            DropLocation.lupine_spell: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.lupine_skeleton]),
            DropLocation.lupine_bones: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.lupine_skeleton]),
            DropLocation.lupine_onyx: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.lupine_skeleton]),
            DropLocation.lupine_10c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.lupine_skeleton]),
            DropLocation.infested_antidote: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.infested_corpse]),
            DropLocation.infested_bones: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.infested_corpse]),
            DropLocation.sucsarian_drop_1: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.sucsarian_dagger]),
            DropLocation.sucsarian_drop_2: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.sucsarian_spear]),
            DropLocation.sucsarian_10c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.sucsarian_spear] or
                                                                                self.can_reach_any_region(state, self.enemy_regions[Enemy.sucsarian_dagger])),
            DropLocation.sucsarian_obsidian: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.sucsarian_spear] or
                                                                                     self.can_reach_any_region(state, self.enemy_regions[Enemy.sucsarian_dagger])),
            DropLocation.sucsarian_snowflake_obsidian: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.sucsarian_spear] or
                                                                                               self.can_reach_any_region(state, self.enemy_regions[Enemy.sucsarian_dagger])),
            DropLocation.sucsarian_throwing_knife: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.sucsarian_spear] or
                                                                                           self.can_reach_any_region(state, self.enemy_regions[Enemy.sucsarian_dagger])),
            DropLocation.vesta_fairy_moss: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.vesta]),
            DropLocation.vesta_yellow_morel: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.vesta]),
            DropLocation.vesta_dest_angel: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.vesta]),
            DropLocation.ceres_fairy_moss: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.ceres]),
            DropLocation.ceres_yellow_morel: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.ceres]),
            DropLocation.ceres_dest_angel: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.ceres]),
            DropLocation.gloom_fairy_moss: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.gloom_wood]),
            DropLocation.gloom_health_vial: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.gloom_wood]),
            DropLocation.gloom_dest_angel: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.gloom_wood]),
            DropLocation.cetea_drop: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.cetea]),
            DropLocation.cetea_10c: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.cetea]),
            DropLocation.cetea_ocean_bone_shell: lambda state: self.can_reach_any_region(state, self.enemy_regions[Enemy.cetea]),
            DropLocation.sea_demon: lambda state: self.can_reach_any_region(state, immovable_enemies[Enemy.demon]),
            DropLocation.sanguis_book: lambda state: state.can_reach_region(LunacidRegion.holy_battleground, self.player),

            # All Quenchsanity Rules
            Quench.rapier: lambda state: self.can_get_weapon(state, Weapon.rapier, self.world.options),
            Quench.shadow_blade: lambda state: self.can_get_weapon(state, Weapon.shadow_blade, self.world.options),
            Quench.shining_blade: lambda state: self.can_get_weapon(state, Weapon.shining_blade, self.world.options),
            Quench.rusted_sword: lambda state: self.can_get_weapon(state, Weapon.rusted_sword, self.world.options),
            Quench.torch: lambda state: self.can_get_weapon(state, Weapon.torch, self.world.options),
            Quench.replica_sword: lambda state: self.can_get_weapon(state, Weapon.replica_sword, self.world.options),
            Quench.obsidian_poisonguard: lambda state: self.can_get_weapon(state, Weapon.obsidian_poisonguard, self.world.options),
            Quench.obsidian_cursebrand: lambda state: self.can_get_weapon(state, Weapon.obsidian_cursebrand, self.world.options),
            Quench.lyrian_longsword: lambda state: self.can_get_weapon(state, Weapon.lyrian_longsword, self.world.options),
            Quench.elfen_sword: lambda state: self.can_get_weapon(state, Weapon.elfen_sword, self.world.options),
            Quench.crossbow: lambda state: self.can_get_weapon(state, Weapon.crossbow, self.world.options),
            Quench.broken_lance: lambda state: self.can_get_weapon(state, Weapon.broken_lance, self.world.options),
            Quench.broken_hilt: lambda state: self.can_get_weapon(state, Weapon.broken_hilt, self.world.options),
            Quench.brittle_arming_sword: lambda state: self.can_get_weapon(state, Weapon.brittle_arming_sword, self.world.options),
            Quench.stone_club: lambda state: self.can_get_weapon(state, Weapon.stone_club, self.world.options),
            Quench.iron_club: lambda state: self.can_get_weapon(state, Weapon.iron_club, self.world.options),
            Quench.iron_claw: lambda state: self.can_get_weapon(state, Weapon.iron_claw, self.world.options),
            Quench.steel_claw: lambda state: self.can_get_weapon(state, Weapon.steel_claw, self.world.options),
            Quench.obsidian_seal: lambda state: self.can_get_weapon(state, Weapon.obsidian_seal, self.world.options),
            Quench.scythe: lambda state: self.can_kill_death(state, self.world.options),

            # All Etna's Pupil Rules
            AlchemyLocation.explosives: lambda state: self.can_obtain_all_alchemy_items([Alchemy.ashes, Alchemy.fire_opal], state, self.world.options),
            AlchemyLocation.knife: lambda state: self.can_obtain_alchemy_item(Alchemy.ocean_bone_shard, state, self.world.options),
            AlchemyLocation.health: lambda state: self.can_obtain_all_alchemy_items([Alchemy.opal, Alchemy.yellow_morel, Alchemy.lotus_seed_pod],
                                                                                    state, self.world.options),
            AlchemyLocation.mana: lambda state: self.can_obtain_all_alchemy_items([Alchemy.opal, Alchemy.onyx, Alchemy.lotus_seed_pod], state,
                                                                                  self.world.options),
            AlchemyLocation.moonlight: lambda state: self.can_obtain_all_alchemy_items([Alchemy.ashes, Alchemy.moon_petal, Alchemy.obsidian], state,
                                                                                       self.world.options),
            AlchemyLocation.spectral: lambda state: self.can_obtain_all_alchemy_items([Alchemy.ectoplasm, Alchemy.ikurrilb_root, Alchemy.fire_opal], state,
                                                                                      self.world.options),
            AlchemyLocation.poison_knife: lambda state: self.can_obtain_all_alchemy_items([Alchemy.destroying_angel_mushroom, Alchemy.ocean_bone_shell], state,
                                                                                          self.world.options),
            AlchemyLocation.staff_of_osiris: lambda state: self.can_obtain_all_alchemy_items([Alchemy.onyx, Alchemy.ikurrilb_root, Alchemy.bones], state,
                                                                                             self.world.options),
            AlchemyLocation.poison_urn: lambda state: self.can_obtain_all_alchemy_items([Alchemy.destroying_angel_mushroom, Alchemy.ocean_bone_shard,
                                                                                         Alchemy.bloodweed], state, self.world.options),
            AlchemyLocation.fairy_moss: lambda state: self.can_obtain_all_alchemy_items([Alchemy.moon_petal, Alchemy.bloodweed, Alchemy.yellow_morel], state,
                                                                                        self.world.options),
            AlchemyLocation.antidote: lambda state: self.can_obtain_all_alchemy_items([Alchemy.destroying_angel_mushroom, Alchemy.lotus_seed_pod], state,
                                                                                      self.world.options),
            AlchemyLocation.banner: lambda state: self.can_obtain_all_alchemy_items([Alchemy.ashes, Alchemy.bones], state,
                                                                                    self.world.options),
            AlchemyLocation.holy: lambda state: self.can_obtain_all_alchemy_items([Alchemy.moon_petal, Alchemy.opal], state,
                                                                                  self.world.options),
            AlchemyLocation.warp: lambda state: self.can_obtain_all_alchemy_items([Alchemy.snowflake_obsidian, Alchemy.onyx, Alchemy.obsidian], state,
                                                                                  self.world.options),
            AlchemyLocation.wisp: lambda state: self.can_obtain_all_alchemy_items([Alchemy.snowflake_obsidian, Alchemy.ectoplasm, Alchemy.moon_petal], state,
                                                                                  self.world.options),
            AlchemyLocation.limbo: lambda state: state.has_all([Alchemy.broken_sword, Alchemy.fractured_life, Alchemy.fractured_death], self.player),
        }

    def is_vampire(self, options: LunacidOptions):
        return options.starting_class == options.starting_class.option_vampire

    def can_reach_any_region(self, state: CollectionState, spots: List[str]):
        for spot in spots:
            if state.can_reach_region(spot, self.player):
                return True
        return False

    def can_reach_all_regions(self, state: CollectionState, spots: List[str]):
        all_rule = True
        for spot in spots:
            all_rule = all_rule and state.can_reach_region(spot, self.player)
        return all_rule

    def can_reach_location(self, state: CollectionState, spot: str):
        return state.can_reach(spot, "Location", self.player)

    def can_jump_given_height(self, state: CollectionState, height: str, options: LunacidOptions) -> bool:
        if height == "Low":
            return True
        elif height == "Medium":
            medium_spells = {Spell.barrier, Spell.icarian_flight, Spell.coffin, Spell.rock_bridge}
            movement_item_rule = True
            if options.dropsanity != options.dropsanity.option_off:
                medium_spells.add(MobSpell.summon_snail)
            return state.has_any(medium_spells, self.player) & movement_item_rule
        else:
            high_spells = {Spell.barrier, Spell.rock_bridge, Spell.icarian_flight}
            return state.has_any(high_spells, self.player)

    def has_door_key(self, key: str, state: CollectionState, options: LunacidOptions) -> bool:
        return options.door_locks == options.door_locks.option_false or state.has(key, self.player)

    def has_light_source(self, state: CollectionState) -> bool:
        sources = base_light_sources.copy()
        sources.extend(source for source in shop_light_sources)
        return state.has_any(sources, self.player)

    def can_level_reasonably(self, state: CollectionState):
        can_you = self.can_reach_any_region(state, [LunacidRegion.forbidden_archives_2, LunacidRegion.boiling_grotto, LunacidRegion.yosei_forest,
                                                    LunacidRegion.sealed_ballroom, LunacidRegion.fetid_mire, LunacidRegion.forest_canopy,
                                                    LunacidRegion.forlorn_arena, LunacidRegion.castle_le_fanu_white, LunacidRegion.castle_le_fanu_red,
                                                    LunacidRegion.sanguine_sea, LunacidRegion.terminus_prison, LunacidRegion.temple_of_silence_secret])
        return can_you

    def has_spell(self, spell: str, state: CollectionState):
        return state.has(spell, self.player)

    def has_all_spells(self, spells: List[str], state: CollectionState):
        return state.has_all(spells, self.player)

    def has_every_spell(self, state: CollectionState, options: LunacidOptions, starting_weapon: str = None) -> bool:
        every_spell = list(set.union(set(Spell.base_spells), set(MobSpell.drop_spells)))
        if starting_weapon is not None and starting_weapon in every_spell:
            every_spell.remove(starting_weapon)
        mob_spell_regions = [LunacidRegion.forlorn_arena, LunacidRegion.castle_le_fanu_red, LunacidRegion.castle_le_fanu_white,
                             LunacidRegion.terminus_prison_dark,
                             LunacidRegion.labyrinth_of_ash, LunacidRegion.boiling_grotto, LunacidRegion.forbidden_archives_3, LunacidRegion.sand_temple,
                             LunacidRegion.temple_of_silence_interior, LunacidRegion.sealed_ballroom]
        if options.dropsanity == options.dropsanity.option_off:
            every_spell = Spell.base_spells
            return self.has_all_spells(every_spell, state) and self.can_reach_all_regions(state, mob_spell_regions)
        else:
            return self.has_all_spells(every_spell, state)

    def can_purchase_item(self, state: CollectionState, options: LunacidOptions) -> bool:
        if options.shopsanity == options.shopsanity.option_false:
            return True
        return state.can_reach_region(LunacidRegion.boiling_grotto, self.player) and state.has(Spell.ignis_calor, self.player)

    def has_blood_spell_access(self, state: CollectionState) -> bool:
        return state.has_any(blood_spells, self.player)

    def has_keys_for_basin_door(self, state: CollectionState, options: LunacidOptions) -> bool:
        if options.shopsanity == options.shopsanity.option_false:
            return True
        if options.entrance_randomization == options.entrance_randomization.option_true:
            return state.has(UniqueItem.enchanted_key, self.player, 2)
        else:
            return state.has(UniqueItem.enchanted_key, self.player)

    def has_keys_for_canopy(self, state: CollectionState, options: LunacidOptions) -> bool:
        if options.shopsanity == options.shopsanity.option_false:
            return state.has(UniqueItem.enchanted_key, self.player)
        return state.has(UniqueItem.enchanted_key, self.player, 2)

    def has_key_to_switch(self, state: CollectionState, key: str, options: LunacidOptions) -> bool:
        return options.switch_locks == options.switch_locks.option_false or state.has(key, self.player)

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
        return state.has_any(element_options, self.player) or state.has(Weapon.wand_of_power, self.player)

    def has_ranged_element_access(self, element: str | List[str], state: CollectionState):
        if isinstance(element, str):
            element = [element]
        ranged_options = [item for item in ranged_weapons]
        ranged_options.extend([item for item in ranged_spells])
        element_options = [item for item in self.elements if self.elements[item] in element and item in ranged_options]
        return state.has_any(element_options, self.player)

    def has_coins_for_door(self, options: LunacidOptions, state: CollectionState):
        return state.has(Coins.strange_coin, self.player, options.required_strange_coin.value)

    def has_black_book_count(self, options: LunacidOptions, state: CollectionState, amount: int):
        if options.dropsanity == options.dropsanity.option_off:
            can_reach_battle = state.can_reach_region(LunacidRegion.holy_battleground, self.player)
            if amount == 1:
                return can_reach_battle or state.has(UniqueItem.black_book, self.player)
            if amount == 2:
                split_case = can_reach_battle and state.has(UniqueItem.black_book, self.player)
                return split_case or state.has(UniqueItem.black_book, self.player, 2)
            if amount == 3:
                return can_reach_battle and state.has(UniqueItem.black_book, self.player, 2)
        else:
            return state.has(UniqueItem.black_book, self.player, amount)

    def can_buy_jotunn(self, options: LunacidOptions, state: CollectionState):
        if options.shopsanity == options.shopsanity.option_true:
            return state.has(Weapon.jotunn_slayer, self.player)
        return self.can_reach_location(state, BaseLocation.fate_lucid_blade) and state.has(Voucher.sheryl_dreamer_voucher, self.player)

    def can_defeat_the_prince(self, state: CollectionState):
        return (self.has_element_access([Elements.light, Elements.dark_and_light], state) and
                self.can_reach_any_region(state, [LunacidRegion.castle_le_fanu_white, LunacidRegion.forbidden_archives_2,
                                                  LunacidRegion.sealed_ballroom, LunacidRegion.boiling_grotto, LunacidRegion.forlorn_arena]))

    def can_reach_monster(self, enemy: str, state: CollectionState):
        locations = all_drops_by_enemy[enemy]
        return self.can_reach_any_region(state, locations)

    def can_get_weapon(self, state: CollectionState, weapon: str, options: LunacidOptions):
        if weapon in Weapon.base_weapons:
            return state.has(weapon, self.player)
        elif weapon in Weapon.shop_weapons:
            if options.shopsanity == options.shopsanity.option_true:
                return state.has(weapon, self.player)
            else:
                return state.has(Voucher.sheryl_initial_voucher, self.player)
        if weapon in Weapon.drop_weapons:
            if options.dropsanity != options.dropsanity.option_off:
                return state.has(weapon, self.player)
            for enemy in all_drops_by_enemy:
                if weapon in all_drops_by_enemy[enemy]:
                    return self.can_reach_any_region(state, self.enemy_regions[enemy])
        if weapon in Weapon.quenchsanity_weapons:
            return state.has(weapon, self.player)
        return False

    def can_kill_death(self, state: CollectionState, options: LunacidOptions):
        if options.etnas_pupil == options.etnas_pupil.option_true:
            return state.has(Weapon.limbo, self.player) and state.can_reach_region(LunacidRegion.mausoleum, self.player),

        return state.has_all({Alchemy.fractured_life, Alchemy.fractured_death, Alchemy.broken_sword},
                             self.player) and state.can_reach_region(LunacidRegion.mausoleum, self.player),

    def can_obtain_alchemy_item(self, alchemy_item: str, state: CollectionState, options: LunacidOptions):
        if options.dropsanity == options.dropsanity.option_randomized:
            return state.has(alchemy_item, self.player)
        acceptable_regions = []
        for enemy in all_drops_by_enemy:
            if alchemy_item in all_drops_by_enemy[enemy]:
                for region in self.enemy_regions[enemy]:
                    if region not in acceptable_regions:
                        acceptable_regions.append(region)
        for plant in all_alchemy_plant_data:
            if alchemy_item == plant.drop:
                for region in plant.regions:
                    if region not in acceptable_regions:
                        acceptable_regions.append(region)
        return self.can_reach_any_region(state, acceptable_regions)

    def can_obtain_all_alchemy_items(self, alchemy_items: List[str], state: CollectionState, options: LunacidOptions):
        alchemy_rule = False
        for item in alchemy_items:
            alchemy_rule = alchemy_rule and self.can_obtain_alchemy_item(item, state, options)
        return alchemy_rule

    def set_lunacid_rules(self, world_elements: Dict[str, str], enemy_regions: Dict[str, List[str]]) -> None:
        multiworld = self.world.multiworld
        self.elements = world_elements
        self.enemy_regions = enemy_regions
        for region in multiworld.get_regions(self.player):
            if region.name in self.region_rules:
                for entrance in region.entrances:
                    entrance.access_rule = self.region_rules[region.name]
                for location in region.locations:
                    location.access_rule = self.region_rules[region.name]
            for entrance in region.entrances:
                multiworld.register_indirect_condition(region, entrance)
                if entrance.name in self.entrance_rules:
                    entrance.access_rule = entrance.access_rule and self.entrance_rules[entrance.name]
            for loc in region.locations:
                if loc.name in self.location_rules:
                    loc.access_rule = loc.access_rule and self.location_rules[loc.name]

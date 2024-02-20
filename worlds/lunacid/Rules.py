from BaseClasses import CollectionState, MultiWorld
from typing import Dict, List, Tuple, TYPE_CHECKING
from ..generic.Rules import set_rule, CollectionRule

from .data.spell_data import all_spells, spell_drop_locations, light_spells, blood_spells, spell_light_sources, jump_spells
from .data.weapon_data import light_weapons, ranged_weapons, weapon_light_sources
from .data.item_data import item_light_sources
from .Options import LunacidOptions
from .strings.regions_entrances import LunacidEntrance, LunacidRegion
from .strings.spells import Spell, MobSpell
from .strings.items import UniqueItem, Progressives, Switch, Alchemy
from .strings.locations import BaseLocation, ShopLocation
from .strings.weapons import Weapon

if TYPE_CHECKING:
    from . import LunacidWorld


class LunacidRules:
    player: int
    world: "LunacidWorld"
    region_rules: Dict[str, CollectionRule]
    entrance_rules: Dict[str, CollectionRule]
    location_rules: Dict[str, CollectionRule]

    def __init__(self, world: "LunacidWorld") -> None:
        self.player = world.player
        self.world = world
        self.world.options = world.options

        self.region_rules = {
            LunacidRegion.temple_of_silence_entrance: lambda state: self.has_light_source(state) and self.has_keys_for_basin_door(state, self.world.options),
            LunacidRegion.temple_of_silence_interior: lambda state: self.has_light_source(state) and
                                                                    self.has_key_to_switch(state, Switch.temple_switch, self.world.options),
            LunacidRegion.forest_canopy: lambda state: self.has_keys_for_canopy(state, self.world.options),
            LunacidRegion.throne_chamber: lambda state: state.has(Progressives.vampiric_symbol, self.player, 3),
            LunacidRegion.terminus_prison: lambda state: state.has("Defeat Prince Crilall Fanu", self.player),
            LunacidRegion.castle_le_fanu_white: lambda state: state.has(Progressives.vampiric_symbol, self.player, 1),
            LunacidRegion.castle_le_fanu_blue: lambda state: state.has(Progressives.vampiric_symbol, self.player, 2),
            LunacidRegion.chamber_of_fate: lambda state: state.has_all({UniqueItem.earth_talisman, UniqueItem.water_talisman}, self.player),
            LunacidRegion.sealed_ballroom: lambda state: self.has_poison_dark_blood_access(state, self.world.options),
            LunacidRegion.vampire_tomb: lambda state: self.has_key_to_switch(state, Switch.tomb_lightning_gate_2, self.world.options),
            LunacidRegion.mausoleum: lambda state: self.has_key_to_switch(state, Switch.tomb_lightning_gate_1, self.world.options) and
                                                   self.has_light_source(state),
            LunacidRegion.sand_temple: lambda state: self.has_all_keys_to_switch(state,
                                                                            [Switch.grotto_valve_switch_1, Switch.grotto_valve_switch_2],
                                                                            self.world.options),
            LunacidRegion.forlorn_arena: lambda state: self.has_key_to_switch(state, Switch.prison_arena_switch, self.world.options),
            LunacidRegion.terminus_prison_dark: lambda state: self.has_key_to_switch(state, Switch.prison_shortcut_switch, self.world.options) or
                                                              state.has(Spell.icarian_flight, self.player)

        }

        self.entrance_rules = {
            LunacidEntrance.basin_to_archives: lambda state: state.has_any({Spell.rock_bridge, Spell.coffin}, self.player),
            LunacidEntrance.archives_to_chasm: lambda state: state.has(Progressives.vampiric_symbol, self.player, 2) and
                                                             state.has(Spell.icarian_flight, self.player),
            LunacidEntrance.wings_to_surface: lambda state: state.has_all({Spell.icarian_flight, Spell.spirit_warp}, self.player) or
                                                            (state.has(Spell.icarian_flight, self.player) and self.can_reach_region(
                                                                state, LunacidRegion.temple_of_silence_interior)),
            LunacidEntrance.basin_to_surface: lambda state: state.has_all({Spell.icarian_flight, Spell.spirit_warp}, self.player) or
                                                            (state.has(Spell.icarian_flight, self.player) and state.can_reach(
                                                                LunacidRegion.temple_of_silence_interior, None, self.player)),
            LunacidEntrance.yosei_to_yosei_lower: lambda state: self.can_jump_high(state) or self.has_blood_spell_access(state),
            LunacidEntrance.castle_to_red: self.has_blood_spell_access,
            LunacidEntrance.archives_3_to_archives_1b: lambda state: self.has_key_to_switch(state, Switch.archives_elevator_switch_1_to_3, self.world.options),
            LunacidEntrance.archives_2_to_archives_1: lambda state: self.has_key_to_switch(state, Switch.archives_elevator_switch_1_to_2, self.world.options),
            LunacidEntrance.archives_2_to_archives_3: lambda state: self.has_key_to_switch(state, Switch.archives_elevator_switch_2_to_3, self.world.options)
                                                                    and self.has_key_to_switch(state, Switch.archives_elevator_switch_1_to_2, self.world.options),
        }

        self.location_rules = {
            BaseLocation.temple_blood_altar: self.has_blood_spell_access,
            BaseLocation.archives_daedalus_one: lambda state: state.has(UniqueItem.black_book, self.player),
            BaseLocation.archives_daedalus_two: lambda state: state.has(UniqueItem.black_book, self.player, 2),
            BaseLocation.archives_daedalus_third: lambda state: state.has(UniqueItem.black_book, self.player, 3),
            BaseLocation.sea_pillar: lambda state: state.has_any({Spell.icarian_flight, Spell.rock_bridge}, self.player),
            BaseLocation.tomb_demi_chest: self.can_jump_high,
            BaseLocation.mausoleum_upper_table: self.can_jump_high,
            BaseLocation.mausoleum_kill_death: lambda state: state.has_all({Alchemy.fractured_life, Alchemy.fractured_death, Alchemy.broken_sword},
                                                                           self.player),
            BaseLocation.corrupted_room: lambda state: state.has(UniqueItem.corrupted_key, self.player),
            BaseLocation.yosei_hanging_in_trees: lambda state: state.has_any(ranged_weapons, self.player),
            BaseLocation.castle_upper_floor_coffin_double: lambda state: state.has(Progressives.vampiric_symbol, self.player, 3),
            BaseLocation.prison_f3_bottomless_pit: lambda state: state.has_any({Spell.icarian_flight, Spell.spirit_warp}, self.player),
            BaseLocation.throne_book: lambda state: state.has("Defeat Prince Crilall Fanu", self.player),
            BaseLocation.sand_chest_overlooking_crypt: self.can_jump_high,
            BaseLocation.arena_water_underwater_temple: lambda state: state.has_any({Spell.icarian_flight, Spell.rock_bridge}, self.player),
            BaseLocation.arena_earth_earthen_temple: self.can_jump_high,
            "Free Sir Hicket": lambda state: state.has(Spell.ignis_calor, self.player),
            ShopLocation.buy_ocean_elixir_sheryl: lambda state: self.can_purchase_item(state, self.world.options),
            ShopLocation.buy_privateer_musket: lambda state: self.can_purchase_item(state, self.world.options),
            ShopLocation.buy_oil_lantern: lambda state: self.can_purchase_item(state, self.world.options),
            ShopLocation.buy_jotunn_slayer: lambda state: self.can_reach_location(state, "LA: The Weapon to Kill an Immortal")
        }

    def can_reach_region(self, state: CollectionState, spot: str):
        return state.can_reach(spot, "Region", self.player)

    def can_reach_location(self, state: CollectionState, spot: str):
        return state.can_reach(spot, "Location", self.player)

    def can_jump_high(self, state: CollectionState) -> bool:
        return state.has_any(jump_spells, self.player)

    def has_light_source(self, state: CollectionState) -> bool:
        sources = []
        sources.extend(source for source in spell_light_sources)
        sources.extend(source for source in weapon_light_sources)
        sources.extend(source for source in item_light_sources)
        return state.has_any(sources, self.player)

    def can_reach_spell_drop(self, state: CollectionState, drop: str) -> bool:
        drop_locations = spell_drop_locations[drop]
        drop_rule = True
        for locations in drop_locations:
            drop_rule += state.can_reach(locations, "Location", self.player)
        return drop_rule

    def can_reach_every_spell_drop_region(self, state: CollectionState) -> bool:
        drop_rule = True
        for drop in spell_drop_locations:
            drop_rule += self.can_reach_spell_drop(state, drop)
        return drop_rule

    def has_every_spell(self, state: CollectionState) -> bool:
        return state.has_all({spell.name for spell in all_spells}, self.player) & self.can_reach_every_spell_drop_region(state)

    def can_purchase_item(self, state: CollectionState, options: LunacidOptions) -> bool:
        if options.shopsanity == options.shopsanity.option_false:
            return True
        return state.has("Sir Hicket's Freedom from Armor", self.player)

    def has_light_element_access(self, state: CollectionState) -> bool:
        return state.has_any(light_spells + light_weapons, self.player)

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
        if options.switchlocks == options.switchlocks.option_false:
            return True
        return state.has(key, self.player)

    def has_all_keys_to_switch(self, state: CollectionState, keys: List[str], options: LunacidOptions) -> bool:
        rule = True
        for key in keys:
            rule = rule and self.has_key_to_switch(state, key, options)
        return rule

    def has_poison_dark_blood_access(self, state: CollectionState, options: LunacidOptions) -> bool:
        poison_or_dark_attacks = [Spell.slime_orb, Spell.blood_strike]
        if options.dropsanity == options.dropsanity.option_true:
            poison_or_dark_attacks.append(MobSpell.dark_skull)
        if options.shopsanity == options.shopsanity.option_true:
            poison_or_dark_attacks.append(Weapon.privateer_musket)
        return state.has_any(poison_or_dark_attacks, self.player)

    def set_lunacid_rules(self) -> None:
        multiworld = self.world.multiworld

        for region in multiworld.get_regions(self.player):
            if region.name in self.region_rules:
                for entrance in region.entrances:
                    entrance.access_rule = self.region_rules[region.name]
            for entrance in region.entrances:
                if entrance.name in self.entrance_rules:
                    entrance.access_rule = entrance.access_rule and self.entrance_rules[entrance.name]
            for loc in region.locations:
                if loc.name in self.location_rules:
                    loc.access_rule = self.location_rules[loc.name]


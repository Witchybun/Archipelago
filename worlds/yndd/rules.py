from BaseClasses import CollectionState
from typing import Dict, List, TYPE_CHECKING

from worlds.generic.Rules import CollectionRule

from .options import DreamOptions
from .strings.regions_entrances import DreamRegions, DreamEntrances
from .strings.items import Abilities, NexusDoors, Game, NasuItem, DockItem, WildernessItem, MallItem, Movement, Glitch, \
    ConnectorKeys, AoOniItem, Songs, WitchAdventureItem, SchoolItem, BlockItem, GoalItems, ApartmentItem
from .strings.locations import Streets, Wilderness, Nasu, Docks, AoOni, WitchAdventure, Mall, School, Sewer, Blocks

if TYPE_CHECKING:
    from . import DreamWorld


class DreamRules:
    player: int
    world: "DreamWorld"
    region_rules: Dict[str, CollectionRule]
    entrance_rules: Dict[str, CollectionRule]
    location_rules: Dict[str, CollectionRule]
    doors: Dict[str, bool]

    def __init__(self, world: "DreamWorld") -> None:
        self.player = world.player
        self.world = world
        self.world.options = world.options
        self.doors = self.world.doors

        self.region_rules = {
            DreamRegions.streets: lambda state: self.can_run(state),
            DreamRegions.mannequin_room: lambda state: self.can_jump(state) and
                                                       (self.can_run(state) or state.has(Abilities.lantern, self.player)),
            DreamRegions.docks_lighthouse: lambda state: self.can_run(state) and self.can_jump(state),
        }

        self.entrance_rules = {
            DreamEntrances.nasu_game_path: lambda state: state.has(Game.nasu, self.player),
            DreamEntrances.ao_oni_game_path: lambda state: state.has(Game.ao_oni, self.player),
            DreamEntrances.ao_oni_1_to_2: lambda state: self.can_reach_level_in_ao_oni(state, 1),
            DreamEntrances.ao_oni_2_to_3: lambda state: self.can_reach_level_in_ao_oni(state, 2),
            DreamEntrances.ao_oni_3_to_4: lambda state: self.can_reach_level_in_ao_oni(state, 3),
            DreamEntrances.ao_oni_4_to_5: lambda state: self.can_reach_level_in_ao_oni(state, 4),
            DreamEntrances.witch_game_path: lambda state: state.has(Game.witch_adventure, self.player),

            DreamEntrances.streets_to_sewers: lambda state: self.has_key_for_connector(ConnectorKeys.street_to_sewers, state),
            DreamEntrances.sewers_to_streets: lambda state: self.has_key_for_connector(ConnectorKeys.street_to_sewers, state),
            DreamEntrances.streets_to_butcher_front: lambda state: self.can_run(state),
            DreamEntrances.butcher_feeding_to_road: lambda state: self.can_climb(state),
            DreamEntrances.road_to_monoe: lambda state: state.has(Abilities.knife, self.player),

            DreamEntrances.wilderness_homes_doors: lambda state: state.has(DockItem.boards, self.player) and
                                                                 state.has(WildernessItem.red_eye, self.player) and
                                                                 self.can_run(state) and self.can_jump(state),
            DreamEntrances.wilderness_town_to_sewers: lambda state: self.has_key_for_connector(ConnectorKeys.wilderness_to_sewers, state),
            DreamEntrances.sewers_to_wilderness_town: lambda state: self.has_key_for_connector(ConnectorKeys.wilderness_to_sewers, state),
            DreamEntrances.third_train: lambda state: self.has_key_for_connector(ConnectorKeys.wilderness_to_docks, state),
            DreamEntrances.fourth_train: lambda state: self.has_key_for_connector(ConnectorKeys.wilderness_to_docks, state),
            DreamEntrances.hamsa_path: lambda state: state.has(Abilities.hamsa, self.player),
            DreamEntrances.temple_base_to_garden: lambda state: state.has(WildernessItem.sun, self.player) and
                                                                state.has(WildernessItem.moon, self.player) and
                                                                state.has(WildernessItem.war, self.player) and
                                                                state.has(WildernessItem.death, self.player),

            DreamEntrances.storage_to_sewers: lambda state: self.has_key_for_connector(ConnectorKeys.mall_to_sewers, state),
            DreamEntrances.sewers_to_storage: lambda state: self.has_key_for_connector(ConnectorKeys.mall_to_sewers, state),
            DreamEntrances.upper_storage_to_roof: lambda state: state.has(MallItem.rooftop_key, self.player),
            DreamEntrances.enter_mannequin_room: lambda state: state.has(MallItem.warehouse_key, self.player),

            DreamEntrances.dock_train_to_lighthouse: lambda state: state.has(DockItem.sad_fish, self.player),
            DreamEntrances.fisher_to_w: lambda state: self.can_jump(state),
            DreamEntrances.crate_to_scale: lambda state: self.can_run(state),

            DreamEntrances.school_front_to_first: lambda state: self.needs_item_or_pinch_skip(state, Abilities.umbrella),
            DreamEntrances.school_third_to_bathroom: lambda state: state.has(SchoolItem.key, self.player),
            DreamEntrances.school_third_to_storm: lambda state: self.needs_item_or_pinch_skip(state, SchoolItem.photo),
            DreamEntrances.school_storm_to_front: lambda state: state.has(Abilities.umbrella, self.player) and self.can_jump(state)
                                                                and state.has(MallItem.valve, self.player),
            DreamEntrances.school_storm_front_to_lever: lambda state: state.has(SchoolItem.lever, self.player),

            DreamEntrances.blocks_to_snow: lambda state: state.has(BlockItem.girl, self.player, 6),

            DreamEntrances.nexus_to_streets: lambda state: self.can_enter_door("Streets", state),
            DreamEntrances.nexus_to_wilderness: lambda state: self.can_enter_door("Wilderness", state),
            DreamEntrances.nexus_to_docks: lambda state: self.can_enter_door("Docks", state),
            DreamEntrances.nexus_to_mall: lambda state: self.can_enter_door("Mall", state),
            DreamEntrances.nexus_to_school: lambda state: self.can_enter_door("School", state),
            DreamEntrances.nexus_to_sewers: lambda state: self.can_enter_door("Sewers", state),
            DreamEntrances.nexus_to_apartment: lambda state: self.can_enter_apartment(state),

            DreamEntrances.apartment_top_to_roof: lambda state: state.has(ApartmentItem.key, self.player),
            DreamEntrances.apartment_roof_to_ufo: lambda state: self.can_enter_ufo(state),

            DreamEntrances.to_normal_end: lambda state: state.has(Abilities.umbrella, self.player) and self.can_jump(state),
            DreamEntrances.to_secret_end: lambda state: self.can_play_song(Songs.finale, state),
        }

        self.location_rules = {
            Nasu.nasu_points_3: lambda state: state.has(NasuItem.nasu_get, self.player),
            Nasu.nasu_points_4: lambda state: state.has(NasuItem.nasu_get, self.player),
            Nasu.nasu_points_5: lambda state: state.has(NasuItem.nasu_get, self.player) and state.has(NasuItem.doubler, self.player),
            Nasu.nasu_points_6: lambda state: state.has(NasuItem.nasu_get, self.player) and state.has(NasuItem.doubler, self.player),

            AoOni.floor_1_mansion_key: lambda state: state.has(AoOniItem.key, self.player),
            AoOni.floor_2_mansion_key: lambda state: state.has(AoOniItem.key, self.player, 2),
            AoOni.floor_3_mansion_key: lambda state: state.has(AoOniItem.key, self.player, 3),
            AoOni.floor_4_mansion_key: lambda state: state.has(AoOniItem.key, self.player, 4),
            AoOni.floor_5_mansion_key: lambda state: state.has(AoOniItem.key, self.player, 5),

            WitchAdventure.boss_2: lambda state: state.has(WitchAdventureItem.heart_container, self.player),
            WitchAdventure.boss_3: lambda state: state.has(WitchAdventureItem.heart_container, self.player, 2),
            WitchAdventure.boss_4: lambda state: state.has(WitchAdventureItem.heart_container, self.player, 3) and
                                                 state.has(WitchAdventureItem.heal_unlock, self.player),
            WitchAdventure.boss_5: lambda state: state.has(WitchAdventureItem.heart_container, self.player, 4) and
                                                 state.has(WitchAdventureItem.heal_unlock, self.player),

            Streets.diary_2: lambda state: state.has(Abilities.knife, self.player) and self.can_climb(state) and
                                           self.can_run(state),
            Streets.diary_secret: lambda state: state.has(Abilities.hamsa, self.player),
            Streets.egg: lambda state: state.has(Abilities.knife, self.player),

            Wilderness.red_eye: lambda state: state.has(Abilities.knife, self.player),
            Wilderness.diary_piori: lambda state: state.has(Abilities.knife, self.player),
            Wilderness.moon_glyph: lambda state: self.can_play_song(Songs.bagu, state),
            Wilderness.diary_endless: lambda state: state.has(Abilities.umbrella, self.player)
                                                    and state.has(Abilities.hat_scarf, self.player),
            Wilderness.diary_lookout: lambda state: state.has(Abilities.hamsa, self.player),

            Mall.hidden_storage: lambda state: state.has(Abilities.hamsa, self.player),
            Mall.rooftop_key: lambda state: state.has(Abilities.umbrella, self.player) and
                                            state.has(Abilities.lantern, self.player),
            Mall.diary_upper_boxes: lambda state: state.has(Abilities.umbrella, self.player) and
                                            state.has(Abilities.lantern, self.player),

            School.triangle: lambda state: state.has(SchoolItem.brush, self.player),
            School.brush: lambda state: state.has(SchoolItem.books, self.player),
            School.picture_2: lambda state: state.has(SchoolItem.triangle, self.player),
            School.toilet_key: lambda state: state.has(Abilities.hamsa, self.player),
            School.diary_zipper: lambda state: state.has(Abilities.hamsa, self.player),

            Docks.yen_6: lambda state: self.can_run(state),
            Docks.boarded_art: lambda state: state.has(Abilities.hamsa, self.player),
            Docks.diary_strober: lambda state: state.has(DockItem.sad_fish, self.player),
            Docks.blood_bag: lambda state: state.has(DockItem.yen, self.player, 10),
            Docks.sad_fish: lambda state: state.has(DockItem.blood_bag, self.player),
            Docks.dirty_game_cartridge: lambda state: state.has(Abilities.hamsa, self.player),
            Docks.mask_of_fear: lambda state: state.has(Abilities.lantern, self.player),
            Docks.jellyfish: lambda state: self.can_jump(state) and state.has(Abilities.umbrella, self.player),

            Sewer.jellyfish: lambda state: state.has_all([Abilities.umbrella, Abilities.hat_scarf, Abilities.uboa_mask], self.player),
            Blocks.diary_blocks: lambda state: self.can_jump(state),
            Blocks.girl_1: lambda state: self.can_jump(state) and state.has(Abilities.umbrella, self.player),
            Blocks.girl_2: lambda state: self.can_jump(state) and state.has(Abilities.umbrella, self.player),
            Blocks.girl_3: lambda state: self.can_jump(state) and state.has(Abilities.umbrella, self.player),
            Blocks.girl_4: lambda state: self.can_jump(state) and state.has(Abilities.umbrella, self.player),
            Blocks.girl_5: lambda state: self.can_jump(state) and state.has(Abilities.umbrella, self.player),
            Blocks.girl_6: lambda state: self.can_jump(state) and state.has(Abilities.umbrella, self.player),

        }

    def can_reach_level_in_ao_oni(self, state: CollectionState, level: int):
        if "Ao Oni" not in self.world.options.randomize_console.value:
            return True
        return state.has(AoOniItem.mansion_key, self.player, level)

    def can_enter_apartment(self, state: CollectionState):
        have_count = state.count_from_list(GoalItems.eggs, self.player)
        need_count = self.world.options.required_eggs.value
        return have_count >= need_count

    def can_enter_ufo(self, state: CollectionState):
        have_count = state.count_from_list(GoalItems.jellyfish, self.player)
        need_count = self.world.options.required_jellyfish.value
        return have_count >= need_count

    def can_enter_door(self, door: str, state: CollectionState):
        if self.doors[door]:
            return True
        return state.has(NexusDoors.door_to_key[door], self.player)

    def has_key_for_connector(self, item: str, state: CollectionState):
        if self.world.options.lock_connectors:
            return state.has(item, self.player)
        return True

    def can_jump(self, state: CollectionState):
        if "Jump" in self.world.options.starting_basic_movement.value:
            return True
        return state.has(Movement.jump, self.player),

    def can_climb(self, state: CollectionState):
        if "Climb" in self.world.options.starting_basic_movement.value:
            return True
        return state.has(Movement.climb, self.player),

    def can_run(self, state: CollectionState):
        if "Run" in self.world.options.starting_basic_movement.value:
            return True
        return state.has(Movement.run, self.player),

    def has_lantern(self, state: CollectionState):
        if self.world.options.dark_room_require_lantern:
            return state.has(Abilities.lantern, self.player)
        return True

    def can_play_song(self, song: str, state: CollectionState):
        has_song = True
        if self.world.options.song_lock:
            has_song = state.has(song, self.player)
        return has_song and state.has(Abilities.flute, self.player)

    def needs_item_or_pinch_skip(self, state: CollectionState, item: str):
        if self.world.options.pinch_skip:
            return True
        count = 1
        if item == SchoolItem.photo:
            count = 4
        return state.has(item, self.player, count) or state.has(Glitch.glitch, self.player)

    def set_yume_nikki_rules(self, doors: Dict[str, bool]) -> None:
        self.doors = doors
        for region in self.world.get_regions():
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
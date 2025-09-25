from typing import TYPE_CHECKING, Dict, List

from BaseClasses import CollectionState
from worlds.madou.strings.locations import HarpyPath, Spell, ShadyWell, DarkForest, ForestOfLight, LightGarden, MagicTown, SatanVilla, AncientRuins, School, \
    AncientVillage, DragonAreas, Bestiary
from worlds.madou.strings.region_entrances import MadouEntrance
from worlds.madou.strings.items import Tool, Custom, Special, Souvenir, EventItem, Gem, SpellItem, FlightUnlocks
from worlds.madou.options import MadouOptions
from worlds.generic.Rules import CollectionRule

if TYPE_CHECKING:
    from . import MadouWorld


class MadouRules:
    world: "MadouWorld"
    region_rules: Dict[str, CollectionRule]
    entrance_rules: Dict[str, CollectionRule]
    location_rules: Dict[str, CollectionRule]

    def __init__(self, world: "MadouWorld") -> None:
        self.player = world.player
        self.world = world
        self.world.options = world.options

        self.region_rules = {

        }

        self.entrance_rules = {
            MadouEntrance.village_to_nw_cave: lambda state: state.has(Tool.ribbit_boots, self.player),
            MadouEntrance.nw_cave_to_village: lambda state: state.has(Tool.ribbit_boots, self.player),
            MadouEntrance.forest_to_frog: lambda state: state.has(Tool.ribbit_boots, self.player),
            MadouEntrance.frog_to_forest: lambda state: state.has(Tool. ribbit_boots, self.player),
            MadouEntrance.ruins_to_ancient_ruins: lambda state: state.has(Tool.magic_bracelet, self.player),
            MadouEntrance.ancient_to_zoh: lambda state: state.has(Special.elephant_head, self.player),
            MadouEntrance.nw_cave_to_smoky: lambda state: state.has(Custom.bomb, self.player),
            MadouEntrance.death_to_bazaar: lambda state: state.has(Special.bazaar_pass, self.player) and state.has(Tool.ribbit_boots, self.player),
            MadouEntrance.smoky_left_to_right: lambda state: state.has(Tool.ribbit_boots, self.player),
            MadouEntrance.magic_village_to_tower: lambda state: self.can_fight_generic_at_level(state, 5, self.world.options) and self.can_reach_tower(state, self.world.options),
            MadouEntrance.headmaster_to_school_maze: lambda state: self.can_fight_generic_at_level(state, 3, self.world.options),
            MadouEntrance.smoky_to_graveyard: lambda state: state.has(Special.dark_flower, self.player) and state.has(Special.leaf, self.player),
            MadouEntrance.flight_magic_to_ruins: lambda state: state.has(FlightUnlocks.ruins_town, self.player),
            MadouEntrance.flight_magic_to_wolf: lambda state: state.has(FlightUnlocks.wolf_town, self.player),
            MadouEntrance.flight_magic_to_ancient: lambda state: state.has(FlightUnlocks.ancient_village, self.player),
            MadouEntrance.flight_magic_to_sage: lambda state: state.has(FlightUnlocks.sage_mountain, self.player),
            MadouEntrance.flight_ruins_to_magic: lambda state: state.has(FlightUnlocks.magic_village, self.player),
            MadouEntrance.flight_ruins_to_ancient: lambda state: state.has(FlightUnlocks.ancient_village, self.player),
            MadouEntrance.flight_ruins_to_wolf: lambda state: state.has(FlightUnlocks.wolf_town, self.player),
            MadouEntrance.flight_ruins_to_sage: lambda state: state.has(FlightUnlocks.sage_mountain, self.player),
            MadouEntrance.flight_wolf_to_magic: lambda state: state.has(FlightUnlocks.magic_village, self.player),
            MadouEntrance.flight_wolf_to_ruins: lambda state: state.has(FlightUnlocks.ruins_town, self.player),
            MadouEntrance.flight_wolf_to_ancient: lambda state: state.has(FlightUnlocks.ancient_village, self.player),
            MadouEntrance.flight_wolf_to_sage: lambda state: state.has(FlightUnlocks.sage_mountain, self.player),
            MadouEntrance.flight_ancient_to_magic: lambda state: state.has(FlightUnlocks.magic_village, self.player),
            MadouEntrance.flight_ancient_to_ruins: lambda state: state.has(FlightUnlocks.ruins_town, self.player),
            MadouEntrance.flight_ancient_to_wolf: lambda state: state.has(FlightUnlocks.wolf_town, self.player),
            MadouEntrance.flight_ancient_to_sage: lambda state: state.has(FlightUnlocks.sage_mountain, self.player),
            MadouEntrance.flight_sage_to_magic: lambda state: state.has(FlightUnlocks.magic_village, self.player),
            MadouEntrance.flight_sage_to_ruins: lambda state: state.has(FlightUnlocks.ruins_town, self.player),
            MadouEntrance.flight_sage_to_wolf: lambda state: state.has(FlightUnlocks.wolf_town, self.player),
            MadouEntrance.flight_sage_to_ancient: lambda state: state.has(FlightUnlocks.ancient_village, self.player),
        }

        self.location_rules = {
            SatanVilla.satan: lambda state: state.has(Special.secret_stone, self.player, 3),
            ForestOfLight.sukiyapodes_2: lambda state: state.has(Special.light_orb, self.player),
            DarkForest.dark_flower: lambda state: state.has(Special.dark_orb, self.player),
            LightGarden.purple_orb: lambda state: state.has(Tool.toy_elephant, self.player),
            MagicTown.white_gem: lambda state: self.has_souvenirs(state, self.world.options),
            #  Gold Tablets
            Spell.fire_school: lambda state: state.has(Tool.magical_dictionary, self.player),
            Spell.fire_library: lambda state: self.has_gems(state) and state.has(Tool.magical_dictionary, self.player),
            Spell.ice_storm_underground: lambda state: state.has(Tool.magical_dictionary, self.player),
            Spell.ice_storm_library: lambda state: self.has_gems(state) and state.has(Tool.magical_dictionary, self.player),
            Spell.thunder_northwestern: lambda state: state.has(Tool.magic_ribbon, self.player) and state.has(Tool.magical_dictionary, self.player),
            Spell.thunder_library: lambda state: self.has_gems(state) and state.has(Tool.magical_dictionary, self.player),
            Spell.diacute_library: lambda state: self.has_gems(state) and state.has(Tool.magical_dictionary, self.player),
            #  Combat Rules
            ForestOfLight.orb: lambda state: self.can_fight_generic_at_level(state, 1, self.world.options),
            ForestOfLight.ribbit_boots: lambda state: self.can_fight_generic_at_level(state, 1, self.world.options),
            ForestOfLight.sukiyapodes_1: lambda state: self.can_fight_generic_at_level(state, 1, self.world.options),
            AncientRuins.zoh_daimaoh: lambda state: self.can_fight_generic_at_level(state, 1, self.world.options),
            HarpyPath.bag: lambda state: state.has(Tool.panotty_flute, self.player) and self.can_fight_generic_at_level(state, 2, self.world.options),
            ShadyWell.arachne: lambda state: state.has(Special.ripe_cucumber, self.player) and self.can_fight_generic_at_level(state, 2, self.world.options),
            School.magical_dictionary: lambda state: self.can_fight_generic_at_level(state, 3, self.world.options),
            AncientVillage.elder: lambda state: self.can_fight_generic_at_level(state, 3, self.world.options),
            AncientVillage.villager_1: lambda state: self.can_fight_generic_at_level(state, 3, self.world.options),
            AncientVillage.villager_2: lambda state: self.can_fight_generic_at_level(state, 3, self.world.options),
            AncientVillage.villager_3: lambda state: self.can_fight_generic_at_level(state, 3, self.world.options),
            AncientVillage.villager_4: lambda state: self.can_fight_generic_at_level(state, 3, self.world.options),
            AncientVillage.villager_5: lambda state: self.can_fight_generic_at_level(state, 3, self.world.options),
            AncientVillage.villager_6: lambda state: self.can_fight_generic_at_level(state, 3, self.world.options),
            DragonAreas.firefly_egg: lambda state: self.can_fight_generic_at_level(state, 4, self.world.options),
            DragonAreas.stone: lambda state: self.can_fight_generic_at_level(state, 4, self.world.options) and state.has(Special.firefly_egg, self.player, 2),
            MagicTown.suketoudara: lambda state: state.has(Special.secret_stone, self.player, 7) and self.can_fight_generic_at_level(state, 4, self.world.options),
            Bestiary.wood_man: lambda state: state.has(EventItem.hammer_switch, self.player)  # Enemies don't spawn unless you hit the switch.


        }

    def has_all(self, items: List[str], state: CollectionState):
        rule = True
        for item in items:
            rule = rule & state.has(item, self.player)
        return rule

    def has_souvenirs(self, state: CollectionState, options: MadouOptions):
        if options.souvenir_hunt:
            return self.has_all(Souvenir.souvenirs, state)
        return self.has_all(EventItem.shops, state)

    def has_gems(self, state: CollectionState):
        return self.has_all(Gem.gems, state)

    def can_fight_generic_at_level(self, state: CollectionState, level: int, options: MadouOptions):
        stun_rule = True
        diacute_count = max(0, level - 1)
        total_combat_spell_items = state.count_from_list(SpellItem.combat_spells, self.player)
        starting_spells = options.starting_magic.value
        if "Fire" in starting_spells:
            total_combat_spell_items += 1
        if "Ice Storm" in starting_spells:
            total_combat_spell_items += 1
        if "Thunder" in starting_spells:
            total_combat_spell_items += 1
        average_count = total_combat_spell_items//3
        if level > 1:
            stun_rule = state.has(SpellItem.bayoen, self.player)
        return state.has(SpellItem.diacute, self.player, diacute_count) and stun_rule and average_count >= min(4, level)

    def can_reach_tower(self, state: CollectionState, options: MadouOptions):
        required_stones = options.required_secret_stones.value
        return state.has(Special.secret_stone, self.player, required_stones)

    def set_madou_rules(self) -> None:
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

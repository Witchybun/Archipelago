from BaseClasses import CollectionState
from typing import Dict, List, TYPE_CHECKING

from worlds.generic.Rules import CollectionRule

from .strings.regions_entrances import FlipwitchEntrance, FlipwitchRegion
from .strings.items import Coin, Upgrade, QuestItem, Unlock
from .strings.locations import WitchyWoods, Quest

if TYPE_CHECKING:
    from . import FlipwitchWorld


class FlipwitchRules:
    player: int
    world: "FlipwitchWorld"
    region_rules: Dict[str, CollectionRule]
    entrance_rules: Dict[str, CollectionRule]
    location_rules: Dict[str, CollectionRule]

    def __init__(self, world: "FlipwitchWorld") -> None:
        self.player = world.player
        self.world = world
        self.world.options = world.options

        self.region_rules = {
        }

        self.entrance_rules = {
            FlipwitchEntrance.witchy_to_spirit: lambda state: state.has(Unlock.crystal_block, self.player)
        }

        self.location_rules = {
            WitchyWoods.gacha: lambda state: state.has(Coin.lucky_coin, self.player),
            WitchyWoods.fairy: lambda state: state.has(Upgrade.peachy_peach, self.player),
            Quest.magic_mentor: lambda state: state.has(QuestItem.fairy_bubble, self.player),
            Quest.need_my_cowbell: lambda state: state.has(QuestItem.cowbell, self.player),
        }

    def can_complete_quest(self, state: CollectionState):
        return state.can_reach_region(FlipwitchRegion.witch_woods, self.player) and state.has(QuestItem.fairy_bubble, self.player)


    def set_flipwitch_rules(self) -> None:
        multiworld = self.world.multiworld
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

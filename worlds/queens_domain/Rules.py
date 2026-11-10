import dataclasses

from BaseClasses import CollectionState
from typing import Dict, List, TYPE_CHECKING, Any, override

from NetUtils import JSONMessagePart
from rule_builder.options import OptionFilter
from rule_builder.rules import False_, True_, Rule, HasAll, HasAny, CanReachRegion, Has, CanReachLocation
from .strings.items import HeldWeapon
from .strings.regions_entrances import NeasiedEntrance

if TYPE_CHECKING:
    from . import QueensDomainWorld


class QueensDomainRules:
    player: int
    world: "QueensDomainWorld"
    entrance_rules: Dict[str, Rule[Any]]
    location_rules: Dict[str, Rule[Any]]

    def __init__(self, world: "QueensDomainWorld") -> None:
        self.player = world.player
        self.world = world
        self.world.options = world.options

        self.entrance_rules = {
            NeasiedEntrance.camp_to_main_lower: self.can_break_wall(),
            NeasiedEntrance.camp_to_beach: Has(HeldWeapon.holy_sword_endu),
        }

        self.location_rules = {

        }

    def can_break_wall(self):
        return True_()  # Honestly there should be a starting weapon or just remove this dumb wall.


    def set_queens_domain_rules(self) -> None:
        multiworld = self.world.multiworld
        for region in multiworld.get_regions(self.player):
            for entrance in region.entrances:
                if entrance.name in self.entrance_rules:
                    self.world.set_rule(entrance, self.entrance_rules[entrance.name])
            for loc in region.locations:
                if loc.name in self.location_rules:
                    self.world.set_rule(loc, self.location_rules[loc.name])

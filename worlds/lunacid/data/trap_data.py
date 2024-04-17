from dataclasses import dataclass
from typing import List
from BaseClasses import ItemClassification

from .game_item import GameItem
from ..strings.items import Traps


@dataclass(frozen=True)
class TrapItem(GameItem):
    code: int
    name: str
    classification: ItemClassification

    def __repr__(self):
        return f"{self.name} (Classification: {self.classification})"


all_traps: List[TrapItem] = []


def create_trap(code: int, name: str, classification: ItemClassification):
    trap = TrapItem(name, code, classification)
    all_traps.append(trap)
    return trap


health_viai = create_trap(70, Traps.health_viai, ItemClassification.trap)
poison = create_trap(71, Traps.poison_trap, ItemClassification.trap)
blindness = create_trap(72, Traps.blindness_trap, ItemClassification.trap)
slowness = create_trap(73, Traps.slowness_trap, ItemClassification.trap)
mana_drain = create_trap(74, Traps.mana_drain_trap, ItemClassification.trap)
xp_drain = create_trap(75, Traps.xp_drain_trap, ItemClassification.trap)
curse = create_trap(76, Traps.curse_trap, ItemClassification.trap)
bleed = create_trap(77, Traps.bleed_trap, ItemClassification.trap)
eggnog = create_trap(78, Traps.eggnog, ItemClassification.trap)
coal = create_trap(79, Traps.coal, ItemClassification.trap)



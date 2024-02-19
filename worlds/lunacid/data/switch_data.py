from dataclasses import dataclass
from typing import List
from BaseClasses import ItemClassification

from .game_item import GameItem
from ..strings.items import Switch


@dataclass(frozen=True)
class SwitchItem(GameItem):
    code: int
    name: str
    classification: ItemClassification

    def __repr__(self):
        return f"{self.name} (Classification: {self.classification})"


all_switches: List[SwitchItem] = []


def create_switch(code: int, name: str, classification: ItemClassification):
    switch = SwitchItem(name, code, classification)
    all_switches.append(switch)
    return switch


hollow_basin_switch_near_demi = create_switch(131, Switch.hollow_basin_switch_near_demi, ItemClassification.useful)
temple_switch = create_switch(132, Switch.temple_switch, ItemClassification.progression)
fetid_mire_switch = create_switch(133, Switch.fetid_mire_switch, ItemClassification.useful)
tomb_shortcut_switch = create_switch(134, Switch.tomb_shortcut_switch, ItemClassification.useful)
tomb_crypt_switch = create_switch(135, Switch.tomb_crypt_switch, ItemClassification.useful)
tomb_light_switch_1 = create_switch(136, Switch.tomb_light_switch_1, ItemClassification.useful)
tomb_light_switch_2 = create_switch(137, Switch.tomb_light_switch_2, ItemClassification.useful)
tomb_light_switch_3 = create_switch(138, Switch.tomb_light_switch_3, ItemClassification.useful)
tomb_lightning_gate_1 = create_switch(139, Switch.tomb_lightning_gate_1, ItemClassification.progression)
tomb_lightning_gate_2 = create_switch(140, Switch.tomb_lightning_gate_2, ItemClassification.progression)
archives_switch = create_switch(141, Switch.archives_switch, ItemClassification.useful)
ballroom_switch = create_switch(142, Switch.ballroom_switch, ItemClassification.useful)
grotto_valve_switch_1 = create_switch(143, Switch.grotto_valve_switch_1, ItemClassification.progression)
grotto_valve_switch_2 = create_switch(144, Switch.grotto_valve_switch_2, ItemClassification.progression)
grotto_calor_switch = create_switch(145, Switch.grotto_calor_switch, ItemClassification.useful)
grotto_temple_switch = create_switch(146, Switch.grotto_temple_switch, ItemClassification.useful)
prison_shortcut_switch = create_switch(147, Switch.prison_shortcut_switch, ItemClassification.progression)
prison_arena_switch = create_switch(148, Switch.prison_arena_switch, ItemClassification.progression)
arena_water_switch = create_switch(149, Switch.arena_water_switch, ItemClassification.useful)
arena_earth_switch = create_switch(150, Switch.arena_earth_switch, ItemClassification.useful)
ash_switch = create_switch(151, Switch.ash_switch, ItemClassification.useful)


all_switches_by_name = {switch.name: switch for switch in all_switches}

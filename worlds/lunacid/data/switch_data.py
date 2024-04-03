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


hollow_basin_switch_near_demi = create_switch(201, Switch.hollow_basin_switch_near_demi, ItemClassification.useful)
temple_switch = create_switch(202, Switch.temple_switch, ItemClassification.progression)
fetid_mire_switch = create_switch(203, Switch.fetid_mire_switch, ItemClassification.useful)
tomb_crypt_switch = create_switch(205, Switch.tomb_switches, ItemClassification.useful)
tomb_light_switch_1 = create_switch(206, Switch.tomb_light_switches, ItemClassification.useful)
archives_switch = create_switch(209, Switch.archives_switch, ItemClassification.useful)
archives_elevator_2_to_3 = create_switch(211, Switch.archives_elevator_switches, ItemClassification.progression)
ballroom_switch = create_switch(213, Switch.ballroom_switch, ItemClassification.useful)
grotto_valve_switch_1 = create_switch(214, Switch.grotto_valves_switches, ItemClassification.progression)
grotto_calor_switch = create_switch(216, Switch.grotto_switches, ItemClassification.useful)
grotto_temple_switch = create_switch(217, Switch.grotto_temple_switch, ItemClassification.useful)
prison_shortcut_switch = create_switch(218, Switch.prison_shortcut_switch, ItemClassification.progression)
prison_arena_switch = create_switch(219, Switch.prison_arena_switch, ItemClassification.progression)
arena_water_switch = create_switch(220, Switch.arena_water_switch, ItemClassification.useful)
arena_earth_switch = create_switch(221, Switch.arena_earth_switch, ItemClassification.useful)
ash_switch = create_switch(222, Switch.ash_switch, ItemClassification.useful)


all_switches_by_name = {switch.name: switch for switch in all_switches}

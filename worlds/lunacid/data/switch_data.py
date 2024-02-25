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


hollow_basin_switch_near_demi = create_switch(181, Switch.hollow_basin_switch_near_demi, ItemClassification.useful)
temple_switch = create_switch(182, Switch.temple_switch, ItemClassification.progression)
fetid_mire_switch = create_switch(183, Switch.fetid_mire_switch, ItemClassification.useful)
tomb_shortcut_switch = create_switch(184, Switch.tomb_shortcut_switch, ItemClassification.useful)
tomb_crypt_switch = create_switch(185, Switch.tomb_crypt_switch, ItemClassification.useful)
tomb_light_switch_1 = create_switch(186, Switch.tomb_light_switch_1, ItemClassification.useful)
tomb_light_switch_2 = create_switch(187, Switch.tomb_light_switch_2, ItemClassification.useful)
tomb_light_switch_3 = create_switch(188, Switch.tomb_light_switch_3, ItemClassification.useful)
archives_switch = create_switch(191, Switch.archives_switch, ItemClassification.useful)
archives_elevator_1_to_2 = create_switch(192, Switch.archives_elevator_switch_1_to_2, ItemClassification.useful)
archives_elevator_2_to_3 = create_switch(193, Switch.archives_elevator_switch_2_to_3, ItemClassification.progression)
archives_elevator_1_to_3 = create_switch(194, Switch.archives_elevator_switch_1_to_3, ItemClassification.progression)
ballroom_switch = create_switch(195, Switch.ballroom_switch, ItemClassification.useful)
grotto_valve_switch_1 = create_switch(196, Switch.grotto_valve_switch_1, ItemClassification.progression)
grotto_valve_switch_2 = create_switch(197, Switch.grotto_valve_switch_2, ItemClassification.progression)
grotto_calor_switch = create_switch(198, Switch.grotto_calor_switch, ItemClassification.useful)
grotto_temple_switch = create_switch(199, Switch.grotto_temple_switch, ItemClassification.useful)
prison_shortcut_switch = create_switch(200, Switch.prison_shortcut_switch, ItemClassification.progression)
prison_arena_switch = create_switch(201, Switch.prison_arena_switch, ItemClassification.progression)
arena_water_switch = create_switch(202, Switch.arena_water_switch, ItemClassification.useful)
arena_earth_switch = create_switch(203, Switch.arena_earth_switch, ItemClassification.useful)
ash_switch = create_switch(204, Switch.ash_switch, ItemClassification.useful)


all_switches_by_name = {switch.name: switch for switch in all_switches}

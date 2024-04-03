from dataclasses import dataclass
from typing import List
from BaseClasses import ItemClassification

from .game_item import GameItem
from ..strings.items import Door


@dataclass(frozen=True)
class DoorItem(GameItem):
    code: int
    name: str
    classification: ItemClassification

    def __repr__(self):
        return f"{self.name} (Classification: {self.classification})"


all_doors: List[DoorItem] = []


def create_door(code: int, name: str, classification: ItemClassification):
    door = DoorItem(name, code, classification)
    all_doors.append(door)
    return door


basin_broken_steps = create_door(251, Door.basin_broken_steps, ItemClassification.progression)
basin_rickety_bridge = create_door(252, Door.basin_rickety_bridge, ItemClassification.progression)
basin_temple_sewers = create_door(253, Door.basin_temple_sewers, ItemClassification.progression)
forest_door_in_trees = create_door(254, Door.forest_door_in_trees, ItemClassification.progression)
forest_patchouli = create_door(255, Door.forest_patchouli, ItemClassification.progression)
sea_westward = create_door(256, Door.sea_westward, ItemClassification.progression)
sea_eastward = create_door(257, Door.sea_eastward, ItemClassification.progression)
sea_double_doors = create_door(258, Door.sea_double_doors, ItemClassification.progression)
archives_sealed_door = create_door(259, Door.archives_sealed_door, ItemClassification.progression)
chasm_surface_door = create_door(260, Door.chasm_surface_door, ItemClassification.progression)
ballroom_key = create_door(261, Door.ballroom_key, ItemClassification.progression)
throne_key = create_door(262, Door.throne_key, ItemClassification.progression)
prison_key = create_door(263, Door.prison_key, ItemClassification.progression)
forlorn_key = create_door(264, Door.forlorn_key, ItemClassification.progression)
burning_key = create_door(265, Door.burning_key, ItemClassification.progression)
ash_key = create_door(266, Door.ash_key, ItemClassification.progression)
sucs_key = create_door(267, Door.sucs_key, ItemClassification.progression)
sleeper_key = create_door(268, Door.sleeper_key, ItemClassification.progression)
ballroom_rooms_key = create_door(269, Door.ballroom_rooms_key, ItemClassification.progression)
tower_key = create_door(270, Door.tower_key, ItemClassification.progression)

all_doors_by_name = {door.name: door for door in all_doors}

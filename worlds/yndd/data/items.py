from dataclasses import dataclass
from typing import List
from BaseClasses import ItemClassification
from ..strings.items import Abilities, WildernessItem, DockItem, MallItem, SchoolItem, Game, GoalItems, Filler, \
    NasuItem, AoOniItem, WitchAdventureItem, Movement, NexusDoors, ConnectorKeys, Songs, BlockItem, ApartmentItem


@dataclass(frozen=True)
class DreamItemData:
    code: int
    name: str
    classification: ItemClassification

    def __repr__(self):
        return f"{self.code} {self.name} (Classification: {self.classification})"


all_items: List[DreamItemData] = []


def create_item(code: int, name: str, classification: ItemClassification):
    item = DreamItemData(code, name, classification)
    all_items.append(item)

    return item


base_start_id = 0
base_items = [
    create_item(base_start_id + 1, Abilities.umbrella, ItemClassification.progression | ItemClassification.useful),
    create_item(base_start_id + 2, Abilities.knife, ItemClassification.progression | ItemClassification.useful),
    create_item(base_start_id + 3, Abilities.lantern, ItemClassification.progression | ItemClassification.useful),
    create_item(base_start_id + 4, Abilities.hamsa, ItemClassification.progression | ItemClassification.useful),
    create_item(base_start_id + 5, Abilities.flute, ItemClassification.progression | ItemClassification.useful),
    create_item(base_start_id + 6, Abilities.hat_scarf, ItemClassification.progression | ItemClassification.useful),
    create_item(base_start_id + 7, Abilities.uboa_mask, ItemClassification.progression | ItemClassification.useful),
    create_item(base_start_id + 10, WildernessItem.red_eye, ItemClassification.progression | ItemClassification.useful),
    create_item(base_start_id + 11, WildernessItem.kite, ItemClassification.progression | ItemClassification.useful),
    create_item(base_start_id + 12, WildernessItem.sun, ItemClassification.progression | ItemClassification.useful),
    create_item(base_start_id + 13, WildernessItem.moon, ItemClassification.progression | ItemClassification.useful),
    create_item(base_start_id + 14, WildernessItem.war, ItemClassification.progression | ItemClassification.useful),
    create_item(base_start_id + 15, WildernessItem.death, ItemClassification.progression | ItemClassification.useful),
    create_item(base_start_id + 16, WildernessItem.kalimba, ItemClassification.useful),
    create_item(base_start_id + 20, DockItem.yen, ItemClassification.progression_skip_balancing),
    create_item(base_start_id + 21, DockItem.sad_fish, ItemClassification.progression | ItemClassification.useful),
    create_item(base_start_id + 22, DockItem.boards, ItemClassification.progression | ItemClassification.useful),
    create_item(base_start_id + 23, DockItem.blood_bag, ItemClassification.progression | ItemClassification.useful),
    create_item(base_start_id + 25, MallItem.warehouse_key, ItemClassification.progression | ItemClassification.useful),
    create_item(base_start_id + 26, MallItem.rooftop_key, ItemClassification.progression | ItemClassification.useful),
    create_item(base_start_id + 27, MallItem.valve, ItemClassification.progression | ItemClassification.useful),
    create_item(base_start_id + 30, SchoolItem.photo, ItemClassification.progression_skip_balancing),
    create_item(base_start_id + 31, SchoolItem.books, ItemClassification.progression | ItemClassification.useful),
    create_item(base_start_id + 32, SchoolItem.brush, ItemClassification.progression | ItemClassification.useful),
    create_item(base_start_id + 33, SchoolItem.triangle, ItemClassification.progression | ItemClassification.useful),
    create_item(base_start_id + 34, SchoolItem.key, ItemClassification.progression | ItemClassification.useful),
    create_item(base_start_id + 35, SchoolItem.lever, ItemClassification.progression | ItemClassification.useful),
    create_item(base_start_id + 36, BlockItem.girl, ItemClassification.progression | ItemClassification.useful),
    create_item(base_start_id + 37, ApartmentItem.key, ItemClassification.progression | ItemClassification.useful),
    create_item(base_start_id + 40, GoalItems.street_egg, ItemClassification.progression_skip_balancing),
    create_item(base_start_id + 41, GoalItems.street_jellyfish, ItemClassification.progression_skip_balancing),
    create_item(base_start_id + 42, GoalItems.school_egg, ItemClassification.progression_skip_balancing),
    create_item(base_start_id + 43, GoalItems.school_jellyfish, ItemClassification.progression_skip_balancing),
    create_item(base_start_id + 44, GoalItems.mall_egg, ItemClassification.progression_skip_balancing),
    create_item(base_start_id + 45, GoalItems.mall_jellyfish, ItemClassification.progression_skip_balancing),
    create_item(base_start_id + 46, GoalItems.wilderness_egg, ItemClassification.progression_skip_balancing),
    create_item(base_start_id + 47, GoalItems.wilderness_jellyfish, ItemClassification.progression_skip_balancing),
    create_item(base_start_id + 48, GoalItems.docks_egg, ItemClassification.progression_skip_balancing),
    create_item(base_start_id + 49, GoalItems.docks_jellyfish, ItemClassification.progression_skip_balancing),
    create_item(base_start_id + 50, GoalItems.sewers_egg, ItemClassification.progression_skip_balancing),
    create_item(base_start_id + 51, GoalItems.sewers_jellyfish, ItemClassification.progression_skip_balancing),
    create_item(base_start_id + 55, Game.nasu, ItemClassification.progression),
    create_item(base_start_id + 56, Game.ao_oni, ItemClassification.progression),
    create_item(base_start_id + 57, Game.witch_adventure, ItemClassification.progression),
    create_item(base_start_id + 60, Filler.nothing, ItemClassification.filler),
]

nasu_start_id = 100
nasu_items = [
    create_item(nasu_start_id + 1, NasuItem.nasu_get, ItemClassification.progression),
    create_item(nasu_start_id + 2, NasuItem.doubler, ItemClassification.progression),
    create_item(nasu_start_id + 3, NasuItem.starting_points, ItemClassification.useful),
]

ao_oni_start_id = 110
ao_oni_items = [
    create_item(ao_oni_start_id + 1, AoOniItem.key, ItemClassification.progression),
    create_item(ao_oni_start_id + 2, AoOniItem.mansion_key, ItemClassification.progression | ItemClassification.useful),
    create_item(ao_oni_start_id + 3, AoOniItem.poniko, ItemClassification.useful),
    create_item(ao_oni_start_id + 4, AoOniItem.monoko, ItemClassification.useful),
    create_item(ao_oni_start_id + 5, AoOniItem.monoe, ItemClassification.useful),
    create_item(ao_oni_start_id + 6, AoOniItem.doll, ItemClassification.filler),
    create_item(ao_oni_start_id + 7, AoOniItem.lighter, ItemClassification.filler),
    create_item(ao_oni_start_id + 8, AoOniItem.handkerchief, ItemClassification.filler),
]

witch_adventure_start_id = 130
witch_adventure_items = [
    create_item(witch_adventure_start_id + 1, WitchAdventureItem.heart_container, ItemClassification.progression),
    create_item(witch_adventure_start_id + 2, WitchAdventureItem.heal_unlock, ItemClassification.progression),
]

movement_start_id = 140
movement_items = [
    create_item(movement_start_id + 1, Movement.jump, ItemClassification.progression | ItemClassification.useful),
    create_item(movement_start_id + 2, Movement.climb, ItemClassification.progression | ItemClassification.useful),
    create_item(movement_start_id + 3, Movement.run,  ItemClassification.progression | ItemClassification.useful),
]

nexus_door_start_id = 150
nexus_door_items = [
    create_item(nexus_door_start_id + 1, NexusDoors.street, ItemClassification.progression),
    create_item(nexus_door_start_id + 2, NexusDoors.school, ItemClassification.progression),
    create_item(nexus_door_start_id + 3, NexusDoors.wilderness, ItemClassification.progression),
    create_item(nexus_door_start_id + 4, NexusDoors.mall, ItemClassification.progression),
    create_item(nexus_door_start_id + 5, NexusDoors.docks, ItemClassification.progression),
    create_item(nexus_door_start_id + 6, NexusDoors.sewer, ItemClassification.progression),
]

connector_start_id = 160
connector_items = [
    create_item(connector_start_id + 1, ConnectorKeys.wilderness_to_docks, ItemClassification.progression),
    create_item(connector_start_id + 2, ConnectorKeys.mall_to_sewers, ItemClassification.progression),
    create_item(connector_start_id + 3, ConnectorKeys.wilderness_to_sewers, ItemClassification.progression),
    create_item(connector_start_id + 4, ConnectorKeys.street_to_sewers, ItemClassification.progression),
]

song_start_id = 170
song_items = [
    create_item(song_start_id + 1, Songs.bagu, ItemClassification.progression | ItemClassification.useful),
    create_item(song_start_id + 2, Songs.oman, ItemClassification.progression | ItemClassification.useful),
    create_item(song_start_id + 3, Songs.train, ItemClassification.progression | ItemClassification.useful),
    create_item(song_start_id + 4, Songs.finale, ItemClassification.progression | ItemClassification.useful),
]

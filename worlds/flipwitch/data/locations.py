from dataclasses import dataclass
from typing import Optional, List

from ..strings.locations import WitchyWoods, SpiritTown, Quest
from ..strings.regions_entrances import FlipwitchRegion


@dataclass(frozen=True)
class FlipwitchLocation:
    location_id: Optional[int]
    name: str
    region: str


all_locations = []


# Some locations vary on multiple regions, so we default to Hollow Basin first.
def create_location(location_id: Optional[int], name: str, region: str):
    location = FlipwitchLocation(location_id, name, region)
    if location_id is not None:
        all_locations.append(location)
    return location


LOCATION_CODE_START = 0
witchy_woods_location_start = 0
witchy_woods_locations = [
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 1, WitchyWoods.peachy_peach, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 2, WitchyWoods.rundown_chest, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + witchy_woods_location_start + 3, WitchyWoods.fairy, FlipwitchRegion.witch_woods),
]

gacha_location_start = 50
gacha_locations = [
    create_location(LOCATION_CODE_START + gacha_location_start + 1, WitchyWoods.lucky_machine, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + gacha_location_start + 2, WitchyWoods.lucky_rundown, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + gacha_location_start + 3, WitchyWoods.gacha, FlipwitchRegion.witch_woods),
]

quest_location_start = 100
quest_locations = [
    create_location(LOCATION_CODE_START + quest_location_start + 1, Quest.magic_mentor, FlipwitchRegion.witch_woods),
    create_location(LOCATION_CODE_START + quest_location_start + 2, Quest.need_my_cowbell, FlipwitchRegion.witch_woods),
]

shop_location_start = 150
shop_locations = [
    create_location(LOCATION_CODE_START + shop_location_start + 1, SpiritTown.fairy_bubble, FlipwitchRegion.witch_woods),
]

costume_location_start = 200
costume_locations = [
    create_location(LOCATION_CODE_START + costume_location_start + 1, WitchyWoods.navy_costume, FlipwitchRegion.witch_woods),
]

from dataclasses import dataclass, field
from enum import IntFlag
from random import Random
from typing import List, Tuple, Dict, Optional, Protocol, Iterable, Set

from BaseClasses import MultiWorld, Region, Entrance

from worlds.flipwitch.strings.regions_entrances import FlipwitchRegion, FlipwitchEntrance


class RegionFactory(Protocol):
    def __call__(self, name: str, regions: Iterable[str]) -> Region:
        raise NotImplementedError


connector_keyword = " to "


def link_flipwitch_areas(world: MultiWorld, player: int):
    for (entrance, region) in flipwitch_entrances:
        world.get_entrance(entrance, player).connect(world.get_region(region, player))


@dataclass(frozen=True)
class RegionData:
    name: str
    exits: List[str] = field(default_factory=list)

    def get_merged_with(self, exits: List[str]):
        merged_exits = []
        merged_exits.extend(self.exits)
        if exits is not None:
            merged_exits.extend(exits)
        merged_exits = list(set(merged_exits))
        return RegionData(self.name, merged_exits)

    def get_clone(self):
        return self.get_merged_with(None)


class RandomizationFlag(IntFlag):
    NOT_RANDOMIZED = 0b0
    RANDOMIZED = 0b1


@dataclass(frozen=True)
class ConnectionData:
    name: str
    destination: str
    origin: Optional[str] = None
    reverse: Optional[str] = None
    flag: RandomizationFlag = RandomizationFlag.NOT_RANDOMIZED

    def __post_init__(self):
        if connector_keyword in self.name:
            origin, destination = self.name.split(connector_keyword)
            if self.reverse is None:
                super().__setattr__("reverse", f"{destination}{connector_keyword}{origin}")


flipwitch_regions = [
    RegionData(FlipwitchRegion.menu, [FlipwitchEntrance.menu_to_woods]),
    RegionData(FlipwitchRegion.witch_woods, [FlipwitchEntrance.witchy_to_spirit]),
    RegionData(FlipwitchRegion.spirit_town),
]

flipwitch_entrances = [
    ConnectionData(FlipwitchEntrance.menu_to_woods, FlipwitchRegion.witch_woods),
    ConnectionData(FlipwitchEntrance.witchy_to_spirit, FlipwitchRegion.spirit_town),
]


def create_regions(region_factory: RegionFactory) -> Dict[str, Region]:
    final_regions = flipwitch_regions
    regions: Dict[str: Region] = {region.name: region_factory(region.name, region.exits) for region in
                                  final_regions}
    entrances: Dict[str: Entrance] = {entrance.name: entrance
                                      for region in regions.values()
                                      for entrance in region.exits}

    connections = flipwitch_entrances

    for connection in connections:
        if connection.name in entrances:
            entrances[connection.name].connect(regions[connection.destination])

    return regions


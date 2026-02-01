from dataclasses import dataclass, field
from typing import Optional, Protocol, List, Tuple, Dict

from BaseClasses import Region, MultiWorld, Entrance
from worlds.uktena64.strings.regions import BaseEntrance, BaseRegion, JebRegion, JebEntrance, JeebRegion, JeebEntrance

connector_keyword = " to "

@dataclass(frozen=True)
class ConnectionData:
    name: str
    destination: str
    origin: Optional[str] = None
    reverse: Optional[str] = None

    def __post_init__(self):
        if connector_keyword in self.name:
            origin, destination = self.name.split(connector_keyword)
            if self.reverse is None:
                super().__setattr__("reverse", f"{destination}{connector_keyword}{origin}")


class RegionFactory(Protocol):
    def __call__(self, name: str, regions: List[ConnectionData]) -> Region:
        raise NotImplementedError

@dataclass(frozen=True)
class RegionData:
    name: str
    exits: List[ConnectionData] = field(default_factory=list)

    def get_merged_with(self, exits: List[ConnectionData]):
        merged_exits = []
        merged_exits.extend(self.exits)
        if exits is not None:
            merged_exits.extend(exits)
        merged_exits = list(set(merged_exits))
        return RegionData(self.name, merged_exits)

    def get_clone(self):
        return self.get_merged_with(None)

uktena_regions = [
    RegionData(BaseRegion.menu, [ConnectionData(BaseEntrance.menu_to_jeb_campaign, JebRegion.campaign),
                                 ConnectionData(BaseEntrance.menu_to_jeeb_campaign, JeebRegion.campaign)]),

    RegionData(JebRegion.campaign, [ConnectionData(JebEntrance.campaign_to_cabin, JebRegion.cabin),
                                    ConnectionData(JebEntrance.campaign_to_turkey, JebRegion.turkey),
                                    ConnectionData(JebEntrance.campaign_to_frozen, JebRegion.frigid),
                                    ConnectionData(JebEntrance.campaign_to_howling, JebRegion.howling),
                                    ConnectionData(JebEntrance.campaign_to_bleeding, JebRegion.bleeding)]),
    RegionData(JebRegion.cabin),
    RegionData(JebRegion.turkey),
    RegionData(JebRegion.frigid),
    RegionData(JebRegion.howling),
    RegionData(JebRegion.bleeding),
    RegionData(JeebRegion.campaign, [ConnectionData(JeebEntrance.campaign_to_bbq, JeebRegion.bbq),
                                     ConnectionData(JeebEntrance.campaign_to_ritual, JeebRegion.ritual),
                                     ConnectionData(JeebEntrance.campaign_to_lake, JeebRegion.lake),
                                     ConnectionData(JeebEntrance.campaign_to_pallid, JeebRegion.pallid),
                                     ConnectionData(JeebEntrance.campaign_to_burning, JeebRegion.burning)]),
    RegionData(JeebRegion.bbq),
    RegionData(JeebRegion.ritual),
    RegionData(JeebRegion.lake),
    RegionData(JeebRegion.pallid),
    RegionData(JeebRegion.burning),
]

uktena_connections: List[ConnectionData] = []
for region_data_info in uktena_regions:
    uktena_connections.extend(region_data_info.exits)

def create_regions(region_factory: RegionFactory, multiworld: MultiWorld) -> Tuple[Dict[str, Region], Dict[str, Entrance]]:
    final_regions = uktena_regions
    regions: Dict[str: Region] = {region.name: region_factory(region.name, region.exits) for region in
                                  final_regions}
    entrances: Dict[str: Entrance] = {}
    for region in regions.values():
        for entrance in region.exits:
            multiworld.register_indirect_condition(region, entrance)
            entrances[entrance.name] = entrance

    for connection in uktena_connections:
        if connection.name in entrances:
            entrances[connection.name].connect(regions[connection.destination])
    return regions, entrances

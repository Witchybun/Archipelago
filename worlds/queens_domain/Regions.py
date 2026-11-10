from entrance_rando import EntranceType
from dataclasses import dataclass, field
from typing import List, Tuple, Dict, Optional, Protocol, Iterable

from BaseClasses import MultiWorld, Region, Entrance

from worlds.queens_domain.strings.regions_entrances import NeasiedRegion, NeasiedEntrance


class RegionFactory(Protocol):
    def __call__(self, name: str, regions: Iterable[str]) -> Region:
        raise NotImplementedError

@dataclass(frozen=True)
class EntranceData:
    entrance_name: str
    region_exit: Optional[str] = None
    randomized: bool = False
    dead_end: bool = False
    type: EntranceType = EntranceType.ONE_WAY

@dataclass(frozen=True)
class RegionData:
    name: str
    exits: List[EntranceData] = field(default_factory=list)


# Format is Region name, list of entrances.
# Entrance format is name of entrance, connecting region.
# The method below stitches them together generically.
queens_domain_regions = [
    RegionData("Menu", [
        EntranceData("Menu to Isle of Neasied Start", NeasiedRegion.starting_soldier_camp),
    ]),
    RegionData(NeasiedRegion.starting_soldier_camp, [
        EntranceData(NeasiedEntrance.camp_to_beach, NeasiedRegion.secret_eye_beach),
        EntranceData(NeasiedEntrance.camp_to_main_lower, NeasiedRegion.main_lower_area),
    ]),

]

def create_regions(starting_area: str, region_factory: RegionFactory, multiworld: MultiWorld) -> Tuple[Dict[str, Region], Dict[str, Entrance]]:
    final_regions = queens_domain_regions.copy()
    regions: Dict[str, Region] = {region.name: region_factory(region.name, region.exits) for region in
                                  final_regions}
    entrances: Dict[str, Entrance] = {}
    for region in regions.values():
        for entrance in region.exits:
            multiworld.register_indirect_condition(region, entrance)
            entrances[entrance.name] = entrance

    for connection in lunacid_entrances:
        if connection.entrance_name in entrances:
            entrances[connection.entrance_name].randomization_type = connection.type
            if connection.entrance_name == LunacidEntrance.rest_to_start:
                start_region = starting_location_to_region[starting_area]
                entrances[connection.entrance_name].connect(regions[start_region])
                continue
            entrances[connection.entrance_name].connect(regions[connection.region_exit])
    return regions, entrances

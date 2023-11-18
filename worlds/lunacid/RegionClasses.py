from enum import IntFlag
from typing import Optional, List
from dataclasses import dataclass, field

connector_keyword = " to "


class RandomizationFlag(IntFlag):
    NOT_RANDOMIZED = 0
    RANDOMIZED = 1


@dataclass(frozen=True)
class RegionData:
    name: str
    exits: List[str] = field(default_factory=list)

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

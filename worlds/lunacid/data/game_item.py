from dataclasses import dataclass


@dataclass(frozen=True)
class GameItem:
    name: str

    def __repr__(self):
        return f"{self.name}"

    def __lt__(self, other):
        return self.name < other.name

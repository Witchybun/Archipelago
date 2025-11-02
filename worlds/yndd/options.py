from dataclasses import dataclass
from typing import ClassVar, Protocol

from Options import Choice, Toggle, PerGameCommonOptions, Range, OptionSet, OptionDict


class DreamOption(Protocol):
    internal_name: ClassVar[str]


class Goal(Choice):
    """Choose which ending is required to complete the game.
    Apartment: Clear Apartment.
    Masada: Sleep in the bed on Masada's ship.
    """
    internal_name = "goal"
    display_name = "Goal"
    option_apartment = 0
    option_masada = 1
    default = 0

class LocalGoals(OptionSet):
    """Determine if Eggs or Jellyfish are in their vanilla positions or randomized."""
    internal_name = "local_goals"
    display_name = "Local Goals"
    valid_keys = ["Eggs", "Jellyfish"]
    default = ["Eggs", "Jellyfish"]

class RequiredEggs(Range):
    """How many eggs are required to unlock Apartment."""
    internal_name = "required_eggs"
    display_name = "Required Eggs"
    range_start = 1
    range_end = 6
    default = 5


class RequiredJellyfish(Range):
    """How many jellyfish are required to meet Masada.  Note that you need the eggs required above to reach
    the room that takes you there."""
    internal_name = "required_jellyfish"
    display_name = "Required Jellyfish"
    range_start = 1
    range_end = 6
    default = 5


class StartingDoors(Choice):
    """Determines how the doors in Nexus behave.
    Vanilla: All doors are unlocked at start save Heart Door.
    Choice: A select number of doors are unlocked at start.
    Range: A random number of doors are unlocked at start.
    """
    internal_name = "starting_doors"
    display_name = "Starting Doors"
    option_vanilla = 0
    option_choice = 1
    option_range = 2


class StartingDoorsChoice(OptionSet):
    """Determines which doors are open at start.  Only does anything if Starting Doors: Choice is set."""
    internal_name = "starting_doors_choice"
    display_name = "Starting Doors Choice"
    valid_keys = ["Streets", "Wilderness", "Mall", "Sewers", "Docks", "School"]
    default = ["Streets", "Wilderness", "Mall", "Sewers", "Docks", "School"]


class StartingDoorsRange(Range):
    """Determines how many doors are open at start.  Only does anything if Starting Doors: Range is set."""
    internal_name = "starting_doors_range"
    display_name = "Starting Doors Range"
    range_start = 1
    range_end = 6
    default = 6


class StartingBasicMovement(OptionSet):
    """What starting movement you have, and anything removed is shuffled and turned off at start."""
    internal_name = "basic_movement"
    display_name = "Starting Basic Movement"
    valid_keys = ["Jump", "Climb", "Run"]
    default = ["Jump", "Climb", "Run"]


class RandomizeConnectors(Toggle):
    """Randomizes the connectors between areas (Wilderness to Swamp, etc)."""
    internal_name = "randomize_connectors"
    display_name = "Randomize Connectors"


class LockConnectors(Toggle):
    """Makes the connectors between areas (Wilderness to Swamp, etc) locked unless you receive an item that allows it.
    If Randomize Connectors is toggled, items requirements may be disjointed (Train needs Train Pass, but Sewers needs Manhole Remover,
    so if Train goes to Sewers you might not be able to go back the way you came)."""
    internal_name = "lock_connectors"
    display_name = "Lock Connectors"


class RandomizeConsole(OptionSet):
    """Which console games have items/locations associated with them.  If a game has a goal in which locations
    are optionally collected, release protocol follows the generated game's release protocol.  Typing !!release [Game Name] in
    the in-game console will release it if enabled after goal.
    Nasu: Hi-score milestones.  Allowing the player to heal, a score doubler, and heal filler are added.
    Ao Oni: Keys, Friends, and Bonus Items are locations and items.  Goal is reached after 5 floors.  The 5 floors are
    randomly picked out of the first 20 in sequential order.
    Witch Adventure: """
    internal_name = "randomize_console"
    display_name = "Randomize console"
    valid_keys = ["Nasu", "Ao Oni", "Witch Adventure"]
    default = []


class SongLock(Toggle):
    """Each song you can usually play for an effect to happen is an item, and without it playing the tune does nothing.
    The Flute's description will tell you which songs you have."""
    internal_name = "song_lock"
    display_name = "Song Lock"


class DarkRoomsRequireLamp(Toggle):
    """Some rooms are doable without a light, but it's annoying.  Toggling this off puts them in logic without one."""
    internal_name = "dark_room_requires_lantern"
    display_name = "Dark Room Requires Lantern"
    default = True


class PinchSkip(Toggle):
    """You can skip requiring the umbrella to enter the school if you pinch yourself while Monoko screams at you.
    Similarly, requiring the picture can be skipped. This puts that trick in logic."""
    internal_name = "pinch_skip"
    display_name = "Pinch Skip"


class ItemColors(OptionDict):
    """Lets you determine the colors of items in-game using hexadecimal.  This includes Progression, Useful, Trap, Filler, Gifts, and
    Cheated (!getitem, starting inventory, etc)."""
    internal_name = "item_colors"
    valid_keys = ["ProgUseful", "Progression", "Useful", "Trap", "Filler", "Gift", "Cheat"]
    display_name = "Item Colors"
    default = {
        "ProgUseful": "#FF8000",
        "Progression": "#A335EE",
        "Useful": "#0070DD",
        "Trap": "#FA8072",
        "Filler": "#1EFF00",
        "Gift": "#FF8DA1",
        "Cheat": "#FF0000",
    }


@dataclass
class DreamOptions(PerGameCommonOptions):
    goal: Goal
    local_goals: LocalGoals
    required_eggs: RequiredEggs
    required_jellyfish: RequiredJellyfish
    starting_doors: StartingDoors
    starting_doors_choice: StartingDoorsChoice
    starting_doors_range: StartingDoorsRange
    starting_basic_movement: StartingBasicMovement
    randomize_connectors: RandomizeConnectors
    lock_connectors: LockConnectors
    randomize_console: RandomizeConsole
    song_lock: SongLock
    dark_room_require_lantern: DarkRoomsRequireLamp
    pinch_skip: PinchSkip
    item_colors: ItemColors

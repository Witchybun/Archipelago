from dataclasses import dataclass
from typing import ClassVar, Protocol

from Options import Choice, Toggle, DeathLink, PerGameCommonOptions, Range, OptionSet, OptionDict


class QueensDomainOption(Protocol):
    internal_name: ClassVar[str]


class Goal(OptionSet):
    """Choose which goal is required to complete the game.  Any ending included can be used to goal.
    If no goal is chosen, default will be to lose to Queen Siraatsu.
    Lose to Queen Siraatsu: Beat Queen Siraatsu without the True Holy Sword Akunra.
    Seal Queen Siraatsu: Beat Enraged Queen Siraatsu.
    Destroy Siphena: Beat Soul of Siphena.
    Eat Siphena: Eat Soul of Siphena.
    Get Stickbugged: Open the chest at the top of Tower of Knowledge."""
    internal_name = "goal"
    display_name = "Goal"
    valid_keys = ["Lose to Queen Siraatsu", "Seal Queen Siraatsu", "Destroy Siphena", "Eat Siphena", "Get Stickbugged"]
    default = ["Lose to Queen Siraatsu"]


class RequiredSkulls(Range):
    """Determines how many silver skulls are required to goal on Eat Siphena.  Does nothing otherwise."""
    internal_name = "required_skulls"
    display_name = "Required Skulls"
    range_start = 1
    range_end = 69
    default = 69

class LogicalCestus(Toggle):
    """Adds the Cestus and Black Diamond Claw to platforming logic."""
    internal_name = "logical_cestus"
    display_name = "logical_cestus"


class LogicalThrust(Toggle):
    """Adds the Pandora Sword, Ancient Short Sword, and Iron Fist to platforming logic for their thrust.
    Iron Fist's thrusts only go up to 4, based on energy cells."""
    internal_name = "logical_thrust"
    display_name = "Logical Thrust"


class IncludeRustedShortSword(Toggle):
    """If logical thrust is on, this includes the Rusted Short Sword's one thrust.
    This is a temporary weapon which loses the lunge on evolution.
    Evolving the weapon can cause a softlock, you have been warned."""
    internal_name = "include_rusted"
    display_name = "Include Rusted Short Sword"


class Filler(OptionDict):
    """Lets you decide which filler are added to the game and their weights.  If the set is empty or all values are zero,
    Silver and Deep Knowledge will be forced included with weights of 1. Amount received in game is a random value between 1~5, favoring 1~2.
    Most filler is self-explanatory save the following:
    Deep Knowledge: You get 1 level.
    Weight of the Dream (Nothing): Is a nothing item.  Useful if you feel like other items make the game too easy.
    Demi's Gift for a Stranger: Attempts to give a random player a random gift.  If it fails or is a solo game, does nothing."""

    internal_name = "filler"
    display_name = "Filler"
    valid_keys = [item for item in default_filler_weights]
    default = default_filler_weights


class FillerLocalPercent(Range):
    """How much of filler is forced local?  Helpful when you don't want to fill the multiworld with your own junk but its fine if some of it bleeds out.
    Note that 0% just means none of it is *forced* to be local, not that it is all non-local."""
    internal_name = "filler_local_percent"
    display_name = "Filler Local Percent"
    range_start = 0
    range_end = 98
    default = 0


@dataclass
class QueensDomainOptions(PerGameCommonOptions):
    goal: Goal
    required_skulls: RequiredSkulls
    logical_cestus: LogicalCestus
    logical_thrust: LogicalThrust
    include_rusted: IncludeRustedShortSword
    filler: Filler
    filler_local_percent: FillerLocalPercent

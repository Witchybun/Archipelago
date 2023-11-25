from dataclasses import dataclass
from Options import Choice, Toggle, DeathLink, PerGameCommonOptions


class Ending(Choice):
    """Choose which ending is required to complete the game.
    Ending A: Reach Chamber of the Sleeper without all spells and awaken the Dreamer.
    Ending CD: Reach Chamber of the Sleeper and stare into the water pool.
    Ending E: Reach Chamber of the Sleeper with all spells and awaken the Dreamer."""
    internal_name = "ending"
    display_name = "Ending"
    option_any_ending = 0
    option_ending_a = 1
    option_ending_cd = 2
    option_ending_e = 3
    default = 0


class Shopsanity(Toggle):
    """Choose whether the unique items Sheryl the Crow sells are locations."""
    internal_name = "shopsanity"
    display_name = "Shopsanity"


class Dropsanity(Toggle):
    """Choose whether the unique items monsters drop are locations."""
    internal_name = "dropsanity"
    display_name = "Dropsanity"


class Switchsanity(Toggle):
    """Choose whether the switches in the game are locations, and their action of opening doors is an item."""
    internal_name = "switchsanity"
    display_name = "Switchsanity"


class Arbitraryfiller(Toggle):
    """Choose how non-progression items are handled.
    Off: Original location items are used for the randomizer.
    On: Any item denoted as filler from Lunacid is used for the randomizer."""
    internal_name = "arbitraryfiller"
    display_name = "Arbitrary Filler"


class LunacidDeathLink(DeathLink):
    """When you die, everyone dies. The reverse is also true.
    Note that this causes a Game Over; save often!"""
    internal_name = "death_link"


@dataclass
class LunacidOptions(PerGameCommonOptions):
    ending = Ending
    shopsanity = Shopsanity
    dropsanity = Dropsanity
    switchsanity = Switchsanity
    arbitraryfiller = Arbitraryfiller
    death_link = LunacidDeathLink

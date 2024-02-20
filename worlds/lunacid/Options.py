from dataclasses import dataclass
from Options import Choice, Toggle, DeathLink, PerGameCommonOptions, Range


class Ending(Choice):
    """Choose which ending is required to complete the game.
    Ending A: Reach Chamber of the Sleeper without all spells and awaken the Dreamer.
    Ending B: Obtain 30 Strange Coins and enter the door located in the Labyrinth of Ash.
    Ending CD: Reach Chamber of the Sleeper and stare into the water pool.
    Ending E: Reach Chamber of the Sleeper with all spells and awaken the Dreamer."""
    internal_name = "ending"
    display_name = "Ending"
    option_any_ending = 0
    option_ending_a = 1
    option_ending_b = 2
    option_ending_cd = 3
    option_ending_e = 4
    default = 0


class ExperienceMod(Range):
    """Multiplier for gained experience as a percent.  Ranges from 25% to 400%."""
    internal_name = "experience"
    display_name = "Experience Modifier"
    range_start = 25
    range_end = 400
    default = 100


class StrangeCoinBundle(Choice):
    """Changes the drop total of the strange coins from 10 to any divisor of 30, helping it become more of a maguffin hunt.
    Note: Filler will be replaced to compensate."""
    internal_name = "strangecoinbundle"
    display_name = "Strange Coin Bundle"
    option_one = 0
    option_two = 1
    option_three = 2
    option_five = 3
    option_six = 4
    option_ten = 5
    option_fifteen = 6
    option_thirty = 7
    default = 5


class FillerBundle(Range):
    """Changes how many of the non-unique filler items are given to the player when such an item is received."""
    internal_name = "fillerbundle"
    display_name = "Filler Bundle"
    range_start = 1
    range_end = 5
    default = 1


class Shopsanity(Toggle):
    """Choose whether the unique items Sheryl the Crow sells are locations."""
    internal_name = "shopsanity"
    display_name = "Shuffle Shop Items"


class Dropsanity(Toggle):
    """Choose whether the unique items monsters drop are locations."""
    internal_name = "dropsanity"
    display_name = "Mob Drops"


class SwitchLocks(Toggle):
    """All physical switches (not mirages) are locked, and cannot be flipped without their relevant item.
    Note: Removes filler at random to compensate."""
    internal_name = "switchlock"
    display_name = "Lock Switches"


@dataclass
class LunacidOptions(PerGameCommonOptions):
    ending: Ending
    experience: ExperienceMod
    strangecoinbundle: StrangeCoinBundle
    fillerbundle: FillerBundle
    shopsanity: Shopsanity
    dropsanity: Dropsanity
    switchlocks: SwitchLocks
    death_link: DeathLink

from Options import Choice, Toggle, Range, DeathLink, PerGameCommonOptions
import random


class ChoiceIsRandom(Choice):
    randomized: bool = False

    @classmethod
    def from_text(cls, text: str) -> Choice:
        text = text.lower()
        if text == "random":
            cls.randomized = True
            return cls(random.choice(list(cls.name_lookup)))
        for option_name, value in cls.options.items():
            if option_name == text:
                return cls(value)
        raise KeyError(
            f'Could not find option "{text}" for "{cls.__name__}", '
            f'known options are {", ".join(f"{option}" for option in cls.name_lookup.values())}')


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


class Fillershuffle(Choice):
    """Choose how non-progression items are handled.
    Shuffled: Only use the items and counts obtainable from their respective locations in the original game.
    Random: Choose items from the entire game (includes some monster drops and alchemy creations).
    Note that items from un-toggled options will not be chosen."""
    internal_name = "fillershuffle"
    display_name = "Filler Shuffle"
    option_shuffled = 0
    option_random = 1
    default = 0


class LunacidDeathLink(DeathLink):
    """When you die, everyone dies. The reverse is also true.
    Note that this causes a Game Over; save often!"""


class LunacidOptions(PerGameCommonOptions):
    ending: Ending
    shopsanity = Shopsanity
    dropsanity = Dropsanity
    switchsanity = Switchsanity
    fillershuffle = Fillershuffle
    death_link: LunacidDeathLink

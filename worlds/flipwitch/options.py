from dataclasses import dataclass

from Options import Toggle, Choice, DefaultOnToggle, Range, PerGameCommonOptions, StartInventoryPool


class StartingGender(Choice):
    """Decides the starting gender state."""
    internal_name = "starting_gender"
    display_name = "Starting Gender"
    option_female = 0
    option_male = 1
    default = 0


class ShuffleChaosPieces(Toggle):
    """Shuffles the six Chaos Pieces in your game.
    Off: All pieces are placed in their original locations.
    On: All six Chaos Pieces can be found anywhere in the multiworld.
    If you want to plando these, turn this on first.
    """
    internal_name = "shuffle_chaos_pieces"
    display_name = "Shuffle Chaos Pieces"


class Gachapon(Toggle):
    """Shuffles the rewards of the gachapon rewards."""
    internal_name = "gachapon"
    display_name = "Gachapon"


class CrystalTeleports(Toggle):
    """Shuffles the crystal teleports.  Item is obtained by interacting with a teleport panel.
    This doesn't do anything right now."""
    internal_name = "crystal_teleports"
    display_name = "Crystal Teleports"


class DeathLink(Toggle):
    """If on: Whenever another player on death link dies, you will be returned to the starting room."""
    display_name = "Death Link"


@dataclass
class FlipwitchOptions(PerGameCommonOptions):
    starting_gender: StartingGender
    shuffle_chaos_pieces: ShuffleChaosPieces
    gachapon: Gachapon
    crystal_teleports: CrystalTeleports
    death_link: DeathLink

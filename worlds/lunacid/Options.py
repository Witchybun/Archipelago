from dataclasses import dataclass
from typing import ClassVar, Protocol

from Options import Choice, Toggle, DeathLink, PerGameCommonOptions, Range


class LunacidOption(Protocol):
    internal_name: ClassVar[str]


class Ending(Choice):
    """Choose which ending is required to complete the game.
    Ending A: Reach Chamber of the Sleeper without all spells and awaken the Dreamer.
    Ending B: Obtain enough Strange Coins and enter the door located in the Labyrinth of Ash.
    Ending CD: Reach Chamber of the Sleeper and stare into the water pool.
    Ending E: Reach Chamber of the Sleeper with all spells after watching the White VHS Tape and awaken the Dreamer."""
    internal_name = "ending"
    display_name = "Ending"
    option_any_ending = 0
    option_ending_a = 1
    option_ending_b = 2
    option_ending_cd = 3
    option_ending_e = 4
    default = 1


class Class(Choice):
    """The class you play as.
    Note: The following classes are handled differently in the game:
    Royal receives nothing from Demi, and so the location doesn't exist for them.
    Vampire has free access to the cattle cells and the first area, so the first vampiric symbol is unnecessary."""
    internal_name = "starting_class"
    display_name = "Class"
    option_thief = 0
    option_knight = 1
    option_witch = 2
    option_vampire = 3
    option_undead = 4
    option_royal = 5
    option_cleric = 6
    option_shinobi = 7
    option_forsaken = 8


class EntranceRandomization(Toggle):
    """Shuffles the entrances around.  The only untouched entrances are crystal warps (including spell/item), entrance to Chamber of Fate, entrance to
    Grave of the Sleeper, and the doors of Tower of Abyss."""
    internal_name = "entrance_randomization"
    display_name = "Entrance Randomization"


class Experience(Range):
    """Multiplier for gained experience as a percent.  Ranges from 25% to 400%."""
    internal_name = "experience"
    display_name = "Experience Modifier"
    range_start = 25
    range_end = 400
    default = 100


class WeaponExperience(Range):
    """Multiplier for gained weapon experience as a percent.  Ranges from 25% to 400%"""
    internal_name = "weapon_experience"
    display_name = "Weapon Experience Modifier"
    range_start = 25
    range_end = 400
    default = 100


class RequiredStrangeCoins(Range):
    """Changes the required coins needed to open the door for Ending B."""
    internal_name = "required_strange_coin"
    display_name = "Required Strange Coins"
    range_start = 1
    range_end = 60
    default = 30


class TotalStrangeCoins(Range):
    """The total amount of strange coins placed in the multiworld.  Matches required if lower than it.
    Note: Filler will be replaced to compensate."""
    internal_name = "total_strange_coin"
    display_name = "Total Strange Coins"
    range_start = 1
    range_end = 60
    default = 30


class RandomElements(Toggle):
    """Randomizes the elements of almost all weapons and spells.  Guaranteed Poison ranged option.
    Lucid Blade and Wand of Power are not randomized (either due to limitation, or to guarantee victory)"""
    internal_name = "random_elements"
    display_name = "Random Elements"


class Shopsanity(Toggle):
    """Choose whether the unique items Sheryl the Crow sells are locations.
    Adds 9 locations."""
    internal_name = "shopsanity"
    display_name = "Shuffle Shop Items"


class Dropsanity(Choice):
    """Choose whether the items monsters drop are locations.
    Off: All drops are vanilla.
    Uniques: Only the unique first-drop items (weapons, spells, elixirs) are locations.  Adds 19 locations.
    Randomized: Each drop is a location.  WARNING SOME DROPS ARE HORRIBLE TO GET.  Adds 143 locations."""
    internal_name = "dropsanity"
    display_name = "Mob Drops"
    option_off = 0
    option_uniques = 1
    option_randomized = 2
    default = 0


class Quenchsanity(Toggle):
    """If a weapon can gain experience, if it is quenched, it returns a check.
    Quenching a weapon now no longer upgrades the weapons, and all quench weapons are added to the pool.
    Exceptions: Brittle Arming Sword repairs itself for the sake of the player, and Death Scythe is removed from the inventory as normal."""
    internal_name = "quenchsanity"
    display_name = "Quenchsanity"


class EtnasPupil(Toggle):
    """Become Etna's pupil!  As in, all alchemy creations are locations to check.  Cmon saying -sanity a lot is boring.
    If Dropsanity: Randomized is selected, each material is force placed on drops or alchemy spots to ensure repeatability."""
    internal_name = "etnas_pupil"
    display_name = "Etna's Pupil"


class NormalizedDrops(Toggle):
    """Every enemy drop is normalized against the chance of dropping nothing.  Specifically, if an enemy
    has a weight of X to drop nothing, everything else also has a weight of X, and is split evenly for every
    item it could drop.  Helps with the sin of the Angel Feather."""
    internal_name = "normalized_drops"
    display_name = "Normalized Drops"


class SwitchLocks(Toggle):
    """All physical switches (not mirages) are locked, and cannot be flipped without their relevant item.
    Note: Removes filler at random to compensate."""
    internal_name = "switch_lock"
    display_name = "Lock Switches"


class DoorLocks(Toggle):
    """All physical doors leading to new zones are locked, and cannot be opened without their relevant item.
    Note: Removes filler at random to compensate."""
    internal_name = "door_lock"
    display_name = "Lock Doors"


class SecretDoorLock(Toggle):
    """All secret doors are locked until receiving the Dusty Crystal Orb."""
    internal_name = "secret_door_lock"
    display_name = "Secret Door Lock"


class ExcludeTower(Toggle):
    """Option to not include the entirety of Tower of Abyss, as it can be time-consuming.
    Will remove the Tower of Abyss Keyring (if Door Locks is Chosen), Crystal Lamp, Moonlight,
    and an Earth and Ocean Elixir from the pool.  Removes 11 locations."""
    internal_name = "exclude_tower"
    display_name = "Exclude Tower"


class ExcludeCoinLocations(Toggle):
    """Excludes the locations where one has to shoot a blood spell in the Temple of Silence, Kill the Jotunn, and kill Death.
    Perhaps it just makes you feel bad.  With this the locations just don't give anything.  Removes 3 locations."""
    internal_name = "exclude_coin_locations"
    display_name = "Exclude Coin Locations"


class ExcludeDaedalus(Toggle):
    """Excludes the locations associated with giving Daedalus Black Books.  Also removes the Black Books from the pool."""
    internal_name = "exclude_daedalus"
    display_name = "Exclude Daedalus"


class CraftedFiller(Toggle):
    """Allows for items mainly made with alchemy to be added as filler.  This excludes Crystal Shards, Health Vials, Mana Vials, Antidotes, and Cloth Bandages.
    Note: Bombs are overpowered, so it might make the game too easy."""
    internal_name = "crafted_filler"
    display_name = "Crafted Filler"


class DropFiller(Toggle):
    """Adds Angel Feather, Shrimp, and dropped alchemy materials into the filler pool.
    Note: Angel Feather is overpowered, so it might make the game too easy."""
    internal_name = "drop_filler"
    display_name = "Drop Filler"


class FillerBundle(Range):
    """Changes how many of the non-unique filler items are given to the player when such an item is received."""
    internal_name = "filler_bundle"
    display_name = "Filler Bundle"
    range_start = 1
    range_end = 5
    default = 1


class TrapPercent(Range):
    """Percent of filler items to be converted to traps."""
    internal_name = "trap_percent"
    display_name = "Trap Percent"
    range_start = 0
    range_end = 100
    default = 20


@dataclass
class LunacidOptions(PerGameCommonOptions):
    ending: Ending
    starting_class: Class
    entrance_randomization: EntranceRandomization
    experience: Experience
    weapon_experience: WeaponExperience
    random_elements: RandomElements
    required_strange_coin: RequiredStrangeCoins
    total_strange_coin: TotalStrangeCoins
    shopsanity: Shopsanity
    dropsanity: Dropsanity
    quenchsanity: Quenchsanity
    etnas_pupil: EtnasPupil
    normalized_drops: NormalizedDrops
    secret_door_lock: SecretDoorLock
    switch_locks: SwitchLocks
    door_locks: DoorLocks
    exclude_tower: ExcludeTower
    exclude_coin_locations: ExcludeCoinLocations
    exclude_daedalus: ExcludeDaedalus
    crafted_filler: CraftedFiller
    drop_filler: DropFiller
    filler_bundle: FillerBundle
    trap_percent: TrapPercent
    death_link: DeathLink

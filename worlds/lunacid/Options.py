from dataclasses import dataclass
from typing import ClassVar, Protocol

from Options import Choice, Toggle, DeathLink, PerGameCommonOptions, Range, OptionSet, OptionDict
from worlds.lunacid.data.item_data import all_filler_items
from .strings.items import Trap, Coins


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
    Vampire has free access to the cattle cells and the first area, so the first vampiric symbol is unnecessary.
    Custom is an advanced option.  If on a website its values will not be visible.  You know how it is smh."""
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
    option_custom = 9


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


class EnemyRandomization(Toggle):
    """Shuffles the in-game enemies around. Each enemy in the game is replaced by some other enemy."""
    internal_name = "enemy_randomization"
    display_name = "Enemy Randomization"


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


class RemoveLocations(OptionSet):
    """Removes certain locations from being in the pool at all.  Helps to avoid situations where even filler is not wanted on locations you would not do.
    Choices are as follows with additional item removal information associated with the location removal:
    Tower of Abyss: Also removes Crystal Lamp, Moonlight, and an Earth and Ocean Elixir from the pool.  11 Locations.
    Strange Coins: Removes blood altar location in Temple of Silence, Kill the Jotunn and Kill Death.  3 Locations.
    Daedalus: Removes all Black Books from the pool.  3 Locations."""
    internal_name = "remove_locations"
    display_name = "Remove Locations"
    valid_keys = frozenset({"Tower of Abyss", "Strange Coins", "Daedalus"})
    preset_none = frozenset()
    preset_all = valid_keys
    default = frozenset()


class Filler(OptionSet):
    """Lets you decide which filler are added to the game.  If the set is empty, only silver and exp is included.
    Amount received in game is a random value between 1~5, favoring 1~2.
    Acceptable Filler: Blood Wine, Light Urn, Cloth Bandage, Dark Urn, Bomb, Poison Urn, Wisp Heart, Staff of Osiris,
    Moonlight Vial, Spectral Candle, Health Vial, Mana Vial, Fairy Moss, Crystal Shard, Poison Throwing Knife,
    Throwing Knife, Holy Water, Antidote, Survey Banner, Pink Shrimp, Angel Feather, Fool's Gold, Ectoplasm,
    Snowflake Obsidian, Moon Petal, Fire Opal, Ashes, Fiddlehead, Fire Coral, Vampiric Ashes,
    Opal, Yellow Morel, Lotus Seed Pod, Obsidian, Onyx, Ocean Bone Shard, Bloodweed, Ikurr'ilb Root,
    Destroying Angel Mushroom, Ocean Bone Shell, Bones."""
    internal_name = "filler"
    display_name = "Filler"
    valid_keys = frozenset([item for item in all_filler_items if item != Coins.silver])
    preset_none = frozenset()
    preset_all = valid_keys
    default = frozenset([item for item in all_filler_items if item != Coins.silver])


class Traps(OptionSet):
    """Lets you decide which traps are in your game.  If empty, same as having 0 Trap Percent.
    Certain joyous traps are allowed during Christmas, otherwise are ignored.
    Acceptable Traps: "Bleed Trap", "Poison Trap", "Curse Trap", "Slowness Trap", "Blindness Trap", "Mana Drain Trap", "XP Drain Trap", Coal, Eggnog."""
    internal_name = "traps"
    display_name = "Traps"
    valid_keys = frozenset(Trap.all_traps + Trap.christmas_gifts)
    preset_none = frozenset()
    preset_all = valid_keys
    default = frozenset(Trap.all_traps)


class TrapPercent(Range):
    """Percent of filler items to be converted to traps."""
    internal_name = "trap_percent"
    display_name = "Trap Percent"
    range_start = 0
    range_end = 100
    default = 20


class CustomMusic(Toggle):
    """Lets you use custom music.  If on, will read from a CustomMusic folder in the game's base directory.  Only accepts mp3 files.
    If no music is supplied, will be the same as if this setting was off."""
    internal_name = "custom_music"
    display_name = "Custom Music"


class ItemColors(OptionDict):
    """Lets you determine the colors of items in-game using hexadecimal.  This includes Progression, Useful, Trap, Filler, Gifts, and
    Cheated (!getitem, starting inventory, etc).  If an item has multiple flags, the colors are averaged."""
    internal_name = "item_colors"
    valid_keys = ["Progression", "Useful", "Trap", "Filler", "Gift", "Cheat"]
    display_name = "Item Colors"
    default = {
        "Progression": "#AF99EF",
        "Useful": "#6D8BE8",
        "Trap": "#FA8072",
        "Filler": "#00EEEE",
        "Gift": "#9DAE11",
        "Cheat": "#FF0000",
    }


class CustomClass(OptionDict):
    """If 'Custom' is chosen for starting class, this is used as a stand-in for that information.
    If Name or Description is 'RANDOM', or any stat is -1, a random value will be supplied.
    Level ranges from 1 to 10.
    Stats (Strength to Resistance) range from 1 to 20.
    Resistances (Normal Res to Dark Res) range from 0 to 300."""
    internal_name = "custom_class"
    display_name = "Custom Class"
    valid_keys = ["Name", "Description", "Level", "Strength", "Speed", "Intelligence", "Defense", "Dexterity", "Resistance", "Normal Res",
                  "Fire Res", "Ice Res", "Poison Res", "Light Res", "Dark Res"]
    default = {
        "Name": "RANDOM",
        "Description": "RANDOM",
        "Level": -1,
        "Strength": -1,
        "Speed": -1,
        "Intelligence": -1,
        "Defense": -1,
        "Dexterity": -1,
        "Resistance": -1,
        "Normal Res": -1,
        "Fire Res": -1,
        "Ice Res": -1,
        "Poison Res": -1,
        "Light Res": -1,
        "Dark Res": -1,
    }


@dataclass
class LunacidOptions(PerGameCommonOptions):
    ending: Ending
    starting_class: Class
    entrance_randomization: EntranceRandomization
    experience: Experience
    weapon_experience: WeaponExperience
    random_elements: RandomElements
    enemy_randomization: EnemyRandomization
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
    remove_locations: RemoveLocations
    filler: Filler
    traps: Traps
    trap_percent: TrapPercent
    custom_music: CustomMusic
    item_colors: ItemColors
    custom_class: CustomClass
    death_link: DeathLink

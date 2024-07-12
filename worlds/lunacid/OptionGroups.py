from Options import DeathLink, ProgressionBalancing, Accessibility, OptionGroup
from .Options import (Ending, Class, EntranceRandomization, Experience, WeaponExperience, RandomElements, RequiredStrangeCoins, TotalStrangeCoins,
                      Shopsanity, Dropsanity, Quenchsanity, EtnasPupil, NormalizedDrops, SecretDoorLock, SwitchLocks, DoorLocks, RemoveLocations, CraftedFiller,
                      DropFiller, FillerBundle, TrapPercent)

lunacid_option_groups = [
    OptionGroup("General", [
        Ending,
        Class,
        RandomElements,
        EntranceRandomization,
        RequiredStrangeCoins,
        TotalStrangeCoins
    ]),
    OptionGroup("Extra Shuffling", [
        Shopsanity,
        Dropsanity,
        Quenchsanity,
        EtnasPupil,
    ]),
    OptionGroup("Locks", [
        DoorLocks,
        SwitchLocks,
        SecretDoorLock
    ]),
    OptionGroup("Tweaks", [
        Experience,
        WeaponExperience,
        NormalizedDrops,
        RemoveLocations,
        CraftedFiller,
        DropFiller,
        FillerBundle,
        TrapPercent
    ]),
    OptionGroup("Advanced Options", [
        RemoveLocations,
        DeathLink,
        ProgressionBalancing,
        Accessibility,
    ])
]

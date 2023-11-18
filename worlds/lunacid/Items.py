from BaseClasses import ItemClassification
from typing import TypedDict, Dict, List, Set


class ItemDict(TypedDict):
    name: str
    count: int
    classification: ItemClassification

base_id = 1909000

item_table: List[ItemDict] = [
    # Weapons
    {'name': "Axe of Harming",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Battle Axe",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Blade of Jusztina",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Blade of Opheilia",
        'count': 1,
     'classification': ItemClassification.useful},
    {'name': "Blessed Wind",
        'count': 1,
        'classification': ItemClassification.useful}

]

event_table: Dict[str, str] = {
    "OpenedDCGateW": "D01Z05S24",
    "OpenedDCGateE": "D01Z05S12",
    "OpenedDCLadder": "D01Z05S20",
    "OpenedWOTWCave": "D02Z01S06",
    "RodeGOTPElevator": "D02Z02S11",
    "OpenedConventLadder": "D02Z03S11",
    "BrokeJondoBellW": "D03Z02S09",
    "BrokeJondoBellE": "D03Z02S05",
    "OpenedMOMLadder": "D04Z02S06",
    "OpenedTSCGate": "D05Z02S11",
    "OpenedARLadder": "D06Z01S23",
    "BrokeBOTTCStatue": "D08Z01S02",
    "OpenedWOTHPGate": "D09Z01S05",
    "OpenedBOTSSLadder": "D17Z01S04"
}

group_table: Dict[str, Set[str]] = {
    "wounds"  : ["Holy Wound of Attrition",
                 "Holy Wound of Contrition",
                 "Holy Wound of Compunction"],

    "masks"   : ["Deformed Mask of Orestes",
                 "Mirrored Mask of Dolphos",
                 "Embossed Mask of Crescente"],

    "marks"   : ["Mark of the First Refuge",
                 "Mark of the Second Refuge",
                 "Mark of the Third Refuge"],

    "tirso"   : ["Bouquet of Rosemary",
                 "Incense Garlic",
                 "Olive Seeds",
                 "Dried Clove",
                 "Sooty Garlic",
                 "Bouquet of Thyme"],

    "tentudia": ["Tentudia's Carnal Remains",
                 "Remains of Tentudia's Hair",
                 "Tentudia's Skeletal Remains"],

    "egg"     : ["Melted Golden Coins",
                 "Torn Bridal Ribbon",
                 "Black Grieving Veil"],

    "bones"   : ["Parietal bone of Lasser, the Inquisitor",
                 "Jaw of Ashgan, the Inquisitor",
                 "Cervical vertebra of Zicher, the Brewmaster",
                 "Clavicle of Dalhuisen, the Schoolchild",
                 "Sternum of Vitas, the Performer",
                 "Ribs of Sabnock, the Guardian",
                 "Vertebra of John, the Gambler",
                 "Scapula of Carlos, the Executioner",
                 "Humerus of McMittens, the Nurse",
                 "Ulna of Koke, the Troubadour",
                 "Radius of Helzer, the Poet",
                 "Frontal of Martinus, the Ropemaker",
                 "Metacarpus of Hodges, the Blacksmith",
                 "Phalanx of Arthur, the Sailor",
                 "Phalanx of Miriam, the Counsellor",
                 "Phalanx of Brannon, the Gravedigger",
                 "Coxal of June, the Prostitute",
                 "Sacrum of the Dark Warlock",
                 "Coccyx of Daniel, the Possessed",
                 "Femur of Karpow, the Bounty Hunter",
                 "Kneecap of Sebastien, the Puppeteer",
                 "Tibia of Alsahli, the Mystic",
                 "Fibula of Rysp, the Ranger",
                 "Temporal of Joel, the Thief",
                 "Metatarsus of Rikusyo, the Traveller",
                 "Phalanx of Zeth, the Prisoner", 
                 "Phalanx of William, the Sceptic",
                 "Phalanx of Aralcarim, the Archivist",
                 "Occipital of Tequila, the Metalsmith",
                 "Maxilla of Tarradax, the Cleric",
                 "Nasal bone of Charles, the Artist",
                 "Hyoid bone of Senex, the Beggar",
                 "Vertebra of Lindquist, the Forger",
                 "Trapezium of Jeremiah, the Hangman",
                 "Trapezoid of Yeager, the Jeweller",
                 "Capitate of Barock, the Herald",
                 "Hamate of Vukelich, the Copyist",
                 "Pisiform of Hernandez, the Explorer",
                 "Triquetral of Luca, the Tailor",
                 "Lunate of Keiya, the Butcher",
                 "Scaphoid of Fierce, the Leper",
                 "Anklebone of Weston, the Pilgrim",
                 "Calcaneum of Persian, the Bandit",
                 "Navicular of Kahnnyhoo, the Murderer"],
    
    "power"   : ["Life Upgrade",
                 "Fervour Upgrade",
                 "Empty Bile Vessel",
                 "Quicksilver"],

    "prayer"  : ["Seguiriya to your Eyes like Stars",
                 "Debla of the Lights",
                 "Saeta Dolorosa",
                 "Campanillero to the Sons of the Aurora",
                 "Lorquiana",
                 "Zarabanda of the Safe Haven",
                 "Taranto to my Sister",
                 "Solea of Excommunication",
                 "Tiento to your Thorned Hairs",
                 "Cante Jondo of the Three Sisters",
                 "Verdiales of the Forsaken Hamlet",
                 "Romance to the Crimson Mist",
                 "Zambra to the Resplendent Crown",
                 "Cantina of the Blue Rose",
                 "Mirabras of the Return to Port"]
}

tears_set: Set[str] = [
    "Tears of Atonement (500)",
    "Tears of Atonement (625)",
    "Tears of Atonement (750)",
    "Tears of Atonement (1000)",
    "Tears of Atonement (1250)",
    "Tears of Atonement (1500)",
    "Tears of Atonement (1750)",
    "Tears of Atonement (2000)",
    "Tears of Atonement (2100)",
    "Tears of Atonement (2500)",
    "Tears of Atonement (2600)",
    "Tears of Atonement (3000)",
    "Tears of Atonement (4300)",
    "Tears of Atonement (5000)",
    "Tears of Atonement (5500)",
    "Tears of Atonement (9000)",
    "Tears of Atonement (10000)",
    "Tears of Atonement (11250)",
    "Tears of Atonement (18000)",
    "Tears of Atonement (30000)"
]

reliquary_set: Set[str] = [
    "Reliquary of the Fervent Heart",
    "Reliquary of the Suffering Heart",
    "Reliquary of the Sorrowful Heart"
]

skill_set: Set[str] = [
    "Combo Skill",
    "Charged Skill",
    "Ranged Skill",
    "Dive Skill",
    "Lunge Skill"
]
from enum import Enum


class PlayerClass(Enum):
    MAGE = "mage"
    WARRIOR = "warrior"
    ARCHER = "archer"
    THIEF = "thief"
    MONK = "monk"


class Profession(Enum):
    SCHOLAR = "scholar"
    CRAFTER = "crafter"
    HUNTER = "hunter"
    GUARD = "guard"
    HEALER = "healer"

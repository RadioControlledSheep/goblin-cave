import random
from enum import Enum


class ItemType(Enum):
    WEAPON = "weapon"
    ARMOUR = "armour"
    CONSUMABLE = "consumable"
    MISC = "miscellaneous"
    TRASH = "trash"


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Consumable(Item):
    def __init__(self, name, description, stat, modifier):
        super().__init__(name, description)
        self.ability = stat
        self.modifier = modifier


def consumables():
    consumables = set({})
    mana_potion = Consumable(
        "Mana Potion",
        --"A swirling potion, restores up to 2d8+20 mana",
        "mana",
        "2d8+20",
    )
    consumables.add(mana_potion)
    healing_potion = Consumable(
        "Healing Potion",
        "A viscous red potion, restores up to 2d8+20 health",
        "health",
        "2d8+20",
    )
    consumables.add(healing_potion)
    bandage = Consumable(
        "Bandages",
        "Some simple bandages, restores up to 2d8+10 health",
        "health",
        "2d8+10",
    )
    consumables.add(bandage)
    return consumables


#   Items:
#   Caltrops
#   Rope
#   Grapple
#   Torch


class Weapon(Item):
    def __init__(self, name, description, damage, damage_type, two_handed=False):
        super().__init__(name, description)
        self.damage = damage
        self.damage_type = damage_type
        self.two_handed = two_handed


def weapons():
    weapons = set({})
    dagger = Weapon(
        "Dagger", "A simple dagger", "1d4", DamageType.PIERCE, two_handed=False
    )
    weapons.add(dagger)
    short_sword = Weapon(
        "Short Sword",
        "A short one handed weapon",
        "1d6",
        DamageType.PIERCE,
        two_handed=False,
    )
    weapons.add(short_sword)
    rapier = Weapon(
        "Rapier", "A narrow piercing sword", "1d6", DamageType.PIERCE, two_handed=False
    )
    weapons.add(rapier)


#   Weapons:
#   Dagger P 1d4
#   Short Sword P 1d6
#   Rapier P 1d6
#   Staff B 1d6
#   Mace B 2d4
#   Morningstar B 1d8
#   Longsword S 1d8
#   Hand Axe S 1d6
#   Battle Axe S 1d8
#   2 Handed Sword S 1d12
#   Short bow P 1d6
#   Long bow P 1d8
#   Crossbow P 1d10


class Armour(Item):
    def __init__(
        self,
        name,
        description,
        armour_value,
        weak_against=set({}),
        strong_against=set({}),
        off_hand=False,
    ):
        super().__init__(name, description)
        self.armour_value = armour_value
        self.off_hand = off_hand
        self.weak = weak_against
        self.strong = strong_against


def armour_set():
    robes = Armour(
        "Cloth Robes",
        "Looks like a dressing gown, offers about as much protection too",
        1,
    )
    leather = Armour(
        "Leather", "Cured dead animal skin", 2, set({}), {DamageType.ELECTRIC}
    )
    studded_leather = Armour(
        "Studded Leather",
        "Cured dead animal skin with metal bits added",
        3,
        set({}),
        {DamageType.ELECTRIC},
    )
    chainmail = Armour(
        "Chainmail",
        "Interlocking steel rings, worn over a gambeson",
        5,
        {DamageType.PIERCE, DamageType.ELECTRIC},
        {DamageType.SLASH},
    )
    cuirass = Armour(
        "Cuirass",
        "Beaten metal, protects the torso",
        7,
        {DamageType.FIRE, DamageType.ELECTRIC},
    )
    buckler = Armour(
        "Buckler", "A small round shield.", 1, {DamageType.BLUNT}, set({}), True
    )
    shield = Armour(
        "Shield",
        "A shield made of laminated wood",
        3,
        {DamageType.FIRE},
        {DamageType.BLUNT},
        True,
    )
    armours = set({})
    armours.add(robes)
    armours.add(leather)
    armours.add(studded_leather)
    armours.add(chainmail)
    armours.add(cuirass)
    armours.add(buckler)
    armours.add(shield)
    return armours


class Spell:
    def __init__(self, name, desciption, mana_cost, damage, damage_type):
        self.name = name
        self.description = desciption
        self.mana_cost = mana_cost
        self.damage = damage
        self.damage_type = damage_type


#   Spells:
#
#   Armour - Mage, Monk
#   Arcane Dart - Mage
#   Acid Spray - Mage
#   Fire blast - Mage
#   Ice shard - Mage
#   Shock - Mage
#
#   Light Healing - Monk
#   Major Healing - Monk
#   Holy Bolt - Monk
#   Blessed Weapon - Monk
#
#   First Strike - Archer
#   Piercing Shot - Archer
#   Blunt Shot - Archer
#   Flaming Shot - Archer
#   Acid Shot - Archer
#
#   Cleaving Strike - Warrior
#   Power hit - Warrior
#   Counterstrike - Warrior
#   Whirlwind Attack - Warrior
#
#   Smoke bomb - Thief
#   Vital Strike - Thief
#   Dodging Attack - Thief
#   Disengage - Thief
#
#
#


class DamageType(Enum):
    SLASH = "slashing"
    PIERCE = "piercing"
    BLUNT = "bludeoning"
    ARCANE = "arcane"
    FIRE = "fire"
    WATER = "water"
    ACID = "acid"
    ELECTRIC = "electric"

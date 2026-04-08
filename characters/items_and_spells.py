from enum import Enum


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description


#   Items:
#   Recovery Potion
#   Healing Potion
#   Bandage
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


#   Weapons:
#   Dagger P
#   Short Sword P
#   Rapier P
#   Staff B
#   Mace B
#   Morningstar B
#   Longsword S
#   Hand Axe S
#   Battle Axe S
#   2 Handed Sword S
#   Short bow P
#   Long bow P
#   Crossbow P


class Armour(Item):
    def __init__(self, name, description, armour_value, off_hand=False):
        super().__init__(name, description)
        self.armour_value = armour_value
        self.off_hand = off_hand


#   Armours:
#   Robes 1
#   Leather 2
#   Studded Leather 3
#   Brigadine 4
#   Chain shirt 5
#   Chain mail 6
#   Breastplate 8
#   Platemail 10
#   Buckler 1
#   Kite Shield 3
#   Tower Shield 5


class ArmourLocation(Enum):
    OFF_HAND = "off_hand"
    BODY = "body"
    FOOTWEAR = "footwear"
    HEAD = "head"


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

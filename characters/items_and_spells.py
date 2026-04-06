from enum import Enum


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Weapon(Item):
    def __init__(self, name, description, damage, two_handed=False):
        super().__init__(name, description)
        self.damage = damage
        self.two_handed = two_handed


class Armour(Item):
    def __init__(self, name, description, armour_location, armour_value):
        super().__init__(name, description)
        self.armour_location = armour_location
        self.armour_value = armour_value


class Armour_location(Enum):
    OFF_HAND = "off_hand"
    BODY = "body"
    FOOTWEAR = "footwear"
    HEAD = "head"

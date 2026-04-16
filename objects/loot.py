import random

from objects.items_and_spells import armour_set


def generate_loot(items, weights, number_of_loots=1):
    return random.choices(items, weights, k=number_of_loots)


def armour_roll():
    armour = armour_set()
    weights = [10, 20, 20, 10, 5, 20, 15]
    return generate_loot(armour, weights)

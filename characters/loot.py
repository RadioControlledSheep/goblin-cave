import random


def generate_loot(items, weights, number_of_loots):
    return random.choices(items, weights, k=number_of_loots)

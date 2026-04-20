#   roll initiative with agility modifier
#   for each mob/player:
#       select attack from list
#       select target
#       roll to hit - agility/intelligemce possibly strength modifier vs agility
#       roll damage - strength/intelligence possibly agility modifier
#       adjust damage for attack type vs resistances/weaknesses
#       deduct damage from health
def combat(player, enemies):  # receive list of enemies and player
    initiatives = {player: roll_initiative(player)}
    for enemy in enemies:
        initiatives.update({enemy: roll_initiative(enemy)})
    sorted_initiatives = dict(
        sorted(initiatives.items(), key=lambda item: item[1], reverse=True)
    )
    for character in sorted_initiatives:
        character.attack()


def roll_initiative(character):
    return 1


def attack():  # should be in Character class
    pass

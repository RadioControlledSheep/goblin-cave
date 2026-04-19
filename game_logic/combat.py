#   roll initiative with agility modifier
#   for each mob/player:
#       select attack from list
#       select target
#       roll to hit - agility/intelligemce possibly strength modifier vs agility
#       roll damage - strength/intelligence possibly agility modifier
#       adjust damage for attack type vs resistances/weaknesses
#       deduct damage from health
def combat(player, enemies):  # receive list of enemies and player
    player_initiative = {player.name: roll_initiative(player)}
    pass


def roll_initiative(character):
    pass


def attack():  # should be in Character class
    pass

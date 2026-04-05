# Generate the world, holding room, monsters, player, current room.
from characters.generate_character import generate_character


def generate_world():
    # populate rooms
    # launch player generation
    # set room to starting location
    rooms = []
    player = generate_character()
    print("This is where main state is!")
    world = World(
        rooms, player, wandering_monsters=[], turn_counter=1, current_location=1
    )
    return world


class World:
    def __init__(
        self, rooms, player, wandering_monsters, turn_counter, current_location
    ):
        self.rooms = rooms
        self.player = player
        self.wandering_monsters = wandering_monsters
        self.turn_counter = turn_counter
        self.current_location = current_location

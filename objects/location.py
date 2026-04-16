class Location:
    def __init__(
        self,
        location_id,
        name,
        description,
        short_description,
        exits,
        items,
        mobs,
        interactables,
        bonus_options,
    ):
        self.location_id = location_id
        self.name = name
        self.desciption = description
        self.short_description = short_description
        self.exits = exits
        self.items = items
        self.mobs = mobs
        self.interactables = interactables
        self.bonus_options = bonus_options
        self.visited = False

    def build_description(self, player):
        pass

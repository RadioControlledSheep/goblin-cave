import random
import time

from game_logic.clearscreen import clearscreen
from objects.classes_professions import PlayerClass


class Character:
    def __init__(self, name, strength, agility, intelligence, stamina):
        self.name = name
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.stamina = stamina
        self.armour = 0
        self.max_health = stamina * 10
        self.current_health = self.max_health
        self.max_mana = intelligence * 10
        self.current_mana = self.max_mana
        self.equipped_weapon = None
        self.equipped_armour = None
        self.equipped_offhand = None
        self.spells = {}


class Player(Character):
    def __init__(
        self, name, strength, agility, intelligence, stamina, player_class, profession
    ):
        super().__init__(name, strength, agility, intelligence, stamina)
        self.player_class = player_class
        self.profession = profession
        self.inventory = {}
        self.xp = 0
        self.level = 1
        self.next_level_xp = 5

    def add_xp(self, xp):
        self.xp += xp
        if self.xp >= self.next_level_xp:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.next_level_xp += self.level * 5
        print(
            f"You have grown stronger, congratulations on reaching level {self.level}"
        )
        time.sleep(1)
        strength_gain = random.randint(1, 3)
        agility_gain = random.randint(1, 3)
        intelligence_gain = random.randint(1, 3)
        stamina_gain = random.randint(1, 3)
        if self.player_class == PlayerClass.WARRIOR:
            strength_gain += random.randint(1, 3)
            stamina_gain += random.randint(1, 3)
        elif self.player_class == PlayerClass.MAGE:
            intelligence_gain += random.randint(2, 6)
        elif self.player_class == PlayerClass.ARCHER:
            agility_gain += random.randint(2, 6)
        elif self.player_class == PlayerClass.THIEF:
            agility_gain += random.randint(1, 3)
            intelligence_gain += random.randint(1, 3)
        elif self.player_class == PlayerClass.MONK:
            intelligence_gain += random.randint(2, 6)
        self.strength += strength_gain
        self.agility += agility_gain
        self.intelligence += intelligence_gain
        self.stamina += stamina_gain
        self.max_health = self.stamina * 10
        self.current_health = self.max_health
        print(
            f"You have gained {strength_gain} strength, {agility_gain} agility, {intelligence_gain} intelligence, and {stamina_gain} stamina."
        )
        time.sleep(1)
        print(
            f"Your have been healed and your new maximum health is {self.max_health}."
        )
        time.sleep(1)
        print("Go forth and slay your enemies.")

    def show_player(self):
        clearscreen()
        print(f"Name: {self.name.capitalize()}\n")
        print(f"Class: {self.player_class.value.capitalize()}")
        print(f"Profession: {self.profession.value.capitalize()}\n")
        print(f"Stength:\t{self.strength}")
        print(f"Agility:\t{self.agility}")
        print(f"Intelligence:\t{self.intelligence}")
        print(f"Stamina:\t{self.stamina}\n")
        print(f"Health:\t{self.current_health}/{self.max_health}")
        print(f"Mana:\t{self.current_mana}/{self.max_mana}\n")
        print("\nEquipment:")
        print(f"Armour: {self.equipped_armour} Damage Reduction: {self.armour}")
        if self.equipped_weapon != None:
            print(
                f"Weapon: {self.equipped_weapon} Damage: {self.equipped_weapon.damage}"
            )
        else:
            print(f"Weapon: {self.equipped_weapon}")

        if self.equipped_offhand != None:
            print(f"Offhand: {self.equipped_offhand}")

        print("\nSpells and Abilities:")
        for spell in self.spells:
            print(spell)

        input("Enter to Continue")

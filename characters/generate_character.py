# import os
import shutil
import textwrap
import time

from characters.classes_professions import PlayerClass
from game_logic.clearscreen import clearscreen


def generate_character():
    name = get_name()
    player_class = choose_class(name)
    profession = choose_profession(name)
    player = generate_stats(name, player_class, profession)
    return player


def get_name():
    clearscreen()
    name = input("What is your name, adventurer?\n")
    time.sleep(0.5)
    response = input(f"so your name is {name}? (y/n)")
    if response.capitalize() == "Y":
        return name
    return get_name()


def choose_class(name):
    terminal_width = shutil.get_terminal_size().columns
    # os.get_terminal_size().columns
    clearscreen()
    class_text = []
    class_text.append(
        f"\n{name} now is the time to choose your class, this will be the fundamental focus of your characters identity and nature going forward.  This will define your initial starting attibutes, spells (if any),  and gear as well as how your character progresses.\n"
    )
    class_text.append(
        '\nFirst we have the Mage, these individuals looked at the rules of the universe and said "Hold my beer!".\n'
    )
    class_text.append(
        "Whether it is generating fire to burn their enemies with no regard to the area this may effect, or making objects from nothing, if you feel the laws of enthropy and conservation of mass are more of what you call guidelines then maybe this is the class for you.\n"
    )
    class_text.append(
        '\nSecondly we have the modest Warrior, if you are looking for a more refined solution to any given problem than "Hit it with a stick!" then either this may not be the class for you, or you have yet to find a big enough stick.\n'
    )
    class_text.append(
        '\nNext comes the Archer.  They saw their friend the warrior getting up close and personal with their foes and decided that a better choice would be to make sure they stood a good distance behind them and "supported" them from there with a trusty bow.\n'
    )
    class_text.append(
        "\nAnother option is the humble Monk, these men of the people will give up all their worldly possessions and go amongst the stinking masses to tend for the sick and look after the needy.  If you feel the urge to shave the top of your head so that your chosen almighty being can see your thoughts without that pesky half inch of hair blocking their otherwise omnipotent omiscience then this could be the one for you."
        + "  Of course I must check that I did mention the whole giving up the worldly possessions and stinking masses thing.\n"
    )
    class_text.append(
        "\nFinally there is the Rogue.  For purely alturistic reasons these individuals focus on the stealthy redistribution of assets.  Experts at being where they really shouldn't and even if they were well \"I didn't do it, nobody saw me do it, you can't prove anything!\" is a mantra they live by.  If a life in the shadows would brighten up your day then this may be the one for you.\n\n"
    )
    for texts in class_text:
        for lines in textwrap.wrap(
            texts, width=terminal_width, replace_whitespace=False
        ):  #
            print(lines)
    print("\n")
    print(
        "Please choose from 1 - Mage, 2 - Warrior, 3 - Archer, 4 - Monk, or 5 - Thief\n"
    )
    class_choice = input("Enter choice(1-5): ")
    chosen_class = "none"
    if class_choice == "1":
        chosen_class = PlayerClass.MAGE
    elif class_choice == "2":
        chosen_class = PlayerClass.WARRIOR
    elif class_choice == "3":
        chosen_class = PlayerClass.ARCHER
    elif class_choice == "4":
        chosen_class = PlayerClass.MONK
    elif class_choice == "5":
        chosen_class = PlayerClass.THIEF
    else:
        return choose_class(name)
    response = input(
        f"You have chosen to play as a {chosen_class.value}, is this correct?(y/n)"
    )
    if response.capitalize() == "Y":
        return chosen_class

    return choose_class(name)


def choose_profession(name):
    return "none"


def generate_stats(name, player_class, profession):
    return "none"

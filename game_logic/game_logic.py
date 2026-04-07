import shutil
import time

from game_logic.clearscreen import clearscreen


def show_start_screen():
    terminal_width = shutil.get_terminal_size().columns
    clearscreen()
    print("Goblin Cave\n".center(terminal_width))
    """time.sleep(2)
    print("Explore...")
    time.sleep(1)
    print("Fight...")
    time.sleep(1)
    print("Grow...")
    time.sleep(1)
    print("Repeat...\n")
    time.sleep(2)
    print("or die...")"""
    time.sleep(0.5)


def exit_game():
    print("\nExiting game, good bye...")
    time.sleep(2)
    clearscreen()

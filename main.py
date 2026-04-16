from game_logic.game_logic import exit_game, show_start_screen
from objects.world import generate_world


def main():
    playing = True
    while playing:
        show_start_screen()
        generate_world()
        playing = False

    exit_game()


if __name__ == "__main__":
    main()

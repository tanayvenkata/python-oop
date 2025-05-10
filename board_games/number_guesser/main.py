"""NUMBER GUESSING GAME"""

from src.game import NumberGuessingGame
from src.ui import GameUI


def main():
    """Plays the number guessing game"""

    # Create game and UI instances
    game = NumberGuessingGame()
    ui = GameUI()

    # Start the game
    ui.display_welcome()
    game.start_game()

    # Main game loop - only check if game is active
    while game.is_active:
        # Get player's guess
        player_guess = ui.receive_player_guess()

        # Process the guess and get updated game info
        # play_round handles game over checks
        game_info = game.play_round(player_guess)

        # # Display result of this round
        ui.display_guess_result(game_info)

    # If game is no longer active, show closing stats
    ui.display_closing(game_info)


if __name__ == "__main__":
    main()

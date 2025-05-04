from src.game import Hangman
from src.ui import GameUI

def play_game():
    game = Hangman()
    ui = GameUI()

    # Set Up the Game
    game.load_words()
    game.choose_secret_word()

    # Display welcome message
    ui.display_start()

    # main loop that runs unitl game over
    while game.active:

        # Share opening 
        info = game.get_info()
        ui.update_hangman(info)
        ui.display_partial_word(info)

        # Prompt user and validate guess 
        player_guess = ui.get_guess()
        # Log guess into game stats
        game.log_guess(player_guess)

        # Get game stats from game module
        result = game.get_info()
        # Have UI display necessary info
        ui.display_result(result)

        # Update win status
        game.check_win_status()
        # See if user maxed out guesses or won
        game.check_game_status()
    
    # When game is over, display stats
    result = game.get_info()
    ui.display_result(result)
    ui.closing_message(result)

def main():
    play_game()

if __name__ == "__main__":
    main()

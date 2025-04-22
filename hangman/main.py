from game import Hangman
from ui import GameUI
from display import Display


class MainGame:
    """Main class that coordinates all game components"""

    def __init__(self):
        self.ui = GameUI()
        self.display = Display()

    def setup_game(self):
        self.display.intro_message()
        difficulty = self.ui.get_difficulty()
        self.game = Hangman(difficulty)

    def play(self):
        self.setup_game()
        self.game.start_game()

        while self.game.active:
            game_stats = self.game.get_user_data()

            self.display.update_hangman(game_stats["wrong_guesses"])
            if self.game.check_game_over():
                break
            self.display.visual_guesses(
                game_stats["guesses_left"], game_stats["chars_guessed"]
            )
            self.display.partial_word(
                game_stats["secret_word"], game_stats["chars_guessed"]
            )

            user_guess = self.ui.get_guess()

            if not self.ui.valid_guess():
                self.game.invalid_guess()
                self.display.result(False)
            else:
                guess_right = self.game.check_guess(user_guess)
                self.display.result(guess_right)

        if self.game.did_win():
            print(f"SAVED! You correctly guessed the word: {game.self.secret_word}")
        else:
            print(f"Dead! The word was: {self.game.secret_word}")


if __name__ == "__main__":
    game = MainGame()
    game.play()

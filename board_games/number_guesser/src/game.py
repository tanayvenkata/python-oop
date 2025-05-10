from src.config import (
    DEFAULT_MIN,
    DEFAULT_MAX,
    DEFAULT_ATTEMPTS,
    TOO_HIGH,
    TOO_LOW,
    CORRECT,
)


class NumberGuessingGame:
    """A number guessing game where the player tries to guess a secret number."""

    def __init__(self):
        self.min_num = DEFAULT_MIN
        self.max_num = DEFAULT_MAX
        self.max_attempts = DEFAULT_ATTEMPTS
        self.guess_attempts = 0
        self._secret_number = None
        self.is_active = False
        self.info = {}

    def start_game(self):
        """Resets game information"""
        import random

        self._secret_number = random.randint(self.min_num, self.max_num)
        self.guess_attempts = 0
        self.is_active = True
        self.info = {}

    def end_game(self) -> None:
        """End the current game."""
        self.is_active = False

    def evalate_guess(self, player_guess):
        """Compares player's guess to the secret number"""
        self.guess_attempts += 1
        if player_guess < self._secret_number:
            return TOO_LOW
        elif player_guess > self._secret_number:
            return TOO_HIGH
        return CORRECT

    def game_information(self):
        """Updates the game info for other classes' use"""
        self.info = {
            "Attempts Used": self.guess_attempts,
            "Max Attempts": self.max_attempts,
            "Secret Number": self._secret_number,
            "Recent Guess Result": None,
        }
        return self.info

    def play_round(self, player_guess):
        """Compound function to eval guess and update game info"""
        result = self.evalate_guess(player_guess)

        if self.guess_attempts >= self.max_attempts or result == CORRECT:
            self.end_game()

        self.info = self.game_information()
        self.info["Recent Guess Result"] = result

        return self.info

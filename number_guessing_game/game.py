from config import DEFAULT_MIN, DEFAULT_MAX, DEFAULT_ATTEMPTS


class NumberGuessingGame:
    """
    A number guessing game where the player tries to guess a secret number.

    Attributes:
        min_num (int): lower bound of secret number range
        max_num (int): upper bound of secret number range
        max_attempts (int): Max guesses allowed
        guess_attempts (int): Number of guesses user has taken
        game_over (bool): Flag indicating if the game is over
        win (bool): Flag indicating if player won
    """

    def __init__(
        self, min_num=DEFAULT_MIN, max_num=DEFAULT_MAX, max_attempts=DEFAULT_ATTEMPTS
    ):
        """
        Initialize a new game with specified parameters.

        Args:
            min_num (int, optional): Lower bound of seceret number. Defaults to 1.
            max_num (int, optional): Upper bound of seceret number. Defaults to 100.
            max_attempts (int, optional): Max allowed guesses. Defaults to 15.
        """
        self.min_num = min_num
        self.max_num = max_num
        self.max_attempts = max_attempts
        self.guess_attempts = 0
        self.game_over = False
        self.win = False

    def start_game(self):
        """
        Start a new game.

        Creations:
            Creates a new random variable.
            Resets guess attempts, game over flag, and win flag to 0, *False
        """
        import random

        self.secret_number = random.randint(self.min_num, self.max_num)

        self.guess_attempts = 0
        self.game_over = False
        self.win = False

    def make_guess(self, guess: str) -> dict:
        self.guess_attempts += 1

        result = {
            "status": "",
            "remaining_attempts": self.max_attempts - self.guess_attempts,
        }

        if guess == "q":
            self.game_over = True
            result["status"] = "GAME_OVER"
        elif self.guess_attempts > self.max_attempts:
            self.game_over = True
            result["status"] = "OUT_OF_ATTEMPTS"
        else:
            try:
                guess = int(guess)
            except ValueError:
                result["status"] = "VALUE_ERROR"
            else:
                if guess < self.secret_number:
                    result["status"] = "LOW"
                elif guess > self.secret_number:
                    result["status"] = "HIGH"
                else:  # guess == self.secret_number
                    self.win = True
                    self.game_over = True
                    result["status"] = "WIN"
        return result

    def game_stats(self):
        stats = {
            "Attempts Used": self.guess_attempts,
            "Max Attempts": self.max_attempts,
            "Number Range": f"{self.min_num}-{self.max_num}",
            "Win": self.win,
            "Secret Number": self.secret_number,
        }

        return stats

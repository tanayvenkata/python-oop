from .config import (
    BORDER,
    DEFAULT_MIN,
    DEFAULT_MAX,
    DEFAULT_ATTEMPTS,
    CORRECT,
    BUFFER,
)


class GameUI:

    def __init__(self):
        self.border = BORDER
        self.min_num = DEFAULT_MIN
        self.max_num = DEFAULT_MAX
        self.max_attempts = DEFAULT_ATTEMPTS

    def display_welcome(self):
        """How to play"""
        print(BORDER)
        print("Welcome to the Number Guessing Game!")
        print(
            f"Try to guess the secret number between {self.min_num} and {self.max_num}."
        )
        print(f"You have {self.max_attempts} attempts. Good luck!")
        print(BORDER)

    def display_closing(self, game_info):
        """Wraps up the stats and displays"""
        if game_info["Recent Guess Result"] == CORRECT:
            game_info["Win Status"] = True
        else:
            game_info["Win Status"] = False

        max_key_length = max(len(key) for key in game_info.keys())

        print(BORDER)
        print("Game Stats:")
        for key, value in game_info.items():
            print(f"{key:{max_key_length}}{BUFFER}: {value}")
        print(BORDER)

    def receive_player_guess(self):
        """Gets and validates player's input"""
        while True:
            if (user_input := input("Enter a number: ")).isdigit():
                number = int(user_input)
                return number
            else:
                print("Invalid input. Please enter only digits.")

    def display_guess_result(self, info):
        """Intra-round update messaging"""
        result = info["Recent Guess Result"]
        print(result)
        print(f'You\'ve used {info["Attempts Used"]} of {info["Max Attempts"]} guesses')
        print(BORDER)

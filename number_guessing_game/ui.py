from config import BORDER


class GameUI:

    def __init__(self, oGame):
        self.min_num = oGame.min_num
        self.max_num = oGame.max_num

    def display_welcome(self):
        print(BORDER)
        print("Welcome to the Number Guessing Game!")
        print(f"Try to guess the secret number between {self.min_num} and {self.max_num}.")
        print("You have 15 attempts. Good luck!")
        print(BORDER)

    def get_guess(self):
        return input(f"Enter guess (or hit 'q' to quit): ")

    def display_result(self, result):
        match result["status"]:
            case "GAME_OVER":
                print("Game Over.")
            case "LOW":
                print(
                    f"Guess is too low...\nYou have {result['remaining_attempts']} guesses left."
                )
            case "HIGH":
                print(
                    f"Guess is too high...\nYou have {result['remaining_attempts']} guesses left."
                )
            case "WIN":
                print(f"You Won!")
            case "VALUE_ERROR":
                print("Need to input a number!")
        print(BORDER)

    def display_stats(self, stats):
        # Print header
            print("\nPLAYER STATS")  
            print("-"*26)
            print(f"Stat{' '*12}|{' '*3}Value")
            print("-"*26)
            
            # Print each stat
            for k, v in stats.items():
                # Format with proper spacing
                print(f"{k:<15} | {v:>7}")
            print("-"*26)


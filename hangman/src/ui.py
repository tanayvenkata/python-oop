"""Handles the user interface with the game (inputs)"""

from config import BORDER, MAX_GUESS_ALLOWED, HANGMANPICS

class GameUI:
    def __init__(self):
        pass

    def display_start(self):
        """How to play"""
        print(BORDER)
        print("Welcome to Hangman!")
        print(
            f"Try to guess the secret word. {MAX_GUESS_ALLOWED} wrong guesses allowed."
        )
        print(f"Good luck!")
        print(BORDER)

    def get_guess(self):
        """Prompt user for guess, validate, then return char"""

        # Loop through until we get a valid input
        while True:
            guess = input("Please input a letter: ").strip().lower()

            # Validate guess
            if len(guess) != 1:
                print("Only one letter at a time!")
            elif not guess.isalpha():
                print("Letters only (a-z) please.")
            else:
                # return guess for game class use
                return guess
    
    def update_hangman(self, info):
        index = min(info["Guess Attempts"], len(HANGMANPICS) - 1)
        print(f"{HANGMANPICS[index]}")

    def display_partial_word(self, info):
        """Display the status of guesses vs secret word."""
        display_word = list(info["Secret Word"])
        for i, letter in enumerate(display_word):
            if letter not in info["Letters Guessed"]:
                display_word[i] = "_"
        display_word = "".join(display_word)
        print(f"Your progress on the secret word: {display_word}")

    def display_result(self, info):
        print("\n")
        if info["Correct Guess"] == True:
            print("Correct")
        else:
            print("Incorrect")
        print(f"You have {info['Guesses Left']} guesses left.")
        print(f"Letters guessed: {sorted(info['Letters Guessed'])}")

    def closing_message(self, info):
        """Print ending message depending on info."""
        print(BORDER)
        if info["Game Won"] == True:
            print("\nCongrats, you win!")
        else:
            print("Sorry, you lost.")

        for k, v in info.items():
            print(f"{k}: {v}")
        print(BORDER)
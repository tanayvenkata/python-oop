"""Handles the game display. Prints"""

import config


class Display:
    def __init__(self):
        pass

    def intro_message(self):
        print("\nWelcome to hangman. Guess the correct letter before the man is hung.")

    def visual_guesses(self, guesses_left, letters_guessed):
        print(f"\nYou have {guesses_left} guesses left.")
        print(f"You've guessed the following characters: {letters_guessed}")

    def partial_word(self, secret_word, letters_guessed):
        secret_word_list = list(secret_word)
        for i, letter in enumerate(secret_word_list):
            if letter not in letters_guessed:
                secret_word_list[i] = "_"
        partial_word_display = "".join(secret_word_list)

        print(partial_word_display)

    def update_hangman(self, wrong_guesses):
        index = min(wrong_guesses, len(config.HANGMAN_GRAPHICS) - 1)
        print(f"\n{config.HANGMAN_GRAPHICS[index]}")

    def result(self, truthy):
        if truthy:
            print("\nCorrect")
        else:
            print("\nIncorrect")

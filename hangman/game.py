"""The Hangman Game. This file handles the game logic"""

import config
import os
import random


class Hangman:

    def __init__(self, level="medium"):
        current_file_dir = os.path.dirname(os.path.abspath(__file__))
        word_file = f"{level}.txt"
        self.word_list_path = os.path.join(current_file_dir, "word_lists", word_file)
        self.level = level
        self.guessed_letters = set()
        self.number_of_wrong_guesses = 0
        self.max_wrong_guesses = config.MAX_GUESS
        self.secret_word = None
        self.active = False
        self.game_won = False

    def start_game(self):
        self.active = True
        self.game_won = False
        self.secret_word = self.get_word()

    def get_word(self):
        try:
            with open(self.word_list_path, "r") as file:
                file_data = file.readlines()
                words = [word.strip() for word in file_data]
                self.secret_word = random.choice(words).casefold()
                return self.secret_word
        except FileNotFoundError:
            raise FileNotFoundError(f"Word list file not found: {self.word_list_path}")
        except ValueError as e:
            raise ValueError(f"Error processing word list: {e}")
        except Exception as e:
            raise Exception(f"Unexpected error while getting word: {e}")

    def check_guess(self, guess_c):
        """If c not in word or c already guessed: false"""
        if guess_c not in self.secret_word or guess_c in self.guessed_letters:
            self.number_of_wrong_guesses += 1
            self.guessed_letters.add(guess_c)
            return False
        else:
            self.guessed_letters.add(guess_c)
            return True

    def invalid_guess(self):
        self.number_of_wrong_guesses += 1

    def check_game_over(self):
        if self.number_of_wrong_guesses > self.max_wrong_guesses:
            return True
        elif self.did_win():
            return True
        return False

    def did_win(self):
        if self.number_of_wrong_guesses >= self.max_wrong_guesses:
            return False
        for c in self.secret_word:
            if c not in self.guessed_letters:
                return False
        return True

    def get_user_data(self):
        """returns a dictionary with easy access to info.
        we send this to main.py to use in display and UI"""
        user_info = {
            "chars_guessed": self.guessed_letters,
            "guesses_left": self.max_wrong_guesses - self.number_of_wrong_guesses,
            "wrong_guesses": self.number_of_wrong_guesses,
            "secret_word": self.secret_word,
        }

        return user_info

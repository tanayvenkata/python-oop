"""The Hangman Game. This file handles the game logic"""

from .config import WORD_FILE, DEFAULT_WORD, MAX_GUESS_ALLOWED


class Hangman:

    def __init__(self):
        self.word_file = WORD_FILE
        self.words = None
        self._secret_word = None
        self.guess_attempts = 0
        self.active = True
        self.win = False
        self.guessed_letters = set()
        self.recent_guess = None

    @property
    def secret_word(self):
        return self._secret_word

    @secret_word.setter
    def secret_word(self, value):
        self._secret_word = value

    def load_words(self):
        """Load the words from the file into a list."""
        try:
            with open(self.word_file, "r") as file:
                self.words = [line.strip() for line in file if line.strip()]
                return self.words
        except FileNotFoundError as e:
            return e

    def choose_secret_word(self):
        """Select a word from a class list."""
        import random

        if self.words:
            self._secret_word = random.choice(self.words)
        else:
            self._secret_word = DEFAULT_WORD

    def check_win_status(self):
        """Determine if letter in guess == letters in secret word."""
        self.win = self.guessed_letters.issuperset(set(self.secret_word))

    def check_game_status(self):
        """Check if game has ended if max guess limit or won game."""
        if self.win or self.guess_attempts >= MAX_GUESS_ALLOWED:
            self.active = False

    def log_guess(self, guess):
        """Update counter and log guess. log if most recent guess was correct."""
        self.guessed_letters.add(guess)

        # Update if the guess was right or not
        if guess in set(self.secret_word):
            self.recent_guess = True
        else:
            self.guess_attempts += 1
            self.recent_guess = False

    def get_info(self):
        """Return a dictionary of all info for other module's use"""
        game_info = {
            "Guess Attempts": self.guess_attempts,
            "Game Active": self.active,
            "Game Won": self.win,
            "Letters Guessed": self.guessed_letters,
            "Guesses Left": MAX_GUESS_ALLOWED - self.guess_attempts,
            "Secret Word": self.secret_word,
            "Correct Guess": self.recent_guess,
        }

        return game_info

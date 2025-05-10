"""Constants for the hangman game"""

import os

""" Word File """
WORD_FILE = WORD_FILE = os.path.join(os.path.dirname(__file__), "words.txt")
DEFAULT_WORD = "amazing"

""" Display Settings """
BORDER_CHAR = "="
BORDER_LENGTH = 10
BORDER = BORDER_CHAR * BORDER_LENGTH
BUFFER = "   "

"""Max Guess"""
MAX_GUESS_ALLOWED = 6

""" Result Values """
TOO_HIGH = "Too High..."
TOO_LOW = "Too Low..."
CORRECT = "Correct!"

"""ASCII"""
HANGMANPICS = [
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]

"""
Tic Tac Toe Game - Configuration Module
Contains game constants and settings.
"""

# Board Size X by X
BOARD_SIZE = 3
BOARD = [[0, 1, 2],
         [3, 4, 5],
         [6, 7, 8],
         ]

PLACEMENT_HELPER = {'0': (0, 0),
                    '1': (0, 1),
                    '2': (0, 2), 
                    '3': (1, 0),
                    '4': (1, 1),
                    '5': (1, 2),
                    '6': (2, 0),
                    '7': (2, 1),
                    '8': (2, 2),
                    }



WINNING_MOVES = [
    {0, 1, 2},  # top row
    {3, 4, 5},  # middle row
    {6, 7, 8},  # bottom row
    {0, 3, 6},  # left column
    {1, 4, 7},  # middle column
    {2, 5, 8},  # right column
    {0, 4, 8},  # diagonal from top-left to bottom-right
    {2, 4, 6}   # diagonal from top-right to bottom-left
]

MOVES = {0, 1, 2, 3, 4, 5, 6, 7, 8}

# Game settings
MAX_SCORE = 3
BASE_SCORE = 100
MAX_NUMBER_SLOTS = 9

# Display elements
BORDER = "=" * 40
MOVE_SYMBOLS = {
    "x": "x",
    "o": "o",
}

USER_SYMBOL = "x"
COMPUTER_SYMBOL = "o"

# Score file settings
SCORE_FILE = "high_scores.json"
MAX_HIGH_SCORES = 5
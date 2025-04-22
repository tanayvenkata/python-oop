"""Handles the user interface with the game (inputs)"""


class GameUI:
    def __init__(self):
        self.user_guess = None
        self.difficulty = None

    def get_difficulty(self):
        self.difficulty = input(
            "Please input number for difficulty.\n[1] Easy\n[2] Medium\n=> "
        )
        try:
            if int(self.difficulty) == 1:
                self.difficulty = "easy"
            else:
                self.difficulty = "medium"
        except:
            self.difficulty = "medium"
        return self.difficulty

    def get_guess(self):
        self.user_guess = input("Please guess a lowercase letter: ")
        return self.user_guess

    def valid_guess(self):
        if self.user_guess.isalpha() and len(self.user_guess) == 1:
            self.user_guess = self.user_guess.casefold()
            return True
        else:
            return False

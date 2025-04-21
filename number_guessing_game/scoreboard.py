from game import NumberGuessingGame
from config import BASE_SCORE

class Scoreboard:
    """
    Manages high scores for the number guessing game.

    Attributes:
        score_file (str): Path to text file
        max_scores (int): Max number of scores to keep track of
        scores (dict): DIctionary of username and score mappings
    """

    def __init__(self, oGame, score_file="scores.txt", max_scores=5):
        import os

        current_dir = os.getcwd()

        self.score_file = os.path.join(current_dir, score_file)
        self.max_scores = max_scores
        self.game = oGame
        self.scores = self.load_scores()

    def load_scores(self):
        import json

        try:
            with open(self.score_file, "r") as file:
                file_json = json.load(file)
                return file_json
        except FileNotFoundError:
            return {}

    def save_scores(self):
        import json

        with open(self.score_file, "w") as file:
            json.dump(self.scores, file, indent=4)

    def check_score(self):
        """Check if the current score is eligible for the scoreboard"""
        user_score = self.get_score()

        # if fewer scores than max scores allowed, then add it!
        if len(self.scores) < self.max_scores:
            return True

        if len(self.scores) > 0:
            lowest_score = min(self.scores.values())
            return user_score > lowest_score

        return True

    def update_scoreboard(self, username, score):
        """Update scoreboard with new score and username"""

        # add new score to dictionary
        self.scores[username] = score

        # Remove scores out of the top 5
        while len(self.scores) > self.max_scores:
            lowest_username = min(self.scores, key=self.scores.get)
            del self.scores[lowest_username]

        self.save_scores()

    def get_username(self):
        import random

        username = (
            input("Enter your player name: ") or f"Player{random.randint(1, 100)}"
        )
        return username

    def get_score(self):
        self.user_score = int(
            BASE_SCORE
            * (self.game.max_attempts - self.game.guess_attempts + 1)
            / self.game.max_attempts
        )
        return self.user_score

    def display_scores(self):
        print("\nHIGH SCORES")
        if not self.scores:
            print("No high scores yet!")
        else:
            # Sort scores from highest to lowest
            sorted_scores = sorted(
                self.scores.items(), key=lambda x: x[1], reverse=True
            )

            # Print header
            print("---------------------")
            print("Player       | Score")
            print("---------------------")

            # Print each score
            for username, score in sorted_scores:
                # Format with proper spacing (12 chars for name, 5 for score)
                print(f"{username:<12} | {score:>5}")
            print("---------------------")

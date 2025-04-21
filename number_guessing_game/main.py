"""NUMBER GUESSING GAME"""

from game import NumberGuessingGame
from ui import GameUI
from scoreboard import Scoreboard


if __name__ == "__main__":
    game = NumberGuessingGame()
    ui = GameUI(game)
    scoreboard = Scoreboard(game)

    ui.display_welcome()
    game.start_game()

    while not game.game_over:
        user_guess = ui.get_guess()
        result = game.make_guess(user_guess)
        ui.display_result(result)

    stats = game.game_stats()
    ui.display_stats(stats)

    if game.win and scoreboard.check_score():
        username = scoreboard.get_username()
        score = scoreboard.get_score()
        scoreboard.update_scoreboard(username, score)

    scoreboard.display_scores()  # Have the scoreboard display results

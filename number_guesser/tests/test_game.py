"""
Tests for the game module
"""

import pytest
from src.game import NumberGuessingGame


class TestNumberGame:
    """Test suite for the NumberGame class."""

    @pytest.fixture
    def game(self):
        """Create a fresh game instance for each test."""
        return NumberGuessingGame()

    def test_init(self, game):
        """Test game initialization."""
        assert game.min_num == 1
        assert game.max_num == 100
        assert game.max_attempts == 15
        assert game.guess_attempts == 0
        assert game._secret_number is None
        assert game.is_active is False
        assert game.info == {}

    def test_start_game(self, game):
        """Test starting a new game."""
        game.start_game()
        assert game._secret_number is not None
        assert game._secret_number >= game.min_num
        assert game._secret_number <= game.max_num
        assert game.is_active is True
        assert game.guess_attempts == 0
        assert game.info == {}

    def test_end_game(self, game):
        """Test starting a new game."""
        game.start_game()
        game.end_game()
        assert game.is_active is False

    @pytest.mark.parametrize(
        "guess, expected_result",
        [(75, "Too High..."), (25, "Too Low..."), (50, "Correct!")],
    )
    def test_evaluate_guess_parametrized(self, game, guess, expected_result):
        """Test check_guess with parameterized inputs."""
        game.start_game()
        game.guess_attempts = 3
        game._secret_number = 50

        assert game.evalate_guess(guess) == expected_result
        assert game.guess_attempts == 4

    def test_game_information(self, game):
        """Test if game information dictionary is accurately returned."""
        game.start_game()
        info = game.game_information()

        assert set(info.keys()) == {
            "Attempts Used",
            "Max Attempts",
            "Secret Number",
            "Recent Guess Result",
        }

        assert info["Attempts Used"] == game.guess_attempts
        assert info["Max Attempts"] == game.max_attempts
        assert info["Secret Number"] == game._secret_number
        assert info["Recent Guess Result"] is None

    @pytest.mark.parametrize(
        "player_guess, expected_result",
        [(75, "Too High..."), (25, "Too Low..."), (50, "Correct!")],
    )
    def test_play_round(self, game, player_guess, expected_result):
        """Test if compound function modifies and returns self.info."""
        game.start_game()
        game._secret_number = 50

        result = game.play_round(player_guess)
        assert result["Recent Guess Result"] == expected_result

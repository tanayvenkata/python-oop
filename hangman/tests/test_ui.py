"""
Tests for the ui module
"""

import pytest
from src.ui import GameUI
from unittest.mock import patch
from src.config import DEFAULT_WORD, BORDER


class TestGameUI:
    """Test suite for the GameUI class."""

    @pytest.fixture
    def ui(self):
        """Create a fresh UI instance for each test."""
        return GameUI()

    def test_display_start(self, ui):
        """Starting message"""
        with patch("builtins.print") as mock_print:
            ui.display_start()

        assert mock_print.call_count == 5
        calls = [call[0][0] for call in mock_print.call_args_list]
        assert calls[0] == BORDER
        
    def test_get_guess(self, ui):
        """test incorrect user guess 2x and then good guess"""
        with patch("builtins.input", side_effect=["abc", "&", " Z  "]):
            with patch("builtins.print") as mock_print:
                result = ui.get_guess()
                
                # expecting final result to be z
                assert result == 'z'

                # two messages printed and stated below
                assert mock_print.call_count == 2
                calls = [call[0][0] for call in mock_print.call_args_list]
                assert calls[0] == "Only one letter at a time!"
                assert calls[1] == "Letters only (a-z) please."

    def test_display_result(info):
        """Test messaging at end of round or win/lose case."""
        




'''

class TestGameUI:
    """Test suite for the GameUI class."""

    @pytest.fixture
    def ui(self):
        """Create a fresh ui instance for each test."""
        return GameUI()

    def test_init(self, ui):
        """Test ui initialization."""
        assert ui.border == "=" * 10
        assert ui.min_num == 1
        assert ui.max_num == 100
        assert ui.max_attempts == 15

    def test_display_welcome(self, ui):
        """Test the display welcome message."""
        with patch("builtins.print") as mock_print:
            ui.display_welcome()

        # Check that print was called the correct number of times
        assert mock_print.call_count == 5

        # Check that each print call had the correct arguments
        calls = [call[0][0] for call in mock_print.call_args_list]
        assert calls[0] == "=" * 10  # BORDER
        assert calls[1] == "Welcome to the Number Guessing Game!"
        assert (
            calls[2]
            == f"Try to guess the secret number between {ui.min_num} and {ui.max_num}."
        )
        assert calls[3] == f"You have {ui.max_attempts} attempts. Good luck!"
        assert calls[4] == "=" * 10  # BORDER

    def test_display_closing(self, ui):
        """Test the closing message."""
        # Create a mock game_info dictionary
        mock_game_info = {
            "Attempts Used": 5,
            "Max Attempts": 15,
            "Secret Number": 42,
            "Recent Guess Result": "Correct!",
        }

        with patch("builtins.print") as mock_print:
            ui.display_closing(mock_game_info)

            # Check that print was called the correct number of times
            # The function should print:
            # 1. BORDER
            # 2. "Game Stats:"
            # 3-7. Each key-value pair (5 items after adding "Win Status")
            # 8. BORDER
            assert mock_print.call_count == 8

            calls = [call[0][0] for call in mock_print.call_args_list]

            # Check the border and header
            assert calls[0] == "=" * 10  # BORDER
            assert calls[1] == "Game Stats:"

            # Check that Win Status was set to True (since Recent Guess Result is "Correct")
            # Find the Win Status line in the calls
            win_status_found = False
            for call in calls[2:-1]:  # Skip first two and last call
                if "Win Status" in call:
                    win_status_found = True
                    assert "True" in call
            assert win_status_found, "Win Status not found in printed output"

            # Check the closing border
            assert calls[-1] == "=" * 10  # BORDER

    def test_receive_player_guess_valid_input(self, ui):
        """Test validate and return valid player guess"""
        with patch("builtins.input", return_value="50"):
            result = ui.receive_player_guess()

            assert result == 50

    def test_receive_player_guess_invalid_input(self, ui):
        """Test validate and return invalid -> valid player guess"""
        with patch("builtins.input", side_effect=["abc", "50"]):
            with patch("builtins.print") as mock_print:
                result = ui.receive_player_guess()

                assert result == 50

                assert mock_print.call_count == 1
                calls = [call[0][0] for call in mock_print.call_args_list]
                assert calls[0] == "Invalid input. Please enter only digits."

    def test_display_guess_result(self, ui):
        """Test appropriate message displayed"""
        mock_game_info = {
            "Attempts Used": 5,
            "Max Attempts": 15,
            "Secret Number": 42,
            "Recent Guess Result": "Correct",
        }

        with patch("builtins.print") as mock_print:
            ui.display_guess_result(mock_game_info)
            assert mock_print.call_count == 3

            calls = [call[0][0] for call in mock_print.call_args_list]
            assert calls[0] == "Correct"
            assert calls[1] == "You've used 5 of 15 guesses"
            assert calls[2] == "=" * 10  # BORDER



'''
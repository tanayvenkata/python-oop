"""
Tests for the game module
"""

import pytest
from src import Board


class TestBoard:
    """Test suite for the Board class."""

    @pytest.fixture
    def board(self):
        """Create a fresh board instance for each test."""
        return Board()

    def test_make_move(self, board):
        pass

    def test_is_full_true(self, board):
        """Board is full only when none are empty."""
        board.grid = [["x" for _ in range(3)] for _ in range(3)]
        assert board.is_full() == True

    def test_is_full_false(self, board):
        """Board is not full if more than 1 spot open."""
        board.grid = [[" " for _ in range(3)] for _ in range(3)]
        board.grid[2][2] = "x"
        assert board.is_full() == False

    def test_check_winner_row_win(self, board):
        board.grid = [["X", "X", "X"], [" ", "O", " "], ["O", " ", "O"]]
        assert board.check_winner() == True

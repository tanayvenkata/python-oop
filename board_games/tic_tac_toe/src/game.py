from .board import Board
from .ui import UI


class TicTacToe:
    """
    Handles all game operations for tic tac toe game.
    """

    def __init__(self, size):
        self.size = size
        self.board = Board(self.size)
        self.ui = UI()
        self.current_player = "X"

    def switch_player(self):
        """Switches player symbol/turn."""
        self.current_player = "O" if self.current_player == "X" else "X"

    def play(self):
        self.ui.display_welcome()

        while True:
            self.board.display()
            row, col = self.ui.get_move(self.current_player, self.size)
            move_successful = self.board.make_move(row, col, self.current_player)

            if not move_successful:
                print("Spot already taken. Try again.")
                continue

            self.ui.announce_move(self.current_player, row, col)

            if self.board.check_winner():
                self.board.display()
                self.ui.announce_winner(self.current_player)
                break
            if self.board.is_full():
                self.board.display()
                self.ui.announce_tie()
                break

            self.switch_player()

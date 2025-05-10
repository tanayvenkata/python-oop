from .config import BOARD_DIVIDER, EMPTY


class Board:
    def __init__(self, size=3):
        self.size = size
        self.grid = [[" " for _ in range(self.size)] for _ in range(self.size)]

    def display(self):
        """Display the board to terminal."""
        for row in self.grid:
            print("|".join(row))
            print(BOARD_DIVIDER * self.size)

    def make_move(self, row, col, symbol):
        """Adds symbol given the row/col to grid."""
        if self.grid[row][col] == EMPTY:
            self.grid[row][col] = symbol
            return True
        return False

    def is_full(self):
        """Returns true if full else false."""
        return all(slot != EMPTY for row in self.grid for slot in row)

    def all_same_and_not_empty(self, cells):
        """Helper function to check if all same/not empty."""
        return all(cell == cells[0] and cell != EMPTY for cell in cells)

    def check_winner(self):
        row_cells = [row for row in self.grid]
        col_cells = [
            [self.grid[i][j] for i in range(self.size)] for j in range(self.size)
        ]
        left_diagonal_cells = [self.grid[i][i] for i in range(self.size)]
        right_diagonal_cells = [
            self.grid[i][self.size - 1 - i] for i in range(self.size)
        ]
        diagonals = [left_diagonal_cells, right_diagonal_cells]

        lines = row_cells + col_cells + diagonals

        return any(map(self.all_same_and_not_empty, lines))

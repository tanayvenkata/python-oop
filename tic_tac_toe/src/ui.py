class UI:
    """
    Handles all user interface operations with the tic tac toe game.
    """

    def display_welcome(self):
        print("Welcome to TicTacToe")

    def get_move(self, player_symbol, board_size):
        while True:
            try:
                print("Enter the row followed by column of your move.")
                row = int(input(f"Player {player_symbol}, enter your row: "))
                col = int(input(f"Player {player_symbol}, enter your col: "))
                if 0 <= row < board_size and 0 <= col < board_size:
                    return row, col
                else:
                    print(
                        f"Invalid move. Value must be between 0 and {board_size - 1} inclusive."
                    )
            except ValueError:
                print("Invalid input. Please enter integers only.")

    def announce_move(self, player_symbol, row, col):
        print(f"Player {player_symbol} selected ({row},{col}).")

    def announce_winner(self, player_symbol):
        print(f"Player {player_symbol} wins!")

    def announce_tie(self):
        print(f"It's a tie!")

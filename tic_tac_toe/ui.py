import config

class UI():
    """
    Handles all user interface operations with the tic tac toe game. 
    """

    def display_welcome(self):
        print(config.BORDER)
        print("Welcome to TicTacToe")
        print(config.BORDER)
        print(f"First to score {config.MAX_SCORE} points wins the match!")
        print("\nBoard Setup::")
        for row in config.BOARD:
            print(f"- {row} Hit '{row[0]}', '{row[1]}', or '{row[2]}' to place symbol")
        print("- 'quit' or 'q' to exit the game")
        print(config.BORDER)

    def display_board(self, board):
        print("The current board. Place your symbol on any open cell.")
        for row in board:
            print(row)
        print(config.BORDER)

    def get_player_placement(self, numbers_taken):
        # We need to validate, then if its good we send number out. 
        while True:
            user_input = input("\nYour move: ").strip()

            # Check for quit command
            if user_input in ["quit", "q"]:
                return "quit"
            
            # Return the input to be later used by placement helper
            # Ensure input valid num and nothing is there already
            if user_input in config.PLACEMENT_HELPER and int(user_input) not in numbers_taken:
                return int(user_input)

            # Invalid input
            print(f"Invalid move.")

    def who_won(self):
        print("Player Won")

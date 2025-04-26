"""
TicTacToe/
|
|—main.py 		# game entry 
|-game.py       # game logic and main class
|-ui.py         # handles user input
|-display.py    # visual display of game state
|
|
"""

from game import TicTacToe
from ui import UI

def main():
    # Initialize class objects here
    game = TicTacToe()
    ui = UI()

    ui.display_welcome()

    # Playing the Game. inner loop will be playing an instance of the game. 
    playing = True
    while playing:              
        game.reset_round()

        while not game.round_finished():

            # get most recent nums taken list 
            numbers_taken = game.get_numbers_taken()
            # get int version of number if its valid 
            player_move = ui.get_player_placement(numbers_taken)

            if player_move == 'quit':
                playing = False
                break

            # add the int num to the player's move and nums taken 
            game.add_player_number(player_move)
            game.add_numbers_taken(player_move)

            # convert the player move into coordinate positions (so we can modify board)
            coordinates = game.get_result(player_move)

            # update the board with the coordinates 
            player_board = game.update_board(coordinates)

            # display new board
            ui.display_board(player_board)

            if game.round_finished():
                break

            print(f"numbers taken: {game._numbers_taken}")

            # say computer is playing now + add delay 
            print("Computer Play Now")
            # get computer number 
            computer_num = game.generate_computer_number()

            # add the int num to the player's move and nums taken 
            game.add_computer_number(computer_num)
            game.add_numbers_taken(computer_num)

            # convert computer number to position
            position = game.get_result(computer_num)
            # update board with computer position
            game.update_board(position, "computer")
            # display new board again 
            ui.display_board(player_board)

        playing=False
        ui.display_board(player_board)
        if game.player_win:
            print("You Win!")
        elif game.player_win is None:
            print("Draw")
        else:
            print("You Lost")

if __name__ == "__main__":
    main()
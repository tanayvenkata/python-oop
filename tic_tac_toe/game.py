import config

class TicTacToe():
    """
    Handles all game operations for tic tac toe game. 
    """

    def __init__(self):
        self._numbers_taken = set()
        self.player_moves = set()
        self.computer_moves = set()
        self.board = config.BOARD
        self.player_win = False

    def reset_round(self):
        self._numbers_taken = set()
        self.player_moves = set()
        self.computer_moves = set()
        self.board = config.BOARD
        self.player_win = False

    def add_numbers_taken(self, number):
        self._numbers_taken.add(number)
    
    def get_numbers_taken(self):
        return self._numbers_taken
    
    def add_player_number(self, number):
        self.player_moves.add(number)
    
    def get_player_moves(self):
        return self.player_moves
    
    def add_computer_number(self, number):
        self.computer_moves.add(number)
    
    def get_computer_moves(self):
        return self.computer_moves
    
    def generate_computer_number(self):
        from random import choice
        computer_number = choice(config.MOVES - self.get_numbers_taken())
        return computer_number

    def get_result(self, player_move):
        '''We're given the player's move. we must return the position to mark'''
        position = config.PLACEMENT_HELPER[str(player_move)]
        return position
    
    def update_board(self, position, player='player'):
        if player == 'computer':
            player = config.COMPUTER_SYMBOL
        else:
            player = config.USER_SYMBOL
        x, y = position[0], position[1]
        self.board[x][y] = config.MOVE_SYMBOLS[player]
        return self.board

    def generate_computer_number(self):
        from random import choice
        available_moves = list(config.MOVES - self.get_numbers_taken())
        computer_number = choice(available_moves)
        return computer_number
    
    def round_finished(self):
        # check if anyone won
        for win in config.WINNING_MOVES:
            if self.get_computer_moves().issuperset(win):
                self.player_win = False
                return True
            elif self.get_player_moves().issuperset(win):
                self.player_win = True
                return True
        # if board fills nobody wins and game ends 
        if len(self.get_numbers_taken()) == config.MAX_NUMBER_SLOTS:
            self.player_win = None
            return True
        # Otherwise game isnt over
        return False
    

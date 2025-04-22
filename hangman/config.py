"""Game Constants"""

MAX_GUESS = 6
HANGMAN_GRAPHICS = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]


"""
Hangman/
|
|—main.py 		# game entry 
|-game.py       # game logic and main class
|-ui.py         # handles user input
|-display.py    # visual display of game state
|-scoreboard.py # create a scoreboard to save score data
|
|-word_lists/
|       |-easy.txt   # easy words
|       |-hard.txt   # hard words
"""

"""
game = Hangman()
ui = GameUI(game)
display = Display(game)

display.display_start()
game.game_start()

while not game.game_over():
    # ask user for guess
    # check if guess is right or wrong
    # if r --> update the display of letters
    # if w --> add body part to hangman
    # both cases: add to chars guessed and print the body 

    # if user wins -> congrats them
    # if user doesnt win -> end of game
    # both cases: print stats / reveal word / update scoreboard
"""

"""
game.py
1. open file path. get word. return word.  
2. create empty list based on word. return list. 
3. check guess in word. return bool. 
display.py
1. take word (cat). print _ _ _. 
2. print letters guessed in alphabetical order. guesses: aehij.
3. print guesses left. max wrong guesses - wrong guesses. 
4. print the hangman ascii. 
5. print message like wrong or right. 
ui.py
1. get guesses from user. 
2. validate users input. not c guessed already, is instance c. 
3. return c 
4. get user choice of easy / medium (e/m) and if invalid default to easy. input[0]
main.py
1. 
"""

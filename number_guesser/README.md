# Number Guessing Game

A simple number guessing game implemented in Python using object-oriented programming principles.

## Project Structure

```
num_guess_game/
├── src/
│   ├── __init__.py
│   ├── game.py        # Main game class
│   ├── ui.py          # Player class
│   └── config.py      # Magic numbers and strings
├── tests/
│   ├── __init__.py
│   ├── test_game.py   # Tests for game class
│   └── test_ui.py     # Tests for UI class
├── conftest.py        # Pytest configuration
├── main.py            # Entry point to run the game
├── README.md          # Project documentation
└── requirements.txt   # Project dependencies
```

## How to Run

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the game: `python main.py`

## How to Test

Run tests using pytest:

```
pytest
```

For coverage report:

```
pytest --cov=src tests/
```

## Game Features

- Interactive number guessing game
- Configurable range and difficulty
- Player statistics tracking
- Object-oriented design with proper separation of concerns
- Comprehensive test suite

## Implementation Details

The game is implemented using three main classes:

1. **NumberGame**: Handles the game logic, including generating a random number, processing guesses, and tracking game state.
2. **UI**: Manages player data, including name, win/loss statistics, and guess history.
3. **Config**: Helper variables. 

The code follows best practices:
- Type hints for better IDE support and documentation
- Comprehensive docstrings
- Clean separation of concerns
- Well-structured tests

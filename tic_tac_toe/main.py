from src.game import TicTacToe


def main():
    size = int(input("Enter board size: "))
    game = TicTacToe(size)
    game.play()


if __name__ == "__main__":
    main()

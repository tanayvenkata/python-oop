import random
from .config import SUITS, RANKS
from .card import Card


class Deck:
    def __init__(self):
        """Hosts a list of card objects."""
        self.cards = [
            Card(rank=rank, suit=suit) for suit in SUITS for rank in RANKS
        ]

    def shuffle(self):
        """Randomizes deck."""
        random.shuffle(self.cards)

    def deal_card(self):
        """Returns last card in deck."""
        if self.cards:
            return self.cards.pop()
        else:
            raise ValueError("No more cards in the deck!")

    def __str__(self):
        return f"Deck of {len(self.cards)} cards."

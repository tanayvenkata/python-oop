from .hand import Hand
from . import config as cf 


class Player:
    def __init__(self, name, bankroll=cf.START):
        self.name = name
        self.bankroll = bankroll
        self.hand = Hand([])
        self.current_bet = 0

        self.said_stand = False

    def __str__(self):
        return f"{self.name}: ${self.bankroll} | Bet: {self.current_bet} | Hand: {self.hand.cards}"

    def reset_hand(self):
        self.hand = Hand([])
        self.current_bet = 0
        self.said_stand = False

    def place_bet(self, bet):
        if bet > self.bankroll:
            raise ValueError("Insufficient funds to place that bet.")
        self.bankroll -= bet
        self.current_bet = bet

    def hit(self, card):
        self.hand.add_card(card)

    def stand(self):
        self.said_stand = True

    def win_bet(self, multiplier=1):
        self.bankroll += int(self.current_bet * (1 + multiplier))

    def push_bet(self):
        self.bankroll += self.current_bet

    def lose_bet(self):
        pass  # Bet already deducted in place_bet

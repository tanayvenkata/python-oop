from .player import Player
from .dealer import Dealer
from .deck import Deck
from .ui import UI
from . import config as cf

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.player = Player(cf.PLAYER)
        self.dealer = Dealer()
        self.ui = UI()
        self.active = True
        self.round = 1

    def draw_card(self):
        return self.deck.deal_card()

    def play_round(self):
        self.player.reset_hand()
        self.dealer.reset_hand()

        if len(self.deck.cards) < 15:
            self.deck = Deck()
            self.deck.shuffle()
            self.ui.show_result("Shuffling new deck...")

        while True:
            bet = self.ui.ask_for_bet(self.player.bankroll)
            try:
                self.player.place_bet(bet)
                break
            except ValueError:
                print("Bet exceeds bankroll. Try again.")

        for _ in range(2):
            self.player.hit(self.draw_card())
            self.dealer.hit(self.draw_card())

        self.ui.show_hand(self.player.hand, owner="Player")
        self.ui.show_hand(self.dealer.hand, owner="Dealer", reveal_all=False)

        if self.player.hand.is_blackjack():
            self.ui.show_hand(self.dealer.hand, owner="Dealer", reveal_all=True)
            self.ui.show_result("BLACKJACK! You win 1.5x your bet!")
            self.player.win_bet(multiplier=1.5)
            return

        while True:
            action = self.ui.get_player_action()
            if action == "hit":
                self.player.hit(self.draw_card())
                self.ui.show_hand(self.player.hand)
                if self.player.hand.is_bust():
                    break
            else:
                self.player.stand()
                break

        if self.player.hand.is_bust():
            self.ui.show_result("You busted! Dealer wins.")
            self.player.lose_bet()
            return

        self.ui.show_hand(self.dealer.hand, owner="Dealer", reveal_all=True)
        while self.dealer.should_hit():
            self.dealer.hit(self.draw_card())
            self.ui.show_hand(self.dealer.hand, owner="Dealer", reveal_all=True)

        if self.dealer.hand.is_bust():
            self.ui.show_result("Dealer busts! You win.")
            self.player.win_bet()
            return

        player_total = self.player.hand.get_best_total()
        dealer_total = self.dealer.hand.get_best_total()

        if player_total > dealer_total:
            self.player.win_bet()
            self.ui.show_result("You win!")
        elif player_total < dealer_total:
            self.player.lose_bet()
            self.ui.show_result("Dealer wins.")
        else:
            self.player.push_bet()
            self.ui.show_result("Push! It's a tie.")

        self.ui.show_round_end_summary(self.player, self.dealer, self.round)

    def run(self):
        self.ui.show_intro(self.player.bankroll)
        while self.active:
            self.play_round()
            self.round += 1
            if not self.ui.ask_play_again():
                self.active = False
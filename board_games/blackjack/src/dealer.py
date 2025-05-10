from .hand import Hand


class Dealer:
    def __init__(self):
        self.hand = Hand([])

    def __str__(self, reveal=False):
        if reveal:
            return f"Dealer | Full Hand: {[str(card) for card in self.hand.cards]}"
        return f"Dealer | Showing: {self.hand.cards[0]}"

    def hit(self, card):
        self.hand.add_card(card)

    def reset_hand(self):
        self.hand = Hand([])

    def should_hit(self):
        total = self.hand.get_best_total()
        return total is not None and total < 17

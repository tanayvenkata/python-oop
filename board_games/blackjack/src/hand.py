class Hand:

    def __init__(self, cards):
        self.cards = cards

    def add_card(self, card):
        self.cards.append(card)

    def get_best_total(self):
        possible_totals = []

        if (total := sum(self._get_card_value(card) for card in self.cards)) < 22:
            possible_totals.append(total)

        num_aces = sum(1 for card in self.cards if card.rank == "A")

        for i in range(1, num_aces + 1):
            adjusted_total = total - 10 * (i + 1)
            if total < 22:
                possible_totals.append(adjusted_total)

        if possible_totals:
            return sorted(possible_totals)[-1]
        else:
            return None

    def is_blackjack(self):
        if len(self.cards) == 2 and self.get_best_total() == 21:
            return True

    def is_bust(self):
        return self.get_best_total() is None

    def _get_card_value(self, card):
        if card.rank in ("J", "Q", "K"):
            return 10
        elif card.rank == "A":
            return 11
        else:
            return int(card.rank)

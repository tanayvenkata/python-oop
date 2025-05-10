class UI:
    def show_intro(self, bankroll):
        print("=" * 40)
        print("🎴 Welcome to Blackjack! 🎴")
        print("=" * 40)
        print("Rules:")
        print("- Beat the dealer without going over 21.")
        print("- Blackjack pays 1.5x your bet.")
        print("- Dealer hits until 17.")
        print(f"\nYou start with ${bankroll}. Good luck!\n")

    def ask_for_bet(self, bankroll):
        print("\n" + "=" * 40)
        print(f"Current Bankroll: ${bankroll}")
        while True:
            try:
                bet = int(input("Enter your bet: "))
                return bet
            except ValueError:
                print("Invalid input. Please enter a whole number.")

    def show_hand(self, hand, owner="Player", reveal_all=True):
        print(f"\n--- {owner}'s Hand ---")
        if not reveal_all and owner == "Dealer":
            print(f"[{hand.cards[0]}, Hidden]")
        else:
            cards_str = ", ".join(str(card) for card in hand.cards)
            total = hand.get_best_total()
            print(f"[{cards_str}] → Total: {total}")

    def get_player_action(self):
        print("\n--- Your Move ---")
        while True:
            action = input("Choose action (hit/stand): ").strip().lower()
            if action in ("hit", "stand"):
                return action
            print("Invalid input. Type 'hit' or 'stand'.")

    def show_result(self, result_str):
        print("\n>>> " + result_str)

    def ask_play_again(self):
        return input("\nPlay another round? (y/n): ").strip().lower() == "y"

    def show_round_end_summary(self, player, dealer, round_num):
        print("\n" + "-" * 40)
        print(f"📦 End of Round {round_num}")
        self.show_hand(player.hand, owner="Player")
        self.show_hand(dealer.hand, owner="Dealer", reveal_all=True)
        print(f"💰 Bankroll: ${player.bankroll}")
        print("-" * 40)
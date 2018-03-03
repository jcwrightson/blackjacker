from hand import Hand


class Player:
    def __init__(self, name, dealer):

        self.dealer = dealer
        self.name = name

        if dealer:
            self.hand = Hand()
            self.score = 0
        else:
            self.hands = [Hand()]
            self.scores = []
        # self.hand = Hand()

        self.has_blackjack = False
        self.is_bust = False
        self.winner = False
        self.draw = False

    def split(self):
        if not self.dealer:
            self.hands.append(Hand())

            card_to_split = self.hands[0].cards[1]
            del self.hands[0].cards[1]

            self.hands[1].cards.append(card_to_split)




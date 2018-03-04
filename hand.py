class Hand:
    def __init__(self):
        self.cards = []
        self.score = 0
        self.has_blackjack = False
        self.is_bust = False
        self.winner = False
        self.draw = False

    def extend_hand(self, new_card):
        return self.cards.extend(new_card)

    def calculate_score(self):

        self.score = 0

        for x in range(len(self.cards)):
            if isinstance(self.cards[x], int):
                self.score = self.score + self.cards[x]
            else:
                if self.cards[x] != 'A':
                    self.score = self.score + 10
                else:
                    if self.score + 11 > 21:
                        self.score = self.score + 1
                    else:
                        self.score = self.score + 11

        if self.score == 21 and len(self.cards) == 2:
            # if isinstance(self.cards[0], str) and isinstance(self.cards[1], str):
            if self.cards[0] == 'A' or self.cards[1] == 'A':
                    self.has_blackjack = True
                    return "BlackJack"
        else:
            if self.score > 21:
                self.is_bust = True
                return "Bust"
        return self.score



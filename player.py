class Player:
    def __init__(self, name, dealer):

        self.dealer = dealer
        self.name = name
        self.hand = []
        self.score = 0
        self.has_blackjack = False
        self.is_bust = False
        self.winner = False
        self.draw = False


    def replace_hand(self, new_hand):
        self.hand = new_hand
        return self.hand

    def extend_hand(self, new_card):
        return self.hand.extend(new_card)

    def set_score(self, score):
        self.score = score
        return self.score

    def calculate_score(self):

        self.score = 0

        for x in range(len(self.hand)):
            if isinstance(self.hand[x], int):
                self.score = self.score + self.hand[x]
            else:
                if self.hand[x] != 'A':
                    self.score = self.score + 10
                else:
                    if self.score + 11 > 21:
                        self.score = self.score + 1
                    else:
                        self.score = self.score + 11

        if self.score == 21 and len(self.hand) == 2:
            if isinstance(self.hand[0], str) and isinstance(self.hand[1], str):
                self.has_blackjack = True
                return "BlackJack"
        else:
            if self.score > 21:
                self.is_bust = True
                return "Bust"
        return self.score



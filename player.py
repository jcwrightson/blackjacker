from hand import Hand
from purse import Purse


class Player:
    def __init__(self, name, dealer, init_purse, bet_per_hand):

        self.dealer = dealer
        self.name = name
        self.purse = Purse(init_purse)

        if dealer:
            self.hand = Hand()
        else:
            self.hands = [Hand()]
            self.bet_per_hand = bet_per_hand

    def reset(self):
        if self.dealer:
            self.hand = Hand()
        else:
            self.hands = [Hand()]

    def split(self):
        if not self.dealer:
            self.hands.append(Hand())

            card_to_split = self.hands[0].cards[1]
            del self.hands[0].cards[1]

            self.hands[1].cards.append(card_to_split)
            self.bet(1)

    def bet(self, amount):
        self.purse.spend(amount * self.bet_per_hand)
        return self.purse.value

    def win(self, amount):
        self.purse.collect(amount * self.bet_per_hand)
        return self.purse.value


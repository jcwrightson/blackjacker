import random


class Cards:
    def __init__(self):

        self.deck = []

    def generate_deck(self):

        deck = []
        for x in range(4):
            for y in range(12):

                if y == 1:
                    deck.append("A")
                else:
                    if y == 11:
                        deck.append("J")
                        deck.append("Q")
                        deck.append("K")
                    else:
                        if y != 0:
                            deck.append(y)
        return deck

    def generate_game(self, no_of_decks):
        for x in range(no_of_decks):
            self.deck.extend(self.generate_deck())

        self.shuffle(self.deck)
        return self.deck

    def shuffle(self, cards):

        random.shuffle(cards)

    def get_card_value(self, card):
        if isinstance(card, int):
            return card
        else:
            if card == 'A':
                return 11
            else:
                return 10

from player import Player
from cards import Cards



class BlackJack:

    def __init__(self, no_of_decks, allow_splitting):

        self.no_of_decks = no_of_decks
        self.allow_splitting = allow_splitting

        self.cards = Cards().generate_game(no_of_decks)
        self.players = []
        self.house = Player('House', True)

        self.has_split = False

    def add_player(self, name):

        self.players.append(Player(name, False))
        return self.players

    def deal(self):

        self.house = Player('House', True)

        # for p in range(len(self.players)):
        #     self.players[p].hands = [Hand()]

        if len(self.players) != 0:

            if (len(self.players) + 1) * 2 > len(self.cards):
                self.cards = Cards().generate_game(self.no_of_decks)

            for z in range(len(self.players)):
                self.players[z] = Player(self.players[z].name, False)

            for y in range(2):
                for x in range(len(self.players)):

                    self.players[x].hands[0].extend_hand([self.cards[0]])
                    del self.cards[0]

                self.house.hand.extend_hand([self.cards[0]])
                del self.cards[0]

    def split(self, player, cards):

        if not player.dealer:
            player.split()

    def dealer_stand_soft_17(self, player):
        if isinstance(player.hand.calculate_score(), int):
            if player.hand.score < 17:
                self.hit(player, 0, self.dealer_stand_soft_17)

    def basic_strategy(self, player):

        def should_hit_hard(h):
            if player.hands[h].score < 12:
                return True
            else:
                if player.hands[h].score < 17 and Cards().get_card_value(self.house.hand.cards[1]) > 6:
                    return True
                else:
                    if player.hands[h].score == 12 and Cards().get_card_value(self.house.hand.cards[1]) < 4:
                        return True

            return False

        def should_hit_soft(h):
            if player.hands[h].score < 17:
                return True
            else:
                if player.hands[h].score == 18 and Cards().get_card_value(self.house.hand.cards[1]) < 8:
                    return True
            return False

        def should_split():

            if len(player.hands[0].cards) == 2:
                if player.hands[0].cards[0] == player.hands[0].cards[1]:
                    return True

            return False

        if self.allow_splitting and should_split():
            player.split()
            self.has_split = True
            self.hit(player, 0, False)
            self.hit(player, 1, False)

        for h in range(len(player.hands)):

            if isinstance(player.hands[h].calculate_score(), int):
                    if len(player.hands[h].cards) == 2:
                        if isinstance(player.hands[h].cards[0], int) and isinstance(player.hands[h].cards[1], int):

                            if should_hit_hard(h):
                                self.hit(player, h, self.basic_strategy)

                        else:

                            if should_hit_soft(h):
                                self.hit(player, h, self.basic_strategy)
                    else:

                        if should_hit_hard(h):
                            self.hit(player, h, self.basic_strategy)

    def hit(self, player, h, cb):

        if len(self.cards) == 0:
            self.cards = Cards().generate_game(self.no_of_decks)
        if not player.dealer:
            player.hands[h].extend_hand([self.cards[0]])
        else:
            player.hand.extend_hand([self.cards[0]])

        del self.cards[0]

        if cb:
            cb(player)


    def show_status(self):

        print("Cards Remaining: ", len(self.cards))

        print("\n..................................")
        print("HOUSE: ", self.house.hand.cards, ' : ', self.house.hand.calculate_score())
        print("..................................\n")

        for x in range(len(self.players)):

            for y in range(len(self.players[x].hands)):

                if y > 0:
                    print('-', self.players[x].name, self.players[x].hands[y].cards, " : ",
                          self.players[x].hands[y].calculate_score())
                else:
                    print(self.players[x].name, self.players[x].hands[y].cards, " : ",
                          self.players[x].hands[y].calculate_score())

        print("\n----------------------------------\n\n\n")

    def show_results(self):
        print("\n----------------------------------\n\n\n")


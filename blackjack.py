from player import Player
from cards import Cards
from purse import Purse
from game import Game


class BlackJack:

    def __init__(self, no_of_decks, allow_splitting):

        print("\n##############################")
        print("#        BLACKJACKER         #")
        print("##############################\n")

        self.no_of_decks = no_of_decks
        self.allow_splitting = allow_splitting

        self.cards = Cards().generate_game(no_of_decks)
        self.players = []
        self.house = Player('House', True, 0, False)

        self.has_split = False

        self.games_played = 0

    def add_player(self, name, purse, bet_per_hand):

        self.players.append(Player(name, False, purse, bet_per_hand))
        return self.players

    def deal(self):

        self.house.reset()
        self.games_played = self.games_played + 1

        if len(self.players) != 0:

            if (len(self.players) + 1) * 2 > len(self.cards):
                self.cards = Cards().generate_game(self.no_of_decks)

            for z in range(len(self.players)):
                self.players[z].reset()
                self.players[z].purse.reset_wager()
                self.players[z].bet(1)

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

        dealers_up_card = Cards().get_card_value(self.house.hand.cards[1])

        def should_hit_hard(h):
            if player.hands[h].score < 12:
                return True
            else:
                if player.hands[h].score < 17 and dealers_up_card > 6:
                    return True
                else:
                    if player.hands[h].score == 12 and dealers_up_card < 4:
                        return True

            return False

        def should_hit_soft(h):
            if player.hands[h].score < 17:
                return True
            else:
                if player.hands[h].score == 18 and dealers_up_card < 8:
                    return True
            return False

        def should_split():
            player_total = Cards().get_card_value(player.hands[0].cards[0]) + Cards().get_card_value(
                player.hands[0].cards[1])

            if len(player.hands[0].cards) == 2:

                if player.hands[0].cards[0] == player.hands[0].cards[1]:

                    if isinstance(player.hands[0].cards[0], int) and isinstance(player.hands[0].cards[1], int):

                        if player_total <= 6 and dealers_up_card < 8:
                            return True
                        else:
                            if player_total == 12 and dealers_up_card < 7:
                                if dealers_up_card != 2:
                                    return True
                            else:
                                if player_total == 14 and dealers_up_card < 8:
                                    return True
                            if player_total > 14:
                                if player_total == 18 and (dealers_up_card == 7 or dealers_up_card == 11 or dealers_up_card == 10):
                                    return False
                                if player_total == 20:
                                    return False
                                return True
                    else:
                        if player.hands[0].cards[0] == 'A':
                            return True

            return False

        if self.allow_splitting and should_split():
            player.split()
            self.has_split = True
            self.hit(player, 0, False)
            self.hit(player, 1, False)

        def is_soft(hand):
            for h in range(len(hand.cards)):
                return hand.cards[h] == 'A'
            return False

        for h in range(len(player.hands)):

            if isinstance(player.hands[h].calculate_score(), int):

                if is_soft(player.hands[h]):
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

    def find_winner(self, game):

        for h in range(len(game.player.hands)):
            if game.player.hands[h].has_blackjack and not game.house.hand.has_blackjack:
                game.house.purse.spend(3 * game.player.bet_per_hand)
                game.player.purse.collect(3 * game.player.bet_per_hand)
                game.player.purse.collect_wager(1)
            else:
                if game.player.hands[h].is_bust:

                    self.house.purse.collect(1 * game.player.bet_per_hand)
                    game.player.purse.collect_wager(1)

                    if not game.house.hand.is_bust:
                        self.house.purse.collect(1 * game.player.bet_per_hand)
                        game.player.purse.collect_wager(1)
                else:
                    if game.house.hand.is_bust:

                        game.player.purse.collect(2 * game.player.bet_per_hand)
                        game.player.purse.collect_wager(1)
                    else:
                        if game.house.hand.score > game.player.hands[h].score:
                            # self.house_wins.append(True)
                            # self.player_wins.append(False)

                            self.house.purse.collect(1 * game.player.bet_per_hand)
                            game.player.purse.collect_wager(1)
                        else:
                            if game.house.hand.score == game.player.hands[h].score:

                                game.player.purse.collect(1 * game.player.bet_per_hand)
                                game.house.purse.spend(1 * game.player.bet_per_hand)
                                game.player.purse.collect_wager(1)

                            else:
                                game.player.purse.collect(2 * game.player.bet_per_hand)
                                game.house.purse.spend(2 * game.player.bet_per_hand)
                                game.player.purse.collect_wager(1)

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


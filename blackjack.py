from player import Player
from cards import Cards


class BlackJack:

    def __init__(self, no_of_decks):

        print("\n##############################")
        print("#        BLACKJACKER         #")
        print("##############################\n")

        self.no_of_decks = no_of_decks

        self.cards = Cards().generate_game(no_of_decks)
        self.players = []
        self.house = Player('House', True)

        self.log = []

        self.house_hands = []
        self.player_hands = []

        self.house_scores = []
        self.player_scores = []

        self.house_blackjacks = []
        self.player_blackjacks = []

        self.house_busts = []
        self.player_busts = []

        self.house_wins = []
        self.player_wins = []

    def add_player(self, name):

        self.players.append(Player(name, False))
        return self.players

    def deal(self):

        self.house = Player('House', True)

        if len(self.players) != 0:

            if (len(self.players) + 1) * 2 > len(self.cards):
                self.cards = Cards().generate_game(self.no_of_decks)

            for z in range(len(self.players)):
                self.players[z] = Player(self.players[z].name, False)

            for y in range(2):
                for x in range(len(self.players)):

                    self.players[x].extend_hand([self.cards[0]])
                    del self.cards[0]

                self.house.extend_hand([self.cards[0]])
                del self.cards[0]

    def stick_or_twist(self, player):

        def should_hit_hard():
            if player.score < 12:
                return True
            else:
                if player.score < 17 and Cards().get_card_value(self.house.hand[1]) > 6:
                    return True
                else:
                    if player.score == 12 and Cards().get_card_value(self.house.hand[1]) < 4:
                        return True

            return False

        def should_hit_soft():
            if player.score < 17:
                return True
            else:
                if player.score == 18 and Cards().get_card_value(self.house.hand[1]) < 8:
                    return True
            return False

        if isinstance(player.calculate_score(), int):
            if player.dealer:
                if player.score < 17:
                    self.twist(player)
            else:
                if len(player.hand) == 2:
                    if isinstance(player.hand[0], int) and isinstance(player.hand[1], int):

                        if should_hit_hard():
                            self.twist(player)

                    else:

                        if should_hit_soft():
                            self.twist(player)
                else:

                    if should_hit_hard():
                        self.twist(player)

    def twist(self, player):

        if len(self.cards) == 0:
            self.cards = Cards().generate_game(self.no_of_decks)

        player.extend_hand([self.cards[0]])
        del self.cards[0]

        self.stick_or_twist(player)

    def find_winner(self):

        for x in range(len(self.players)):
            if not self.players[x].is_bust:
                if self.house.is_bust:
                    self.players[x].winner = True
                else:
                    if self.players[x].has_blackjack and not self.house.has_blackjack:
                        self.players[x].winner = True
                    else:
                        if not self.players[x].has_blackjack and self.house.has_blackjack:
                            self.house.winner = True
                        else:
                            if self.players[x].score > self.house.score:
                                self.players[x].winner = True
                            else:
                                self.house.winner = True
            else:
                if self.house.is_bust:
                    self.house.winner = False
                    self.players[x].winner = False

    def show_status(self):

        print("Cards Remaining: ", len(self.cards))

        print("\n..................................")
        print("HOUSE: ", self.house.hand, ' : ', self.house.calculate_score())
        print("..................................\n")

        for x in range(len(self.players)):

            print(self.players[x].name, self.players[x].hand, " : ", self.players[x].calculate_score())

        print("\n----------------------------------\n\n\n")

    def show_results(self):
        print("\n----------------------------------\n\n\n")


    def log_game(self, game):
        self.log.append(game)

        self.house_hands.append(game.house.hand)
        self.house_scores.append(game.house.score)
        self.player_hands.append(game.player.hand)
        self.player_scores.append(game.player.score)

        if game.player.calculate_score() == 'BlackJack':
            self.player_blackjacks.append(True)
        else:
            self.player_blackjacks.append(False)

        if game.player.score > 21:
            self.player_busts.append(True)
        else:
            self.player_busts.append(False)

        if game.house.calculate_score() == 'BlackJack':
            self.house_blackjacks.append(True)
        else:
            self.house_blackjacks.append(False)

        if game.house.score > 21:
            self.house_busts.append(True)
        else:
            self.house_busts.append(False)

        self.find_winner()

        self.house_wins.append(game.house.winner)
        self.player_wins.append(game.player.winner)

    def print_log(self):

        player_black_jacks = 0
        player_busts = 0
        player_wins = 0

        house_black_jacks = 0
        house_busts = 0
        house_wins = 0

        print("\n\n")

        print("......................................", "\n")
        for x in range(len(self.house_hands)):

            if self.player_blackjacks[x]:
                player_black_jacks = player_black_jacks + 1

            if self.player_busts[x]:
                player_busts = player_busts + 1

            if self.house_blackjacks[x]:
                house_black_jacks = house_black_jacks + 1

            if self.house_busts[x]:
                house_busts = house_busts + 1

            if self.house_wins[x]:
                house_wins = house_wins + 1

            if self.player_wins[x]:
                player_wins = player_wins + 1

        print('Player BlackJacks: ', player_black_jacks, '/', len(self.house_hands))
        print('House BlackJacks: ', house_black_jacks, '/', len(self.house_hands))

        print('Player Wins: ', player_wins, '/', len(self.house_hands))
        print('House Wins: ', house_wins, '/', len(self.house_hands))

        print('Player Busts: ', player_busts, '/', len(self.house_hands))
        print('House Busts: ', house_busts, '/', len(self.house_hands))



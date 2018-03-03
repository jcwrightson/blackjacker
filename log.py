class Log:
    def __init__(self):

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

        self.draws = []

    def log_game(self, game):

        game.house.hand.calculate_score()
        self.house_hands.append(game.house.hand.cards)
        self.house_scores.append(game.house.hand.score)
        self.house_blackjacks.append(game.house.hand.has_blackjack)
        self.house_busts.append(game.house.hand.is_bust)

        for h in range(len(game.player.hands)):

            game.player.hands[h].calculate_score()
            self.player_blackjacks.append(game.player.hands[h].has_blackjack)

            self.player_hands.append(game.player.hands[h].cards)
            self.player_scores.append(game.player.hands[h].score)
            self.player_busts.append(game.player.hands[h].is_bust)

        self.find_winner(game)

    def find_winner(self, game):

        for h in range(len(game.player.hands)):
            if game.player.hands[h].is_bust:
                self.player_wins.append(False)
                if not game.house.hand.is_bust:
                    self.house_wins.append(True)
            else:
                if game.house.hand.is_bust:
                    self.house_wins.append(False)
                    self.player_wins.append(True)
                else:
                    if game.house.hand.score > game.player.hands[h].score:
                        self.house_wins.append(True)
                        self.player_wins.append(False)
                    else:
                        if game.house.hand.score == game.player.hands[h].score:
                            self.draws.append(True)
                        else:
                            self.house_wins.append(False)
                            self.player_wins.append(True)

    def no_of_player_blackjacks(self):

        c = 0
        for x in range(len(self.player_blackjacks)):
            if self.player_blackjacks[x]:
                c = c + 1
        return c

    def no_of_house_blackjacks(self):

        c = 0
        for x in range(len(self.house_blackjacks)):
            if self.house_blackjacks[x]:
                c = c + 1
        return c

    def no_of_player_busts(self):

        c = 0
        for x in range(len(self.player_busts)):
            if self.player_busts[x]:
                c = c + 1
        return c

    def no_of_house_busts(self):

        c = 0
        for x in range(len(self.house_busts)):
            if self.house_busts[x]:
                c = c + 1
        return c

    def no_of_player_wins(self):

        c = 0
        for x in range(len(self.player_wins)):
            if self.player_wins[x]:
                c = c + 1
        return c

    def no_of_house_wins(self):

        c = 0
        for x in range(len(self.house_wins)):
            if self.house_wins[x]:
                c = c + 1
        return c

    def print_log(self):

        print("Games Played: ", len(self.house_hands), "\nSplits: ",
              (len(self.player_hands) - len(self.house_hands)))
        print("......................................", "\n")

        print('Player BlackJacks: ', self.no_of_player_blackjacks())
        print('House BlackJacks: ', self.no_of_house_blackjacks())
        print('Player Wins: ', self.no_of_player_wins())
        print('House Wins: ', self.no_of_house_wins())
        print('Player Busts: ', self.no_of_player_busts())
        print('House Busts: ', self.no_of_house_busts())



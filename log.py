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

        self.player_purse = []
        self.house_purse = []

        self.last_game = False

    def log_game(self, game):

        game.house.hand.calculate_score()
        self.house_hands.append(game.house.hand.cards)
        self.house_scores.append(game.house.hand.score)
        self.house_blackjacks.append(game.house.hand.has_blackjack)
        self.house_busts.append(game.house.hand.is_bust)

        self.player_purse.append(game.player.purse.value)
        self.house_purse.append(game.house.purse.value)

        for h in range(len(game.player.hands)):

            game.player.hands[h].calculate_score()
            self.player_blackjacks.append(game.player.hands[h].has_blackjack)

            self.player_hands.append(game.player.hands[h].cards)
            self.player_scores.append(game.player.hands[h].score)
            self.player_busts.append(game.player.hands[h].is_bust)

            self.player_wins.append(game.player.hands[h].winner)
            self.draws.append(game.player.hands[h].draw)

        self.last_game = game

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

    def no_of_draws(self):

        c = 0
        for x in range(len(self.draws)):
            if self.draws[x]:
                c = c + 1
        return c

    def print_log(self):

        print("\nSplits: ", (len(self.player_hands) - len(self.house_hands)))
        print("......................................", "\n")

        print('Player BlackJacks: ', self.no_of_player_blackjacks())
        print('House BlackJacks: ', self.no_of_house_blackjacks())
        print('Player Wins: ', self.no_of_player_wins())
        print('Draws: ', self.no_of_draws())
        print('Player Busts: ', self.no_of_player_busts())
        print('House Busts: ', self.no_of_house_busts())

        # print('Player Purse: ', self.player_purse[len(self.player_purse)-1])
        print('Player Purse: ', self.last_game.player.purse.value)
        print('House Purse: ', self.last_game.house.purse.value)
        # print('House Purse: ', self.house_purse[len(self.house_purse)-1])



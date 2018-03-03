from blackjack import BlackJack
from game import Game
from log import Log


if __name__ == '__main__':

    # Settings
    no_of_games = 10
    no_of_decks = 6
    allow_splitting = True
    echo_game = False

    #Logging
    log = Log()

    # Init new game
    newGame = BlackJack(no_of_decks, allow_splitting)

    # Add new player
    newGame.add_player('Player')

    # Lets Play!!
    def play():

        newGame.deal()

        for x in range(len(newGame.players)):
            newGame.basic_strategy(newGame.players[x])

        newGame.dealer_stand_soft_17(newGame.house)

        log.log_game(Game(newGame.house, newGame.players[0]))

        if echo_game:
            newGame.show_status()


    # for y in range(no_of_games):
    #     play()


    # while not newGame.has_split:
    #     play()

    while log.no_of_player_wins() != 1000:
        play()

    # Show results
    log.print_log()

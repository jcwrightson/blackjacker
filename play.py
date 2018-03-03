from blackjack import BlackJack
from game import Game


if __name__ == '__main__':

    # Settings
    no_of_games = 10
    no_of_decks = 6
    echo_game = True

    # Init new game
    newGame = BlackJack(no_of_decks)

    # Add new player
    newGame.add_player('Player')

    # Lets Play!!
    def play():

        newGame.deal()

        for x in range(len(newGame.players)):
            newGame.basic_strategy(newGame.players[x])

        newGame.dealer_stand_soft_17(newGame.house)

        newGame.log_game(Game(newGame.house, newGame.players[0]))

        if echo_game:
            newGame.show_status()


    for y in range(no_of_games):
        play()

    # Show results
    newGame.print_log()

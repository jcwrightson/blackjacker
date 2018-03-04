from blackjack import BlackJack
from game import Game
from log import Log

import _thread


if __name__ == '__main__':

    # Settings
    no_of_games = 10
    no_of_decks = 6
    allow_splitting = True
    # echo_game = False
    echo_game = True
    loop_for_condition = False

    purse_value = 500
    bet_per_hand = 5

    #Logging
    log = Log()

    # Init new game
    newGame = BlackJack(no_of_decks, allow_splitting)

    # Add new player
    newGame.add_player('Player', purse_value, bet_per_hand)

    # Lets Play!!
    def play():

        newGame.deal()

        for x in range(len(newGame.players)):
            newGame.basic_strategy(newGame.players[x])

        newGame.dealer_stand_soft_17(newGame.house)

        this_game = Game(newGame.house, newGame.players[0])
        log.log_game(this_game)
        newGame.find_winner(this_game)

        if loop_for_condition:
            print("\rGames Played: {} Player Purse: {}".format(newGame.games_played, newGame.players[0].purse.value), end="")

        if echo_game:
            newGame.show_status()


    if loop_for_condition:
        def input_thread(L):
            derp = input()
            L.append(derp)

        L = []
        _thread.start_new_thread(input_thread, (L,))

        print("\nPress [Enter] to stop.")

        while newGame.players[0].purse.value <= 2000:

            play()

            if L:
                break

    else:
        for y in range(no_of_games):
            play()

    # Show results
    log.print_log()

# TODO: Add entry point code here
from dealer import Dealer
from player import Player
gameOn = True
dealer = Dealer()
player = Player()

while gameOn:
    dealer.get_card()
    dealer.show_most_recent_card()
    player_guess = player.makeGuess()
    dealer.get_card()
    player.compareCards(dealer.cards[-2], dealer.cards[-1], player_guess)
    play_again = player.ask_play_again()
    if not play_again:
        break

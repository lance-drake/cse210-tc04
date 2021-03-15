"""


"""

class Player:
    # Player class that keeps track of a player during each game.

    def __init__(self): 
        self.score = 300

    def ask_play_again(self):
        result = input("Do you want to play again(y,n): ")
        if result == "y":
            return True
        elif result == "n":
            return False
            
    def makeGuess(self):
        result = input("Will the next card be higher or lower (h,l): ")
        if result == "h":
            return "more"
        elif result == "l":
            return "less"

    def compareCards(self, lastCard, newCard, moreLess): 

        if moreLess == "more":
            if lastCard < newCard:
                print("You were right!\n The previous card: {} \n The new card: {} \nYou guessed: {}, your points were increased by 100!".format(lastCard,newCard,moreLess))
                self.score += 100
                return
            elif lastCard > newCard:
                print("You were wrong!\n The previous card: {} \n the new card: {} \nYou guessed : {},\n Your points were reduced by 75.".format(lastCard,newCard,moreLess))
                self.score -= 75
                return
        elif moreLess == "less":
            if lastCard > newCard:
                print("You were right!\n The previous card: {} \n The new card: {} \nYou guessed: {}, your points were increased by 100!".format(lastCard,newCard,moreLess))
                self.score += 100
                return
            elif lastCard < newCard:
                print("You were wrong!\n The previous card: {} \n the new card: {} \nYou guessed : {},\n Your points were reduced by 75.".format(lastCard,newCard,moreLess))
                self.score -= 75
                return



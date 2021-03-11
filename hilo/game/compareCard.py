

def compareCards(lastCard, moreLess): 
    newCard = dealer.drawCard()
    if moreLess == "more":
        if lastCard < newCard:
            print("You were right!\n The previous card: {} \n The new card: {} \nYou guessed: {}, your points were increased by 100!".format(oldCard,newCard,moreLess)
            player.score += 100
            return
        elif lastcard > newCard:
            print("You were wrong!\n The previous card: {} \n the new card: {} \nYou guessed : {},\n Your points were reduced by 75.".format(oldCard,newCard,moreLess)
            player.score -= 75
            return
    elif moreless == "Less":
        if lastCard > newCard:
            print("You were right!\n The previous card: {} \n The new card: {} \nYou guessed: {}, your points were increased by 100!".format(oldCard,newCard,moreLess)
            player.score += 100
            return
        elif lastcard < newCard:
            print("You were wrong!\n The previous card: {} \n the new card: {} \nYou guessed : {},\n Your points were reduced by 75.".format(oldCard,newCard,moreLess)
            player.score -= 75
            return
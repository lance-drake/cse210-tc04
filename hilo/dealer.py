import random

class Dealer:

    def __init__(self):
        self.cards = []
        self.num_card = 0

    def get_card(self):
        result = random.randint(1,13)
        self.cards.append(result)
        self.num_card +=1

    def show_most_recent_card(self):
        print("The card is: " + str(self.cards[-1]))
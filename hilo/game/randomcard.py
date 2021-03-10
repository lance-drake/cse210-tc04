import random

class cards_number:
   def playing_cards(self):
        for i in range(1):
            result = random.randint(1,13)
            self.cards.append(result)
        self.num_card +=1
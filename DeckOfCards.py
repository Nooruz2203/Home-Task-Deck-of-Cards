from random import shuffle
import random


class Cards:
    def __init__(self,name,value):
        self.name = name
        self.value = value

    def show(self):
        print('{}  {}'.format(self.value,self.name))

# card = Cards('Бубны', 6)
# card.show()

class DeckOfCards:
    def __init__(self):
        self.cards = []
        self.deal()
    def deal(self):
        for n in ['Червы','Бубны','Трефы','Пики']:
            for v in [2,3,4,5,6,7,8,9,10,'J', 'Q', 'K','A']:
                self.cards.append(Cards(n,v))
                print(n,v)
                # print(len(self.cards))

    def mix(self):
        for i in range(len(self.cards),0):
            r = random.randint(0,i)
            self.cards[i],self.cards[r] = self.cards[r], self.cards[i]
            print(r,i)

deck = DeckOfCards() 
deck.deal()
# deck.mix()

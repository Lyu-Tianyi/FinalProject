'''
Created on Dec 7, 2018

@author: l0t0y
'''
from random import random

class CardsDataEmulator():
    
    card1 = 0
    card2 = 0
    cards = ""
    
    def cardsGenerator(self):
        self.card1 = random(1, 13)
        self.card2 = random(1, 13)
    
        self.cards = str(self.card1) + ":" + str(self.card2)
        print(self.cards)
    
        return self.cards
'''
Created on Dec 7, 2018

@author: l0t0y
'''
from random import random
from numpy.random.mtrand import randint

'''
This part show be a object detection classifier which can recognize the cards value and send out the value data as an string.
But didn't figure out how to extract the data from the classifier, so i was using a emulator to emulate cards data.
The output string has 2 values separated by ':'
'''

class CardsDataEmulator():
    
    card1 = 0
    card2 = 0
    cards = "0:0"
    
    def __init__(self):
        self.cardsGenerator()
    
    def cardsGenerator(self):
        self.card1 = randint(1, 13)
        self.card2 = randint(1, 13)
    
        self.cards = str(self.card1) + ":" + str(self.card2)
        print(self.cards)
    
        return self.cards
    
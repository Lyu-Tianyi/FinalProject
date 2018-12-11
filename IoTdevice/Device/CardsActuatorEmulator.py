'''
Created on Oct 12, 2018

@author: l0t0y
'''
from Device.sense_hat import SenseHat

'''
This is a virtual Actuator for presenting the move of the player,
if move = 0, show 'hit', move = 1, show 'stand', move = 55, show 'split', else will show 'error'.
The sensorHat LED will print the message out.
'''

class CardsActuatorEmulator:
     
    cardsActuatorData=None
    moveData=None
    senseHat=None
    
    def __init__(self):
        
        self.senseHat=SenseHat()
                     
    def process_message(self,cardsActuatorData):
        
        self.cardsActuatorData=cardsActuatorData
        if self.cardsActuatorData!=None:
            if int(self.cardsActuatorData) == 0:
                self.moveData = "hit"
            elif int(self.cardsActuatorData) == 1:
                self.moveData = "stand"
            elif int(self.cardsActuatorData) == 55:
                self.moveData = "split"
            else:
                self.moveData = "error"
        self.doAction()
                
    def doAction(self):
        
        self.senseHat.show_message(self.moveData) 
                
                
    
        
        
        

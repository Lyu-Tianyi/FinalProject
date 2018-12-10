'''
Created on Oct 12, 2018

@author: l0t0y
'''
from Device.sense_hat import SenseHat


'''
This is a virtual Actuator for presenting 
temperature is being lowered or increased 
by showing the delta between current Temperature 
and expected Temperature n SenseHatLED.
'''

class CardsActuatorEmulator:
     
    cardsActuatorData=None    
    senseHat=None
    
    def __init__(self):
        
        self.senseHat=SenseHat()
                     
    def process_message(self,cardsActuatorData):
        
        self.cardsActuatorData=cardsActuatorData 
        self.doAction()
                
    def doAction(self):
        
        self.senseHat.show_message(self.cardsActuatorData) 
                
                
    
        
        
        

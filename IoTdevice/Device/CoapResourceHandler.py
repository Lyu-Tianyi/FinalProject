'''
Created on Dec 6, 2018

@author: l0t0y
'''

import threading
from coapthon.resources.resource import Resource
from Device.CardsDataEmulator import CardsDataEmulator
from Device.CardsActuatorEmulator import CardsActuatorEmulator
from Device.sense_hat import SenseHat

class CoapResourceHandler(Resource):
    
    cardsData=None
    actuatorData=None
    cardsActuatorEmulator=CardsActuatorEmulator()
    
    
    def __init__(self, name = "TestCoapResource", coap_server = None):
        
        super(CoapResourceHandler, self).__init__(name, coap_server, visible = True, observable = True, allow_children = True)
        
        self.cardsData=""
        
        self.payload="hi"
        self.read_cards()
        
    
    #Read cards data from the cardsDaraEmulator
    def read_cards(self):
        
        self.cardsData=CardsDataEmulator()  
        self.payload=self.cardsData
        self.period=20

        timer = threading.Timer(self.period, self.read_cards)
        timer.setDaemon(True)
        timer.start()
        
        self._coap_server.notify(self)
        
    #Implementing GET and POST
    def render_GET(self, request):
        
        self.cardsData=CardsDataEmulator()  
        self.payload=self.cardsData
        print("Trigger Get request...." + str(self.payload))
        return self
    
    def render_POST(self, request):
        print("Message"+request.payload)
        CardsActuatorEmulator.process_message(request.payload)

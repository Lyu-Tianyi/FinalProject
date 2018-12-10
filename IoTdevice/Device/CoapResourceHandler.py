'''
Created on Dec 6, 2018

@author: l0t0y
'''
import threading
from coapthon.resources.resource import Resource
from Device.CardsDataEmulator import CardsDataEmulator
from Device.CardsActuatorEmulator import CardsActuatorEmulator

class CoapResourceHandler(Resource):
    
    cardsData=None

    command=None
    
    sumData=None
    
    actuator=None
    
    def __init__(self, name = "TestCoapResource", coap_server = None):
        
        super(CoapResourceHandler, self).__init__(name, coap_server, visible = True, observable = True, allow_children = True)

        self.cardsData=""
        self.command=""
        self.sumData=""
        self.payload="hi"
        
    def read_cards(self):
        
        self.cardsData=CardsDataEmulator.cardsGenerator()
        self.actuator=CardsActuatorEmulator.process_message(self, self.sumData + " " + self.command)
        self.payload=self.cardsData
        
        self.period=20

        timer = threading.Timer(self.period, self.read_cards)
        timer.setDaemon(True)
        timer.start()
        
        self.coap_server.notify(self)
        
    # only ‘GET’ is provided; review the CoAPthon documentation for
    # examples implementing ‘PUT’, ‘POST’, ‘DELETE’: https://github.com/Tanganelli/CoAPthon
    def render_GET(self, request):
        print("Successfully retrieved this message from TestCoapResource. Payload: " + str(self.payload))
        return self
    
    def render_POST(self, request):
        print(request.get_payload())
        

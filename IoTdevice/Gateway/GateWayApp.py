'''
Created on Dec 6, 2018

@author: l0t0y
'''

from Gateway.GetCardsCoAPClient import GetCardsCoAPClient 
from Gateway.mqttActuatorSubClient import MqttActuatorSubClient




#Start listening new cards data from device
getCardsClient=GetCardsCoAPClient()
getCardsClient.getCardsWithObserver("....")

#Start listening new actuator data from cloud
getActuatorClient=MqttActuatorSubClient()
getActuatorClient.start_Listening_ActuatorData()


while True:
    pass




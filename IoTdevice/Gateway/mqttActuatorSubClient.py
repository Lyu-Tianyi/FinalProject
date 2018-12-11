'''
Created on Dec 6, 2018

@author: l0t0y
'''
from Gateway.MqttClientConnector import MqttClientConnector
from coapthon.client.helperclient import HelperClient 

'''
This is a mqtt sub client which will subscribe to the topic of 'move' on ubidots and get the value back
And there is also a coap client inside which can POST the actuator data back to raspberry pi
'''

class MqttActuatorSubClient():
    
    coapClient = None
    mqttClient = None
    
    coap_port=5683  
    coap_host="localhost"

    cards_actuator_data="Hi"
    
    def __init__(self):
        
        self.initCoapClient()
        self.initMqttClient()
    
    #Initialize the coapclient
    def initCoapClient(self):
        
        try:
            self.coapClient = HelperClient(server = (self.coap_host, self.coap_port))
            print("Created CoAP coapClient ref: " + str(self.coapClient))
            
        except Exception:
            print("Failed to create CoAP helper coapClient reference using host: " + self.coap_host)
            pass
        
    #Initialize the mqttsubclient
    def initMqttClient(self):
        try:
            
            self.mqttClient=MqttClientConnector("D:\\git\\repository2\\iot-gateway\\ubidots_cert.pem", self.on_connect, self.on_message, self.on_publish, self.on_subscribe)
            print("Created MQTTClient ref......")
            
        except Exception:
            print("Failed to create MQTT CLIENT " + self.mqtt_host)
            pass
    
    #POST the actuatorData back to coapserver
    def postCardsCommandToServer(self,resource):
        
        print("Post for resource: " + resource)

        response = self.coapClient.post(resource,self.cards_actuator_data) 

        if response:
            print("Response: "+response.pretty_print())
        else:
            print("No response received for GET using resource: " + resource)
            self.coapClient.stop()
            
    #Subscribe to topic 'move' on Ubidots
    def start_Listening_ActuatorData(self):
        
        print("Start subscribing ActuatorData from cloud....")
        self.mqttClient.subscribeTopic("/v1.6/devices/iotfinalproject/move",1)
    
    #Callback functions
    
    def on_connect(self, clientConn, data, flags, resultCode):
        print("Client connected to server. Result: " + str(resultCode))
    
    #Customize callback function when subscribed actuatorData arrived
    def on_message(self, clientConn, data, msg):
        print("MoveData arrived....Transfering to device")
        self.cards_command_data=str(msg)
        self.postCardsCommandToServer("iot/move")
    
    def on_publish(self, client, userdata, result):
        print("Published success")
        
    def on_subscribe(self):
        print("Successfuly subscribed!!")
        
        
        
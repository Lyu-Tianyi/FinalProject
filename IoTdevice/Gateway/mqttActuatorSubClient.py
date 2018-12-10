'''
Created on Dec 6, 2018

@author: l0t0y
'''
from Gateway.MqttClientConnector import MqttClientConnector
from coapthon.client.helperclient import HelperClient 


class MqttActuatorSubClient():
    
    coapClient = None
    mqttClient = None
    
    coap_port=5683  
    coap_host="192.168.0.6"

    
    cards_actuator_data="Hi"
    
    
    
    def __init__(self):
        
        self.initCoapClient()
        self.initMqttClient()



    
    def initCoapClient(self):
        
        try:
            self.coapClient = HelperClient(server = (self.coap_host, self.coap_port))
            print("Created CoAP coapClient ref: " + str(self.coapClient))
            
        except Exception:
            print("Failed to create CoAP helper coapClient reference using host: " + self.coap_host)
            pass
 
 
 
        
    def initMqttClient(self):
        try:
            
            self.mqttClient=MqttClientConnector("D:\\git\\repository2\\iot-gateway\\ubidots_cert.pem", self.on_connect, self.on_message, self.on_publish, self.on_subscribe)
            print("Created MQTTClient ref......")
            
        except Exception:
            print("Failed to create MQTT CLIENT " + self.mqtt_host)
            pass
        
    def postCardsCommandToServer(self,resource):
        
        print("Post for resource: " + resource)

        response = self.coapClient.post(resource,self.cards_actuator_data) 

        if response:
            print("Response: "+response.pretty_print())
        else:
            print("No response received for GET using resource: " + resource)
            self.coapClient.stop()
            
  
  
  
    def start_Listening_ActuatorData(self):
        
        print("Start subscribing ActuatorData from cloud....")
        self.mqttClient.subscribeTopic("/v1.6/devices/iotfinalproject/move",1)
        
   

    def on_connect(self, clientConn, data, flags, resultCode):
        print("Client connected to server. Result: " + str(resultCode))
        
    def on_message(self, clientConn, data, msg):
        
        print("CommandData arrived....Transfering to device")
        self.cards_command_data=str(msg)
        self.postCardsCommandToServer("iot/cardsCommand")
    
    def on_publish(self, client, userdata, result):
        print("Published success")
        
    def on_subscribe(self):
        print("Successfuly subscribed!!")
        
        
        
'''
Created on Dec 6, 2018

@author: l0t0y
'''

import getopt
import socket
import sys
from coapthon.client.helperclient import HelperClient
from coapthon.utils import parse_uri
from Gateway.MqttClientConnector import MqttClientConnector
from coapthon.messages.response import Response
from paho import mqtt
from Gateway.SmtpClientConnector import SmtpClientConnector

'''
This is a coap client on gateway device, using observer to get the cards value from raspberry pi coap server.
When the new values posted, it will observe by the observer and get the value
And there are two mqtt client build in this coap client to publish the values of 'command' and 'sum' to ubidots
There is also a SMTP client to send email to my mailbox
'''

class GetCardsCoAPClient():
    
    coapClient = None
    mqttClient = None
    smtpClient = None
    
    coap_port=5683  
    coap_host="127.0.0.1"
    
    def __init__(self):
        
        self.initCoapClient()
        self.initMqttClient()
        self.smtpClient=SmtpClientConnector()
    
    #Initialize coap client
    def initCoapClient(self):
        
        try:
            self.coapClient = HelperClient(server = (self.coap_host, self.coap_port))
            print("Created CoAP coapClient ref: " + str(self.coapClient))
            
        except Exception:
            print("Failed to create CoAP helper coapClient reference using host: " + self.coap_host)
            pass
 
 
 
    #Initialize mqtt client
    def initMqttClient(self):
        try:
            
            self.mqttClient=MqttClientConnector("D:\\git\\repository2\\iot-gateway\\ubidots_cert.pem", self.on_connect, self.on_message, self.on_publish_cards, self.on_subscribe)
            print("Created MQTTClient ref......")
            
        except Exception:
            print("Failed to create MQTT CLIENT " + self.mqtt_host)
            pass



    #CoapCallBackFunction
    def callback(self,response):
        
        print("Message arrived....transfering message to MqttClient......")
        
        print(str(response))
        
        # Calculate and give command and sum values
        message = response.payload
        card1, card2 = message.split(":")
          
        if int(card1) > 10:
            card1_int = 10
        else:
            card1_int = int(card1)
        if int(card2) > 10:
            card2_int = 10
        else:
            card2_int = int(card2)
          
        sum_int = card1_int + card2_int
          
        if int(card1)==int(card2):
            command = 1
        else:
            command = 0
          
        cardssum = str(sum_int)
          
        
        #Publish CardsCommandData and CardsSumData to cloud 
        self.mqttClient.connect()
        self.mqttClient.publishMessage("/v1.6/devices/iotfinalproject/command", command, 1)                
        self.mqttClient.publishMessage("/v1.6/devices/iotfinalproject/sum", cardssum, 1)
        self.mqttClient.disconnect()      
        
           
        #send EmailNotification 
        self.smtpClient.publishMessage("CardsNotification",
                                       "Total sum value: " + cardssum + "/n" +
                                       "Command value: " + command)
        
        
        print("CoapClient Callback end!!")
        


    #GET cards value form the observer from coap server
    def getCardsWithObserver(self,resource):
    
        print("GET for resource: " + resource)
        #response = self.coapClient.observe(resource, self.callback)
        response=self.coapClient.observe(resource, self.callback, 10)
        if response:
            print(response.pretty_print())
        else:
            print("No response received for GET using resource: " + resource)
            self.coapClient.stop()


    #MqttCallBackFunctions
        
    def on_connect(self,mqttc,obj,flags,rc):
        print("Successfully Connect to GatewayBroker!! rc: "+str(rc))

    #custom callback when subscribed actuatorData arrive, then tiger temperature ActuatorEmulator     
    def on_message(self,mqttc, obj, msg):
        print("Message arrived from topic:"+msg.topic + " QoS:" + str(msg.qos) + " Message:" + str(msg.payload.decode("utf-8")))
        
        
    #custom callback when Temperature SensorData publish success
    def on_publish_cards(self,mqttc, obj, mid):
        print("Successfully Published cardsData to topic iot/cardsData !! mid: " + str(mid) )       
        
    #custom callback when successfully subscribe to Temperature Actuator
    def on_subscribe(self,mqttc, obj, mid, granted_qos):
        print("Successfully Subscribed  !! " + str(mid) + " Granted_QoS:" + str(granted_qos))
        


    
    
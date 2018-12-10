'''
Created on Dec 7, 2018

@author: l0t0y
'''
from paho.mqtt.client import Client
import ssl


class MqttClientConnector():
               

    _mqttClient=None 
    
    BROKER_ENDPOINT = "things.ubidots.com"
    TLS_PORT = 8883  # Secure port
    MQTT_USERNAME = "A1E-5VsW5TXS0AK4b0wO0osGIFB5qZWk31"  # Put here your Ubidots TOKEN
    MQTT_PASSWORD = ""  # Leave this in blank
    DEVICE_LABEL = "truck"
    TLS_CERT_PATH = None  # Put here the path of your TLS cert
    

    #Allow user to use this constructor to pass custom callBack methods
    def __init__(self,TLS_CERT_PATH,on_connect,on_message,on_publish,on_subscribe):
            
        self._mqttClient=Client()   
        self.TLS_CERT_PATH=TLS_CERT_PATH  
           
        self._mqttClient.on_connect=on_connect
        self._mqttClient.on_message=on_message
        self._mqttClient.on_publish=on_publish
        self._mqttClient.on_subscribe=on_subscribe
        
                
    def connect(self):

            try:
                
                self._mqttClient.username_pw_set(self.MQTT_USERNAME, self.MQTT_PASSWORD)
            
                self._mqttClient.tls_set(self.TLS_CERT_PATH , certfile=None,
                                          keyfile=None, cert_reqs=ssl.CERT_REQUIRED,
                                          tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
            
                self._mqttClient.tls_insecure_set(False)
                self._mqttClient.connect(self.BROKER_ENDPOINT,self.TLS_PORT)
                self._mqttClient.loop_start()
                print("Connect successfully....")

            except Exception as e:
                
                print("Cloud not connect to broker "+self.BROKER_ENDPOINT+" "+str(e))
            

    def disconnect(self):
            
        self._mqttClient.disconnect()
        self._mqttClient.loop_stop()
        
               
    def publishMessage(self,topic,message,qos):
        
        print("Publishing message:"+message+" to broker: "+self.BROKER_ENDPOINT+" Topic:"+topic)
        self._mqttClient.publish(topic,message,qos)
    
    
    def subscribeTopic(self,topic,qos):
        
        print("Subscribing to topic:"+topic+".....")
        self._mqttClient.subscribe(topic,qos)
    



  
def on_connect(mqttc,obj,flags,rc):
    print("Successfully Connect to GatewayBroker!! rc: "+str(rc))
  
 
def on_message(mqttc, obj, msg):
    print("Message arrived from topic:"+msg.topic + " QoS:" + str(msg.qos) + " Message:" + str(msg.payload.decode("utf-8")))
           
   
def on_publish(mqttc, obj, mid):
    print("Successfully published  !! mid: " + str(mid) )       
        
    
def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Successfully Subscribed to topic!! " + str(mid) + " Granted_QoS:" + str(granted_qos))



# client=MqttClientConnector("C:/Users/Leo/Documents/ubidots_cert.pem", on_connect, on_message, on_publish, on_subscribe)
# 
# client.connect()
# 
# client.publishMessage("/v1.6/devices/iotfinalproject/sum", "18",1)
# 
# 
# while True:
#     pass

    
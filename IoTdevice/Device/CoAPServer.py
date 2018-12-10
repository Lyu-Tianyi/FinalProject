'''
Created on Dec 6, 2018

@author: l0t0y
'''
from coapthon.server.coap import CoAP
from Device.CoapResourceHandler import CoapResourceHandler

class CoapServerConnector(CoAP):
    
    def __init__(self, ipAddr = "localhost", port = 5683, multicast = False):
        
        CoAP.__init__(self, (ipAddr, port), multicast)
        self.port = 5683
        self.ipAddr = ipAddr
        self.useMulticast = multicast
        self.initResources()
            
    def initResources(self):
        self.add_resource('test', CoapResourceHandler())
        print("CoAP server initialized. Binding: " + self.ipAddr + ":" + str(self.port))
        print(self.root.dump())
    
def main():
    ipAddr = "localhost"
    port = 5683
    useMulticast = False
    coapServer = None
    try:
        coapServer = CoapServerConnector(ipAddr, port, useMulticast)
        print("Created CoAP server successfully")
        try:
            coapServer.listen(10)
            print("Created CoAP server ref: " + str(coapServer))
        except Exception:
            print("Failed to create CoAP server reference bound to host: " + ipAddr)
            pass
    except KeyboardInterrupt:
        print("CoAP server shutting down due to keyboard interrupt...")
    if coapServer:
        coapServer.close()
        print("CoAP server app exiting.")
if __name__ == '__main__':
    main()





        
'''
Created on Sep 22, 2018

@author: l0t0y
'''

from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart

'''
This is a simple SMTP connector
Use for send email to my unique address
'''

class SmtpClientConnector():
    def __init__(self):
        print('Configuration data...\n')
        
    def publishMessage(self, topic, data):
        host = "smtp.gmail.com"
        port = 465
        fromAddr = "loveinu007@gmail.com"
        toAddr = "loveinu007@gmail.com"
        authToken = ""
        msg = MIMEMultipart()
        msg['From'] = fromAddr
        msg['To'] = toAddr
        msg['Subject'] = topic
        msgBody = str(data)
        msg.attach(MIMEText(msgBody))
        msgText = msg.as_string()
        # send e-mail notification
        smtpServer = smtplib.SMTP_SSL(host, port)
        smtpServer.ehlo()
        smtpServer.login(fromAddr, authToken)
        smtpServer.sendmail(fromAddr, toAddr, msgText)
        smtpServer.close()
        
    def sendEmailMessage(self,topic,message):
        for destinAddr in self.destinAddr:
            
            msg=MIMEText(str(message))
            msg["From"]=self.sourceAddr
            msg["to"]=destinAddr
            msg["Subject"]=topic
        
            try:
                mailServer=smtplib.SMTP_SSL(self.host,self.port)
                mailServer.ehlo()
                mailServer.login(self.sourceAddr,self.passphrase)
                mailServer.send_message(msg,self.sourceAddr,destinAddr)
                mailServer.close()
                print("Sent successfully to "+destinAddr)
            except Exception as e:
                print("Failed to send email\n"+e)
    
    def printInfo(self):
        print("host:"+self.host+"\nport:"+str(self.port)+"\nFromAddr:"+self.sourceAddr+"\ntoAddr:"+self.destinAddr+"\n"+
              "authToken:"+self.passphrase)
        
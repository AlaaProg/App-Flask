# -*- coding: utf-8 -*-

from flask_mail import Message,Mail


class SendMail(Mail):
    
    def __init__(self,app):
      
        super(SendMail,self).__init__(app) 
        
        
    def sendMessage(self,**kw):
        msg = Message(kw["title"])
        
        msg.sender     = kw["_from"]
        msg.recipients = [kw["_to"]]
        msg.html       = kw["body"]
        
        self.send(msg)
    

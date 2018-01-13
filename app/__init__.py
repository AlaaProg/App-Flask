# -*- coding: utf-8 -*-
 
import os
##
from flask import Flask
from app.config    import config
###
from app.model     import Router
from app.model     import SendMail
from app.model     import Token
from app.model     import Cookies
from app.model     import DBJson
#
from app.Databases import SQLite
#
from app.Controller import Pages

app = Flask(os.getcwd())

config(app)

class model:
	

	def __init__(self):

		self.mail    = SendMail (  app)
		self.token   = Token    (  app)
		self.sqlite  = SQLite   (  app)
		self.dbJson  = DBJson   (  app)
		self.cookies = Cookies


	def __dir__(self): 

		return ['mail', 'sqlite', 'token']
route  = Router(app)
pages  = Pages(model())

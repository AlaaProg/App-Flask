import importlib as lib ,os
#####
from flask import Flask
from app.config    import config
#####
from app.model     import Router,SendMail,Token,Cookies
#####
from app.DB import SQLite,MySQL,DBJson


app = Flask(os.getcwd())

config(app)

class model:
	

	def __init__(self):

		self.mail    = SendMail (  app)
		self.token   = Token    (  app)
		self.sqlite  = SQLite   (  app)
		#self.mysql   = MySQL    (  app)
		self.dbJson  = DBJson   (  app)
		self.cookies = Cookies


	def __dir__(self): 

		return ['mail', 'sqlite', 'token',"mysql","cookies","dbJson"]

class Controllers():

	def __init__(self,App):
		self.Controll = {}
		for  i in os.listdir("app/Controller"):
			if not i.startswith("__"):
				model = i.strip(".py")
				Cl = lib.import_module("app.Controller.%s"%model,model)
				self.Controll.update({model:getattr(Cl,model)(App)})
		
	def __getattr__(self,k):
		return self.Controll.get(k)

	def __dir__(self):
		return self.Controll.keys()


route  = Router(app)
view  = Controllers(model())

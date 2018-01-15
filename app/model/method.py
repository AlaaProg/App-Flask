from flask import render_template


class Router():

	def __init__(self,app):
		self.app = app

	def get(self,path,function=None,html=None,**kws):
		if function == None:
			a = lambda **kw:render_template(str(html),**kw,**kws)
			self.app.add_url_rule(path,html,a, methods=["GET"])

		else:
			self.app.add_url_rule( path,function.__name__,function,methods=["GET"])
	

	def post(self,path,function):
		self.app.add_url_rule(path,function.__name__,function,methods=["POST"])
	

	def PostGet(self,path,function=None,html=None,**kws):
		if function == None:
			a = lambda **kw:render_template(str(html),**kw,**kws)
			self.app.add_url_rule(path,html,a, methods=["GET","POST"])
		else:
			self.app.add_url_rule(path,function.__name__,function,methods=["GET","POST"])

	
	def put(self,path,function):
		self.app.add_url_rule( path, function.__name__, function, methods=["PUT"])

	def delete(self,path,function):
		self.app.add_url_rule( path, function.__name__, function, methods=["DELETE"])


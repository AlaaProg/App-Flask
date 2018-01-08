
class Router():

	def __init__(self,app):
		self.app = app

	def GET(self,path,function):
		self.app.add_url_rule( path, function.__name__, function, methods=["GET"])

	def POST(self,path,function):
		self.app.add_url_rule( path, function.__name__, function, methods=["POST"])

	def PUT(self,path,function):
		self.app.add_url_rule( path, function.__name__, function, methods=["PUT"])

	def DELETE(self,path,function):
		self.app.add_url_rule( path, function.__name__, function, methods=["DELETE"])



class Route():

	def __init__(self,app):
		self.app = app

	def GET(self,path,function):
		self.app.add_url_rule( path, function.__name__, function, methods=["GET"])

	def POST(self,path,function):
		self.app.add_url_rule( path, function.__name__, function, methods=["POST"])

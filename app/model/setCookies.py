from flask import make_response,redirect,request

class Cookies():

	def __init__(self,path="/"):
		self.resp = make_response(redirect(path))

	def __setitem__(self,k,v):
		self.resp.set_cookie(k,v)

	@staticmethod
	def get(k):
		return request.cookies.get(k)
		

	def save(self):
		return self.resp

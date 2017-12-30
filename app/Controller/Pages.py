from flask import (
		redirect,url_for,request,
		make_response,abort,render_template
	)
from app.Databases import SQLite

class Control(SQLite):
	# self.exce(" command SQL ")

	def __init__(self):
		super(Control,self).__init__("db.sql")


	def index(self):
		return render_template("login.html")



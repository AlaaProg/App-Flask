from flask import (
		redirect,url_for,request,session,
		make_response,abort,render_template,
        jsonify
	)

class Pages():

    def __init__(self,this):
	# this = modle ( sqlite , token , mail )
        self.this = this
	

    def home(self):
        return render_template("home.html")

    def login(self):
        return render_template("login.html")

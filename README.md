# App-Flask


__Route.py__

```
# route. ( GET POST PUT DELETE )
## 
route.get ( "/"     , view.pages.home     )
route.get( "/"     , view.pages.home     )
## 
route.get ( "/login" , view.pages.login    )
route.get( "/login" , view.pages.login )

# You Can't make '2 route' for same html file 
route.get("/home/<name>",html="home.html")
route.get("/login",html="login.html")

```
__Controller -> Page.py__

```
from flask import (
		redirect,url_for,request,session,
		make_response,abort,render_template,jsonify
	)

class Pages():

    def __init__(self,this):
       # this = modle ( sqlite , token , mail )
       self.this = this
	

    def home(self):
        return render_template("home.html")

    def login(self):
        return render_template("login.html")

```

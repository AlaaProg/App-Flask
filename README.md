# App-Flask

__new To Flask__<br>
__I am add 'Class Cookies' in heipers.py__
```
SetCookies And GetCookies 

Exmp:/

	from flask import Cookies
    #setCookies :
	def set (name):

	    # key: 
	    #     html :: render file html 
	    #     path :: redirct to path   

	    cookies = Cookies(html="index.html")
	    cookies["name"] = name 
	    return cookies 
    #getCookies :
	def get():
	    return Cookies.get("name")

    #rint all
	def all_cookies():
	    return str ( Cookies() )	

```

__Route.py__

```
# route. ( GET POST PUT DELETE )
## function python 
route.get ( "/"     , view.pages.home     )
route.post( "/login"     , view.pages.login     )
## function python 
route.get ( "/login" , view.Ctrol.login    )
route.post( "/login" , view.Ctrol.login )

# set path to html File 
route.get("/home/<name>",html="home.html")
route.get("/login",html="login.html")

```
__automatically import  Controllers and set in view__<br>
__you not need do to  import__<br>
__^_^__<br><br>
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
__Controller -> Ctrol.py__

```
from flask import (
		redirect,url_for,request,session,
		make_response,abort,render_template,jsonify
	)

class Ctrol():

    def __init__(self,this):
       self.this = this
	


```

from flask import (
                        redirect,render_template,
                        request,make_response,
                        url_for,abort
                   )

class Ctrol():
   def __init__(self,this):
       self.this = this 
       
    
   def index(self):
   
      return "Hello World"

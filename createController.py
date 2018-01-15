import os,sys

#python createController NameController


if len(sys.argv) != 1 :

	name = sys.argv[1]

	# print (dir(name ))

	newController = """ 

from flask import (redirect,render_template,request,url_for,abort)

class %s():

	def __init__(self,this):
		self.this = this


	"""%(name)

	open("app/Controller/%s.py"%name,"w").write(newController)

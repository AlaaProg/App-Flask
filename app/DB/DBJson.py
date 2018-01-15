#!/usr/bin/env python3

import random,json,os,binascii

class DBJson():

	def __init__(self,app=None):
		self.fileJson = app.config.get("DB:Json")
		# Read JsonFile 
		self.data = open(self.fileJson,"r").read()

	def up(self):
		self.data = open(self.fileJson,"r").read()
	def time(self):
		return time.strftime("%H:%M:%S",time.localtime())
	def str2hex(self,string):
		return binascii.b2a_hex(string.encode("u8")).decode("u8")
	def hex2str(self,hexs):
		return binascii.a2b_hex(hexs.encode("u8")).decode("u8")

	def rm(self,k):
		rjson = json.loads(self.data)
		if rjson.get(k):
			rjson.pop(k)
		open(self.fileJson,"w").write(json.dumps(rjson,sort_keys=True,indent=4))

	def __setitem__(self,k,v):
		self.up()
		rjson = json.loads(self.data)
		rjson[k] = v
		open(self.fileJson,"w").write(json.dumps(rjson,sort_keys=True,indent=4))


	def __delitem__(self,k):
		self.up()
		rjson = json.loads(self.data)
		if rjson.get(k):
			rjson.pop(k)
		open(self.fileJson,"w").write(json.dumps(rjson,sort_keys=True,indent=4))

	def __getitem__(self,k):
		self.up()
		return json.loads(self.data).get(k)

	def __str__(self):
		self.up()
		return str(json.loads(self.data))
		

	def __class__(self):
		pass

	def __dir__(self):
		return ["time","str2hex","hex2str","rm"]




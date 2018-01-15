import mysql.connector as sql


class MySQL():

	def __init__(self,app):
		try:
			self.connect = sql.connect(**app.config["DB:MySQL"])
			self.cur = self.connect.cursor()
		except sql.Error as error:
			print(error)


	def exec(self,command):
		try:
			for i in self.cur.execute(command,multi=True):
				if i.with_rows:
					return self.cur.fetchall()

				self.connect.commit()
		except sql.Error as error:
			return error


	# def __del__(self):
	# 	self.cur.close()
	# 	self.connect.close()

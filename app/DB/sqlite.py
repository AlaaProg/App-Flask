import sqlite3 as sql 


class SQLite():
	def __init__(self,app):
		self.connect = sql.connect(app.config["DB:SQLite"])
		self.cur = self.connect.cursor()

	def exec(self,command):
		try:
			self.cur.execute(command)
			if self.cur.rowcount != -1:
				return self.cur.fetchall()

			self.commit()
		except sql.Error as error:
			return error

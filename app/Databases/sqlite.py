import sqlite3 as sql 


class SQLite():
	def __init__(self,DBName):
		self.connect = sql.connect("app/Databases/dbite/"+DBName)
		self.cur = self.connect.cursor()

	def exec(self,command):
		try:
			self.cur.execute(command)
			if self.cur.rowcount != -1:
				return self.cur.fetchall()

			self.commit()
		except sql.Error as error:
			return error

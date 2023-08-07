"""
This file contains Observer classes.

docs:
https://stackoverflow.com/questions/13514509/search-sqlite-database-all-tables-and-columns
"""

class SQLiteObserver:
	"""
	A mutable class responsible for viewing SQLite objects.
	"""
	def __init__(self):
		"""
		@EFFECTS: construct an Observer instance.
		"""
		pass

	def update(self, conn):
		"""
		@PARAMS: conn is a connection to an SQLite database
		@REQUIRES: conn is an SQLite3.Connection object, and conn is open.
		@MODIFIES: self._data
		@EFFECTS: update Observer with data from the conn.
		"""
		pass

class SchemaViewer(SQLiteObserver):
	""" 
	A mutable class responsible for seeing the schema of an SQLite3 database. 
	"""
	def __init__(self):
		"""
		@EFFECTS: construct an Observer instance.
		"""
		self._data = dict()

	def update(self, conn):
		"""
		@PARAMS: conn is a connection to an SQLite database
		@REQUIRES: conn is an SQLite3.Connection object, and conn is open.
		@MODIFIES: self._data
		@EFFECTS: 
			update Observer with data from the conn.
			specifically, the data is about the schema of the connected database.
		"""
		cur = conn.cursor()
		list_of_tables = cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
		
		for row in list_of_tables:
			table_name = row[0]
			
			cur.execute("SELECT * FROM {};".format(table_name))
			column_names = [description[0] for description in cur.description]

			self._data[table_name] = column_names

		pass

	def getDataAsString(self):
		"""
		@RETURNS: a string of the data in the Observer 
		"""
		ret_str = ""
		for table_name in self._data.keys():
			columns_str = ",".join(self._data[table_name])
			ret_str += "{}({})\n".format(table_name, columns_str)
		
		return ret_str

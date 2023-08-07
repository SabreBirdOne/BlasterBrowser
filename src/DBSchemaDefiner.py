"""
This file contains a DataBuilder, used to define the tables in the BlasterBrowsers database.
"""

import sqlite3

class DBSchemaDefiner:
	"""
	This immutable class defines tables in a database following a schema. It only creates empty tables
	"""
	def __init__(self):
		"""
		@EFFECTS: construct a DBSchemaDefiner instance.
		"""
		
		pass

	def defineSchema(self, cursor):
		"""
		@MODIFIERS: the database pointed by the cursor
		@EFFECTS: define the tables as specified in the schema.
		"""
		pass




import sqlite3

from DBSchemaDefiner import *
from PATHS import *


if __name__ == "__main__":
	

	db_filename = "debug.db"
	db_filepath = os.path.join(DIR_DATA, db_filename)
	con = sqlite3.connect(db_filepath)

	schema_definer = DBSchemaDefiner()
	schema_definer.defineSchema(con)

	con.close()


	pass
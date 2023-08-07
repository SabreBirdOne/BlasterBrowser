"""
This file contains a DataBuilder, used to define the tables in the BlasterBrowsers database.
"""

import sqlite3

class DBSchemaDefiner:
	"""
	This immutable class defines tables in a database following a schema. It only creates empty tables
	
	Representation invariant: 
		self._launch_mechs and self._parts_family_info are maps, and for both:
			keys are strs
			values are strs or None

	Abstraction function:
		self._launch_mechs maps a type of launch mechanism to a description
		self._parts_family_info maps a part type to its parent part type, if it has a parent part type.

	"""
	def __init__(self):
		"""
		@EFFECTS: construct a DBSchemaDefiner instance.
		"""
		self._launch_mechs = {
			"springer": "spring-based launch mechanism. Relatively cheap and reliable parts. Great accuracy and easy to upgrade dart velocity.",
			"flywheeler": "high-speed flywheels launch mechanism. Parts are compact. Pusher mechanism allows semi or fully automatic rates of fire. Flywheels and pusher speeds may be adjustable in some builds.",
			"hpa": "high pressure air launch mechanism. Achieves high dart velocities at high rates of fire. Requires attention",
			"aeb": "automatic electric blaster launch mechanism. Very similar to a springer, and with automated priming for high rates of fire.",
			"stringer": "string-based launch mechanism. Strings are usually elastic, and parts are generally cheap."
		}
		
		self._parts_family_info = {
			"parts": None,
			"muzzles": "parts",
			"scar_muzzles": "muzzles",
			"bcar_muzzles": "muzzles",
			"tracer_muzzles": "muzzles",
			"decorative_muzzles": "muzzles",
			"launch_springs": "parts",
			"barrels": "parts",
			"spring_modifiers": "parts",
		}
		if not self._checkRep(): print("WARNING: DBSchemaDefiner._checkRep() failure")

	def _checkRep(self):
		"""
		@RETURNS: True if representation invariant holds, else False
		"""
		checked_attributes = ["_launch_mechs", "_parts_family_info"]
		for attribute in checked_attributes:
			if hasattr(self, attribute):
				interested = getattr(self, attribute)
				if not isinstance(interested, dict): 
					print("self.{} is not dict".format(attribute))
					return False
				for pair in interested.items():
					if not isinstance(pair[0], str): 
						print("self.{} key {} is not str".format(attribute, pair[0]))
						return False
					if not (isinstance(pair[1], str) or pair[1] is None): 
						return False
		return True

	def defineSchema(self, conn):
		"""
		@PARAMS: conn: a connection to a database
		@REQUIRES: conn is an SQLite3.Connection object.
		@MODIFIES: the database pointed by the connection
		@EFFECTS: define the tables as specified in the schema.
		"""
		try:
			cur = conn.cursor()
			
			conn.commit()
		except Exception as e:
			print("DBSchemaDefiner.defineSchema(): exception: {}. Rolling back...".format(e))
			conn.rollback()

		
		pass





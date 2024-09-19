"""
Elevator module
"""

import data

class Elevator:
	"""
	param: max_capacity = the maximum number of persons allowed inside the elevator
	at any given time
	"""

	current_floor: int
	max_capacity: int
	occupants: data.People

	def __init__(self, max_capacity: int = 8) -> None:
		if max_capacity < 1:
			raise ValueError("max_capacity may not 0 or less.")

		self.current_floor: int = 0
		self.max_capacity = max_capacity
		self.occupants: data.People = []

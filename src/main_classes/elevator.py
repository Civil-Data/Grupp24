"""
Elevator module
"""

import data

class Elevator:
	"""
	Elevator class
	"""

	current_floor: int
	max_capacity: int
	occupants: data.People

	def __init__(self) -> None:
		assert data.ELEVATOR_CAPACITY >= 1

		self.current_floor: int = 0
		self.max_capacity = data.ELEVATOR_CAPACITY
		self.occupants: data.People = []

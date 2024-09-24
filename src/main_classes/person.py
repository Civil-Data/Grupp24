"""
Person module
"""


class Person:
	"""
	param: start_floor = the initial floor that the person is waiting on
	param: end_floor = the floor that the person wants to go to
	"""

	start_floor: int
	end_floor: int
	has_arrived: bool
	distance_traveled: int
	distance_needed: int
	time_spent_waiting: int

	def __init__(self, start_floor: int, end_floor: int, number_of_floors: int) -> None:
		if start_floor < 0:
			raise ValueError("start_floor may not be negative.")

		if end_floor > number_of_floors - 1:
			raise ValueError(
				"end_floor may not exceed total number of floors minus one."
			)

		self.start_floor = start_floor
		self.end_floor = end_floor
		self.has_arrived = False
		self.distance_traveled: int = 0
		self.distance_needed: int = abs(start_floor - end_floor)
		self.time_spent_waiting: int = 0

	def to_json(self, number_of_floors):
		"""
		Save a person class down to a json file
		"""
		return {
			"start_floor": self.start_floor,
			"end_floor": self.end_floor,
			"floors": number_of_floors,
		}

	def to_text(self) -> None:
		"""
		asd
		"""
		print(self.start_floor)
		print(self.end_floor)
		print(self.has_arrived)

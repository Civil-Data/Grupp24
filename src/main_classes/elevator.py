# Author: Joel Scarinius Stävmo, Oskar Sundberg, Linus Savinainen, Samuel Wallander Leyonberg  and Gustav Pråmell
# Update: October 1, 2024
# Description: " "
# Version: 1.0.0
# License: Apache 2.0

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

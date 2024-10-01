# Author: Joel Scarinius Stävmo, Oskar Sundberg, Linus Savinainen, Samuel Wallander Leyonberg  and Gustav Pråmell
# Update: October 1, 2024
# Version: 1.0.0
# License: Apache 2.0

"""
Building module
"""

from main_classes.elevator import Elevator, data

class Building:
	"""
	param: people_queues = a 2D array of where people are in the building
	"""

	people_queues: data.People_queues
	elevator: Elevator

	def __init__(self, people_queues: data.People_queues) -> None:

		self.people_queues = people_queues
		self.elevator = Elevator()
		# Counts how many trips the elevator has made
		self.time_passed = 0
		# Total time spent waiting by all travelers
		self.time_spent_waiting = 0



	def move_elevator(self, previous_floor: int, arrived_floor: int) -> None:
		"""
		Do stuff when the elevator has traveled up or down
		"""
		if not 0 <= arrived_floor < data.NUMBER_OF_FLOORS:
			raise ValueError("arrived_floor out of bounds")

		if not 0 <= previous_floor < data.NUMBER_OF_FLOORS:
			raise ValueError("previous_floor out of bounds")

		self.elevator.current_floor = arrived_floor
		# Increments the number of trips
		self.time_passed += abs(self.elevator.current_floor - previous_floor)

		to_remove: data.People = []
		for person in self.elevator.occupants:
			# All occupants have traveled a certain distance
			person.distance_traveled += abs(self.elevator.current_floor - previous_floor)
			if self.elevator.current_floor == person.end_floor:
				# If anyone has arrived at their destination, remove them from elevator
				person.has_arrived = True
				# The time the person has been waiting is the same as the time from the start until they have arrived
				person.time_spent_waiting += self.time_passed
				# Collect
				to_remove.append(person)

		for person in to_remove:
			self.elevator.occupants.remove(person)

		to_remove.clear()

		# Loop over all people waiting for the elevator at the current floor
		for person in self.people_queues[self.elevator.current_floor]:
			# If there is any availabe room in the elevator, load up on more people
			if len(self.elevator.occupants) < self.elevator.max_capacity:
				# Make sure there's no shenanigans going on
				assert person.start_floor == self.elevator.current_floor
				# Load person on to elevator
				self.elevator.occupants.append(person)
				# Collect
				to_remove.append(person)
			else:
				break

		for person in to_remove:
			self.people_queues[self.elevator.current_floor].remove(person)

	# def to_text(self):
	# 	for people in self.people_queues:
	# 		for person in people:
	# 			print("*****")
	# 			person.to_text()

"""
Function to created random generation of genomes
Saved to text file for now. For multiple testing purposes.
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

import json
import random
import data
from main_classes.person import Person


# Number of genomes in generation
NUMBER_OF_GNEOMES = 100
# Length range on genomes
GENOME_RANGE_START = 22
GENOME_RANGE_END = 24
# numbers of floors
FLOORS = 15
# How many people can be slotted on one floor start range
FLOOR_LENGTH_START = 0
# How many people can be slotted on one floor end range
FLOOR_LENGTH_END = 4


def create_random_generation(
	number_of_gnomes,
	range_start,
	range_end,
	number_of_floors,
	filename=f"Generation_{FLOORS}_{NUMBER_OF_GNEOMES}_{GENOME_RANGE_START}_{GENOME_RANGE_END}.json",
) -> data.Population:
	"""
	Creates json file with set number of generations
	"""

	population_list: data.Population = []

	for _ in range(number_of_gnomes):
		k = random.randint(range_start, range_end)

		# set start to floor 0
		genome_list: data.Genome = []

		# Ensure not the same floor two times in a row
		for _ in range(k):
			next_num = random.choice(range(number_of_floors))
			while len(genome_list) > 1 and next_num == genome_list[-1]:
				next_num = random.choice(range(number_of_floors))

			genome_list.append(next_num)

		population_list.append(genome_list)

		with open(filename, "w", encoding="UTF-8") as file:
			json.dump(population_list, file, indent=4)
	# To ensure success
	return population_list


def create_random_building(
	number_of_floor,
	floor_queue_length_start,
	floor_queue_length_end,
	filename=f"Building_{FLOORS}_{FLOOR_LENGTH_START}_{FLOOR_LENGTH_END}.json",
) -> data.People:
	"""
	Create a building from set parameters
	"""
	building_list: data.People = []

	for i in range(number_of_floor):

		k = random.randint(floor_queue_length_start, floor_queue_length_end)

		for _ in range(k):

			end_floor = random.choice(range(number_of_floor))

			while i == end_floor:
				end_floor = random.choice(range(number_of_floor))

			building_list.append(Person(i, end_floor, FLOORS))

	with open(filename, "w", encoding="UTF-8") as file:
		json.dump(
			[person.to_json(FLOORS) for person in building_list],
			file,
			indent=4,
		)


create_random_generation(NUMBER_OF_GNEOMES, GENOME_RANGE_START, GENOME_RANGE_END, FLOORS)
print(
	f"List of {NUMBER_OF_GNEOMES} generations has been created check file for results!"
)

create_random_building(FLOORS, FLOOR_LENGTH_START, FLOOR_LENGTH_END)
print(
	f"Building of {FLOORS} floors has been created check file for results!"
)

"""
Function to created random generation of genomes
Saved to text file for now. For multiple testing purposes.
"""

import sys
import os
from typing import List

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

import json
import random
import data
from main_classes.person import Person

# All configuration variables are handled from data.py

# How many people can be slotted on one floor start range
FLOOR_LENGTH_START = 1
# How many people can be slotted on one floor end range
FLOOR_LENGTH_END = 1

def create_random_generation(
	number_of_gnomes,
	range_start,
	range_end,
	number_of_floors,
	filename=f"./generations/Generation_{data.NUMBER_OF_FLOORS}_{data.POPULATION_SIZE}_{GENOME_RANGE_START}_{GENOME_RANGE_END}.json",
) -> data.Population:
	"""
	Creates json file with set number of generations
	"""

	population: data.Population = []

	for _ in range(number_of_gnomes):
		k = random.randint(range_start, range_end)

		# set start to floor 0
		genome_list: List[int] = []

		# Ensure not the same floor two times in a row
		for _ in range(k):
			next_num = random.choice(range(number_of_floors))

			while len(genome_list) > 1 and next_num == genome_list[-1]:
				next_num = random.choice(range(number_of_floors))

			genome.append(next_num)

		population.append(genome)

		with open(filename, "w", encoding="UTF-8") as file:
			json.dump(population, file, indent=4)
	# To ensure success
	return population

def create_even_building(
	filename=f"./buildings/Building_{data.NUMBER_OF_FLOORS}_{FLOOR_LENGTH_START}_{FLOOR_LENGTH_END}.json",
) -> data.People:
	"""
	Create a building from set parameters with people evenly distributed among the building's floors
	"""
	# Check that the people can be evenly distributed
	assert data.NUMBER_OF_PEOPLE % data.NUMBER_OF_FLOORS == 0
	# assert data.NUMBER_OF_FLOORS * data.EXP_FLOOR_LENGTH == data.NUMBER_OF_PEOPLE
	
	building_list: data.People = []

	for i in range(data.NUMBER_OF_FLOORS):
		k = random.randint(FLOOR_LENGTH_START, FLOOR_LENGTH_END)
		for _ in range(k):
			end_floor = random.choice(range(data.NUMBER_OF_FLOORS))

			while i == end_floor:
				end_floor = random.choice(range(data.NUMBER_OF_FLOORS))

			building_list.append(Person(i, end_floor, data.NUMBER_OF_FLOORS))

	with open(filename, "w", encoding="UTF-8") as file:
		json.dump(
			[person.to_json(data.NUMBER_OF_FLOORS) for person in building_list],
			file,
			indent=4,
		)


def create_random_building(
    filename=f"./buildings/Building_{data.NUMBER_OF_FLOORS}_{data.EXP_FLOOR_LENGTH}.json",
) -> data.People:
    """
    Create a building from set parameters with people randomly distributed among the building's floors
    """
    building_list: data.People = []

    # create random Person objects
    for _ in range(data.NUMBER_OF_PEOPLE):
        start_floor, end_floor = random.sample(range(data.NUMBER_OF_FLOORS), 2) # 2 unique floors
        building_list.append(Person(start_floor, end_floor, data.NUMBER_OF_FLOORS))

    with open(filename, "w", encoding="UTF-8") as file:
        json.dump(
            [person.to_json(data.NUMBER_OF_FLOORS) for person in building_list],
            file,
            indent=4,
        )

    return building_list


create_random_generation(data.POPULATION_SIZE, data.EXP_RANGE_START, data.EXP_RANGE_END, data.NUMBER_OF_FLOORS)

if data.EXP_RANDOM_BUILDING:
	create_random_building()
else:
	create_even_building()

print(
	f"List of {data.POPULATION_SIZE} generations has been created check file for results!"
)

create_random_building(FLOORS, FLOOR_LENGTH_START, FLOOR_LENGTH_END)
print(
	f"Building of {FLOORS} floors has been created check file for results!"
)

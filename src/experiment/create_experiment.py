# Author: Joel Scarinius Stävmo, Oskar Sundberg, Linus Savinainen, Samuel Wallander Leyonberg  and Gustav Pråmell
# Update: October 1, 2024
# Description: " "
# Version: 1.0.0
# License: Apache 2.0

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

def create_random_generation(
	filename=f"./generations/Generation_{data.NUMBER_OF_FLOORS}_{data.POPULATION_SIZE}_{data.EXP_GENOME_RANGE_START}_{data.EXP_GENOME_RANGE_END}.json",
	) -> None:
	"""
	Creates json file with set number of generations
	"""

	population: data.Population = []

	for _ in range(data.POPULATION_SIZE):
		k = random.randint(data.EXP_GENOME_RANGE_START, data.EXP_GENOME_RANGE_END)

		# set start to floor 0
		genome_list: List[int] = []

		# Ensure not the same floor two times in a row
		for _ in range(k):
			next_num = random.choice(range(data.NUMBER_OF_FLOORS))

			while len(genome_list) > 1 and next_num == genome_list[-1]:
				next_num = random.choice(range(data.NUMBER_OF_FLOORS))

			genome_list.append(next_num)

		population.append(genome_list)

		with open(filename, "w", encoding="UTF-8") as file:
			json.dump(population, file, indent=4)


def create_building(
	filename=f"./buildings/Building_{data.NUMBER_OF_FLOORS}_{data.NUMBER_OF_PEOPLE}_{data.EXP_FLOOR_LENGTH_START}_{data.EXP_FLOOR_LENGTH_END}.json",
	) -> None:
	"""
	Create a building from set parameters with number of people according to FLOOR_LENGTH ranges
	"""
	assert data.EXP_FLOOR_LENGTH_START <= data.EXP_FLOOR_LENGTH_END
	assert data.NUMBER_OF_FLOORS * data.EXP_FLOOR_LENGTH_START <= data.NUMBER_OF_PEOPLE <= data.NUMBER_OF_FLOORS * data.EXP_FLOOR_LENGTH_END

	building_list: data.People = []

	numb_of_ppl_on_floor: List[int] = [data.EXP_FLOOR_LENGTH_START] * data.NUMBER_OF_FLOORS
	remaining_people: int = data.NUMBER_OF_PEOPLE - (data.EXP_FLOOR_LENGTH_START * data.NUMBER_OF_FLOORS)

	# Randomly distribute the remaining people, with respect to the floor limits
	while remaining_people > 0:
		for floor in range(data.NUMBER_OF_FLOORS):
			if remaining_people == 0:
				break

			if random.choice([0, 1]) == 0: # 50% chance
				numb_of_ppl_on_floor[floor] += 1
				remaining_people -= 1
				assert remaining_people >= 0

	assert remaining_people == 0
	assert sum(numb_of_ppl_on_floor) == data.NUMBER_OF_PEOPLE

	# Create people based on the above calculation
	for floor in range(data.NUMBER_OF_FLOORS):
		for _ in range(numb_of_ppl_on_floor[floor]):
			ef: int = random.randint(0, data.NUMBER_OF_FLOORS - 1)
			while ef == floor:
				ef = random.randint(0, data.NUMBER_OF_FLOORS - 1)
			building_list.append(Person(floor, ef, data.NUMBER_OF_FLOORS))

	assert len(building_list) == data.NUMBER_OF_PEOPLE

	for floor in numb_of_ppl_on_floor:
		assert data.EXP_FLOOR_LENGTH_START <= floor <= data.EXP_FLOOR_LENGTH_END

	with open(filename, "w", encoding="UTF-8") as file:
		json.dump(
			[person.to_json(data.NUMBER_OF_FLOORS) for person in building_list],
			file,
			indent=4,
		)

assert data.NUMBER_OF_FLOORS >= 2
create_random_generation()
create_building()

print(
	f"List of {data.POPULATION_SIZE} generations has been created check file for results!"
)

print(
	f"Building of {data.NUMBER_OF_FLOORS} floors has been created check file for results!"
)

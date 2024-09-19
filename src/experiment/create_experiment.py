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
number_of_genomes = 100
# Length range on genomes
range_start = 2
range_end = 12
# numbers of floors
floors = 6
# How many people can be slotted on one floor
floor_length = 100


def create_random_generation(
    number_of_genomes,
    range_start,
    range_end,
    number_of_floors,
    filename=f"Generation_{floors}_{number_of_genomes}.json",
) -> data.Population:

    population_list: data.Population = []

    for _ in range(number_of_genomes):
        k = random.randint(range_start, range_end)

        # set start to floor 0
        genome_list: data.Genome = [0]
        # used if first number doesn't need to be 0
        # genome_list = [random.choice(range(m + 1))]

        # Ensure not the same floor two times in a row
        for _ in range(k - 1):
            next_num = random.choice(range(number_of_floors))
            while next_num == genome_list[-1]:
                next_num = random.choice(range(number_of_floors))

            genome_list.append(next_num)

        population_list.append(genome_list)

        with open(filename, "w") as file:
            json.dump(population_list, file, indent=4)
    # To ensure success
    return population_list


def create_random_building(
    number_of_floor,
    floor_queue_length,
    filename=f"Building_{floors}_{floor_length}.json",
) -> data.People:
    building_list: data.People = []

    for i in range(number_of_floor):

        for _ in range(floor_queue_length):

            end_floor = random.choice(range(number_of_floor))

            while i == end_floor:
                end_floor = random.choice(range(number_of_floor))

            building_list.append(Person(i, end_floor))

    with open(filename, "w") as file:
        json.dump(
            [person.to_json() for person in building_list],
            file,
            indent=4,
        )


create_random_generation(number_of_genomes, range_start, range_end, floors)
# create_random_building(floors, floor_length)

print(
    f"List of {number_of_genomes} generations has been created check file for results!"
)

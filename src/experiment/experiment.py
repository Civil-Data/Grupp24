"""
Experiment module
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

import json
import matplotlib.pyplot as plt
import data

from main_classes.person import Person
from genome import Genome


class ExperimentElevator:
	"""
	param: path to people list json file
	param: path to generation list json file
	"""

	def __init__(self, people: data.People, generation: data.Population) -> None:
		self.people_list: data.People = people
		self.generation_list: data.Population = generation

	def display_experiment(self, name, results) -> None:
		"""
		Plots a graph of best for of every generation
		"""
		generation = [res[0] for res in results]
		fitness_score = [res[1] for res in results]
		genome_length = [res[2] for res in results]
		# plt.xscale("log") # log scaling on axis
		plt.yscale("log")
		plt.plot(generation, fitness_score, label="Fitness Score", color="blue")
		plt.plot(generation, genome_length, label="Genome Length", color="green")
		plt.title(f"Experiment : {name}")
		plt.xlabel("Generation")
		plt.ylabel("Value")
		plt.legend()
		# Show experiment graph after every run
		# plt.show()


def load_population(filename) -> data.Population:
	"""
	Loading in data from a json file for list of genomes
	"""
	with open(filename, "r", encoding="UTF-8") as file:
		pouplation_data = json.load(file)

	genome_list = [Genome(genome_data) for genome_data in pouplation_data]

	return genome_list


def load_building(filename) -> data.People:
	"""
	Loading in data from json file for a list of people
	"""
	with open(filename, "r", encoding="UTF-8") as file:
		people_data = json.load(file)

	people_list = [
		Person(
			start_floor=person_data["start_floor"],
			end_floor=person_data["end_floor"],
			number_of_floors=person_data["floors"],
		)
		for person_data in people_data
	]

	return people_list

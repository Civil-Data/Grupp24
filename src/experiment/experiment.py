# Author: Joel Scarinius Stävmo, Oskar Sundberg, Linus Savinainen, Samuel Wallander Leyonberg  and Gustav Pråmell
# Update: October 1, 2024
# Description: " "
# Version: 1.0.0
# License: Apache 2.0

"""
Experiment module
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

import json
from matplotlib import pyplot
import pandas as pf
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
		generation = [res['Generation'] for res in results]
		fitness_score = [res['Best Fitness'] for res in results]
		best_genome = [res['Best Genome'] for res in results]
		genome_length = [res['Genome Length'] for res in results]
		# time_score = [res['Time Score'] for res in results]
    # pyplot.xscale("log") # log scaling on axis
		pyplot.yscale("log")
		pyplot.plot(generation, fitness_score, label="Fitness Score", color="blue")
		pyplot.plot(generation, genome_length, label="Genome Length", color="green")
		# pyplot.plot(generation, time_score, label="Time Score", color="red")
		pyplot.title(f"Experiment : {name}")
		pyplot.xlabel("Generation")
		pyplot.ylabel("Value")
		pyplot.legend()
		# Show experiment graph after every run
		pyplot.show()

def save_experiment(result: list) -> None:
	"""
	Saves experiment results to csv file
	"""
	data_frame = pf.DataFrame(result)
	data_frame.to_csv("test_results.csv")
	print("Results saved to csv file")


def load_population(filename) -> data.Population:
	"""
	Loading in data from a json file for list of genomes
	"""
	with open(filename, "r", encoding="UTF-8") as file:
		population_data = json.load(file)

	genome_list = [Genome(genome_data) for genome_data in population_data]

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

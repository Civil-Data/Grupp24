"""
Experiment module
"""

import sys
import os

from matplotlib.ticker import ScalarFormatter
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

import json
import matplotlib
matplotlib.use('Agg')  # or 'TkAgg' if you installed Tkinter
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

	def display_experiment(self, name, results_f, results_s, results_t) -> None:
		"""
		Plots a graph of best for of every generation
		"""
		base_file_path = f"./exp_done/{name}.png"

		if os.path.isfile(base_file_path):
			counter = 1
			new_file_path = f"./exp_done/{name}_{counter}.png"
			while os.path.isfile(new_file_path):
				counter += 1
				new_file_path = f"./exp_done/{name}_{counter}.png"
			file_path = new_file_path
		else:
			file_path = base_file_path

		generation_f = [res['Generation'] for res in results_f]
		fitness_score_f = [res['Best Fitness'] for res in results_f]
		generation_s = [res['Generation'] for res in results_s]
		fitness_score_s = [res['Best Fitness'] for res in results_s]
		generation_t = [res['Generation'] for res in results_t]
		fitness_score_t = [res['Best Fitness'] for res in results_t]

		#Plotting data
		pyplot.plot(generation_f, fitness_score_f, label="Fitness Score Swap", color="blue", linewidth=2)
		pyplot.plot(generation_s, fitness_score_s, label="Fitness Score Heuristic Single", color="red", linewidth=2)
		pyplot.plot(generation_t, fitness_score_t, label="Fitness Score Heuristic Sequence", color="orange", linewidth=2)

		#Labels and title
		pyplot.title(f"Experiment : {name}", fontsize=8)
		pyplot.xlabel("Generation", fontsize=14)
		pyplot.ylabel("Fitness Score", fontsize=14)
		
		xticks = np.arange(0, (data.GENERATION_LIMIT + 100), (data.GENERATION_LIMIT//10))
		pyplot.xticks(xticks, fontsize=12)
		pyplot.xlim(-30, data.GENERATION_LIMIT)
		pyplot.yticks(fontsize=12)

		ax = pyplot.gca()
		ax.yaxis.set_major_formatter(ScalarFormatter())
		ax.yaxis.get_major_formatter().set_scientific(False)

		pyplot.legend(fontsize=12)

		#Save file and clear
		pyplot.tight_layout()
		pyplot.savefig(file_path, dpi=300)
		pyplot.clf()

def save_experiment(name:str ,result: list) -> None:
	"""
	Saves experiment results to csv file
	"""
	base_file_path = f"./exp_done/{name}.csv"

	if os.path.isfile(base_file_path):
		counter = 1
		new_file_path = f"./exp_done/{name}_{counter}.csv"
		while os.path.isfile(new_file_path):
			counter += 1
			new_file_path = f"./exp_done/{name}_{counter}.csv"
		file_path = new_file_path
	else:
		file_path = base_file_path
	
	for experiment_name, crossover_name, genome in result:
		result_data = {
				'Name': [experiment_name],
				'Crossover Name': [crossover_name],
				'Arrvied': [f"{genome.how_many_arrived()}/{data.NUMBER_OF_PEOPLE}"],
				'Best Fitness': [genome.fitness_score],
				'Best Genome': [genome.genome],
				'Genome Length': [len(genome.genome)]
			}
		
		data_frame = pf.DataFrame(result_data)
	
		if not os.path.isfile(file_path):
			data_frame.to_csv(file_path, mode='w', header=True, index=False)
		else:
			data_frame.to_csv(file_path, mode='a', header=False, index=False)
	print("Results saved to csv file")


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

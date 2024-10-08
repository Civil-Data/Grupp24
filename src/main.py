# Author: Joel Scarinius Stävmo, Oskar Sundberg, Linus Savinainen, Samuel Wallander Leyonberg  and Gustav Pråmell
# Update: October 1, 2024
# Version: 1.0.0
# License: Apache 2.0

" Main program module "

from typing import List, Tuple
import random
import math
import os
from itertools import product
import copy
from matplotlib import use, pyplot
import data
from tqdm import tqdm

from evolutionary_classes.fitness import Fitness
from evolutionary_classes.populate import Populate
from evolutionary_classes.selection import Selection
from evolutionary_classes.crossover import Crossover
from evolutionary_classes.mutation import Mutation
from chromosome import Chromosome
from main_classes.building import Building
from experiment.experiment import ExperimentElevator, load_building, load_population, save_experiment
from gui.elevator_simulation import run_simulation
from init_and_place_people import place_people, CONST_PEOPLE_LIST

def run_evolution(
	populate_function: data.PopulateFunction,
	fitness_function: data.FitnessFunction,
	selection_function: data.SelectionFunction,
	crossover_function: data.CrossoverFunction,
	mutation_functions: List[data.MutationFunction],
	experiment: ExperimentElevator = None,
):
	"""
	Run the evolution
	"""

	# Get an initial population
	if data.DO_EXP:
		assert experiment is not None
		population: data.Population = experiment.generation_list
	else:
		assert experiment is None
		population: data.Population = populate_function()

	result_data = []

	# Loop over the generations
	for generation in tqdm(range(data.GENERATION_LIMIT), 
							desc="Generations", 
							initial=1, 
							bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]",
							ncols=100,
							ascii=True,
							colour="green"):
		# Loop over the genomes
		for chromosome in population:
			# Always reset to original state between the chromosome iterations
			people_list: data.People = None
			if data.DO_EXP:
				people_list = copy.deepcopy(experiment.people_list)
			else:
				people_list = copy.deepcopy(CONST_PEOPLE_LIST)
				
			building: Building = Building(place_people(people_list))
			chromosome.people = people_list

			# Loop over the floors
			for floor in chromosome.chromosome:
				building.move_elevator(building.elevator.current_floor, floor)

		# All genomes has been run. Prepare the next population of genomes

		# Calculate fitness for each chromosome
		for chromosome in population:
			fitness_function(chromosome)

		# Sort the genomes based on the fitness
		ranked_population: data.Population = sorted(
			population,  # The population to be sorted
			key=lambda chromosome: chromosome.fitness_score,  # Sort based on fitness score
			reverse=False,  # Lowest score first
		)


		result_data_temp = {
			'Generation': generation,
			'Best Fitness': ranked_population[0].fitness_score,
			'Best Chromosome': ranked_population[0].chromosome,
			'Chromosome Length': len(ranked_population[0].chromosome)#,
			# 'Time Score': ranked_population[0].time_score,
		}
		result_data.append(result_data_temp)

		# If the last generation has been ranked, break off since there's no need to calculate another population
		if generation == data.GENERATION_LIMIT - 1:
			break

		next_population: data.Population = []

		# Elitism
		if data.ELITISM_PERC > 0.0:
			# not necessary to check data.ELITISM_PERC, but it looks nicer and saves some time
			numb_elitism_parents: int = math.floor(
				data.POPULATION_SIZE * data.ELITISM_PERC
			)
			# If odd, increase by 1
			if numb_elitism_parents % 2 == 1:
				numb_elitism_parents += 1
			# If that +1 pushes it over the population size
			if numb_elitism_parents > data.POPULATION_SIZE:
				numb_elitism_parents = data.POPULATION_SIZE

			assert 0 <= numb_elitism_parents <= data.POPULATION_SIZE
			assert numb_elitism_parents % 2 == 0

			if numb_elitism_parents > 0:  # <==> numb_elitism_parents >= 2
				for i in range(numb_elitism_parents):
					next_population.append(ranked_population[i])

		while len(next_population) < data.POPULATION_SIZE:
			# Only deal with even populations for now
			assert data.POPULATION_SIZE % 2 == 0

			# Select two parents
			parents: Tuple[Chromosome, Chromosome] = selection_function(ranked_population)
			# Breed two children from those parents with a chance for crossover
			children: Tuple[Chromosome, Chromosome]
			if data.CROSSOVER_CHANCE > random.uniform(0.0, 1.0):
				children = crossover_function(parents[0], parents[1])
			else:
				children = parents

			# A chance to individually apply a random mutation to the children
			for child in children:
				if data.MUTATION_CHANCE > random.uniform(0.0, 1.0):
					mutation_functions[random.randint(0, len(mutation_functions) - 1)](
						child
					)

			# Add the children to the next generation
			next_population += children

		assert len(next_population) == data.POPULATION_SIZE

		# Update the population
		population = next_population

	print(
	f"Top three genomes (arrived/total, fitness, length):   "
	f"({ranked_population[0].how_many_arrived()}/{data.NUMBER_OF_PEOPLE}, {ranked_population[0].fitness_score}, {len(ranked_population[0].chromosome)}) "
	f"({ranked_population[1].how_many_arrived()}/{data.NUMBER_OF_PEOPLE}, {ranked_population[1].fitness_score}, {len(ranked_population[1].chromosome)}) "
	f"({ranked_population[2].how_many_arrived()}/{data.NUMBER_OF_PEOPLE}, {ranked_population[2].fitness_score}, {len(ranked_population[2].chromosome)})"
	)
	print(f"Best Chromosome:\n{ranked_population[0].chromosome}")
	print(
		"Press 'y' to run simulation for best chromosome or any other key to exit"
	)
	if input() == "y":
		run_simulation(ranked_population[0])

	return result_data, ranked_population[0], str(crossover_function.__name__)

def run_experiments(people_folder_path, generation_folder_path) -> List:
	"""
	Running evoultion on specific experiments
	"""
	# Getting all files in experiment folders
	people_experiment = [files for files in os.listdir(people_folder_path)]
	generation_experiment = [files for files in os.listdir(generation_folder_path)]


	if (len(people_experiment) == 0 and len(generation_experiment) == 0):
		print("No experiment found!")
		return []
	elif (len(people_experiment) == 0 and len(generation_experiment) != 0) or (len(people_experiment) != 0 and len(generation_experiment) == 0):
		print("Mismatch between people_experiment and generation_experiment: One is empty while the other is not.")
		return []
 

	# Running through all different combinations of experiments
	# *********************************************************************************************
	# TODO: if there are different lengths/sizes of buildings and generations or something, it craches at
	#		place_people() with error index out of bounds at matrix[person.start_floor].append(person)
	# *********************************************************************************************
	for people_experiment, generation_experiment in product(
		people_experiment, generation_experiment
	):
		people_file_path = os.path.join(
			people_folder_path, people_experiment)
		generation_file_path = os.path.join(
			generation_folder_path, generation_experiment
		)

		people_data = load_building(people_file_path)
		generation_data = load_population(generation_file_path)

		csv_results = []

		experiment_name = (
			f"Floors: {data.NUMBER_OF_FLOORS}, People: {data.NUMBER_OF_PEOPLE}, Generation: {data.GENERATION_LIMIT}"
		)
		current_experiment = ExperimentElevator(people_data, generation_data, experiment_name)
		
		file_name = (f"Floors_{data.NUMBER_OF_FLOORS}_People_{data.NUMBER_OF_PEOPLE}_Generation_{data.GENERATION_LIMIT}")	
		
		results_f, best_results, crossover_name = run(current_experiment)
		csv_results.append((experiment_name, crossover_name, best_results))
		results_s, best_results, crossover_name = run(current_experiment, Crossover.heuristic_crossover_single_gene)
		csv_results.append((experiment_name, crossover_name, best_results))
		results_t, best_results, crossover_name = run(current_experiment, Crossover.heuristic_crossover_sequence_of_genes)
		csv_results.append((experiment_name, crossover_name, best_results))

		current_experiment.display_experiment(file_name, results_f, results_s, results_t)
		save_experiment(file_name ,csv_results)

	return csv_results

def run(exp: ExperimentElevator = None, current_crossover: Crossover = Crossover.swap_last_halves):
	return run_evolution(
			populate_function=Populate.generate_population,
			fitness_function=Fitness.calc_fitness,
			selection_function=Selection.rank,
			crossover_function=current_crossover,
			mutation_functions=[Mutation.swap,
								Mutation.increase_genome_length,
								Mutation.decrease_genome_length],
			experiment=exp
		)

if __name__ == "__main__":
	if data.DO_EXP:
		try:
			use("Qt5Agg")
		except:
			print("Failed to use Qt5Agg PyPlot backend, will use Agg instead")
			use("Agg")
		for i in range(data.NUMBER_OF_EXP):
			run_experiments("./buildings", "./generations")
	else:
		run()

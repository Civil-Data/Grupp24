# Author: Joel Scarinius Stävmo, Oskar Sundberg, Linus Savinainen, Samuel Wallander Leyonberg  and Gustav Pråmell
# Update: October 1, 2024
# Version: 1.0.0
# License: Apache 2.0

"""
Module containing static crossover function(s)
"""
from typing import Tuple
import random
from chromosome import Chromosome
import data

class Crossover:
	"""
	Class containing static crossover function(s)
	"""

	@staticmethod
	def swap_last_halves(parent_1: Chromosome, parent_2: Chromosome) -> Tuple[Chromosome, Chromosome]:
		"""
		Swap the last halves of the parents' genomes.
		If the genomes are of different length, swap with respect to the shorter parent's length.
		"""

		# The parents' genomes may be of different length
		genes_to_swap: int = min(len(parent_1.chromosome), len(parent_2.chromosome)) // 2

		# "take all elements from the start of the list up to (but not including) index genes_to_swap"
		# +
		# "take all elements starting from the index that is genes_to_swap elements to the end of the list"
		offspring_1: Chromosome = Chromosome(parent_1.chromosome[:genes_to_swap] +
									 parent_2.chromosome[genes_to_swap:])
		offspring_2: Chromosome = Chromosome(parent_2.chromosome[:genes_to_swap] +
									 parent_1.chromosome[genes_to_swap:])

		return offspring_1, offspring_2

	@staticmethod
	def heuristic_crossover_single_gene(parent_1: Chromosome, parent_2: Chromosome) -> Tuple[Chromosome, Chromosome]:
		"""
		Creates two offsprings from two parents where the parent with better (lower) fitness score has more of its
		genes represented in the chromosome for each child.
		"""

		# Make sure that parent_1 has a worse score than parent_2
		if parent_1.fitness_score < parent_2.fitness_score:
			parent_1, parent_2 = parent_2, parent_1

		# Calculating the parents' weighted differences in percentage
		total_fitness = parent_1.fitness_score + parent_2.fitness_score

		if total_fitness != 0:
			weight_parent_2 = parent_1.fitness_score / total_fitness
			weight_parent_1 = 1 - weight_parent_2
		else:
			weight_parent_2 = 0.5
			weight_parent_1 = 0.5

		offspring_1_genes = []
		offspring_2_genes = []

		# Based on randomness with favor for parent_2, append and insert genes into the offspring
		for i, gene in enumerate(parent_2.chromosome):
			if random.random() < weight_parent_1:
				offspring_1_genes.append(gene)
				offspring_2_genes.insert(0, gene)
			else:
				if len(parent_1.chromosome) > i:
					offspring_1_genes.append(parent_1.chromosome[i])
					offspring_2_genes.insert(0, parent_1.chromosome[i])
				else:
					offspring_1_genes.append(gene)
					offspring_2_genes.insert(0, gene)

		offspring_1 = Chromosome(offspring_1_genes)
		offspring_2 = Chromosome(offspring_2_genes)

		return offspring_1, offspring_2

	@staticmethod
	def heuristic_crossover_sequence_of_genes(parent_1: Chromosome, parent_2: Chromosome) -> Tuple[Chromosome, Chromosome]:
		"""
		Creates two offsprings from two parents where the parent with better (lower) fitness score has more of its
		genes represented in the chromosome for each child.
		"""

		# Make sure that parent_1 has a worse score than parent_2
		if parent_1.fitness_score < parent_2.fitness_score:
			parent_1, parent_2 = parent_2, parent_1

		# Calculating the parents' weighted differences in percentage
		total_fitness = parent_1.fitness_score + parent_2.fitness_score

		if total_fitness != 0:
			weight_parent_2 = parent_1.fitness_score / total_fitness
		else:
			weight_parent_2 = 0.5

		offset_parent_2 = int(len(parent_2.chromosome) * weight_parent_2)
		offset_parent_1 = int(len(parent_2.chromosome)) - offset_parent_2 -1

		offspring_1: Chromosome = Chromosome(parent_1.chromosome[:offset_parent_1] +
									 parent_2.chromosome[offset_parent_2:])
		offspring_2: Chromosome = Chromosome(parent_2.chromosome[:offset_parent_2] +
									 parent_1.chromosome[offset_parent_1:])

		if len(offspring_1.chromosome) < 3:
			offspring_1.chromosome.append(random.randint(0, data.NUMBER_OF_FLOORS -1))

		if len(offspring_2.chromosome) < 3:
			offspring_2.chromosome.append(random.randint(0, data.NUMBER_OF_FLOORS -1))

		return offspring_1, offspring_2

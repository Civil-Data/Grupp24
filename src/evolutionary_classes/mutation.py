# Author: Joel Scarinius Stävmo, Oskar Sundberg, Linus Savinainen, Samuel Wallander Leyonberg  and Gustav Pråmell
# Update: October 1, 2024
# Version: 1.0.0
# License: Apache 2.0

"""
Module containing static mutation function(s)
"""

import random
import data
from chromosome import Chromosome


class Mutation:
	"""
	Class containing static mutation function(s)
	"""

	@staticmethod
	def swap(chromosome: Chromosome) -> None:
		"""
		Swap to randomly chosen indices.
		"""
		genome_len: int = len(chromosome.chromosome)

		ix_1: int = random.randint(0, genome_len - 1)
		ix_2: int = random.randint(0, genome_len - 1)
		while ix_2 == ix_1:
			ix_2 = random.randint(0, genome_len - 1)

		temp: int = chromosome.chromosome[ix_1]
		chromosome.chromosome[ix_1] = chromosome.chromosome[ix_2]
		chromosome.chromosome[ix_2] = temp

	@staticmethod
	def increase_genome_length(chromosome: Chromosome) -> None:
		"""
		Append a random floor at the end of the chromosome.
		"""
		chromosome.chromosome.append(random.randint(0, data.NUMBER_OF_FLOORS - 1))

	@staticmethod
	def decrease_genome_length(chromosome: Chromosome) -> None:
		"""
		Remove a randomly chosen index.
		"""
		# Ensure that the chromosome length is at least 2 to be able to run the simulation.
		if len(chromosome.chromosome) > 2:
			chromosome.chromosome.pop(random.randint(0, len(chromosome.chromosome) - 1))

	@staticmethod
	def swap_and_inc(chromosome: Chromosome) -> None:
		"""
		Do swap and increase length.
		"""
		Mutation.swap(chromosome)
		Mutation.increase_genome_length(chromosome)

	@staticmethod
	def swap_and_dec(chromosome: Chromosome) -> None:
		"""
		Do swap and decrease length.
		"""
		Mutation.swap(chromosome)
		Mutation.decrease_genome_length(chromosome)

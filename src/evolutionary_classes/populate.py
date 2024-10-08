# Author: Joel Scarinius Stävmo, Oskar Sundberg, Linus Savinainen, Samuel Wallander Leyonberg  and Gustav Pråmell
# Update: October 1, 2024
# Version: 1.0.0
# License: Apache 2.0

"""
Module containing static population generating function(s)
"""

import random
import data
from chromosome import Chromosome

class Populate:
	"""
	Class containing static population generating function(s)
	"""
	@staticmethod
	def generate_population() -> data.Population:
		"""
		Generate a population of random Genomes
		"""

		population: data.Population = []
		for _ in range(data.POPULATION_SIZE):
			population.append(Chromosome([random.randint(0, data.NUMBER_OF_FLOORS - 1) for _ in range(data.GENOME_LENGTH)]))
		return population

# Author: Joel Scarinius Stävmo, Oskar Sundberg, Linus Savinainen, Samuel Wallander Leyonberg  and Gustav Pråmell
# Update: October 1, 2024
# Version: 1.0.0
# License: Apache 2.0

"""
Module containing static fitness function(s)
"""

from chromosome import Chromosome
from data import TIME_PENALTY

class Fitness:
	"""
	Function(s) that calculates fitness of a Chromosome
	"""
	@staticmethod
	def calc_fitness(chromosome: Chromosome) -> None:
		"""
		Calculate the fitness score of a chromosome
		"""
		accumulated_score: int = 0

		for person in chromosome.people:
			accumulated_score += person.time_spent_waiting

			if person.has_arrived:
				# Punish excess travel
				# distance_travel - distance_needed is the excess distance
				accumulated_score += person.distance_traveled - person.distance_needed
			else:
				accumulated_score += TIME_PENALTY

		accumulated_score += len(chromosome.chromosome)

		chromosome.fitness_score = accumulated_score

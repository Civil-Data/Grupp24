"""
Module containing static fitness function(s)
"""

from genome import Genome
from data import TIME_PENALTY

class Fitness:
	"""
	Function(s) that calculates fitness of a Genome
	"""
	@staticmethod
	def calc_fitness(genome: Genome) -> None:
		"""
		Calculate the fitness score of a genome
		"""
		accumulated_score: int = 0

		for person in genome.people:
			accumulated_score += person.time_spent_waiting

			if person.has_arrived:
				accumulated_score += person.distance_traveled - person.distance_needed
			else:
				accumulated_score += TIME_PENALTY

		accumulated_score += len(genome.genome)

		genome.fitness_score = accumulated_score

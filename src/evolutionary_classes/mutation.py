"""
Module containing static mutation function(s)
"""

import random
import data
from genome import Genome


class Mutation:
	"""
	Class containing static mutation function(s)
	"""

	@staticmethod
	def swap(genome: Genome) -> None:
		"""
		Swap to randomly chosen indices.
		"""
		genome_len: int = len(genome.genome)

		ix_1: int = random.randint(0, genome_len - 1)
		ix_2: int = random.randint(0, genome_len - 1)
		while ix_2 == ix_1:
			ix_2 = random.randint(0, genome_len - 1)

		temp: int = genome.genome[ix_1]
		genome.genome[ix_1] = genome.genome[ix_2]
		genome.genome[ix_2] = temp

	@staticmethod
	def increase_genome_length(genome: Genome) -> None:
		"""
		Append a random floor at the end of the genome.
		"""
		genome.genome.append(random.randint(0, data.NUMBER_OF_FLOORS - 1))

	@staticmethod
	def decrease_genome_length(genome: Genome) -> None:
		"""
		Remove a randomly chosen index.
		"""
		genome.genome.pop(random.randint(0, len(genome.genome) - 1))

	@staticmethod
	def swap_and_inc(genome: Genome) -> None:
		"""
		Do swap and increase length.
		"""
		Mutation.swap(genome)
		Mutation.increase_genome_length(genome)

	@staticmethod
	def swap_and_dec(genome: Genome) -> None:
		"""
		Do swap and decrease length.
		"""
		Mutation.swap(genome)
		Mutation.decrease_genome_length(genome)

"""
This module contains tests for the mutation module.
"""

import sys
import os

# Add path to src directory
sys.path.insert(
	0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)

from genome import Genome
from evolutionary_classes.mutation import Mutation
from data import NUMBER_OF_FLOORS

genome = Genome([])


def test_swap() -> None:
	"""
	Test that the swap function actually swaps two random indices in the genome.
	"""
	genome.genome = [1, 2, 3, 4, 5, 6]
	Mutation.swap(genome)
	assert genome.genome != [1, 2, 3, 4, 5, 6]
	assert len(genome.genome) == 6


def test_increase_genome_length() -> None:
	"""
	Test that the increase_genome_length function actually increases the length of the genome.
	"""
	genome.genome = [1, 2, 3, 4, 5, 6]
	Mutation.increase_genome_length(genome)
	assert len(genome.genome) == 7
	assert 0 <= genome.genome[6] < NUMBER_OF_FLOORS


def test_decrease_genome_length() -> None:
	"""
	Test that the decrease_genome_length function actually decreases the length of the genome.
	"""
	genome.genome = [1, 2, 3, 4, 5, 6]
	Mutation.decrease_genome_length(genome)
	assert len(genome.genome) == 5


def test_swap_and_inc() -> None:
	"""
	Test that the swap_and_inc function actually swaps two random indices in the genome and increases the length of the genome.
	"""
	genome.genome = [1, 2, 3, 4, 5, 6]
	Mutation.swap_and_inc(genome)
	assert genome.genome != [1, 2, 3, 4, 5, 6]
	assert len(genome.genome) == 7
	assert 0 <= genome.genome[6] < NUMBER_OF_FLOORS


def test_swap_and_dec() -> None:
	"""
	Test that the swap_and_dec function actually swaps two random indices in the genome and decreases the length of the genome.
	"""
	genome.genome = [1, 2, 3, 4, 5, 6]
	Mutation.swap_and_dec(genome)
	assert genome.genome != [1, 2, 3, 4, 5, 6]
	assert len(genome.genome) == 5

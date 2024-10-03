# Author: Joel Scarinius Stävmo, Oskar Sundberg, Linus Savinainen, Samuel Wallander Leyonberg  and Gustav Pråmell
# Update: October 1, 2024
# Version: 1.0.0
# License: Apache 2.0

"""
This module contains tests for the mutation module.
"""

import sys
import os

# Add path to src directory
sys.path.insert(
	0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)

from chromosome import Chromosome
from evolutionary_classes.mutation import Mutation
from data import NUMBER_OF_FLOORS

chromosome = Chromosome([])


def test_swap() -> None:
	"""
	Test that the swap function actually swaps two random indices in the chromosome.
	"""
	chromosome.chromosome = [1, 2, 3, 4, 5, 6]
	Mutation.swap(chromosome)
	assert chromosome.chromosome != [1, 2, 3, 4, 5, 6]
	assert len(chromosome.chromosome) == 6


def test_increase_genome_length() -> None:
	"""
	Test that the increase_genome_length function actually increases the length of the chromosome.
	"""
	chromosome.chromosome = [1, 2, 3, 4, 5, 6]
	Mutation.increase_genome_length(chromosome)
	assert len(chromosome.chromosome) == 7
	assert 0 <= chromosome.chromosome[6] < NUMBER_OF_FLOORS


def test_decrease_genome_length() -> None:
	"""
	Test that the decrease_genome_length function actually decreases the length of the chromosome.
	"""
	chromosome.chromosome = [1, 2, 3, 4, 5, 6]
	Mutation.decrease_genome_length(chromosome)
	assert len(chromosome.chromosome) == 5
	chromosome.chromosome = [1, 2]
	Mutation.decrease_genome_length(chromosome)
	assert len(chromosome.chromosome) > 1


def test_swap_and_inc() -> None:
	"""
	Test that the swap_and_inc function actually swaps two random indices in the chromosome and increases the length of the chromosome.
	"""
	chromosome.chromosome = [1, 2, 3, 4, 5, 6]
	Mutation.swap_and_inc(chromosome)
	assert chromosome.chromosome != [1, 2, 3, 4, 5, 6]
	assert len(chromosome.chromosome) == 7
	assert 0 <= chromosome.chromosome[6] < NUMBER_OF_FLOORS


def test_swap_and_dec() -> None:
	"""
	Test that the swap_and_dec function actually swaps two random indices in the chromosome and decreases the length of the chromosome.
	"""
	chromosome.chromosome = [1, 2, 3, 4, 5, 6]
	Mutation.swap_and_dec(chromosome)
	assert chromosome.chromosome != [1, 2, 3, 4, 5, 6]
	assert len(chromosome.chromosome) == 5
	chromosome.chromosome = [1, 2]
	Mutation.swap_and_dec(chromosome)
	assert len(chromosome.chromosome) > 1
	assert chromosome.chromosome == [2, 1]

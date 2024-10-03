# Author: Joel Scarinius Stävmo, Oskar Sundberg, Linus Savinainen, Samuel Wallander Leyonberg  and Gustav Pråmell
# Update: October 1, 2024
# Version: 1.0.0
# License: Apache 2.0

"""
This module contains tests for the selection module.
"""

import sys
import os

# Add path to src directory
sys.path.insert(
	0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)

from evolutionary_classes.selection import Selection
from chromosome import Chromosome
from data import Population

genome_1 = Chromosome([])
genome_2 = Chromosome([])
genome_3 = Chromosome([])
genome_4 = Chromosome([])
genome_5 = Chromosome([])
population: Population = [genome_1, genome_2, genome_3, genome_4, genome_5]


def test_rank_selection_with_different_fitness():
	"""
	Test the rank function in the selection module with different fitness scores
	"""

	genome_1.fitness_score = 50
	genome_2.fitness_score = 40
	genome_3.fitness_score = 30
	genome_4.fitness_score = 20
	genome_5.fitness_score = 10

	# Run the rank selection
	parents = Selection.rank(population)

	# Check that two parents are selected
	assert len(parents) == 2

	# Check that selected parents are from the ranked population
	assert parents[0] in population
	assert parents[1] in population

	# Check that the selected parents are not the same
	assert parents[0] != parents[1]


def test_rank_selection_with_identical_fitness():
	"""
	Test the rank function in the selection module with identical fitness scores
	"""
	genome_1.fitness_score = 10
	genome_2.fitness_score = 10
	genome_3.fitness_score = 10
	genome_4.fitness_score = 10
	genome_5.fitness_score = 10

	# Run the rank selection
	parents = Selection.rank(population)

	# Check that two parents are selected
	assert len(parents) == 2

	# Check that selected parents are from the ranked population
	assert parents[0] in population
	assert parents[1] in population

	# Check that the selected parents are not the same
	assert parents[0] != parents[1]

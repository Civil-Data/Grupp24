# Author: Joel Scarinius Stävmo, Oskar Sundberg, Linus Savinainen, Samuel Wallander Leyonberg  and Gustav Pråmell
# Update: October 1, 2024
# Description: " "
# Version: 1.0.0
# License: Apache 2.0

"""
This module contains tests for the crossover module.
"""

import sys
import os

# Add path to src directory
sys.path.insert(
	0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)

from genome import Genome
from evolutionary_classes.crossover import Crossover


def test_swap_last_halves():
	"""
	Test the swap_last_halves function to see that it actually swaps the last halves of the two parents.
	"""
	parent_1 = Genome([1, 2, 3, 4, 5, 6])
	parent_2 = Genome([7, 8, 9, 10, 11, 12])
	offspring_1, offspring_2 = Crossover.swap_last_halves(parent_1, parent_2)
	assert offspring_1.genome == [1, 2, 3, 10, 11, 12]
	assert offspring_2.genome == [7, 8, 9, 4, 5, 6]
	parent_1 = Genome([1, 2, 3, 4])
	parent_2 = Genome([7, 8, 9, 10, 11, 12])
	offspring_1, offspring_2 = Crossover.swap_last_halves(parent_1, parent_2)
	assert offspring_1.genome == [1, 2, 9, 10, 11, 12]
	assert offspring_2.genome == [7, 8, 3, 4]

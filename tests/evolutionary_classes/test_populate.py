"""
This module contains tests for the populate module.
"""

import sys
import os

# Add path to src directory
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)

from evolutionary_classes.populate import Populate
from data import NUMBER_OF_FLOORS, POPULATION_SIZE


def test_generate_population() -> None:
    """
    Test that the generate_population function actually generates a valid population.
    """
    population = Populate.generate_population()
    assert len(population) == POPULATION_SIZE
    for genome in population:
        for i in genome.genome:
            assert 0 <= i < NUMBER_OF_FLOORS

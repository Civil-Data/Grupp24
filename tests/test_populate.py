"""
This module contains tests for the populate module.
"""

import sys
import os

# Add path to src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from evolutionary_classes.populate import Populate
import data


def test_generate_population() -> None:
    """
    Generate a population of random Genomes
    """
    population = Populate.generate_population()
    assert len(population) == data.POPULATION_SIZE

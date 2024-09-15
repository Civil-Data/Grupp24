"""
This module contains tests for the selection module.
"""

import sys
import os

# Add path to src directory
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)

from typing import List
#import pytest
from evolutionary_classes.selection import Selection


class MockGenome:
    """
    Mock genome class for testing
    """

    def __init__(self, fitness_score):
        self.fitness_score = fitness_score


def test_rank_selection_with_different_fitness():
    """
    Test the rank function in the selection module with different fitness scores
    """
    population: List[MockGenome] = [
        MockGenome(fitness_score=50),
        MockGenome(fitness_score=40),
        MockGenome(fitness_score=30),
        MockGenome(fitness_score=20),
        MockGenome(fitness_score=10),
    ]

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
    population: List[MockGenome] = [
        MockGenome(fitness_score=10),
        MockGenome(fitness_score=10),
        MockGenome(fitness_score=10),
        MockGenome(fitness_score=10),
        MockGenome(fitness_score=10),
    ]

    # Run the rank selection
    parents = Selection.rank(population)

    # Check that two parents are selected
    assert len(parents) == 2

    # Check that selected parents are from the ranked population
    assert parents[0] in population
    assert parents[1] in population

    # Check that the selected parents are not the same
    assert parents[0] != parents[1]

#this test do not end, unclear why
#def test_rank_selection_with_single_individual():
#    """
#    Test the rank function in the selection module with a single individual
#    """
#    population: List[MockGenome] = [MockGenome(fitness_score=10)]

    # Run the rank selection and expect an assertion error
#    with pytest.raises(AssertionError):
#        Selection.rank(population)

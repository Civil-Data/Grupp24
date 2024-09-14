"""
This module contains tests for the fitness module.
"""

import sys
import os

# Add path to src directory
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)

from genome import Genome
from evolutionary_classes.fitness import Fitness
from data import PERSON_ARRIVED_SCORE


class MockPerson:
    """
    This is a mock class for the Person class.
    """

    def __init__(self, has_arrived):
        self.has_arrived = has_arrived


def test_calc_fitness_no_people() -> None:
    """
    Test the calc_fitness function to see that it actually calculates the fitness of the genome
    when there are no people in the genome.
    """
    genome = Genome([])
    Fitness.calc_fitness(genome.people)
    assert genome.fitness_score == 0


def test_calc_fitness_no_one_arrived() -> None:
    """
    Test the calc_fitness function to see that it actually calculates the fitness of the genome
    when no one has arrived.
    """
    genome = Genome([MockPerson(False), MockPerson(False)])
    Fitness.calc_fitness(genome)
    assert genome.fitness_score == 0


def test_calc_fitness_some_arrived() -> None:
    """
    Test the calc_fitness function to see that it actually calculates the fitness of the genome
    when some people have arrived.
    """
    genome = Genome([MockPerson(True), MockPerson(False)])
    Fitness.calc_fitness(genome)
    assert genome.fitness_score == PERSON_ARRIVED_SCORE


def test_calc_fitness_all_arrived() -> None:
    """
    Test the calc_fitness function to see that it actually calculates the fitness of the genome
        when all people have arrived.
    """
    genome = Genome([MockPerson(True), MockPerson(True)])
    Fitness.calc_fitness(genome)
    assert genome.fitness_score == 2 * PERSON_ARRIVED_SCORE

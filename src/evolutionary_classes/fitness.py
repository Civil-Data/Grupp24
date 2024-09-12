"""
Module containing static fitness function(s)
"""

from genome import Genome
from data import PERSON_ARRIVED_SCORE

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
            if person.has_arrived:
                accumulated_score += PERSON_ARRIVED_SCORE

        genome.fitness_score = accumulated_score

"""
Module containing static fitness function(s)
"""

from genome import Genome
from data import PERSON_ARRIVED_SCORE, TIME_PENALTY

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
        accumulated_time_score: int = 0

        for person in genome.people:
            if person.has_arrived:
                accumulated_score += PERSON_ARRIVED_SCORE
                accumulated_time_score += person.time_spent_waiting
            else:
                accumulated_time_score += TIME_PENALTY 
        genome.fitness_score = accumulated_score
        genome.time_score = accumulated_time_score

"""
Module containing static fitness function(s)
"""

from genome import Genome

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
                accumulated_score += 10

        genome.fitness_score = accumulated_score

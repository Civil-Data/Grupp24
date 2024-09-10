"""
Module containing static fitness function(s)
"""

import data
from genome import Genome

class Fitness:
    """
    Function(s) that calculates fitness of a Genome
    """
    @staticmethod
    def calc_fitness(genome: Genome) -> int:
        accumulated_score: int = 0

        for person in genome.people:
            if person.has_arrived:
                # Reward based on:
                # More people
                accumulated_score += data.NUMBER_OF_PEOPLE 
                # More floors
                accumulated_score += data.NUMBER_OF_FLOORS
                # Less stops
                accumulated_score += int(round(10.0 * float(1.0 / float(data.GENOME_LENGTH))))

            # Punish based on:
            # Excess travel
            delta_distance = person.distance_traveled - person.distance_needed
            if delta_distance > 0:
                accumulated_score -= delta_distance 

        return accumulated_score

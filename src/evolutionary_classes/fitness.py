"""
Module containing fitness function(s)
"""

from data import Data
from main_classes.elevator import Elevator

class Fitness:
    """
    motsatsen till oskar
    """

    @staticmethod
    def calc_fitness(genome: Data.Genome ,people: Data.People, elavator: Elevator) -> int:
        assert len(people) == Data.NUMBER_OF_PEOPLE

        # Reset stats
        for person in people:
            person.has_arrived = False
            person.distance_traveled = 0

        # Simulate the journey based on the genome
        for floor in genome:
            elavator.travel(elavator.current_floor, floor)

        # The entire elevator journey is now complete, calculate the fitness
        accumulated_score: int = 0

        for person in people:
            if person.has_arrived:
                # Increase the reward based on:
                # More people, more floors, less stops
                accumulated_score += Data.NUMBER_OF_PEOPLE + Data.NUMBER_OF_FLOORS + 100.0 * float(1.0 / float(Data.GENOME_LENGTH))

            delta_distance = person.distance_traveled - person.distance_needed
            if delta_distance > 0:
                # Punish based on:
                # Excess travel, less people, less flors, more stops
                accumulated_score -= delta_distance - Data.NUMBER_OF_PEOPLE - Data.NUMBER_OF_FLOORS - Data.GENOME_LENGTH

        return accumulated_score

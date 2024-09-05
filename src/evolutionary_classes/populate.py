"""
Module containing population generating function(s)
"""

from data import Data
import random

class Populate:
    @staticmethod
    def generate_population() -> Data.Population:
        """
        Generate a population of random Genomes
        """

        # First for loop generates a single random Genome
        # Second for loop to generate multiple Genomes
        return [random.randint(0, Data.NUMBER_OF_FLOORS - 1) for _ in range(Data.GENOME_LENGTH) for _ in range(Data.POPULATION_SIZE)]
    
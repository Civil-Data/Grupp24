"""
Module containing static population generating function(s)
"""

from typing import List
import data
import random
from genome import Genome

class Populate:
    @staticmethod
    def generate_population() -> data.Population:
        """
        Generate a population of random Genomes
        """

        genomes: List[Genome] = []
        for _ in range(data.POPULATION_SIZE):
            genomes.append(Genome(random.randint(0, data.NUMBER_OF_FLOORS - 1) for _ in range(data.GENOME_LENGTH)))
        
        return genomes
    
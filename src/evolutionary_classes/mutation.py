"""
Module containing static mutation function(s)
"""

import random
import data
from genome import Genome
from icecream import ic

class Mutation:
    @staticmethod
    def swap(genome: Genome) -> None:
        genome_len: int = len(list(genome.genome))

        ix_1: int = random.randint(0, genome_len - 1)
        ix_2: int = random.randint(0, genome_len - 1)
        while ix_2 == ix_1:
            ix_2 = random.randint(0, genome_len - 1)

        temp: int = genome.genome[ix_1]
        genome.genome[ix_1] = genome.genome[ix_2]
        genome.genome[ix_2] = temp

    @staticmethod
    def increase_genome_length(genome: Genome) -> None:
        genome.genome.append(random.randint(0, data.NUMBER_OF_FLOORS - 1))

    @staticmethod
    def decrease_genome_length(genome: Genome) -> None:
        genome.genome.pop(random.randint(0, len(genome.genome) - 1))
    
    @staticmethod
    def swap_and_inc(genome: Genome) -> None:
        Mutation.increase_genome_length(Mutation.swap(genome))
    
    @staticmethod
    def swap_and_dec(genome: Genome) -> None:
        Mutation.decrease_genome_length(Mutation.swap(genome))

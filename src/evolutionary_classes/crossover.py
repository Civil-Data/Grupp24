"""
Module containing static crossover function(s)
"""
from typing import Tuple
from genome import Genome

class Crossover:
    @staticmethod
    def swap_last_halves(parent_1: Genome, parent_2: Genome) -> Tuple[Genome, Genome]:

        genome_1 = list(parent_1.genome)
        genome_2 = list(parent_2.genome)

        # The parents' genomes may be of different length
        len_parent_1: int = len(genome_1)
        len_parent_2: int = len(genome_2)

        genes_to_swap: int = min(len_parent_1, len_parent_2)

        # "take all elements from the start of the list up to (but not including) the last n_genes_1 elements"
        # +
        # "take all elements starting from the index that is n_genes_2 elements from the end of the list to the end of the list"
        offspring_1: Genome = Genome(genome_1[:-genes_to_swap] + genome_2[-genes_to_swap:])
        offspring_2: Genome = Genome(genome_2[:-genes_to_swap] + genome_1[-genes_to_swap:])

        return offspring_1, offspring_2

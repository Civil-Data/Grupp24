"""
Module containing static crossover function(s)
"""
from typing import Tuple
from genome import Genome

class Crossover:
    """
    Class containing static crossover function(s)
    """
    @staticmethod
    def swap_last_halves(parent_1: Genome, parent_2: Genome) -> Tuple[Genome, Genome]:
        """
        Swap the last halves of the parents' genomes.
        If the genomes are of different length, swap with respect to the shorter parent's length.
        """

        # The parents' genomes may be of different length
        genes_to_swap: int = min(len(parent_1.genome), len(parent_2.genome)) // 2

        # "take all elements from the start of the list up to (but not including) index genes_to_swap"
        # +
        # "take all elements starting from the index that is genes_to_swap elements to the end of the list"
        offspring_1: Genome = Genome(parent_1.genome[:genes_to_swap] +
                                     parent_2.genome[genes_to_swap:])
        offspring_2: Genome = Genome(parent_2.genome[:genes_to_swap] +
                                     parent_1.genome[genes_to_swap:])

        return offspring_1, offspring_2

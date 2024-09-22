"""
Module containing static crossover function(s)
"""
from typing import Tuple
from genome import Genome
import random

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
    
    @staticmethod
    def heuristic_crossover(parent_1: Genome, parent_2: Genome) ->Tuple[Genome, Genome]:
        """
        Creates two offsprings from two parents where the parent with better (lower) fitness score hase more of its
        genes reprecented in the chromosome for each child.
        """
        
        """
        Make sure that parent_1 i har a wors score than parent_2
        """
        if parent_1.fitness_score < parent_2.fitness_score:
            parent_1, parent_2 = parent_2, parent_1
        
        """
        Caluculating the parents wighted differenses in persentage
        """
        total_fitness = parent_1.fitness_score + parent_2.fitness_score
        
        if total_fitness != 0:
            weight_parent_2 = parent_1.fitness_score / total_fitness
            weight_parent_1 = 1 - weight_parent_2
        else:
            weight_parent_2 = 0.5
            weight_parent_1 = 0.5
        
        offspring_1_genes = []
        offspring_2_genes = []
        
        """
        Based on randomnes with favior for parent_2, append and insert genes into the offsprings
        """        
        for gene in range(len(parent_2.genome)):
            if random.random() < weight_parent_1:
                offspring_1_genes.append(parent_2.genome[gene])
                offspring_2_genes.insert(0, parent_2.genome[gene])
            else:
                if len(parent_1.genome) > gene:
                    offspring_1_genes.append(parent_1.genome[gene])
                    offspring_2_genes.insert(0, parent_1.genome[gene])
                else:
                    offspring_1_genes.append(parent_2.genome[gene])
                    offspring_2_genes.insert(0, parent_2.genome[gene])
                    
        
        offspring_1 = Genome(offspring_1_genes)
        offspring_2 = Genome(offspring_2_genes)
        
        return offspring_1, offspring_2
        

"""
Module containing selection function(s)
"""

from data import Data

class Selection:
    # Roulette Wheel Selection
    # In this method, individuals are selected based on their fitness proportionate to the total
    # fitness of the population. The idea is to create a "roulette wheel" where each individual 
    # has a slice proportional to its fitness.

    # Tournament Selection
    # In tournament selection, a subset of individuals is chosen randomly, and the best individual
    # from this subset is selected. This can be repeated to select multiple individuals.

    # Rank Selection
    # In rank selection, individuals are ranked based on their fitness, and selection is based on
    # this rank rather than raw fitness values. This can help maintain diversity in the population.

    def selection_roulette(population: Data.Population, fitness_function: Data.FitnessFunction) -> tuple[Data.Genome, Data.Genome]:
        

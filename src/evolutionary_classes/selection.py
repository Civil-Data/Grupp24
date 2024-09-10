"""
Module containing static selection function(s)
"""

import random
import data
from typing import List, Tuple
from genome import Genome

class Selection:
    " Class containing static selection function(s) "
    
    # Rank Selection
    # In rank selection, individuals are ranked based on their fitness, and selection is based on
    # this rank rather than raw fitness values. This can help maintain diversity in the population.
    @staticmethod
    def rank(population: data.Population, fitness_function: data.FitnessFunction) -> Tuple[Genome, Genome]:
        
        # Calculate fitness for each genome
        fitness_scores: List[Tuple[Genome, int]] = [(genome, fitness_function(genome)) for genome in population]

        # Sort the genomes based on the fitness
        ranked_population: List[Tuple[Genome, int]] = sorted(
            fitness_scores,
            key=lambda x: x[1], # 'x' is a tuple, [1] is indexing to the int. I.e. sort based on the int value
            reverse=True
        )

        # Hand out the ranks 1, 2, 3, ...
        ranks: List[int] = list(range(1, len(ranked_population) + 1))

        # Calc the probability to get picked by ranks
        total_ranks = sum(ranks)
        selection_probs: list[float] = [rank / total_ranks for rank in ranks]

        # Create a cumulative distribution of selection probabilties
        cumulative_probabilities: List[float] = []
        cumulative_sum: float = 0.0
        for prob in selection_probs:
            cumulative_sum += prob
            cumulative_probabilities.append(cumulative_sum)

        # Select two parents based on the cumulative distribution
        parents: List[Genome] = []
        while len(parents) < 2:  # 2 parents
            random_value = random.uniform(0.0, 1.0)  # Generate a random number between 0 and 1
            for j in range(len(cumulative_probabilities)):
                if random_value <= cumulative_probabilities[j]:
                    selected_parent = ranked_population[j][0]
                    if selected_parent not in parents:  # Check if the parent is already selected
                        parents.append(selected_parent)
                        break  # Exit the for loop after selecting a parent

        assert len(parents) == 2
        return parents


    # Roulette Wheel Selection
    # In this method, individuals are selected based on their fitness proportionate to the totals
    # fitness of the population. The idea is to create a "roulette wheel" where each individual 
    # has a slice proportional to its fitness.

    # Tournament Selection
    # In tournament selection, a subset of individuals is chosen randomly, and the best individual
    # from this subset is selected. This can be repeated to select multiple individuals.

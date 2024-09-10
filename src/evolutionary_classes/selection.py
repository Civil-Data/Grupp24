"""
Module containing static selection function(s)
"""

import random
from typing import List, Tuple
import data
from genome import Genome

class Selection:
    " Class containing static selection function(s) "

    @staticmethod
    def rank(population: data.Population, fitness_function: data.FitnessFunction) -> Tuple[Genome, Genome]:
        """
        In rank selection, individuals are ranked based on their fitness, and selection is
        based on this rank rather than raw fitness values. This can help maintain diversity
        in the population.
        """

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
            for j, value in enumerate(cumulative_probabilities):
                if random_value <= value:
                    selected_parent = ranked_population[j][0]
                    if selected_parent not in parents:  # Check if the parent is already selected
                        parents.append(selected_parent)
                        break  # Exit the for loop after selecting a parent

        assert len(parents) == 2
        return parents

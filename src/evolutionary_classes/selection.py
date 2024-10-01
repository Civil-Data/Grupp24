# Author: Joel Scarinius Stävmo, Oskar Sundberg, Linus Savinainen, Samuel Wallander Leyonberg  and Gustav Pråmell
# Update: October 1, 2024
# Description: " "
# Version: 1.0.0
# License: Apache 2.0

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
	def rank(ranked_population: data.Population) -> Tuple[Genome, Genome]:
		"""
		param: ranked_population = a sorted population in descending order, based on fitness
		In rank selection, individuals are ranked based on their fitness, and selection is
		based on this rank rather than raw fitness values. This can help maintain diversity
		in the population.
		"""

		# Hand out the ranks 1, 2, 3, ...
		ranks: List[int] = list(range(1, len(ranked_population) + 1))
		# ... but 1 is the lowest rank
		ranks.reverse()

		# Calc the probability to get picked by ranks
		total_ranks = sum(ranks)
		selection_probs: List[float] = [rank / total_ranks for rank in ranks]

		# Create a cumulative distribution of selection probabilities
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
					selected_parent = ranked_population[j]
					if selected_parent not in parents:  # Check if the parent is already selected
						parents.append(selected_parent)
						break  # Exit the for loop after selecting a parent

		assert len(parents) == 2
		return parents

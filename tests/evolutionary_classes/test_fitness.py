# Author: Joel Scarinius Stävmo, Oskar Sundberg, Linus Savinainen, Samuel Wallander Leyonberg  and Gustav Pråmell
# Update: October 1, 2024
# Version: 1.0.0
# License: Apache 2.0

"""
This module contains tests for the fitness module.
"""

import sys
import os

# Add path to src directory
sys.path.insert(
	0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)

from chromosome import Chromosome
from main_classes.person import Person
from evolutionary_classes.fitness import Fitness
from data import Population

person1 = Person(2, 5, 10)
person2 = Person(3, 4, 10)
genome_1 = Chromosome([])
genome_2 = Chromosome([])
genome_1.people = [person1, person2]
genome_2.people = []
test_population: Population = [genome_1, genome_2]


def test_calc_fitness_no_people() -> None:
	"""
	Test the calc_fitness function to see that it actually calculates the fitness of the chromosome
	when there are no people in the chromosome.
	"""
	Fitness.calc_fitness(test_population[1])
	assert test_population[1].fitness_score == 0


#def test_calc_fitness_no_one_arrived() -> None:
#	"""
#	Test the calc_fitness function to see that it actually calculates the fitness of the chromosome
#	when no one has arrived.
#	"""
#	test_population[0].people[0].has_arrived = False
#	test_population[0].people[1].has_arrived = False
#	Fitness.calc_fitness(test_population[0])
#	assert test_population[0].fitness_score == 0


#def test_calc_fitness_some_arrived() -> None:
#	"""
#	Test the calc_fitness function to see that it actually calculates the fitness of the chromosome
#	when some people have arrived.
#	"""
#	test_population[0].people[0].has_arrived = True
#	test_population[0].people[1].has_arrived = False
#	Fitness.calc_fitness(test_population[0])
#	assert test_population[0].fitness_score == PERSON_ARRIVED_SCORE


#def test_calc_fitness_all_arrived() -> None:
#	"""
#	Test the calc_fitness function to see that it actually calculates the fitness of the chromosome
#	when all people have arrived.
#	"""
#	test_population[0].people[0].has_arrived = True
#	test_population[0].people[1].has_arrived = True
#	print(len(test_population[0].people))
#	Fitness.calc_fitness(test_population[0])
#	assert test_population[0].fitness_score == 2 * PERSON_ARRIVED_SCORE

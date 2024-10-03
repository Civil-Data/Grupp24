# Author: Joel Scarinius Stävmo, Oskar Sundberg, Linus Savinainen, Samuel Wallander Leyonberg  and Gustav Pråmell
# Update: October 1, 2024
# Version: 1.0.0
# License: Apache 2.0

"""
Chromosome module
"""

from typing import List
from main_classes.person import Person

class Chromosome:
	chromosome: List[int]
	people: List[Person] # 'chromosome' affects 'people'
	fitness_score: int

	def __init__(self, chromosome: List[int]) -> None:
		self.chromosome = chromosome
		self.people = []
		self.fitness_score = 0
	
	def how_many_arrived(self) -> int:
		num: int = 0
		for person in self.people:
			if person.has_arrived:
				num += 1

		return num

"""
Genome module
"""

from typing import List
from main_classes.person import Person

class Genome:
	genome: List[int]
	people: List[Person] # 'genome' affects 'people'
	fitness_score: int

	def __init__(self, genome: List[int]) -> None:
		self.genome = genome
		self.people = []
		self.fitness_score = 0
	
	def how_many_arrived(self) -> int:
		num: int = 0
		for person in self.people:
			if person.has_arrived:
				num += 1

		return num

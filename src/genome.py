"""
Genome module
"""

from typing import List
from main_classes.person import Person

class Genome:
    genome: List[int]
    people: List[Person] # 'genome' affects 'people'

    def __init__(self, genome: List[int]) -> None:
        self.genome = genome
        self.people = []

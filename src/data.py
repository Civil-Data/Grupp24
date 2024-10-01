# Author: Joel Scarinius Stävmo, Oskar Sundberg, Linus Savinainen, Samuel Wallander Leyonberg  and Gustav Pråmell
# Update: October 1, 2024
# Version: 1.0.0
# License: Apache 2.0

"Module containing shared information and configuration data"

from typing import List, Callable, Tuple
from genome import Genome, Person

NUMBER_OF_FLOORS: int = 15
NUMBER_OF_PEOPLE: int = 15

ELEVATOR_CAPACITY: int = 8

GENOME_LENGTH: int = NUMBER_OF_FLOORS
POPULATION_SIZE: int = 100
GENERATION_LIMIT: int = 1000

MUTATION_CHANCE: float = 0.1
CROSSOVER_CHANCE: float = 1.0
# Top % of genomes to directly carry over to the next generation
ELITISM_PERC: float = 0.1

# How much extra time a person who doesn't end up on the right floor gives
TIME_PENALTY: int = 10000

# Whether or not to use the experiment library by Gurra
DO_EXP: bool = True

NUMBER_OF_EXP: int = 1

EXP_RANDOM_BUILDING: bool = True
EXP_EVEN_BUILDING: bool = not EXP_RANDOM_BUILDING
EXP_GENOME_RANGE_START = GENOME_LENGTH // 2 
EXP_GENOME_RANGE_END = GENOME_LENGTH
# How many people can be slotted on one floor, start and end range (incl.)
EXP_FLOOR_LENGTH_START: int = 0
EXP_FLOOR_LENGTH_END: int = NUMBER_OF_PEOPLE

Population = List[Genome]

People = List[Person]
People_queues = List[People]

PopulateFunction = Callable[[], Population]
FitnessFunction = Callable[[Genome], None]
SelectionFunction = Callable[[Population], Tuple[Genome, Genome]]
CrossoverFunction = Callable[[Genome, Genome], Tuple[Genome, Genome]]
MutationFunction = Callable[[Genome], None]

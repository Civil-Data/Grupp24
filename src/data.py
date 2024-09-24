"Module containing shared information and configuration data"

from typing import List, Callable, Tuple
from genome import Genome, Person

NUMBER_OF_FLOORS: int = 15
NUMBER_OF_PEOPLE: int = NUMBER_OF_FLOORS * 3

ELEVATOR_CAPACITY: int = 8

GENOME_LENGTH: int = NUMBER_OF_FLOORS
POPULATION_SIZE: int = 50
GENERATION_LIMIT: int = 1000

MUTATION_CHANCE: float = 0.1
CROSSOVER_CHANCE: float = 1.0
# Top % of genomes to directly carry over to the next generation
ELITISM_PERC: float = 0.0

# How much extra time a person who doesn't end up on the right floor gives
TIME_PENALTY: int = 1000

# Whether or not to use the experiment library by Gurra
DO_EXP: bool = True

EXP_RANDOM_BUILDING: bool = False
EXP_EVEN_BUILDING: bool = not EXP_RANDOM_BUILDING
EXP_GENOME_RANGE_START = GENOME_LENGTH // 2
EXP_GENOME_RANGE_END = GENOME_LENGTH
# How many people can be slotted on one floor start range
EXP_FLOOR_LENGTH_START: int = 1
# How many people can be slotted on one floor end range
EXP_FLOOR_LENGTH_END: int = 1

Population = List[Genome]

People = List[Person]
People_queues = List[People]

PopulateFunction = Callable[[], Population]
FitnessFunction = Callable[[Genome], None]
SelectionFunction = Callable[[Population], Tuple[Genome, Genome]]
CrossoverFunction = Callable[[Genome, Genome], Tuple[Genome, Genome]]
MutationFunction = Callable[[Genome], None]

"Module containing shared information and configuration data"

from typing import List, Callable, Tuple
from genome import Genome, Person

NUMBER_OF_FLOORS: int = 15
NUMBER_OF_PEOPLE: int = NUMBER_OF_FLOORS * 2

ELEVATOR_CAPACITY: int = 8

GENOME_LENGTH: int = NUMBER_OF_FLOORS
POPULATION_SIZE: int = 100
GENERATION_LIMIT: int = 10

MUTATION_CHANCE: float = 0.5
CROSSOVER_CHANCE: float = 1.0
# Top % of genomes to directly carry over to the next generation
ELITISM_PERC: float = 0.0

# How much extra time a person who doesn't end up on the right floor gives
TIME_PENALTY: int = 100

# Whether or not to use the experiment library by Gurra
DO_EXP: bool = False

EXP_RANDOM_BUILDING: bool = True
EXP_RANGE_START = GENOME_LENGTH // 2
EXP_RANGE_END = GENOME_LENGTH
# How many people can be slotted on one floor. Only matters for even buildings
EXP_FLOOR_LENGTH = 3

Population = List[Genome]

People = List[Person]
People_queues = List[People]

PopulateFunction = Callable[[], Population]
FitnessFunction = Callable[[Genome], None]
SelectionFunction = Callable[[Population], Tuple[Genome, Genome]]
CrossoverFunction = Callable[[Genome, Genome], Tuple[Genome, Genome]]
MutationFunction = Callable[[Genome], None]

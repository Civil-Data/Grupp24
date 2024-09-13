"Module containing shared information and configuration data"

from typing import List, Callable, Tuple
from genome import Genome, Person

GENOME_LENGTH: int = 8
POPULATION_SIZE: int = 30
GENERATION_LIMIT: int = 100000
MUTATION_CHANCE: float = 0.01
CROSSOVER_CHANCE: float = 1.0

NUMBER_OF_FLOORS: int = 15
NUMBER_OF_PEOPLE: int = NUMBER_OF_FLOORS * 1

PERSON_ARRIVED_SCORE: int = 10
MAXIMUM_POSSIBLE_SCORE: int = NUMBER_OF_PEOPLE * PERSON_ARRIVED_SCORE

# Top % of genomes to directly carry over to the next generation
ELITISM_PERC: float = 0.0

Population = List[Genome]

People = List[Person]
People_queues = List[People]

PopulateFunction = Callable[[], Population]
FitnessFunction = Callable[[Genome], None]
SelectionFunction = Callable[[Population], Tuple[Genome, Genome]]
CrossoverFunction = Callable[[Genome, Genome], Tuple[Genome, Genome]]
MutationFunction = Callable[[Genome], None]
    

" Module containing shared information and configuration data"

from typing import List, Callable, Tuple
from main_classes.person import Person
from main_classes.elevator import Elevator

class Data:
    """
    Export information and configuration data
    """
    GENOME_LENGTH: int = 8
    POPULATION_SIZE: int = 50
    
    NUMBER_OF_FLOORS: int = 5
    NUMBER_OF_PEOPLE: int = NUMBER_OF_FLOORS * 3

    Genome = List[int]
    Population = List[Genome]

    People = List[Person]
    People_queues = List[People]

    FitnessFunction = Callable[[Genome, People, Elevator], int]
    PopulateFunction = Callable[[], Population]
    SelectionFunction = Callable[[Population, FitnessFunction], Tuple[Genome, Genome]]
    CrossoverFunction = Callable[[Genome, Genome], Tuple[Genome, Genome]]
    MutationFunction = Callable[[Genome], Genome]
    
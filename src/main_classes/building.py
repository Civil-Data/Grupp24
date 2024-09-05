" Building module "

from elevator import Elevator
from data import Data

class Building:
    """
    param: people_matrix = a 2D array representation of which persons are on each floor
    param: genome = the sequence that determines what floors to go to in what order, passed to
    Elevator instantiation
    param: number_of_floors = the total number of floors, starting at 0 for ground floor
    """

    def __init__(self, people_queues: Data.People_queues, genome: Data.Genome, number_of_floors: int) -> None:
        if number_of_floors < 1:
            raise ValueError("number_of_floors may not be less than 1.")
        
        self.people_queues = people_queues
        self.elevator = Elevator(genome, people_queues)
        self.number_of_floors = number_of_floors

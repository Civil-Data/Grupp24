" Person module "

from data import Data

class Person:
    """
    param: start_floor = the initial floor that the person is waiting on
    param: end_floor = the floor that the person wants to go to
    param: has_arrived = a bool that tells if the person has arrived to the desired floor or not
    """

    def __init__(self, start_floor: int, end_floor: int, has_arrived: bool = False) -> None:
        if start_floor < 0:
            raise ValueError("start_floor may not be negative.")
        
        if end_floor > Data.NUMBER_OF_FLOORS - 1:
            raise ValueError("end_floor may not exceed total number of floors minus one.")
        
        self.start_floor = start_floor
        self.end_floor = end_floor
        self.has_arrived = has_arrived
        self.distance_traveled: int = 0
        self.distance_needed: int = start_floor - end_floor

" Elevator module "

from data import Data

class Elevator:
    """
    param: genome = the sequence that determines what floors to go to in what order
    param: max_capacity = the maximum number of persons allowed inside the elevator
    at any given time
    param: occupants = a list of persons currently inside the elevator
    """

    def __init__(self, genome: Data.Genome, people_queues: Data.People_queues, max_capacity: int = 8) -> None:
        if max_capacity < 1:
            raise ValueError("max_capacity may not 0 or less.")

        self.genome = genome
        self.people_queues = people_queues
        self.max_capacity = max_capacity
        self.occupants: Data.People = []
        self.current_floor: int = 0

    def travel(self, previous_floor: int, arrived_floor: int) -> None:
        """
        Do stuff when the elevator has traveled up or down
        """
        if arrived_floor == previous_floor:
            raise ValueError("arrived_floor must not be equal to previous_floor")

        if not 0 <= arrived_floor < Data.NUMBER_OF_FLOORS:
            raise ValueError("arrived_floor out of bounds")

        if not 0 <= previous_floor < Data.NUMBER_OF_FLOORS:
            raise ValueError("previous_floor out of bounds")

        self.current_floor = arrived_floor

        for person in self.occupants:
            # All occupants have traveled a certain distance
            person.distance_traveled += abs(self.current_floor - previous_floor)
            if self.current_floor == person.end_floor:
                # If anyone has arrived at their destination, remove them from elevator
                person.has_arrived = True
                self.occupants.remove(person)

        # Loop over all people waiting for the elevator at the current floor
        for person in self.people_queues[self.current_floor]:
            # If there is any availabe room in the elevator, load up on more people
            if len(self.occupants) < self.max_capacity:
                # Make sure there's no shenanigans going on
                assert person.start_floor == self.current_floor
                
                # Load person on to elevator
                self.occupants.append(person)

                # Remove that person from the queue of people waiting for elevator
                self.people_queues[self.current_floor].remove(person)
            else:
                break
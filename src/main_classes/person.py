"""
Person module
"""

import data


class Person:
    """
    param: start_floor = the initial floor that the person is waiting on
    param: end_floor = the floor that the person wants to go to
    """

    start_floor: int
    end_floor: int
    has_arrived: bool
    distance_traveled: int
    distance_needed: int

    def __init__(self, start_floor: int, end_floor: int) -> None:
        if start_floor < 0:
            raise ValueError("start_floor may not be negative.")

        if end_floor > data.NUMBER_OF_FLOORS - 1:
            raise ValueError(
                "end_floor may not exceed total number of floors minus one."
            )

        self.start_floor = start_floor
        self.end_floor = end_floor
        self.has_arrived = False
        self.distance_traveled: int = 0
        self.distance_needed: int = abs(start_floor - end_floor)

    def to_json(self):
        return {"start_floor": self.start_floor, "end_floor": self.end_floor}

    @classmethod
    def from_json(cls, data):
        return cls(
            start_floor=data["start_floor"],
            end_floor=data["end_floor"],
        )

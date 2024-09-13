"Building module tests"

import sys
import os
import copy

# Add path to src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main_classes.building import Building, data
from main import place_people, init_people


def test_move_elevator():
    "Tests the movement of the elevator"
    people = init_people()
    building = Building(place_people(copy.deepcopy(people)))
    #ensures elevator has been created
    assert building.elevator is not None
    assert building.elevator.current_floor == 0
    #move elevator
    building.move_elevator(building.elevator.current_floor, 2)
    assert building.elevator.current_floor == 2
    building.move_elevator(building.elevator.current_floor,4)
    assert building.elevator.current_floor == 4
    #What happens when the Genomo generates the same floor twice in a row, i.e., [1, 2, 3, 3, 4, ..., n].
    #It is allowed shuold and should therefore result in the elevator not moving floors.
    building.move_elevator(building.elevator.current_floor, building.elevator.current_floor)
    assert building.elevator.current_floor is building.elevator.current_floor


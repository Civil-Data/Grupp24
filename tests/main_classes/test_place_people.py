"place_people module tests"

import sys
import os
from icecream import ic

# To see what is generated, run this file by it self
# Then the ic will print out the data

# Add path to src directory
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)
from main import place_people, init_people
import data


def test_init_people():
    """
    Check that the number of people matches the expected count
    Check that each person has valid floor values
    Check correct initial states
    Check distance_traveled is zero
    Check non-zero distance needed
    """
    people = init_people()
    assert len(people) is data.NUMBER_OF_PEOPLE
    for person in people:
        assert 0 <= person.start_floor <= data.NUMBER_OF_FLOORS
        assert 0 <= person.end_floor <= data.NUMBER_OF_FLOORS
        assert person.has_arrived is not True
        assert person.distance_traveled == 0
        assert person.distance_needed != 0

        ic(person.start_floor)
        ic(person.end_floor)
        ic(person.has_arrived)
        ic(person.distance_traveled)
        ic(person.distance_needed)


def test_place_people():
    "Check that each person is on the correct floor"
    floors = place_people(init_people())
    current_floor = 0
    for floor in floors:
        ic("floor: ", current_floor)
        for person in floor:
            assert person.start_floor == current_floor
            ic(person.start_floor)
        current_floor += 1


if __name__ == "__main__":
    ic.enable()
    test_init_people()
    test_place_people()

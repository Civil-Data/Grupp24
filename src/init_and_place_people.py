import random
from main_classes.person import Person
import data


def init_people() -> data.People:
    """
    Get a list of people with random start and end floors
    """
    return [
        Person(*random.sample(range(data.NUMBER_OF_FLOORS), 2), data.NUMBER_OF_FLOORS)
        for _ in range(data.NUMBER_OF_PEOPLE)
    ]


def place_people(people: data.People) -> data.People_queues:
    """
    Place people on their respective starting floors
    """
    matrix: data.People_queues = [[] for _ in range(data.NUMBER_OF_FLOORS)]
    for person in people:
        matrix[person.start_floor].append(person)

    return matrix


CONST_PEOPLE_LIST: data.People = init_people()

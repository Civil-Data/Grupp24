" Main program module "

from typing import List
import data
import random
import copy
from icecream import ic
from evolutionary_classes.fitness import Fitness
from evolutionary_classes.populate import Populate
from evolutionary_classes.selection import Selection
from evolutionary_classes.crossover import Crossover
from evolutionary_classes.mutation import Mutation
from main_classes.building import Building
from main_classes.person import Person

def run_evolution(
    populate_function: data.PopulateFunction,
    fitness_function: data.FitnessFunction,
    selection_function: data.SelectionFunction,
    crossover_function: data.CrossoverFunction,
    mutation_functions: List[data.MutationFunction],
) -> None:
    """
    Run the evolution
    """

    # Get an initial population
    population: data.Population = populate_function()

    # Loop over the generations
    for _ in range(data.GENERATION_LIMIT):

        # Loop over the genomes
        for genome in population:
            # Always reset to original state between the genome iterations
            people_list: data.People = copy.deepcopy(CONST_PEOPLE_LIST)
            building: Building = Building(place_people(people_list))
            genome.people = people_list

            # Loop over the floors
            for floor in genome.genome:
                building.move_elevator(building.elevator.current_floor, floor)

            next_population: data.Population = []

            while len(next_population) < data.POPULATION_SIZE:
                # Only deal with even populations for now
                assert data.POPULATION_SIZE % 2 == 0 
                
                # Select two parents
                parents = selection_function(population, fitness_function)
                # Breed two children from those parents
                children = crossover_function(parents[0], parents[1])

                # A chance to individually apply a random mutation to the children
                for child in children:
                    if data.MUTATION_CHANCE > random.uniform(0.0, 1.0):
                        mutation_functions[random.randint(0, len(mutation_functions) - 1)](child)

                # Add the children to the next generation
                next_population += children

            assert len(next_population) == data.POPULATION_SIZE

            # Update the population
            population = next_population

def init_people() -> data.People:
    """
    Get a list of people with random start and end floors
    """
    return [Person(*random.sample(range(data.NUMBER_OF_FLOORS), 2)) for _ in range(data.NUMBER_OF_PEOPLE)]

def place_people(people: data.People) -> data.People_queues:
    """
    Place people on their respective starting floors
    """
    matrix: data.People_queues = [[] for _ in range(data.NUMBER_OF_FLOORS)]
    for person in people:
        matrix[person.start_floor].append(person)
    
    return matrix

CONST_PEOPLE_LIST: data.People = init_people()

if __name__ == "__main__":

    run_evolution(
        populate_function = Populate.generate_population,
        fitness_function = Fitness.calc_fitness,
        selection_function = Selection.rank,
        crossover_function = Crossover.swap_last_halves,
        mutation_functions = [Mutation.swap]
    )

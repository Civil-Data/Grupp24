" Main program module "

from typing import List, Tuple
import data
import random
import copy
import math
#from icecream import ic
from evolutionary_classes.fitness import Fitness
from evolutionary_classes.populate import Populate
from evolutionary_classes.selection import Selection
from evolutionary_classes.crossover import Crossover
from evolutionary_classes.mutation import Mutation
from genome import Genome
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
        
        # All genomes has been run. Prepare the next population of genomes

        next_population: data.Population = []

        # Elitism
        numb_elitism_parents: int = math.floor(data.POPULATION_SIZE * data.ELITISM_PERC)
        # If odd, increase by 1
        if numb_elitism_parents % 2 == 1:
            numb_elitism_parents += 1
        # If that +1 pushes it over the population size
        if numb_elitism_parents > data.POPULATION_SIZE:
            numb_elitism_parents = data.POPULATION_SIZE
        
        assert 0 <= numb_elitism_parents <= data.POPULATION_SIZE

        if numb_elitism_parents > 0:
            # Calculate fitness for each genome
            fitness_scores: List[Tuple[Genome, int]] = [(genome, fitness_function(genome)) for genome in population]

            # Sort the genomes based on the fitness
            ranked_population: List[Tuple[Genome, int]] = sorted(
                fitness_scores,
                key=lambda x: x[1], # 'x' is a tuple, [1] is indexing to the int. I.e. sort based on the int value
                reverse=True # Highest score first
            )

            for i in range(numb_elitism_parents):
                next_population.append(ranked_population[i][0]) # index 0 accesses the Genome object of the Tuple

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

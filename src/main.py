" Main program module "

from typing import List, Tuple
import random
import copy
import math
import data

# from icecream import ic
from evolutionary_classes.fitness import Fitness
from evolutionary_classes.populate import Populate
from evolutionary_classes.selection import Selection
from evolutionary_classes.crossover import Crossover
from evolutionary_classes.mutation import Mutation
from genome import Genome
from main_classes.building import Building
from gui.elevator_simulation import run_simulation
from init_and_place_people import CONST_PEOPLE_LIST, place_people


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
    for generation in range(data.GENERATION_LIMIT):

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

        # Calculate fitness for each genome
        for genome in population:
            fitness_function(genome)

        # Sort the genomes based on the fitness
        ranked_population: data.Population = sorted(
            population,  # The population to be sorted
            key=lambda genome: genome.fitness_score,  # Sort based on fitness score
            reverse=True,  # Highest score first
        )

        print(
            f"Gen {generation}   Top three genomes (fitness,length):   ({ranked_population[0].fitness_score},{len(ranked_population[0].genome)}) ({ranked_population[1].fitness_score},{len(ranked_population[1].genome)}) ({ranked_population[1].fitness_score},{len(ranked_population[1].genome)})"
        )

        # Check if we have achieved the max possible score, then break off
        if ranked_population[0].fitness_score == data.MAXIMUM_POSSIBLE_SCORE:
            print("Maximum possible score achieved")
            run_simulation(ranked_population[0])
            break

        next_population: data.Population = []

        # Elitism
        if data.ELITISM_PERC > 0.0:
            # not neccessary to check data.ELITISM_PERC, but it looks nicer and saves some time
            numb_elitism_parents: int = math.floor(
                data.POPULATION_SIZE * data.ELITISM_PERC
            )
            # If odd, increase by 1
            if numb_elitism_parents % 2 == 1:
                numb_elitism_parents += 1
            # If that +1 pushes it over the population size
            if numb_elitism_parents > data.POPULATION_SIZE:
                numb_elitism_parents = data.POPULATION_SIZE

            assert 0 <= numb_elitism_parents <= data.POPULATION_SIZE
            assert numb_elitism_parents % 2 == 0

            if numb_elitism_parents > 0:  # <==> numb_elitism_parents >= 2
                for i in range(numb_elitism_parents):
                    next_population.append(ranked_population[i])

        while len(next_population) < data.POPULATION_SIZE:
            # Only deal with even populations for now
            assert data.POPULATION_SIZE % 2 == 0

            # Select two parents
            parents: Tuple[Genome, Genome] = selection_function(ranked_population)
            # Breed two children from those parents with a chance for crossover
            children: Tuple[Genome, Genome]
            if data.CROSSOVER_CHANCE > random.uniform(0.0, 1.0):
                children = crossover_function(parents[0], parents[1])
            else:
                children = parents

            # A chance to individually apply a random mutation to the children
            for child in children:
                if data.MUTATION_CHANCE > random.uniform(0.0, 1.0):
                    mutation_functions[random.randint(0, len(mutation_functions) - 1)](
                        child
                    )

            # Add the children to the next generation
            next_population += children

        assert len(next_population) == data.POPULATION_SIZE

        # Update the population
        population = next_population


if __name__ == "__main__":

    run_evolution(
        populate_function=Populate.generate_population,
        fitness_function=Fitness.calc_fitness,
        selection_function=Selection.rank,
        crossover_function=Crossover.swap_last_halves,
        mutation_functions=[Mutation.swap, Mutation.increase_genome_length],
    )

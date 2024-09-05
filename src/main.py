" Main program module "

from typing import Tuple
from data import Data
from evolutionary_classes.fitness import Fitness
from evolutionary_classes.populate import Populate
from evolutionary_classes.selection import Selection
from evolutionary_classes.crossover import Crossover
from evolutionary_classes.mutation import Mutation

def run_evolution(
       populate_function: Data.PopulateFunction,
       fitness_function: Data.FitnessFunction,
       #fitness_goal: int,
       selection_function: Data.SelectionFunction,
       crossover_function: Data.CrossoverFunction,
       mutation_function: Data.MutationFunction,
       generation_limit: int = 100
) -> Tuple[Data.Population, int]:
    """
    Run the evolution
    """
    # Get an initial population
    population: Data.Population = populate_function

    # Loop over the generations
    for i in range(generation_limit):

        # Sort the population based on the fitness function
        population = sorted(
            Data.Population,
            key=fitness_function(),
            reverse=True # In descending order
        )

        #if fitness_function(population[0] >= fitness_goal):
        #    break

        # Elitism, directly carry over the absolute top two person to the next generation
        next_population: Data.Population = population[0:2]

        for _ in range(len(population) // 2 - 1):
            # Select two parents
            parents = selection_function(population, fitness_function)

            # Breed two children from those parents
            offsprings = crossover_function(parents[0], parents[1])

            # Eventually apply a mutation to the children
            offsprings[0] = mutation_function(offsprings[0])
            offsprings[1] = mutation_function(offsprings[1])

            # Add the children to the next generation
            next_population += offsprings

        # Update the population and run the process again
        population = next_population

    return population, i

if __name__ == "__main__":
    # Entry point to the main program
    popultion, i = run_evolution(
        populate_function = Populate.generate_population,
        fitness_function = Fitness.calc_fitness,
        #fitness_goal = int,
        selection_function = Selection.,
        crossover_function = Crossover.,
        mutation_function = Mutation.,
        generation_limit = 100
    )

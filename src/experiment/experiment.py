import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

import json
import data
import matplotlib.pyplot as plt

from evolutionary_classes.fitness import Fitness
from evolutionary_classes.populate import Populate
from evolutionary_classes.selection import Selection
from evolutionary_classes.crossover import Crossover
from evolutionary_classes.mutation import Mutation
from main_classes.person import Person
from genome import Genome


class ExperimentElevator:

    def __init__(self, people_path, generation_path) -> None:
        self.people_list: data.People_queues = people_path
        self.generation_list: data.Population = generation_path

    def display_experiment(self, name, results) -> None:
        generation = [res[0] for res in results]
        fitness_score = [res[1] for res in results]
        genome_length = [res[2] for res in results]
        plt.plot(generation, fitness_score, label="Fitness Score", color="blue")
        plt.plot(generation, genome_length, label="Genome Length", color="green")
        plt.title(f"Experiment : {name}")
        plt.xlabel("Generation")
        plt.ylabel("Value")
        plt.legend()
        # Show experiment graph after every run
        # plt.show()


def load_population(filename) -> data.Population:
    """
    Loading in data from a json file
    """
    with open(filename, "r") as file:
        data = json.load(file)

    genome_list = [Genome(genome_data) for genome_data in data]

    return genome_list


def load_building(filename) -> data.People:
    with open(filename, "r") as file:
        data = json.load(file)

    building_list = [Person.from_json(person_data) for person_data in data]

    return building_list


def save_to_excel(results, output_file):
    """
    Function to save results to external output
    """
    data = []

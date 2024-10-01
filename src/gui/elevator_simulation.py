# Author: Joel Scarinius Stävmo, Oskar Sundberg, Linus Savinainen, Samuel Wallander Leyonberg  and Gustav Pråmell
# Update: October 1, 2024
# Version: 1.0.0
# License: Apache 2.0

"""
This module contains the code to run a visual simulation of the elevator using the best genome.
"""

import os
import time
import copy
import pygame
import data
from genome import Genome
from main_classes.building import Building
from init_and_place_people import CONST_PEOPLE_LIST, place_people
from experiment.experiment import load_building

# Constants for Pygame
FPS = 60
ELEVATOR_SPEED = data.NUMBER_OF_FLOORS

pygame.init()
# Set dynamic GUI resolution
SCREEN_INFO = pygame.display.Info()
WINDOW_HEIGHT: int = int(SCREEN_INFO.current_h * 0.85)
WINDOW_WIDTH: int = int(WINDOW_HEIGHT * 0.7)

# Proportions for dynamic sizing
FLOOR_HEIGHT_PROPORTION = 1 / data.NUMBER_OF_FLOORS  # Dynamic based on number of floors
FLOOR_WIDTH_PROPORTION = 0.5     # 50% of window width
ELEVATOR_HEIGHT_PROPORTION = FLOOR_HEIGHT_PROPORTION
ELEVATOR_WIDTH_PROPORTION = ELEVATOR_HEIGHT_PROPORTION
EXIT_BUTTON_SIZE = int(0.05 * WINDOW_WIDTH)

def run_simulation(best_genome: Genome) -> None:
	"""
	Run a visual simulation of the elevator using the best genome.
	"""
	# Initialize Pygame and the screen settings
	screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # Windowed mode
	pygame.display.set_caption("Elevator Simulation")
	font = pygame.font.SysFont(None, 50)
	clock = pygame.time.Clock()

	# Calculate dynamic sizes
	floor_height = int(WINDOW_HEIGHT * FLOOR_HEIGHT_PROPORTION)
	floor_width = int(WINDOW_WIDTH * FLOOR_WIDTH_PROPORTION)
	elevator_width = int(WINDOW_WIDTH * ELEVATOR_WIDTH_PROPORTION)
	elevator_height = int(WINDOW_HEIGHT * ELEVATOR_HEIGHT_PROPORTION)

	if data.DO_EXP:
		people_experiment = list(os.listdir('./buildings'))
		assert len(people_experiment) == 1
		people_list: data.People = copy.deepcopy(load_building(f"./buildings/{people_experiment[0]}"))
	else:
		people_list: data.People = copy.deepcopy(CONST_PEOPLE_LIST)
	building: Building = Building(place_people(people_list))

	assert len(best_genome.people) == len(people_list) == len(CONST_PEOPLE_LIST)

	# Keeps track of the elevator position
	elevator_pos = [
		(WINDOW_WIDTH - elevator_width) // 2 + int(floor_width * 0.2),
		WINDOW_HEIGHT - floor_height - elevator_height,
	]

	# Calculate the building position
	building_x = (WINDOW_WIDTH - int(WINDOW_WIDTH * FLOOR_WIDTH_PROPORTION)) // 2
	building_y = WINDOW_HEIGHT - (data.NUMBER_OF_FLOORS * floor_height)

	# Initialize a list to keep track of people who have arrived at their desired floor
	people_arrived = [0 for _ in range(data.NUMBER_OF_FLOORS)]

	# Track the number of people inside the elevator
	elevator_passengers: data.People = []

	running = True
	for floor in best_genome.genome:
		if not running:
			break

		# Place these two simulation loops here at the top to accurately display the final
		# numbers, but the numbers will update before the elevator visually reaches the floors

		# If instead placed just beneath and outside the 'while elevator_pos[1] != target_y:' loop,
		# the numbers will naturally update as the elevator visually reaches a floor, but not
		# accurately display the final numbers

		# Pick your poison :)

		# Simulate dropping off passengers
		passengers_to_drop = [p for p in elevator_passengers if p.end_floor == floor]
		for passenger in passengers_to_drop:
			elevator_passengers.remove(passenger)
			people_arrived[floor] += 1

		# Simulate picking up people from the current floor
		people_to_pick_up: data.People = building.people_queues[floor]
		picked_up = 0
		while people_to_pick_up and len(elevator_passengers) < data.ELEVATOR_CAPACITY:
			person = people_to_pick_up.pop(0)
			elevator_passengers.append(person)
			picked_up += 1

		target_y = building_y + (data.NUMBER_OF_FLOORS - floor - 1) * floor_height

		while elevator_pos[1] != target_y:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:  # Check for the quit event
					running = False
				elif event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:  # Left mouse button
						if exit_button_rect.collidepoint(event.pos):
							running = False

			if elevator_pos[1] < target_y:
				elevator_pos[1] += min(ELEVATOR_SPEED, target_y - elevator_pos[1])
			elif elevator_pos[1] > target_y:
				elevator_pos[1] -= min(ELEVATOR_SPEED, elevator_pos[1] - target_y)

			screen.fill((75, 75, 75))

			# Draw the building frame
			pygame.draw.rect(
				screen,
				(0, 0, 0),
				(
					building_x,
					building_y,
					int(WINDOW_WIDTH * FLOOR_WIDTH_PROPORTION),
					data.NUMBER_OF_FLOORS * floor_height,
				),
				2,
			)

			# Draw the roof
			pygame.draw.line(
				screen,
				(0, 0, 0),
				(building_x, building_y),
				(building_x + int(WINDOW_WIDTH * FLOOR_WIDTH_PROPORTION), building_y),
				2,
			)

			# Draw the building label
			# building_label = font.render("Building 1", True, (255, 255, 255))
			# screen.blit(building_label, (building_x + 10, building_y - 40))

			# Draw the floor lines and labels
			for i in range(data.NUMBER_OF_FLOORS):
				pygame.draw.line(
					screen,
					(0, 0, 0),
					(building_x, building_y + i * floor_height),
					(building_x + int(WINDOW_WIDTH * FLOOR_WIDTH_PROPORTION), building_y + i * floor_height),
				)
				floor_label = font.render(f"Floor {i}", True, (255, 255, 255))
				screen.blit(
					floor_label,
					(
						building_x + 10,
						building_y + (data.NUMBER_OF_FLOORS - i - 1) * floor_height + 10,
					),
				)

				# Draw the number of people waiting on each floor
				people_waiting = len(building.people_queues[i])
				people_label = font.render(str(people_waiting), True, (255, 0, 0))
				screen.blit(
					people_label,
						(
							building_x - 30,
							building_y
								+ (data.NUMBER_OF_FLOORS - i - 1) * floor_height
								+ 10,
						),
				)

				# Draw the number of people who have arrived at their desired floor
				if people_arrived[i] > 0:
					arrived_label = font.render(
					str(people_arrived[i]), True, (0, 255, 0)
					)
					screen.blit(
						arrived_label,
						(
							building_x + floor_width + 10,
							building_y
								+ (data.NUMBER_OF_FLOORS - i - 1) * floor_height
								+ 10,
						),
					)

			# Draw the elevator and the number of passengers inside
			pygame.draw.rect(
				screen, (0, 0, 0), (*elevator_pos, elevator_width, elevator_height)
			)

			passenger_label = font.render(
				str(len(elevator_passengers)), True, (255, 255, 0)
			)
			screen.blit(
				passenger_label,
				(
					elevator_pos[0] + elevator_width // 2 - 10,
					elevator_pos[1] + elevator_height // 2 - 10,
				),
			)

			# Draw the exit button
			exit_button_rect = pygame.Rect(
				WINDOW_WIDTH - EXIT_BUTTON_SIZE - 10, 10, EXIT_BUTTON_SIZE, EXIT_BUTTON_SIZE
			)
			pygame.draw.rect(screen, (255, 0, 0), exit_button_rect)
			exit_label = font.render("X", True, (255, 255, 255))
			screen.blit(
				exit_label,
				(
					exit_button_rect.x + (EXIT_BUTTON_SIZE - exit_label.get_width()) // 2,
					exit_button_rect.y + (EXIT_BUTTON_SIZE - exit_label.get_height()) // 2,
				),
			)

			pygame.display.flip()
			clock.tick(FPS)


		print(
			f"Moved to floor: {floor} || Dropped off: {len(passengers_to_drop)} || Picked up: {picked_up}."
		)
		# Sleep to simulate the elevator waiting at each floor
		time.sleep(0.5)

	print("Simulation complete.")
	time.sleep(3)
	pygame.quit()

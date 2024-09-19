"""
This module contains the code to run a visual simulation of the elevator using the best genome.
"""

import time
import copy
import pygame
import data
from genome import Genome
from main_classes.building import Building
from init_and_place_people import CONST_PEOPLE_LIST, place_people

# Constants for Pygame
ELEVATOR_WIDTH = 100
ELEVATOR_HEIGHT = 100
FLOOR_WIDTH = 400
FPS = 60
ELEVATOR_CAPACITY = 8
ELEVATOR_SPEED = 10
EXIT_BUTTON_SIZE = 75


def run_simulation(best_genome: Genome) -> None:
	"""
	Run a visual simulation of the elevator using the best genome.
	"""
	# Initialize Pygame and the screen settings
	pygame.init()
	screen_info = pygame.display.Info()
	size = (screen_info.current_w, screen_info.current_h)
	screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
	pygame.display.set_caption("Elevator Simulation")
	font = pygame.font.SysFont(None, 50)
	clock = pygame.time.Clock()

	# Variables for Pygame window
	window_width = screen_info.current_w
	window_height = screen_info.current_h
	floor_height = size[1] // (data.NUMBER_OF_FLOORS + 1)
	# Copy the people list to avoid modifying the original list
	people_list: data.People = copy.deepcopy(CONST_PEOPLE_LIST)
	building: Building = Building(place_people(people_list))
	best_genome.people = people_list

	# Keeps track of the elevator position
	elevator_pos = [
		(window_width - FLOOR_WIDTH) // 2 + (FLOOR_WIDTH - ELEVATOR_WIDTH) // 2,
		window_height - floor_height,
	]

	# Calculate the building position
	building_x = (window_width - FLOOR_WIDTH) // 2
	building_y = (
		window_height - (data.NUMBER_OF_FLOORS * floor_height) - 50
	)  # Move the building down by 50 pixels

	# Initialize a list to keep track of people who have arrived at their desired floor
	people_arrived = [None] * data.NUMBER_OF_FLOORS  # None means no update needed

	# Track the number of people inside the elevator
	elevator_passengers = []

	# Define the exit button
	exit_button_rect = pygame.Rect(
		window_width - EXIT_BUTTON_SIZE - 10, 10, EXIT_BUTTON_SIZE, EXIT_BUTTON_SIZE
	)

	running = True
	for floor in best_genome.genome:
		if not running:
			break

		target_y = building_y + (data.NUMBER_OF_FLOORS - floor - 1) * floor_height

		while elevator_pos[1] != target_y:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				elif event.type == pygame.MOUSEBUTTONDOWN:
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
					FLOOR_WIDTH,
					data.NUMBER_OF_FLOORS * floor_height,
				),
				2,
			)

			# Draw the roof
			pygame.draw.line(
				screen,
				(0, 0, 0),
				(building_x, building_y),
				(building_x + FLOOR_WIDTH, building_y),
				2,
			)

			# Draw the building label
			building_label = font.render("Building 1", True, (255, 255, 255))
			screen.blit(building_label, (building_x + 10, building_y - 40))

			# Draw the floor lines and labels, also draw the number of people waiting and dropped off on each floor
			for i in range(data.NUMBER_OF_FLOORS):
				pygame.draw.line(
					screen,
					(0, 0, 0),
					(building_x, building_y + i * floor_height),
					(building_x + FLOOR_WIDTH, building_y + i * floor_height),
				)
				floor_label = font.render(f"Floor {i}", True, (255, 255, 255))
				screen.blit(
					floor_label,
					(
						building_x + 10,
						building_y
						+ (data.NUMBER_OF_FLOORS - i - 1) * floor_height
						+ 10,
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
				if people_arrived[i] is not None:
					arrived_label = font.render(
						str(people_arrived[i]), True, (0, 255, 0)
					)
					screen.blit(
						arrived_label,
						(
							building_x + FLOOR_WIDTH + 10,
							building_y
							+ (data.NUMBER_OF_FLOORS - i - 1) * floor_height
							+ 10,
						),
					)

			# Draw the elevator and the number of passengers inside
			pygame.draw.rect(
				screen, (0, 0, 0), (*elevator_pos, ELEVATOR_WIDTH, ELEVATOR_HEIGHT)
			)

			passenger_label = font.render(
				str(len(elevator_passengers)), True, (255, 255, 0)
			)
			screen.blit(
				passenger_label,
				(
					elevator_pos[0] + ELEVATOR_WIDTH // 2 - 10,
					elevator_pos[1] + ELEVATOR_HEIGHT // 2 - 10,
				),
			)

			# Draw the exit button
			pygame.draw.rect(screen, (255, 0, 0), exit_button_rect)
			exit_label = font.render("X", True, (255, 255, 255))
			screen.blit(
				exit_label,
				(
					exit_button_rect.x
					+ (EXIT_BUTTON_SIZE - exit_label.get_width()) // 2,
					exit_button_rect.y
					+ (EXIT_BUTTON_SIZE - exit_label.get_height()) // 2,
				),
			)

			pygame.display.flip()
			clock.tick(FPS)

		# Simulate dropping off passengers
		passengers_to_drop = [p for p in elevator_passengers if p.end_floor == floor]
		for passenger in passengers_to_drop:
			elevator_passengers.remove(passenger)
			people_arrived[floor] = (people_arrived[floor] or 0) + 1

		# Simulate picking up people from the current floor
		people_to_pick_up = building.people_queues[floor]
		picked_up = 0
		while people_to_pick_up and len(elevator_passengers) < ELEVATOR_CAPACITY:
			person = people_to_pick_up.pop(0)
			elevator_passengers.append(person)
			picked_up += 1

		print(
			f"Moved to floor: {floor} Dropped off: {len(passengers_to_drop)} and Picked up: {picked_up} passengers."
		)
		# Sleep to simulate the elevator waiting at each floor
		time.sleep(0.5)

	print("Simulation complete.")
	pygame.quit()

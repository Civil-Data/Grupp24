import time
import pygame
import copy
import data
from genome import Genome
from main_classes.building import Building
from shared import CONST_PEOPLE_LIST, place_people

pygame.init()
screen_info = pygame.display.Info()
size = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.display.set_caption("Elevator Simulation")
font = pygame.font.SysFont(None, 24)
clock = pygame.time.Clock()

# Constants for Pygame
WINDOW_WIDTH = screen_info.current_w
WINDOW_HEIGHT = screen_info.current_h
FLOOR_HEIGHT = size[1] // (data.NUMBER_OF_FLOORS + 1)
ELEVATOR_WIDTH = 50
ELEVATOR_HEIGHT = 50
FLOOR_WIDTH = 100
FPS = 180
ELEVATOR_CAPACITY = 8


def run_simulation(best_genome: Genome) -> None:
    """
    Run a visual simulation of the elevator using the best genome.
    """

    people_list: data.People = copy.deepcopy(CONST_PEOPLE_LIST)
    building: Building = Building(place_people(people_list))
    best_genome.people = people_list

    elevator_pos = [
        (WINDOW_WIDTH - FLOOR_WIDTH) // 2 + (FLOOR_WIDTH - ELEVATOR_WIDTH) // 2,
        WINDOW_HEIGHT - FLOOR_HEIGHT,
    ]

    building_x = (WINDOW_WIDTH - FLOOR_WIDTH) // 2
    building_y = (
        WINDOW_HEIGHT - (data.NUMBER_OF_FLOORS * FLOOR_HEIGHT) - 50
    )  # Move the building down by 50 pixels

    # Initialize a list to keep track of people who have arrived at their desired floor
    people_arrived = [None] * data.NUMBER_OF_FLOORS  # None means no update needed

    # Track the number of people inside the elevator
    elevator_passengers = []

    running = True
    for floor in best_genome.genome:
        if not running:
            break

        target_y = building_y + (data.NUMBER_OF_FLOORS - floor - 1) * FLOOR_HEIGHT

        while elevator_pos[1] != target_y:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if elevator_pos[1] < target_y:
                elevator_pos[1] += 1
            elif elevator_pos[1] > target_y:
                elevator_pos[1] -= 1

            screen.fill((75, 75, 75))

            # Draw the building frame
            pygame.draw.rect(
                screen,
                (0, 0, 0),
                (
                    building_x,
                    building_y,
                    FLOOR_WIDTH,
                    data.NUMBER_OF_FLOORS * FLOOR_HEIGHT,
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
            screen.blit(building_label, (building_x + 10, building_y - 30))

            for i in range(data.NUMBER_OF_FLOORS):
                pygame.draw.line(
                    screen,
                    (0, 0, 0),
                    (building_x, building_y + i * FLOOR_HEIGHT),
                    (building_x + FLOOR_WIDTH, building_y + i * FLOOR_HEIGHT),
                )
                floor_label = font.render(f"Floor {i}", True, (255, 255, 255))
                screen.blit(
                    floor_label,
                    (
                        building_x + 10,
                        building_y
                        + (data.NUMBER_OF_FLOORS - i - 1) * FLOOR_HEIGHT
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
                        + (data.NUMBER_OF_FLOORS - i - 1) * FLOOR_HEIGHT
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
                            + (data.NUMBER_OF_FLOORS - i - 1) * FLOOR_HEIGHT
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

            pygame.display.flip()
            clock.tick(FPS)

        # Simulate picking up people from the current floor
        people_to_pick_up = building.people_queues[floor]
        while people_to_pick_up and len(elevator_passengers) < ELEVATOR_CAPACITY:
            person = people_to_pick_up.pop(0)
            elevator_passengers.append(person)

        # Simulate dropping off passengers
        passengers_to_drop = [p for p in elevator_passengers if p.end_floor == floor]
        for passenger in passengers_to_drop:
            elevator_passengers.remove(passenger)
            people_arrived[floor] = (people_arrived[floor] or 0) + 1

        print(f"Elevator moved to floor {floor}")
        time.sleep(1)  # Add a delay to visualize the movement

    print("Simulation complete.")
    pygame.quit()

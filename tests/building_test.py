"""
Building module tests
"""

import sys
import os
import copy

# Add path to src directory 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main_classes.building import Building
from main import place_people, init_people
from main_classes.elevator import Elevator, data

def test_building():
    data.People = init_people()
    building = Building(place_people(copy.deepcopy(data.People)))
    
    assert building.elevator is not None
        

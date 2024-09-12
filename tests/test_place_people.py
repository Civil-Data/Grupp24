"""
place_people module tests
"""

import sys
import os
import copy

# Add path to src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import data
from main import place_people, init_people

def test_init_people():
    people = init_people()
    assert len(people) is data.NUMBER_OF_PEOPLE 

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Run this file: python api-example.py

Run with debugger from the beginning of the file:
    python -m ipdb api-example.py
    or
    python -m pdb api-example.py

Set a breakpoint at any line in the file to execute the python debugger:
    import ipdb; ipdb.set_trace()
    or with pdb
    import pdb; pdb.set_trace()

Challenge:
    Use the Star Wars API to get the following information and print it to the screen.

    Get the total number of the films.
    Name of each film.
    Total number of planets in each film.
    Name of each planet in each film.
    Find the longest starship in each film.
"""

import json
import os
import sys
import requests


class StarWarsClass(object):
    def __init__(self):
        self.base_url = 'http://swapi.co/api/'

    def get_planet_name(self, planet_id):
        rx = requests.get('%splanets/%s/' % (self.base_url, planet_id))
        json_data = rx.json()
        planet_name = json_data['name']
        return planet_name

    def run(self):
        # I'm passing the id of 1 to the get_planet_name function.
        # This method can be re-used in other parts of your program,
        # just send it a different planet id.
        planet_name = self.get_planet_name(1)
        print planet_name

if __name__ == "__main__":
    starwars = StarWarsClass()
    starwars.run()

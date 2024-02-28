'''
Author: Michael Stang
KUID: 3073983
Date: 04-02-2023
Lab: lab07
Last modified: 04-02-2023
Purpose: A class that holds data about pokemon
'''

class Pokemon:
    def __init__(self, name, japanese_name, pokedex_number):
        self.name = name
        self.japanese_name = japanese_name
        self.pokedex_number = pokedex_number
    
    def __lt__(self, other):
        if isinstance(other, Pokemon):
            return self.pokedex_number < other.pokedex_number
        elif isinstance(other, int):
            return self.pokedex_number < other

    def __gt__(self, other):
        if isinstance(other, Pokemon):
            return self.pokedex_number > other.pokedex_number
        elif isinstance(other, int):
            return self.pokedex_number > other

    def __eq__(self, other):
        if isinstance(other, Pokemon):
            return self.pokedex_number == other.pokedex_number
        elif isinstance(other, int):
            return self.pokedex_number == other
    
    def __le__(self, other):
        if isinstance(other, Pokemon):
            return self.pokedex_number <= other.pokedex_number
        elif isinstance(other, int):
            return self.pokedex_number <= other

    def __ge__(self, other):
        if isinstance(other, Pokemon):
            return self.pokedex_number >= other.pokedex_number
        elif isinstance(other, int):
            return self.pokedex_number >= other
    
    def __str__(self):
        return f'{self.name} ({self.japanese_name}) - {self.pokedex_number}'
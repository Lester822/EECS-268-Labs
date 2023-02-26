'''
Author: Michael Stang
KUID: 3073983
Date: 02-17-2023
Lab: lab04
Last modified: 02-17-2023
Purpose: A basic Node class (with an added method to make printing lists look good)
'''

class Node:
    def __init__(self, entry):
        self.entry = entry
        self.next = None

    def __repr__(self):  # This just makes printing lists look good...
        if self.next == None:
            return f'{self.entry}'
        else:
            return f'{self.entry}, {self.next}'

'''
Author: Michael Stang
KUID: 3073983
Date: 02-10-2023
Lab: lab03
Last modified: 02-10-2023
Purpose: A basic node, used in the queue and stack
'''

class Node:
    def __init__(self, entry):
        self.entry = entry
        self.next = None

    def __str__(self):  # Only here to make printing things with nodes look nicer
        if self.next is not None:
            return f'{self.entry},{self.next}'
        else:
            return f'{self.entry}'

    def __repr__(self):
        return f'{self.entry},{self.next}'
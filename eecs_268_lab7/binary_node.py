'''
Author: Michael Stang
KUID: 3073983
Date: 04-02-2023
Lab: lab07
Last modified: 04-02-2023
Purpose: An implementation of a Binary Node
'''

class BinaryNode:
    def __init__(self, entry):
        self.entry = entry
        self.left = None
        self.right = None
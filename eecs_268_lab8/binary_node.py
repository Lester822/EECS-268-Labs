'''
Author: Michael Stang
KUID: 3073983
Date: 04-21-2023
Lab: lab08
Last modified: 04-02-2023
Purpose: Basic class for a Binary Node
'''

class BinaryNode:
    def __init__(self, entry):
        self.entry = entry
        self.left = None
        self.right = None
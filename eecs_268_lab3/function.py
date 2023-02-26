'''
Author: Michael Stang
KUID: 3073983
Date: 02-10-2023
Lab: lab03
Last modified: 02-10-2023
Purpose: A class that represents a function running within a process
'''

class Function:
    def __init__(self, name,*, handle_exceptions='yes'):
        self.name = name
        self.handle_exception = handle_exceptions

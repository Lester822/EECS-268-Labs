'''
Author: Michael Stang
KUID: 3073983
Date: 02-10-2023
Lab: lab03
Last modified: 02-10-2023
Purpose: A class that represents a running process in the 'cpu'
'''

from stack import Stack
from function import Function


class Process:
    def __init__(self, name):
        self.name = name
        print(f'{self.name} starting')
        self.stack = Stack()
        self.stack.push(Function('main', handle_exceptions='no'))

    def add_function(self, name, exception):
        self.stack.push(Function(name, handle_exceptions=exception))
        print(f'{self.name} calls {name}')

    def remove_function(self):
        return self.stack.pop()

    def raise_function(self):
        print(f'{self.name} encountered a raised exception by: {self.stack.peek().name}')
        while self.stack.peek().handle_exception == 'no':  # Repeats until a function is able to handle it
            print(f'{self.name} ends {self.stack.peek().name} due to unhandled exception')
            self.stack.pop()
        print(f'{self.name} has exception handled by: {self.stack.peek().name}')
    
    def __repr__(self):
        return(f'[PROCESS: {self.name} ({self.stack})]')

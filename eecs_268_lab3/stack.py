'''
Author: Michael Stang
KUID: 3073983
Date: 02-10-2023
Lab: lab03
Last modified: 02-10-2023
Purpose: A basic class that implements a node-based stack system
'''

from node import Node


class Stack:
    def __init__(self):
        self.top = None

    def push(self, entry):
        new_node = Node(entry)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.is_empty():
            new_first = self.top.next
            current_first = self.top
            self.top = new_first
            return current_first.entry
        else:
            raise RuntimeError('Pop called on an empty stack')

    def peek(self):
        if not self.is_empty():
            return self.top.entry
        else:
            raise RuntimeError('Peek called on an empty stack')

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

    def __str__(self):
        return f'<{self.top}>'

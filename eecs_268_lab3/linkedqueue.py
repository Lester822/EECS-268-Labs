'''
Author: Michael Stang
KUID: 3073983
Date: 02-10-2023
Lab: lab03
Last modified: 02-10-2023
Purpose: A basic class that implements a node-based queue system
'''

from node import Node


class LinkedQueue:
    def __init__(self):
        self._front = None
        self._back = None


    def enqueue(self, entry):
        new_node = Node(entry)
        if self._front == None:
            self._front = new_node
            self._back = new_node
        else:
            self._back.next = new_node
            self._back = self._back.next


    def dequeue(self):
        if self._front == None:
            raise RuntimeError('Tried to dequeue an empty queue.')
        elif self._front is self._back:
            value = self._front.entry
            self._front = None
            self._back = None
            return value
        else:
            value = self._front.entry
            self._front = self._front.next
            return value


    def peek_front(self):
        if not self.is_empty():
            return self._front
        else:
            raise RuntimeError('Tried to peek an empty queue')


    def is_empty(self):
        if self._front is None:
            return True
        else:
            return False


    def __str__(self):  # Makes printing queues look better
        return f'|{self._front}|'

'''
Author: Michael Stang
KUID: 3073983
Date: 02-17-2023
Lab: lab04
Last modified: 02-17-2023
Purpose: A basic List class (with some extra methods to make printing them look better and give more info).
'''

from node import Node

class LinkedList:
    def __init__(self):
        self._front = None
        self._length = 0

    def length(self):
        """Return the length value"""
        return self._length

    def insert(self, index, entry):
        """Insert a new node into the list"""

        if self.length() == 0:  # if the list is empty
            if index == 0:  # if the desired node to insert is the first
                self._front = Node(entry)
            else:
                raise IndexError(f'Invalid index [{index}] chosen for LinkedList insert method.')

        else:
            if index > 0 and index <= (self.length()):  # if the index given is a valid choice
                before = self._front
                for num in range(index - 1):  # sets before equal to the value before where we want to insert
                    before = before.next
                after = before.next
                before.next = Node(entry)
                before.next.next = after

            elif index == 0:
                before = self._front
                self._front = Node(entry)
                self._front.next = before

            else:
                raise IndexError(f'Invalid index [{index}] chosen for LinkedList insert method.')

        self._length += 1

    def remove(self, index):
        """Remove a node from the list"""

        if index == 0 and self.length() > 0:
            if self.length == 1:
                self._front = None
            else:
                second = self._front.next
                self._front = second

        elif index > 0 and index <= (self.length() - 1):
            jumper = self._front
            for step in range(index-1):
                jumper = jumper.next
            after = jumper.next.next
            jumper.next = after

        else:
            raise IndexError(f'Invalid index [{index}] chosen for LinkedList remove method.')

        self._length -= 1

    def get_entry(self, index):
        """Return the entry in the node at the given index"""
        if index >= 0 and index <= (self.length() - 1) and self.length() > 0:
            current = self._front
            for num in range(index):
                current = current.next
            return current.entry
        else:
            raise IndexError(f'Invalid index [{index}] chosen for LinkedList get_entry method.')

    def set_entry(self, index, entry):
        """ Set the value of a node at index to entry"""
        if index >= 0 and index <= (self.length() - 1) and self.length() > 0:
            current = self._front
            for num in range(index):
                current = current.next
            current.entry = entry
        else:
            raise IndexError(f'Invalid index [{index}] chosen for LinkedList set_entry method.')

    def clear(self):
        """ Clear the list of all values"""
        self._front = None
        self._length = 0

    def __str__(self):
        """ Make sure printing string looks good"""
        if self._front is not None:
            return f'[{self._front}]'
        else:
            return '[]'

'''
Author: Michael Stang
KUID: 3073983
Date: 02-17-2023
Lab: lab04
Last modified: 02-17-2023
Purpose: The main class controlling the browser functions
'''

from linkedlist import LinkedList


class Browser:
    def __init__(self):
        self._current = None
        self._history = LinkedList()

    def navigate_to(self, url):
        """ Change the current focus and add new url"""
        if self._current is not None:
            self._history.insert(self._current + 1, url)
            self._current += 1
            if self._current != self._history.length()-1:
                for num in range(self._current+1, self._history.length())[::-1]:
                    self._history.remove(num)
        else:  # if it is the first URL visited
            self._history.insert(0, url)
            self._current = 0

    def forward(self):
        """ Push focus forward"""
        if (self._history.length() - 1) > self._current:
            self._current += 1

    def back(self):
        """ Push focus (current) back"""
        if self._current > 0 and self._history.length() != 0:
            self._current -= 1

    def history(self):
        """ Print internet history to console"""
        print('Oldest\n===========')
        for num in range(self._history.length()):
            value = self._history.get_entry(num)
            if num == self._current:
                value += f' <==current'
            print(value)
        print('===========\nNewest\n')

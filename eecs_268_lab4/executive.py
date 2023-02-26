'''
Author: Michael Stang
KUID: 3073983
Date: 02-17-2023
Lab: lab04
Last modified: 02-17-2023
Purpose: The primary driver class that acts on functions from a given text file
'''

from linkedlist import LinkedList
from browser import Browser

class Executive:
    def __init__(self):
        filename = input('File Name: ')
        input_file = open(filename, 'r')
        commands = LinkedList()
        for line in input_file:
            commands.insert(commands.length(), line.strip())
        self.commands = commands
        self.browser = Browser()
    def run(self):
        """ Start the program anayzlzing commands"""
        for num in range(self.commands.length()):
            command = self.commands.get_entry(num)
            if command.split()[0].lower() == 'navigate':
                self.exec_navigate(command.split()[1])
            elif command.split()[0].lower() == 'back':
                self.exec_back()
            elif command.split()[0].lower() == 'forward':
                self.exec_forward()
            elif command.split()[0].lower() == 'history':
                self.exec_history()

    def exec_navigate(self, url):
        """ Control browser class to navigate"""
        self.browser.navigate_to(url)

    def exec_forward(self):
        """ Control browser class to go forward"""
        self.browser.forward()

    def exec_back(self):
        """ Control browser class to go back"""
        self.browser.back()

    def exec_history(self):
        """ Control browser class to print history"""
        self.browser.history()

'''
Author: Michael Stang
KUID: 3073983
Date: 04-23-2023
Lab: lab09
Last modified: 04-23-2023
Purpose: The main class that runs the program
'''

from maxheap import MaxHeap
from patient import Patient

class Executive:
    def __init__(self):
        filename = input("FILENAME >> ")
        command_file = open(filename, "r")
        self.commands = []
        for line in command_file:
            self.commands.append(line.strip().split())  # This leads to a list of lists, with each list being the command and its arguments
        self.hospital_queue = MaxHeap()
        self.patient_count = 0
    
    def run(self):
        for command in self.commands:
            if command[0].lower() == 'next':
                self.next()
            elif command[0].lower() == 'treat':
                self.treat()
            elif command[0].lower() == 'count':
                self.count_com()
            elif command[0].lower() == 'arrive':
                self.arrive(command)
    
    def next(self):
        print(f"Next Patient:\n{self.hospital_queue.peek()}")

    def treat(self):
        self.hospital_queue.remove()

    def count_com(self):
        count = len(self.hospital_queue)
        print(f"There are {count} patients waiting.")

    def arrive(self, command):
        self.patient_count += 1
        self.hospital_queue.add(Patient(command[1], command[2], command[3], command[4], command[5], self.patient_count))
        
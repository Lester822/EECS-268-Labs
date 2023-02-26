'''
Author: Michael Stang
KUID: 3073983
Date: 02-10-2023
Lab: lab03
Last modified: 02-10-2023
Purpose: The main driver of the program, processes commands in given file
'''

from process import Process
from linkedqueue import LinkedQueue

class Executive:
    def __init__(self):
        wanted_file = input('File name: ')  # Gets desired file from user
        input_file = open(wanted_file, 'r')
        commands = []  # Will store each command
        for line in input_file:
            commands.append(line.strip())
        self.commands = commands

    def process(self):
        process_queue = LinkedQueue()
        for command in self.commands:  # Goes through each line of the input file
            print(process_queue)
            split_line = command.split()  # Splits the string -> List

            if split_line[0].lower() == 'start':  # If the command is 'start'
                new_process = Process(split_line[1])
                process_queue.enqueue(new_process)

            elif split_line[0].lower() == 'call':  # If the command is 'call'
                try:
                    process_queue.peek_front().entry.add_function(split_line[1], split_line[2])
                    old_process = process_queue.dequeue()
                    process_queue.enqueue(old_process)
                except:
                    print('ERROR: No process created.')

            elif split_line[0].lower() == 'return': # If the command is 'return'
                try:
                    print(f'{process_queue.peek_front().entry.name} has {process_queue.peek_front().entry.remove_function().name} return')
                    if process_queue.peek_front().entry.stack.is_empty(): # Checks if there are still functions running
                        print(f'{process_queue.peek_front().entry.name} process has ended')
                        process_queue.dequeue()
                    else:  # Takes current process to end of queue
                        old_process = process_queue.dequeue()
                        process_queue.enqueue(old_process)
                        
                except:
                    print('ERROR: No process created.')

            elif split_line[0].lower() == 'raise': # If the command is 'raise'
                try:
                    process_queue.peek_front().entry.raise_function()
                    if process_queue.peek_front().entry.stack.is_empty():  # Checks if there are still functions running
                        print(f'{process_queue.peek_front().entry.name} process has ended')
                        process_queue.dequeue()
                    else:
                        old_process = process_queue.dequeue()
                        process_queue.enqueue(old_process)
                except:
                    print('ERROR: No process created.')
            else:
                print('Invalid command')
            

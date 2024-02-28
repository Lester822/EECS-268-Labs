'''
Author: Michael Stang
KUID: 3073983
Date: 04-21-2023
Lab: lab08
Last modified: 04-02-2023
Purpose: Starts the program
'''

from driver import Executive

def main():
# Creating an instance of the Executive class and then calling the run method on that instance.
    my_poke_tree = Executive()
    my_poke_tree.run()
    
main()
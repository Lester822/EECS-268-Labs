'''
Author: Michael Stang
KUID: 3073983
Date: 02-17-2023
Lab: lab04
Last modified: 02-17-2023
Purpose: Starts the program and hands off to executive
'''

from linkedlist import LinkedList
from executive import Executive

def main():
    """ Start program and hand it off to an executive class"""
    my_browser = Executive()   # hands control over to a driver class
    my_browser.run()


if __name__ == '__main__':
    main()

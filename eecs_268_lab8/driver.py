'''
Author: Michael Stang
KUID: 3073983
Date: 04-21-2023
Lab: lab08
Last modified: 04-07-2023
Purpose: Runs the programs commands
'''

from binary_search_tree import BinarySearchTree
from pokemon import Pokemon

class Executive:
    def __init__(self):
        self.filename = None
        self.poke_tree = None
        self.current_tree = None
    
    def get_filename(self):
        '''Return a string from the user of the desired filename'''
        filename = input("Filename: ")
        return filename
    
    def assemble(self):
        '''Gets information from given filename and put into self.filename and self.poke_tree'''
        self.filename = self.get_filename()
        self.poke_tree = BinarySearchTree()
        input_file = open(self.filename, 'r')
        for line in input_file:
            split_line = line.strip().split()
            poke_name = split_line[0]
            poke_id = int(split_line[1])
            poke_japanese_name = split_line[2]
            try:
                self.poke_tree.add(Pokemon(poke_name, poke_japanese_name, poke_id))
            except ValueError:
                pass
        input_file.close()

    def print_menu(self):
        '''Print the menu options to console'''
        print(f'\n\nEnter command:\n1) Search: Get pokemon information based on Pokedex ID\n2) Add: Add a new pokemon to the pokedex\n3) Print: Print the entire pokedex in "pre," "in," or "post" ordering.\n4) Copy: Create a copy of the current tree\n5) Remove: Removes a pokedex id from the tree\n6) Quit: Ends the program\n\n')

    def run(self):
        '''Start the program including getting the user's request for menu options'''
        self.assemble()
        user_req = ''
        while user_req.lower() != 'quit' and user_req != '6':
            self.print_menu()
            user_req = input('>> ')
            if user_req.lower() == 'search' or user_req == '1':
                self.choose_tree()
                self.search_command()
            elif user_req.lower() == 'add' or user_req == '2':
                self.choose_tree()
                self.add_command()
            elif user_req.lower() == 'print' or user_req == '3':
                self.choose_tree()
                self.print_command()
            elif user_req.lower() == 'copy' or user_req == '4':
                self.copy_tree()
            elif user_req.lower() == 'remove' or user_req == '5':
                self.remove_tree()
            elif user_req.lower() == 'quit' or user_req == '6':
                pass
            else:
                print('INVALID COMMAND!')

    def choose_tree(self):
        '''Set self.current_tree to self.poke_tree or self.copy_tree based on user input'''
        if self.poke_tree.copy_tree != None:  # Checks to see if there is a copied tree
            tree_choice = ""
            while tree_choice != 'original' and tree_choice != 'copy':  # Checks to see if user input is valid
                tree_choice = input('Use original tree or copy? ["original"/"copy"]: ')  # Gets user choice for which tree
                if tree_choice.lower() == 'original':
                    self.current_tree = self.poke_tree
                elif tree_choice.lower() == 'copy':
                    self.current_tree = self.poke_tree.copy_tree
                else:
                    print('INVALID CHOICE!')
        else:
            self.current_tree = self.poke_tree

    def search_command(self):
        '''Print information about a pokemon based on user_req'''
        target = int(input('Pokedex ID: '))
        try:
            print(self.current_tree.search(target))
        except:
            print('Not in tree.\n')
    
    def add_command(self):
        '''Add pokemon to self.poke_tree'''
        poke_name = input('Pokemon Name: ')
        poke_japanese_name = input('Japense Pokemon Name: ')
        pokedex_id = int(input("Pokedex ID: "))
        try:
            self.current_tree.add(Pokemon(poke_name, poke_japanese_name, pokedex_id))
        except ValueError:
            print('Pokemon with that ID is already in the BST.')

    def print_command(self):
        '''Get user req for print order and then print to console'''
        user_input = input('Type ["pre"/"in"/"post"]: ')
        if user_input.lower() == 'pre':
            self.current_tree.preorder_action(print)
        elif user_input.lower() == 'in':
            self.current_tree.inorder_action(print)
        elif user_input.lower() == 'post':
            self.current_tree.postorder_action(print)
        else:
            print('INVALID COMMAND!')

    def copy_tree(self):
        try:
            self.poke_tree.copy()
        except Exception:
            print('Tree already copied.')
    
    def remove_tree(self):
        try:
            self.choose_tree()
            target = int(input('Pokedex ID: '))
            self.current_tree.remove(target)
        except KeyError:
            print('No copy to remove.')
        except ValueError:
            print('Invalid input.')
    
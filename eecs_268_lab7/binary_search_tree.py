'''
Author: Michael Stang
KUID: 3073983
Date: 04-02-2023
Lab: lab07
Last modified: 04-02-2023
Purpose: A class that implements a Binary Search Tree
'''

from binary_node import BinaryNode

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, entry):
        '''Public method to add to BST'''
        if self.root == None:
            self.root = BinaryNode(entry)
        else:
            self.rec_add(entry, self.root)
    
    def rec_add(self, entry, cur_node):
        '''Recursivly moves through a BST to add new entries, not meant to be public facing'''
        if cur_node.entry == entry:  # This is the case where the entry is already in the tree, it simply does nothing
            raise ValueError(f"Value {entry} already in Binary Search Tree.")

        elif cur_node.entry > entry:
            if cur_node.left == None:
                cur_node.left = BinaryNode(entry)
            else:
                self.rec_add(entry, cur_node.left)
                
        elif cur_node.entry < entry:
            if cur_node.right == None:
                cur_node.right = BinaryNode(entry)
            else:
                self.rec_add(entry, cur_node.right)
    
    def search(self, target):
        '''Public facing returns item with given keyvalue'''
        search_result = self.rec_search(target, self.root)
        if search_result == False:
            raise Exception(f'Value {target} not found in BST.')
        else:
            return search_result
    
    def rec_search(self, target, cur_node):
        '''Recurvisly navigates tree to return target'''
        if cur_node == None:
            return False
        elif cur_node.entry == target:
            return cur_node.entry
        else:
            if cur_node.entry > target:
                return self.rec_search(target, cur_node.left)
            elif cur_node.entry < target:
                return self.rec_search(target, cur_node.right)

    def preorder_action(self, action):
        '''Does "action" on all nodes in tree in pre-order'''
        self.rec_preorder_action(self.root, action)

    def rec_preorder_action(self, cur_node, action):
        '''Recurive function that goes through all nodes and does action in pre-order'''
        action(cur_node.entry)
        if cur_node.left != None:
            self.rec_preorder_action(cur_node.left, action)
        if cur_node.right != None:
            self.rec_preorder_action(cur_node.right, action)

    def inorder_action(self, action):
        '''Does "action" on all nodes in tree in in-order'''
        self.rec_inorder_action(self.root, action)
    
    def rec_inorder_action(self, cur_node, action):
        '''Recurive function that goes through all nodes and does action in in-order'''
        if cur_node.left != None:
            self.rec_inorder_action(cur_node.left, action)
        action(cur_node.entry)
        if cur_node.right != None:
            self.rec_inorder_action(cur_node.right, action)

    def postorder_action(self, action):
        '''Does "action" on all nodes in tree in post-order'''
        self.rec_postorder_action(self.root, action)

    def rec_postorder_action(self, cur_node, action):
        '''Recurive function that goes through all nodes and does action in post-order'''
        if cur_node.left != None:
            self.rec_postorder_action(cur_node.left, action)
        if cur_node.right != None:
            self.rec_postorder_action(cur_node.right, action)
        action(cur_node.entry)
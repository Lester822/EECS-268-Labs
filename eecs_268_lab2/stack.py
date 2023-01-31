from node import Node


class Stack:
    def __init__(self):
        self.top = None

    def push(self, entry):
        new_node = Node(entry)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.is_empty():
            new_first = self.top.next
            current_first = self.top
            self.top = new_first
            return current_first.entry
        else:
            raise RuntimeError

    def peek(self):
        if not self.is_empty():
            return self.top.entry
        else:
            raise RuntimeError

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

    def __str__(self):
        return f'<{self.top}>'

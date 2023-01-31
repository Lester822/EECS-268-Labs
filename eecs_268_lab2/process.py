from stack import Stack
from function import Function


class Process:
    def __init__(self, name):
        self.name = name
        print(f'{self.name} starting')
        self.stack = Stack()
        self.stack.push(Function('main', handle_exceptions='no'))

    def add_function(self, name, exception):
        self.stack.push(Function(name, handle_exceptions=exception))
        print(f'{self.name} calls {name}')

    def remove_function(self):
        return self.stack.pop()

    def raise_function(self):
        print(f'{self.name} encountered a raised exception by: {self.stack.peek().name}')
        while self.stack.peek().handle_exception == 'no':
            print(f'{self.name} ends {self.stack.peek().name} due to unhandled exception')
            self.stack.pop()
        print(f'{self.name} has exception handled by: {self.stack.peek().name}')
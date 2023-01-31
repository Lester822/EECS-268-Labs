class Node:
    def __init__(self, entry):
        self.entry = entry
        self.next = None

    def __str__(self):
        if self.next is not None:
            return f'{self.entry},{self.next}'
        else:
            return f'{self.entry}'

    def __repr__(self):
        return f'{self.entry},{self.next}'

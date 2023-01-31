from process import Process

class Executive:
    def __init__(self):
        wanted_file = input('File name: ')
        input_file = open(wanted_file, 'r')
        commands = []
        for line in input_file:
            commands.append(line.strip())
        self.commands = commands

    def process(self):
        for command in self.commands:
            split_line = command.split()

            if split_line[0].lower() == 'start':
                new_process = Process(split_line[1])

            if split_line[0].lower() == 'call':
                try:
                    new_process.add_function(split_line[1], split_line[2])
                except:
                    print('ERROR: No process created.')

            if split_line[0].lower() == 'return':
                try:
                    print(f'{new_process.name} has {new_process.remove_function().name} return')
                except:
                    print('ERROR: No process created.')

            if split_line[0].lower() == 'raise':
                try:
                    new_process.raise_function()
                except:
                    print('ERROR: No process created.')

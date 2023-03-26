from flood_map import FloodMap

class Executive:
    def __init__(self):
        filename = input('Filename: ')
        input_file = open(filename, 'r')
        lines = []
        for line in input_file:
            lines.append(line.replace('\n', ''))
        input_file.close()

        self.starting_pos = [int(lines[0].split()[0]), int(lines[0].split()[1])]
        self.water_amount = int(lines[1])
        self.text_map = []
        index = 0
        for line in lines[2:]:
            self.text_map.append([])
            for char in line:
                self.text_map[index].append(char)
            index += 1


    def run(self):
        my_map = FloodMap(self.starting_pos, self.water_amount, self.text_map)
        my_map.run()

    def __str__(self):
        return f'STARTING POS: {self.starting_pos}\nWATER AMOUNT: {self.water_amount}\n\nMAP: {self.text_map}'



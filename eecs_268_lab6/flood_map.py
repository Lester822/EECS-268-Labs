class FloodMap:
    def __init__(self, starting, water_amount, text_map):
        self.starting_pos = starting
        self.water_amount = water_amount
        self.text_map = text_map
        self.height = len(self.text_map)
        self.width = len(self.text_map[0])

    def create_visited_grid(self):
        visited_grid = []
        index = 0
        for line in self.text_map:
            visited_grid.append([])
            for char in line:
                visited_grid[index].append(0)
            index += 1
        return visited_grid

    def check_valid(self):
        if self.width <= 1:
            raise Exception('INVALID MAP SIZE. Map has 1 or less column.')
        if self.height <= 1:
            raise Exception('INVALID MAP SIZE. Map has 1 or less rows.')
        if self.text_map[self.starting_pos[0]][self.starting_pos[1]] == 'H':
            raise Exception('ERROR: STARTED ON HIGH GROUND')
        if self.starting_pos[0] > self.width - 1:
            raise Exception('Invalid Starting Position (outside map)')
        if self.starting_pos[1] > self.height - 1:
            raise Exception('Invalid Starting Position (outside map)')

    def recurse_flood(self, xpos, ypos):
        if not self.water_amount > 0:
            print('Flood ran out of water.')
        else:
            self.text_map[ypos][xpos] = '~'
            self.water_amount -= 1
            if self.text_map[ypos-1][xpos] == ' ':  # up
                self.recurse_flood(xpos, ypos-1)
            if self.text_map[ypos][xpos+1] == ' ':  # right
                self.recurse_flood(xpos+1, ypos)
            if self.text_map[ypos+1][xpos] == ' ':  # down
                self.recurse_flood(xpos, ypos+1)
            if self.text_map[ypos][xpos-1] == ' ':  #
                self.recurse_flood(xpos-1, ypos)

    def print_map(self):
        for item in self.text_map:
            output = ''
            for char in item:
                output += char
            print(output)

    def run(self):
        print(f'Size: {self.height}, {self.width}')
        print(f'Starting position: {self.starting_pos[0]}, {self.starting_pos[1]}')
        self.check_valid()
        self.recurse_flood(self.starting_pos[1], self.starting_pos[0])
        self.print_map()
        print('Flood complete')
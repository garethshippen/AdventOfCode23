class Cell():
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.energised = False

class Splitter(Cell):
    def __init__(self, x, y, symbol):
        super().__init__(x, y, symbol)
        self.split = True
    def turn_off(self):
        self.split = False
        
class Grid():
    def __init__(self, x_leng, y_leng):
        self.x_leng = x_leng # <--- needed?
        self.y_leng = y_leng
        self.grid = {}
        self.count = 0
        self.energised = 0
        self.rays = []
        
    def add_cell(self, cell):
        x = cell.x
        y = cell.y
        assert(x < self.x_leng and y < self.y_leng)
        self.grid[(x,y)] = cell
        self.count += 1
    def get_cell(self, x, y):
        return self.grid[(x,y)]
    def set_symbol(self, x, y, symbol):
        self.grid[(x,y)].symbol = symbol
    def get_symbol(self, x, y):
        return self.grid[(x,y)].symbol
    def set_energised(self, x, y):
        if not self.grid[(x,y)].energised:
            self.energised += 1
        self.grid[(x,y)].energised = True
    def print_energised(self):
        for y in range(self.y_leng):
            for x in range(self.x_leng):
                if self.grid[(x,y)].energised:
                    print("#", end = "")
                else:
                    print(".", end = "")
            print()
    def print_grid(self):
        for y in range(self.y_leng):
            for x in range(self.x_leng):
                print(self.grid[(x,y)].symbol, end = "")
            print()


class Ray():
    def __init__(self, grid, x = -1, y = 0, direction = 3):
        self.x = x
        self.y = y
        self.direction = direction
        self.grid = grid
        self.alive = True
        self.history = [(x, y)]
    
    # update location based on direction
    def shift(self):
        if self.direction == 0:
            self.y -= 1
        elif self.direction == 3:
            self.x += 1
        elif self.direction == 6:
            self.y += 1
        elif self.direction == 9:
            self.x -= 1
        if self.x < 0 or self.x >= grid.x_leng:
            self.alive = False
        elif self.y < 0 or self.y >= grid.y_leng:
            self.alive = False
        if (self.x, self.y) in self.history:
            self.alive = False
        
    # get the new movement instruction to update direction
    def new_direction(self):
        instruction = self.grid.get_symbol(self.x, self.y)
        if (instruction == "."):
            pass # same direction
        elif (instruction == "\\"):
            if (self.direction == 0):
                self.direction = 9
            elif (self.direction == 3):
                self.direction = 6
            elif (self.direction == 6):
                self.direction = 3
            elif (self.direction == 9):
                self.direction = 0
        elif (instruction == "/"):
            if (self.direction == 0):
                self.direction = 3
            elif (self.direction == 3):
                self.direction = 0
            elif (self.direction == 6):
                self.direction = 9
            elif (self.direction == 9):
                self.direction = 6
        elif (instruction == "-"): 
            if (self.direction == 3 or self.direction == 9):
                pass # same direction
            elif (self.direction == 0 or self.direction == 6):
                if grid.get_cell(self.x, self.y).split:
                    self.direction = 3
                    grid.get_cell(self.x, self.y).turn_off()
                    return Ray(grid, self.x, self.y, 9)
                else:
                    self.alive = False
        elif (instruction == "|"): 
            if (self.direction == "0" or self.direction == "6"):
                pass # same direction
            elif (self.direction == 3 or self.direction == 9):
                if grid.get_cell(self.x, self.y).split:
                    self.direction = 0
                    grid.get_cell(self.x, self.y).turn_off()
                    return Ray(grid, self.x, self.y, 6)
                else:
                    self.alive = False
                    
    def move(self):
        self.shift()
        if self.alive:
            grid.set_energised(self.x, self.y)
            return self.new_direction()
    
def setup():
    filename = "day15\\input.txt"
    #filename = "day15\\testinput.txt"
    #filename = "day15\\testinput1.txt"
    raw = []
    with open(filename) as source:
        for line in source.readlines():
            raw.append(line.replace("\n",""))
    x_leng = len(raw[0])
    y_leng = len(raw)
    grid = Grid(x_leng,y_leng)

    for y in range(y_leng):
        for x in range(x_leng):
            grid.add_cell(Cell(x, y, raw[y][x]))
            if raw[y][x] == "-" or raw[y][x] == "|":
                grid.add_cell(Splitter(x, y, raw[y][x]))
            else:
                grid.add_cell(Cell(x, y, raw[y][x]))
    return grid

def ray_positions(x_leng, y_leng):
    positions = []
    for i in range(x_leng):
        positions.append((i, -1, 6))
    for i in range(y_leng):
        positions.append((-1, i, 3))
    for i in range(x_leng):
        positions.append((i, y_leng, 0))
    for i in range(y_leng):
        positions.append((x_leng, i, 9))
    return positions

energised = 0
for position in ray_positions(110, 110):
    grid = setup()
    rays = [Ray(grid, *position)]
                    
    for ray in rays:
        for b in range(1000):
            result = ray.move()
            if result != None:
                rays.append(result)
            if not ray.alive:
                continue
        continue
    
    energised = max(energised, grid.energised)

print(energised)
# 8089

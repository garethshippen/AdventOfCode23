class Cell():
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.energised = False

class Splitter(Cell):
    def __init__(self):
        super.__init__(self)
        if self.symbol == "|":
            self.ports = [0,6]
        elif self.symbol == "-":
            self.ports = [3,9]
    # remember if a ray has come from that direction before.
    # if one has, do not split and redirect

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
        elif (instruction == "-"): # if ray come in from same direction before, kill ray here
            if (self.direction == 3 or self.direction == 9):
                pass # same direction
            elif (self.direction == 0 or self.direction == 6): 
                self.direction = 3
                return Ray(grid, self.x, self.y, 9)
        elif (instruction == "|"): # if ray come in from same direction before, kill ray here
            if (self.direction == "0" or self.direction == "6"):
                pass # same direction
            elif (self.direction == 3 or self.direction == 9):
                self.direction = 0
                return Ray(grid, self.x, self.y, 6)

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
    return grid
grid = setup()

rays = [Ray(grid)]
                
for ray in rays:
    for b in range(1000):
        result = ray.move()
        if result != None:
            rays.append(result)
        if not ray.alive:
            continue
    continue

# 10717 too high at 1313 loops
#grid.print_energised()
print(grid.energised)

""" rays = [Ray(grid)]
for b in range(1000):
    for i,ray in enumerate(rays):
        result = ray.move()
        if result != None:
            rays.append(result)
        if not ray.alive:
            rays.pop(i) """


""" import os
def print_rays(rays):
    coords = []
    for ray in rays:
        coords.append((ray.x,ray.y))
    os.system("cls")
    for y in range(10):
        for x in range(10):
            if (x,y) in coords:
                print("#", end = "")
            else:
                print(".", end="")
        print()

import time
rays = [Ray(grid)]
for h in range(1000):
#while len(rays) > 0:
    for i,ray in enumerate(rays):
        result = ray.move()
        if result != None:
            rays.append(result)
        if not ray.alive:
            rays.pop(i)
        print_rays(rays)
        time.sleep(0.1)


#grid.print_grid() """
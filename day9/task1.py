'''    |7F
        |
  -LF --S-- -J7 
        |
       |LJ     '''

filename = "day9\\input.txt"
#filename = "day9\\testinput.txt"

class Cell():
    def __init__(self, c, x, y):
        self.tile = c
        self.x = x
        self.y = y
        self.ports = self.assign_ports(c)
    
    '''       1
        -2 ---+--- 2 
             -1     '''
    def assign_ports(self, c):
        match c:
            case "|":
                return (1,-1)
            case "-":
                return (2,-2)
            case "L":
                return (1,2)
            case "J":
                return (1,-2)
            case "7":
                return (-1,-2)
            case "F":
                return (2,-1)
            case "S":
                return (3,3)
            case _:
                return (4,4)

    def exit_vector(self, direction):
        ent_vecs = {(0,1):1, (-1,0):2, (0,-1):-1, (1,0):-2}
        ent_vec = ent_vecs[direction]
        exit_port = [i for i in self.ports if i != ent_vec][0]
        ex_vecs = {1:(0,-1), 2:(1,0), -1:(0,1), -2:(-1,0)}
        return ex_vecs[exit_port]
        
    def get_tile(self):
        return self.tile
    def get_coords(self):
        return (self.x, self.y)
    def get_ports(self):
        return self.ports
    def set_ports(self, value):
        self.ports = value
    
    def __str__(self):
        return "Tile: {}\nPorts: {}\nCoords: {}".format(self.get_tile(), self.get_ports(), self.get_coords())

def add_vectors(loc, vec):
    return tuple(map(sum, zip(loc, vec)))

def sub_vectors(next, prev):
    return tuple([next[i] - prev[i] for i in range(len(next))])

def invert_vec(vec):
    return tuple([-1 * i for i in vec])

from collections import OrderedDict

start = None
grid = OrderedDict() # Used to help Task 2
with open(filename) as source:
    for y_axis, line in enumerate(source.readlines()):
        for x_axis in range(len(line)):
            grid[(x_axis, y_axis)] = Cell(line[x_axis], x_axis, y_axis)
            if line[x_axis] == "S":
                start = (x_axis,y_axis)
                
start_cell = grid[start]

#find S's ports
x = start[0]
y = start[1]
ports = []
try:
    if grid.get((x, y-1)).get_tile() in "|7F":
        ports.append(1)
except:
    pass
try:
    if grid.get((x+1, y)).get_tile() in "-J7":
        ports.append(2)
except:
    pass
try:
    if grid.get((x, y+1)).get_tile() in "|LJ":
        ports.append(-1)
except:
    pass
try:
    if grid.get((x-1, y)).get_tile() in "-LF":
        ports.append(-2)
except:
    pass
start_cell.set_ports(tuple(ports))

#exiting these ports means moving like this in the grid
dirs = {1:(0,-1), 2:(1,0), -1:(0,1), -2:(-1,0)} 

# pick an arbitrary port in S cell, and get movement vec
next_dir = dirs[start_cell.get_ports()[0]]
next_cell = grid[add_vectors(start_cell.get_coords(), next_dir)]
loop_cells = [start_cell.get_coords(), next_cell.get_coords()]
counter = 1
while next_cell.get_tile() != "S":
    counter += 1
    next_dir = next_cell.exit_vector(next_dir)
    next_cell = grid[add_vectors(next_cell.get_coords(), next_dir)]
    loop_cells.append(next_cell.get_coords())
    
print(counter//2)
# 6812


# Used for task 2
with open("day9\\pathcoords.txt", "w") as output:
    for coord in loop_cells:
        output.write("{} {}{}".format(coord[0], coord[1], "\n"))

filename = "day13\\input.txt"
#filename = "day13\\testinput.txt"

from functools import reduce

raw = []
with open(filename) as source:
    for line in source.readlines():
        raw.append(line.replace("\n",""))

grid = {}
for y in range(len(raw)):
    for x in range(len(raw[0])):
        grid[(x,y)] = raw[y][x]

y_leng = len(raw)
x_leng = len(raw[0])

def print_grid(matrix_dict):
    for y in range(y_leng):
        for x in range(x_leng):
            print(matrix_dict[(x,y)], end=" ")
        print()

# Modifies grid in place. direction = 0 for north, = 1 for south 
def tilt_col(grid, direction):
    for x in range(x_leng):
        col = "".join([grid[(x,i)] for i in range(y_leng)])
        col = col.split("#")
        newcol = []
        for block in col:
            roll = block.count("O")
            space = block.count(".")
            if direction == 0:
                newcol.append(roll * "O" + space * ".")
            else:
                newcol.append(space * "." + roll * "O")
        newcol = "#".join(newcol)
        for i,char in enumerate(newcol):
            grid[(x,i)] = char

# Modifies grid in place. direction = 0 for west, = 1 for east
def tilt_row(grid, direction):
    for y in range(y_leng):
        row = "".join([grid[(i,y)] for i in range(x_leng)])
        row = row.split("#")
        newrow = []
        for block in row:
            roll = block.count("O")
            space = block.count(".")
            if direction == 0:
                newrow.append(roll * "O" + space * ".")
            else:
                newrow.append(space * "." + roll * "O")
        newrow = "#".join(newrow)
        for i, char in enumerate(newrow):
            grid[(i,y)] = char

def spin(grid):
    tilt_col(grid, 0)
    tilt_row(grid, 0)
    tilt_col(grid, 1)
    tilt_row(grid, 1)

def spins(grid, number_of_spins):
    for i in range(number_of_spins):
        spin(grid)

def hash(grid):
    total = 0
    for y in range(y_leng):
        row = 0
        for x in range(x_leng):
            row += ord(grid[(x,y)])
        total += row * (y + 1)
    return total

def visualise(grid, repeats = 215, scale = 200):
    log = []
    for i in range(repeats):
        log.append(hash(grid))
        spin(grid)
    for i, lo in enumerate(log):
        print(i, int(log.count(lo)/len(log) * scale) * "-" + str(lo))

def find_cycle(grid):
    pass # did it by hand

#print((1000000000-143)%28)

def evaluate(grid):
        total = 0
        for x in range(x_leng):
            for y in range(y_leng):
                if grid[(x,y)] == "O":
                    total += y_leng - y
        return total
    

num_spins = 143 + ((1000000000-143)%28)
spins(grid, num_spins)
ans = evaluate(grid)
print(ans)

# 99875
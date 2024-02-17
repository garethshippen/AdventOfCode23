import cmath

filename = "day17/input.txt"
#filename = "day17/testinput.txt"

def determ(point_a, point_b):
    return point_a[0] * point_b[1] - point_b[0] * point_a[1] 

def shoelace(points):
    total = 0
    for i in range(len(points)-1):
        a = points[i]
        b = points[i+1]
        total += determ(a,b)
    return total/2


def setup(filename):
    raw = []
    with open(filename) as source:
        for line in source.readlines():
            raw.append(line)
    return raw
raw = setup(filename)

def parse(lines):
    directions = []
    for line in lines:
        instruction = line.split()[-1].replace("(#","").replace(")","")
        length = int(instruction[:-1],16)
        direction = instruction[-1]
        dirs = {'0': 'r', '1':'d', '2':'l','3':'u'}
        directions.append((dirs[direction], length))
    return directions
instructions = parse(raw)

directions = {'u': complex(0,-1), 'r': complex(1,0), 'd': complex(0,1), 'l': complex(-1,0)}

coords = [(0,0)]

loc = complex(0,0)
perimeter = 0
for instruction in instructions:
    direction = directions[instruction[0]]
    loc += (direction * instruction[1])
    coords.append((int(loc.real), int(loc.imag)))
    perimeter += instruction[1]

print(shoelace(coords) + perimeter/2 + 1)
# 85070763635666
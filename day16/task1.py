#filename = "day16\\input.txt"
filename = "day16\\testinput.txt"

def setup(filename):
    raw = []
    with open(filename) as source:
        for line in source.readlines():
            raw.append(line.replace("\n",""))
    grid = {}
    for y in range(len(raw)):
        for x in range(len(raw[0])):
            grid[(x,y)] = raw[y][x]
    return grid


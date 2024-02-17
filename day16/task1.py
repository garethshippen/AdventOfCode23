from node import Node
from heapq import heappop, heapify

#filename = "day16\\input.txt"
filename = "day16\\testinput.txt"
#filename = "day16\\testinput1.txt"

def get_nei(grid, coord): # Returns the coordinates of the neighbouring nodes
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    out_coords = []
    for direction in directions:
        out_coords.append((direction[0]+coord[0], direction[1]+coord[1]))
    return out_coords

# Load data and return list of lists
def setup(filename):
    raw = []
    with open(filename) as source:
        for line in source.readlines():
            raw.append(line.replace("\n",""))
    return raw
raw = setup(filename)

# Turn raw into a grid of Nodes
grid = {}
x_size = len(raw[0])
y_size = len(raw)
for y in range(y_size):
    for x in range(x_size):
        grid[(x,y)] = Node(x, y, int(raw[y][x]), x_size, y_size)

a_star = {}
start = (0,0)
end = (x_size-1, y_size-1)

grid[start].g = 0 # Change start node's g value to 0 from inf

open_nodes = [grid[(start)]]
current_node = heappop(open_nodes)
while current_node.coord != end:
    for adjacent in current_node.neighbours:
        neighbour = grid[adjacent]
        if neighbour.open:
            open_nodes.append(neighbour)
            new_g = current_node.g + neighbour.value
            if new_g < neighbour.g:
                neighbour.update_g(new_g)
    current_node.close()
    current_node = heappop(open_nodes)
print(current_node.coord, current_node.g)
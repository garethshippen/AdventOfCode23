from math import inf
from heapq import heappop, heapify

#filename = "day16\\input.txt"
#filename = "day16\\testinput.txt"
filename = "day16\\testinput1.txt"

# Load data and return list of lists
def setup(filename):
    raw = []
    with open(filename) as source:
        for line in source.readlines():
            raw.append(line.replace("\n",""))
    return raw
raw = setup(filename)

# Turn data into grid of values indexed on coordinates
grid = {}
x_size = len(raw[0])
y_size = len(raw)
for y in range(y_size):
    for x in range(x_size):
        grid[(x,y)] = raw[y][x]

# Make dictionary of graph edges
graph = {}
for y in range(y_size):
    for x in range(x_size):
        #rows
        left_coord = (x,y)
        right_coord = (x+1,y)
        left = grid.get(left_coord)
        right = grid.get(right_coord)
        if right:
            graph[left_coord, right_coord] = right
            graph[right_coord, left_coord] = left

        #columns
        top_coord = (x,y)
        bottom_coord = (x,y+1)
        top = grid.get(top_coord)
        bottom = grid.get(bottom_coord)
        if bottom:
            graph[top_coord,bottom_coord] = bottom
            graph[bottom_coord, top_coord] = top

adjacency = {}

for y in range(y_size):
    for x in range(x_size):
        coord = (x,y)
        neighbour_edges = [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]
        neighbour_values = [grid.get((x, y-1)), grid.get((x+1, y)), grid.get((x, y+1)), grid.get((x-1, y))]
        neighbour_data = [a for a in zip(neighbour_edges, neighbour_values) if a[1] is not None]
        adjacency[coord] = neighbour_data
    

""" for key, value in adjacency.items():
    print(key, value)

exit() """
class Node():
    def __init__(self, coords, x_size, y_size, g, prev_node = None):
        self.coords = coords
        self.prev_node = prev_node
        self.g = g
        self.x_size = x_size
        self.y_size = y_size
        self.h = self.taxi()
        self.f = self.g + self.h
    
    def update_g(self, g, prev_node): 
        self.g = g
        self.prev_node = prev_node
        self.f = self.g + self.h
    def taxi(self):
        return self.x_size - self.coords[0] + self.y_size - self.coords[1] - 2
    def __lt__(self, other):
        return self.f < other.f
    def __eq__(self, other):
        return self.coords == other.coords

def check_mem(array, coordinate): 
    for entry in array:
        if entry.coords == coordinate: 
            return entry # i hope this sends the reference not the value
    return None

a_star = {}
start = (0,0)
end = (x_size-1, y_size-1)
open_nodes = [Node(start, x_size, y_size, 0)]
seen = [start]
closed_nodes = []
current_node = open_nodes[0]
while current_node.coords != end:
    current_node = heappop(open_nodes)
    neighbour_edges = adjacency[current_node.coords]
    
    for edge in neighbour_edges:
        neighbour_coord = edge[0]
        edge_value = edge[1]
        g = current_node.g + int(edge_value)
        neighbour_node = check_mem(open_nodes, neighbour_coord)
        if neighbour_node and neighbour_node.g > g:
            neighbour_node.update_g(g, current_node.coords)
        elif neighbour_coord not in seen:
            new_node = Node(neighbour_coord, x_size, y_size, g, current_node.coords)
            seen.append(neighbour_coord)
            open_nodes.append(new_node)
    closed_nodes.append(current_node.coords)
    
print(current_node.coords, current_node.f)
from math import inf
from heapq import heappop, heapify

#filename = "day16\\input.txt"
filename = "day16\\testinput.txt"
#filename = "day16\\testinput1.txt"

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

adjacency = {} # Key: A node, Value: List of tuples. Tuple is grid coord, edge value.

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
    def __init__(self, coord):
        self.coord = coord
        self.h = self.set_h()
        self.g = inf
        self.f = inf
        self.open = True
        self.route = []
    
    @classmethod
    def set_board_size(cls, x_size, y_size):
        cls.x_size = x_size - 1
        cls.y_size = y_size - 1
    
    @classmethod
    def valid_neighbour(cls, path, coord):
        if len(path) < 3:
            return True
        last_three = path[-3:]
        if last_three[0][0] == last_three[1][0] == last_three[2][0] == coord[0] or \
            last_three[0][1] == last_three[1][1] == last_three[2][1] == coord[1]:
                return False
        return True
    
    def set_h(self): 
        try:
            return abs(x_size - self.coord[0]) + abs(y_size - self.coord[1])
        except:
            raise Exception("Board size not initialised.\nCall Node.set_board_size(x_length, y_length)")
    def set_g(self, value):
        self.g = value
        self.f = self.g + self.h
    def get_g(self): return self.g
    def get_f(self): return self.f
    def get_route(self): return self.route
    def set_route(self, route): self.route = route
    def get_open(self): return self.open
    def close(self): self.open = False
    def __lt__(self, other): return self.f < other.f
    
Node.set_board_size(x_size, y_size)
start = (0,0)
end = (x_size-1, y_size-1)

start_node = Node(start)
start_node.set_g(0)
start_node.set_route([])
a_star = {start: start_node}
open_nodes = [start_node]

current_node = open_nodes[0]

counter = 0

''' Start A* '''
while current_node.coord != end:
    current_node = heappop(open_nodes)
    f = current_node.get_f()
    route = current_node.get_route()

    neighbours = adjacency[current_node.coord] # Get edges

    for neighbour in neighbours:
        neighbour_coord = neighbour[0]
        edge_value = neighbour[1]
        g_here = f + int(edge_value)
        path_here = route[:]
        path_here.append(neighbour_coord)

        # Is this a valid neighbour?
        if not Node.valid_neighbour(route, neighbour_coord):
            continue
        
        neighbour_node = a_star.get(neighbour_coord)
        if neighbour_node and not neighbour_node.get_open(): # Node is closed. Don't work with it any further.
            continue
        
        # If the neighbour node doesn't exist, create a new one. 
        if not neighbour_node: # Hasn't been seen before
            neighbour_node = Node(neighbour_coord)
            neighbour_node.set_g(g_here)
            neighbour_node.set_route(path_here)
            open_nodes.append(neighbour_node)
            a_star[neighbour_coord] = neighbour_node

        if g_here < neighbour_node.get_g():
            neighbour_node.set_g(g_here)
            neighbour_node.set_route(path_here)
            
    current_node.close()
    counter += 1
    if counter > 1000:
        break


""" print(a_star[end].get_g())
print(a_star[end].route)

grida = {}
for y in range(13):
    for x in range(13):
        grida[(x,y)] = " "
        
for node in a_star[end].route:
    grida[node] = "#"
    
for y in range(13):
    for x in range(13):
        print(grida[(x,y)], end = "")
    print() """














""" class Node():
    def __init__(self, coords, x_size, y_size, g, route):
        self.coords = coords
        self.g = g
        self.x_size = x_size
        self.y_size = y_size
        self.h = self.taxi()
        self.f = self.g + self.h
        self.route = route
    
    def update_g(self, g, route): 
        def valid_neighbour(route):
            if len(route) < 4:
                return True
            last_four = route[-4:]
            if last_four[0][0] == last_four[1][0] == last_four[2][0] == last_four[3][0] or \
                last_four[0][1] == last_four[1][1] == last_four[2][1] == last_four[3][1]:
                    return False
            return True
        if valid_neighbour(route):
            self.g = g
            self.route = route
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
open_nodes = [Node(start, x_size, y_size, 0, None)]
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
        neighbour_node = check_mem(open_nodes, neighbour_coord) # Checks if the node is already in the heap.
        if neighbour_node and neighbour_node.g > g: # The neighbour node has been expanded. Is the current route shorter than the previous route?
            # copy current nodes route, and add current node coords
            # if neighbour node .valid_neighbour is true, do some swapping
            neighbour_node.update_g(g, current_node.coords + neighbour_coord)
            # else do not consider neighbour
        elif neighbour_coord not in seen:
            route = current_node.route # this not tested
            route.append(current_node.coords) # this not tested
            new_node = Node(neighbour_coord, x_size, y_size, g, route)
            # copy current nodes route and add current node coords
            seen.append(neighbour_coord)
            open_nodes.append(new_node)
    closed_nodes.append(current_node.coords)
    
print(current_node.coords, current_node.f)

# track the previous coords. if neighbour coordinate is fourth in a line, it is not a valid neighbour """
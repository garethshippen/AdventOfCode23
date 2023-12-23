directions = "day7\\directions.txt"
nds = "day7\\nodes.txt"
#directions = "day7\\testdirections.txt"
#nds = "day7\\testnodes.txt"

dirs = None
with open(directions) as directions:
    dirs = directions.readline()

node_table = {}
with open(nds) as nds:
    for node in nds:
        node_table[node[0:3]] = (node[7:10], node[12:15])

def get_direction(count, dirs):
    dirlen = len(dirs)
    c = dirs[count%dirlen]
    if c == "L":
        return 0
    else:
        return 1

def check_nodes(list_of_nodes):
    for node in list_of_nodes:
        if node[-1] != "Z":
            return False
    return True

nodes = []
for node in node_table.keys():
    if node[2] == "A":
        nodes.append(node)


clocks = []
dirlen = len(dirs)
path = []
for node in nodes:
    clock = 0
    while node[2] != 'Z':
        direction = get_direction(clock, dirs)
        node_leaves = node_table[node]
        node = node_leaves[direction]
        path.append(node)
        clock += 1
    clocks.append(clock)
#print(clocks)

from math import lcm
l = lcm(*clocks)

print(l)
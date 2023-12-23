directions = "day7\\directions.txt"
nds = "day7\\nodes.txt"

dirs = None
with open(directions) as directions:
    dirs = directions.readline()

nodes = {}
with open(nds) as nds:
    for node in nds:
        nodes[node[0:3]] = (node[7:10], node[12:15])

def get_direction(count, dirs):
    dirlen = len(dirs)
    c = dirs[count%dirlen]
    if c == "L":
        return 0
    else:
        return 1


clock = 0
dirlen = len(dirs)
node = 'AAA'
while node != 'ZZZ':
    direction = get_direction(clock, dirs)
    node_leaves = nodes[node]
    node = node_leaves[direction]
    clock += 1
print(clock)
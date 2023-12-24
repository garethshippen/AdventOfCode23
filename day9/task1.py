# | north - south
# - east - west
# L north - east
# J north - west
# 7 south - west
# F south - east
# . null
# S starting point

filename = "day9\\input.txt"

grid = []
with open(filename) as source:
    for line in source.readlines():
        grid.append(line.replace("\n",""))
        
print(len(grid))
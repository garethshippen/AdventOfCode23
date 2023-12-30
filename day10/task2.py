filename = "day10\\input.txt"
#filename = "day10\\testinput.txt"

lines = []
with open(filename) as source:
    for line in source.readlines():
        line = line.replace("\n", "")
        lines.append(line)

def find_galaxies(lines):
    galaxies = []
    for y, line in enumerate(lines):
        for x, index in enumerate(line):
            if index == "#":
                galaxies.append([x,y])
    return galaxies
galaxies = find_galaxies(lines)

def find_empty_rows(lines):
    extra_rows = []
    for i, line in enumerate(lines):
        if "#" not in line:
            extra_rows.append(i)
    extra_rows.append(len(lines))
    return extra_rows
extra_rows = find_empty_rows(lines)
        

def find_empty_cols(lines):
    extra_cols = []
    for index in range(len(lines[0])):
        count = 0
        for row in lines:
            if row[index] == "#":
                count += 1
        if count == 0:
            extra_cols.append(index)
    extra_cols.append(len(lines[0]))
    return extra_cols
extra_cols = find_empty_cols(lines)

def expand_galaxy(galaxies, rows, cols):
    new_galaxy = []
    for galaxy in galaxies:
        new_gal = []
        for i, x in enumerate(cols):
            if galaxy[0] < x:
                new_gal.append(galaxy[0] + i * 999999)
                break

        for j, y in enumerate(rows):
            if galaxy[1] < y:
                new_gal.append(galaxy[1] + j * 999999)
                break
        new_galaxy.append(new_gal)
    return new_galaxy
new_galaxy = expand_galaxy(galaxies, extra_rows, extra_cols)

# get pairs of galaxies
from itertools import combinations
pairs = list(combinations(new_galaxy, 2))

# find distances
def man_dist(pair):
    return abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])     
        
total = 0
for pair in pairs:
    try:
        total += man_dist(pair)
    except:
        print(pair)
        
print(total)
#746962097860
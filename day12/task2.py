filename = "day12\\input.txt"
#filename = "day12\\testinput.txt"

raw = []
with open(filename) as source:
    for line in source.readlines():
        raw.append(line.replace("\n", ""))
    

patterns = []
pattern = []
for line in raw:
    if len(line) > 0:
        pattern.append(line)
    else:
        patterns.append(pattern)
        pattern = []
patterns.append(pattern)

def transpose(matrix):
    return ["".join(i) for i in list(map(list,zip(*matrix)))]

""" 
def is_mirror(matrix, index):
    size = len(matrix)
    if index >= size - 1:
        return False
    
    a = index
    b = index + 1
    while matrix[a] == matrix[b]:
        a -= 1
        b += 1
        if a < 0 or b >= size:
            return True
    return False

def mirror_index(matrix):
    for i in range(len(matrix)):
        if is_mirror(matrix, i):
            return (i + 1) * 100
    matrix = transpose(matrix)
    for i in range(len(matrix)):
        if is_mirror(matrix, i):
            return i + 1
"""
# for mirror line get only the rows in range either side of it
# get the difference of row pairs.
# if the total of differences is only 1 or -1 this is the smudge

def mirror_rows(matrix, index): # returns a list of paired rows mirrored about the line index and index + 1
    size = len(matrix)
    if index >= size:
        return None
    a = index
    b = index + 1
    pairs = []
    while (a >= 0) and (b < size):
        pairs.append([matrix[a],matrix[b]])
        a -= 1
        b += 1
    return pairs

def difference(a,b):
    assert len(a) == len(b)
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
    return diff

""" matrix = [
".##.....#....#.",
".##.....#....#.",
"..#.#..##....##",
"...###...#..#..",
"#..##.....##...",
".#.#...#.####.#",
"#.#.....######.",
"##..###...##...",
"#..#..##..##..#",
".##.#.#........",
"#..#..##..##..#",
"#####.#.##.###.",
".#....##.#..#.#",
"..##.#...#..#..",
"#..####..#..#.."
] """

def smudge_mirror(matrix):
    for i in range(len(matrix)):
        pairs = mirror_rows(matrix, i)
        total = 0
        for pair in pairs:
            total += difference(*pair)
        if total == 1:
            return i + 1

def value(matrix):
    a = smudge_mirror(matrix)
    if a is not None:
        return a * 100
    matrix = transpose(matrix)
    a = smudge_mirror(matrix)
    if a is not None:
        return a

total = 0
for i,matrix in enumerate(patterns):
    total += value(matrix)
print(total)
#35915
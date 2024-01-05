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

total = 0
for mat in patterns:
    total += mirror_index(mat)
print(total)
#36041
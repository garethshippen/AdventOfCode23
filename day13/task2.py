filename = "day13\\input.txt"

raw = []
with open(filename) as source:
    for line in source.readlines():
        raw.append(line.replace("\n",""))

def transpose(matrix):
    return ["".join(i) for i in list(map(list,zip(*matrix)))]

a = [
["1","2","3"],
["4","5","6"],
["7","8","9"]
]

def print_mat(matrix):
    for a in matrix:
        print(a)

print_mat(a)
a = transpose(a)
print_mat(a)
a = transpose(a)
print_mat(a)
a = transpose(a)
print_mat(a)
a = transpose(a)
print_mat(a)

exit()
rot = transpose(raw)
tilted = []
for row in rot:
    a = row.split("#")
    new = []
    for block in a:
        round = block.count("O")
        space = block.count(".")
        newstr = "O" * round + "." * space
        new.append(newstr)
    tilted.append("#".join(new))

total = 0
for a in tilted:
    for i, char in enumerate(a):
        if char == "O":
            total += (100 - i)
print(total)
# 109833
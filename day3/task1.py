filename = "day3\\input.txt"

data = []
with open(filename) as inp:
    for line in inp.readlines():
        data.append(line[10:])
        
print(len(data))
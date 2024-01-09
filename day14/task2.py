def aoc_hash(inp):
    total = 0
    for char in inp:
        total += ord(char)
        total *= 17
        total = total % 256
    return total

def run_sequence(step):
    data = step.split("=")
    if len(data) == 2:
        code = data[0]
        lens = data[1]
        box = aoc_hash(code)
        lenses = boxes[box]
        label = code + " " + lens
        for i, ln in enumerate(lenses):
            if code in ln:
                boxes[box][i] = label
                return
        lenses.append(label)
    else:
        code = data[0][:-1]
        box = aoc_hash(code)
        lenses = boxes[box]
        for i, ln in enumerate(lenses):
            if code in ln:
                lenses.pop(i)

filename = "day14\\input.txt"
#filename = "day14\\testinput.txt"

raw = None
with open(filename) as source:
    raw = source.read()

steps = raw.split(",")

boxes = {k:[] for k in range(256)}

for step in steps:
    run_sequence(step)

total = 0
for j in range(256):
    for i,lens in enumerate(boxes[j]):
        total += (j+1) * (i+1) * int(lens[-1])
print(total)
#251353
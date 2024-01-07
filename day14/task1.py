filename = "day14\\input.txt"
#filename = "day14\\testinput.txt"

raw = None
with open(filename) as source:
    raw = source.read()

steps = raw.split(",")

def aoc_hash(inp):
    total = 0
    for char in inp:
        total += ord(char)
        total *= 17
        total = total % 256
    return total

total = 0
for step in steps:
    a = aoc_hash(step)
    total += a
print(total)
# 503154
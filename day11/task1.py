filename = "day11\\input.txt"

lines = []
with open(filename) as source:
    for line in source.readlines():
        parts = line.replace("\n", "").split()
        parts[0] = parts[0].replace(".", "0").replace("#", "1")
        parts[1] = list(parts[1])
        parts[1] = [int(num) for num in parts[1] if num.isdigit()]
        lines.append(parts)

# Generates binary numbers as a string
def bins(n):
    i = 0
    while i < 2**n:
        yield bin(i)[2:].zfill(n)
        i += 1

# generate patterns
from collections import Counter
def generate_patterns(springs):
    patterns = []
    unknowns = Counter(springs)["?"]
    spg = list(springs)
    indicies = [i for i in range(len(spg)) if spg[i] == "?"]
    for pattern in bins(unknowns):
        out_spg = list(springs)
        for i, bit in enumerate(pattern):
            out_spg[indicies[i]] = bit
        patterns.append("".join(out_spg))
    return patterns

# check if a string matches it's signature
import re
def check(springs, signature):
    # [0]*[1]{a}[0]+[1]{b}[0]+[1]{c}[0]*
    search = "^[0]*"
    search += "[0]+".join(["[1]{{{}}}".format(i) for i in signature])
    search += "[0]*$"
    count = 0
    for spring in springs:
        if re.search(search, spring):
            count += 1
    return count

""" y = generate_patterns("1???1???1???01??")
x = check(y, [5,3,1,1,1])
print(x)  """

total = 0
for line in lines:
    springs = line[0]
    signature = line[1]
    total += check(generate_patterns(springs), signature)
print(total)
#8092 too high
filename = "day12\\input.txt"

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


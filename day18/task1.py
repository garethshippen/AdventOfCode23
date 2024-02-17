#filename = "day18/input.txt"
filename = "day18/testinput.txt"

def setup(filename):
    lines = []
    index = None
    with open(filename) as source:
        for i, line in enumerate(source.readlines()):
            lines.append(line)
            if line == "\n":
                index = i
    return lines[:index], lines[index+1:]
instructions, items = setup(filename)

print(len(instructions), len(items))
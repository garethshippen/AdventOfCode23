filename = "day18/input.txt"
#filename = "day18/testinput.txt"

class Item():
    def __init__(self, body):
        self.x = int(body[0][2:])
        self.m = int(body[1][2:])
        self.a = int(body[2][2:])
        self.s = int(body[3][2:])
        self.sum = self.x + self.m + self.a + self.s
    def get_attribute(self, letter):
        if letter == 'x':
            return self.x
        elif letter == 'm':
            return self.m
        elif letter == 'a':
            return self.a
        elif letter == 's':
            return self.s
    
def setup(filename):
    lines = []
    index = None
    with open(filename) as source:
        for i, line in enumerate(source.readlines()):
            if line == "\n":
                index = i
            lines.append(line.replace("\n", ""))
    return lines[:index], lines[index+1:]
inst, items = setup(filename)

pile = [] # Items to process
for item in items:
    body = item[1:-1].split(",")
    pile.append(Item(body))

instructions = {}
for ins in inst:
    name = ins.split("{")[0]
    process = ins.split("{")[1][:-1]
    instructions[name] = process.split(",")
    
def parse_instruction(instruction): # Returns a tokenised form of the instruction, or the next instruction.
    if ">" in instruction or "<" in instruction:
        attribute = instruction[0]
        comparitor = instruction[1]
        result_index = instruction.index(":")
        comparison = instruction[2:result_index]
        result = instruction[result_index+1:]
        return [attribute, comparitor, comparison, result]
    else: # No comparison, just instruction
        return [instruction]
    
def process_instruction(instruction, item):
    if len(instruction) == 1:
        return instruction[0]
    attribute = item.get_attribute(instruction[0])
    comparitor = instruction[1]
    comparison = int(instruction[2])
    result = instruction[3]
    
    if comparitor == "<":
        if attribute < comparison:
            return result
    elif comparitor == ">":
        if attribute > comparison:
            return result
    return False

def run_machine(machine, item):
    for instruction in instructions[machine]:
        instruction = parse_instruction(instruction)
        result = process_instruction(instruction, item)
        if result:
            return result

accept = []
for item in pile:
    result = 'in'
    end = ('A', 'R')
    while result not in end:
        result = run_machine(result, item)
    if result == 'A':
        accept.append(item.sum)

print(sum(accept))
# 333263
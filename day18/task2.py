from copy import deepcopy
from collections import deque

filename = "day18/input.txt"
#filename = "day18/testinput.txt"

class Ranges():
    def __init__(self, x, m, a, s):
        self.data = {'x':range(x[0], x[1]+1),
                    'm':range(m[0], m[1]+1),
                    'a':range(a[0], a[1]+1), 
                    's':range(s[0], s[1]+1)} # 'x':(0,10)

    def show(self):
        print("x: ({},{})\nm: ({},{})\na: ({},{})\ns: ({},{})".format(self.data['x'][0], self.data['x'][-1], self.data['m'][0], self.data['m'][-1], self.data['a'][0], self.data['a'][-1], self.data['s'][0], self.data['s'][-1]))

    def combos(self):
        return len(self.data['x']) * len(self.data['m']) * len(self.data['a']) * len(self.data['s'])

class Instruction():
    def __init__(self, expression):
        self.command = (True if '<' in expression or '>' in expression else False)
        if self.command:
            self.attribute = expression[0]
            self.op = expression[1]
            self.threshold = int(expression.split(":")[0][2:])
            self.destination = expression.split(":")[1]
        else:
            self.destination = expression


    def chop(self, rng): #[pass range, fail range]
        if not self.command:
            return [None, None]
        the_range = rng.data[self.attribute]
        big_diff = self.threshold - the_range[-1]
        little_diff = self.threshold - the_range[0]
        if self.op == ">":
            if big_diff < 0:
                if little_diff < 0:
                    return [rng, None]
                else:
                    pass_range = deepcopy(rng)
                    pass_range.data[self.attribute] = range(self.threshold + 1, the_range[-1]+1)
                    fail_range = deepcopy(rng)
                    fail_range.data[self.attribute] = range(the_range[0], self.threshold+1)
                    return [pass_range, fail_range]
            else:
                return [None, rng]
        elif self.op == "<":
            if little_diff > 0:
                if big_diff > 0:
                    return [rng, None]
                else:
                    pass_range = deepcopy(rng)
                    pass_range.data[self.attribute] = range(the_range[0], self.threshold - 1 + 1)
                    fail_range = deepcopy(rng)
                    fail_range.data[self.attribute] = range(self.threshold, the_range[-1] + 1)
                    return [pass_range, fail_range]
            else:
                return [None, rng]
        else:
            print("Wut?")

    
class Workflow():
    def __init__(self, raw):
        self.raw = raw
        self.name = self.raw.split("{")[0]
        insts = self.raw.split("{")[1][:-1].split(",")
        self.instructions = [Instruction(inst) for inst in insts]

    def process(self, a_range): # [(range, destination), (range, destination), ...]
        results = []
        current_range = a_range
        for instruction in self.instructions:
            if not instruction.command:
                results.append((current_range, instruction.destination))
                continue
            passing, failing = instruction.chop(current_range)
            if passing:
                results.append((passing, instruction.destination))
            if not failing:
                break
            current_range = failing
        return results

def setup(filename):
    lines = []
    with open(filename) as source:
        for line in source.readlines():
            if line == "\n":
                break
            lines.append(line.replace("\n", ""))
    return lines

lines = setup(filename)
workflows = dict()
for line in lines:
    name = line.split("{")[0]
    workflows[name] = Workflow(line)

start_range = (1,4000)
rng = Ranges(start_range, start_range, start_range, start_range)

to_process = deque()
to_process.append((rng, 'in'))

accepted = []
while(to_process):
    current_range, instr = to_process.popleft()
    if instr == "A":
        accepted.append(current_range)
        continue
    if instr != "R":
        workflow = workflows[instr]
        results = workflow.process(current_range)
        to_process.extend(results)

total = 0
for a in accepted:
    total += a.combos()
print(total)
# 130745440937650
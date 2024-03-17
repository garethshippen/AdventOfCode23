from copy import deepcopy
from collections import deque

#filename = "day18/input.txt"
filename = "day18/testinput.txt"

class Ranges():
    def __init__(self, x, m, a, s):
        self.data = {'x':range(x[0], x[1]+1),
                    'm':range(m[0], m[1]+1),
                    'a':range(a[0], a[1]+1), 
                    's':range(s[0], s[1]+1)} # 'x':(0,10)

    """ def chop(self, attribute, op, threshold): #[pass range, fail range]
        the_range = self.data[attribute]
        big_diff = threshold - the_range[-1]
        little_diff = threshold - the_range[0]
        if op == ">":
            if big_diff < 0:
                if little_diff < 0:
                    return [self, None]
                else:
                    pass_range = deepcopy(self)
                    pass_range.data[attribute] = range(threshold + 1, the_range[-1]+1)
                    fail_range = deepcopy(self)
                    fail_range.data[attribute] = range(the_range[0], threshold+1)
                    return [pass_range, fail_range]
            else:
                return [None, self]
        elif op == "<":
            if little_diff > 0:
                if big_diff > 0:
                    return [self, None]
                else:
                    pass_range = deepcopy(self)
                    pass_range.data[attribute] = range(the_range[0], threshold - 1 + 1)
                    fail_range = deepcopy(self)
                    fail_range.data[attribute] = range(threshold, the_range[-1] + 1)
                    return [pass_range, fail_range]
            else:
                return [None, self]
        else:
            print("Wut?")
            """
    def show(self):
        print("x: ({},{})\nm: ({},{})\na: ({},{})\ns: ({},{})".format(self.data['x'][0], self.data['x'][-1], self.data['m'][0], self.data['m'][-1], self.data['a'][0], self.data['a'][-1], self.data['s'][0], self.data['s'][-1]))

class Instruction():
    def __init__(self, expression):
        self.command = (True if '<' in expression or '>' in expression else False)
        if self.command:
            self.attribute = expression[0]
            self.op = expression[1]
            self.threshold = int(expression.split(":")[0][2:])
            self.destination = expression.split(":")[1]


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

    def process(self, a_range):
        results = []
        current_range = a_range
        for instruction in self.instructions:
            passing, failing = instruction.chop(current_range) # !!!!!!! Need to handle these being None
            results.append((passing, instruction.destination))
            current_range = failing
        return results

work = Workflow("px{a<2006:qkq,m>2090:A,rfg}")
print(work.raw)
print(work.name)
print(work.instructions)
exit()

start_range = (1,4000)
rng = Ranges(start_range, start_range, start_range, (1351, 4000))

inst = Instruction('ppx')
print(inst.command)
passing, failing = inst.chop(rng)

if passing:
    print("P")
    passing.show()
print()
if failing:
    print("F")
    failing.show()
exit()








def get_components(a_rule):
    return a_rule[0], a_rule[1], int(a_rule[2:])

def setup(filename):
    lines = []
    with open(filename) as source:
        for line in source.readlines():
            if line == "\n":
                break
            lines.append(line.replace("\n", ""))
    return lines

workflows = setup(filename)
start_range = (1,4000)
rng = Ranges(start_range, start_range, start_range, start_range)

instructions = {} # instruction name: [[condition, inst], [condition, inst], [inst]...]
for ins in workflows:
    name = ins.split("{")[0]
    process = ins.split("{")[1][:-1]
    a = []
    for thing in process.split(","):
        a.append(thing.split(":"))
    instructions[name] = a

""" for ins, val in instructions.items():
    print(ins, val)
exit() """

rule = instructions['in']
print(rule)
exit()
filters = deque()
#filters.append([rng, rule]) # A list of lists of Ranges objects, and a list of commands
filters.append([rng, ['qqz']]) # A list of lists of Ranges objects, and a list of commands

#filters = [   [Range, [  ['s<1351', 'px'], ['qqz']  ]  ]   ]
""" 
Pass the range into the first instruction in its rule
chop the range if needed
the passing range gets added to filters with its new instruction
the failing range gets passed to the next instruction in the rule
"""
#first_rule = filters[range/rule pair][rule in range/rule pair][nth instruction in rules][expresion or next]

print(filters)

head = filters.popleft()
current_range = head[0]
current_pair = head[1][0] # instruction/destination
current_rule = current_pair[0] # current instruction
pass_inst = head[1][0][1] # pass destination
if '<' in current_rule or '>' in current_rule:
    att, op, thresh = get_components(current_rule)
    passing, failing = current_range.chop(att, op, thresh)
    filters.append([passing, pass_inst])
else:
    filters.append([current_range, pass_inst])

print(filters)

""" 
passed range put in filters queue
failed range must go into the next instruction
"""
from copy import deepcopy

#filename = "day18/input.txt"
filename = "day18/testinput.txt"

class Ranges():
    def __init__(self, x, m, a, s):
        self.data = {'x':range(x[0], x[1]+1),
                    'm':range(m[0], m[1]+1),
                    'a':range(a[0], a[1]+1), 
                    's':range(s[0], s[1]+1)} # 'x':(0,10)

    def member(self, attribute, threshold):
        if threshold in self.data[attribute]:
            return True
        else:
            return False

    def chop(self, attribute, op, threshold):
        the_range = self.data[attribute]
        big_diff = threshold - the_range[-1]
        little_diff = threshold - the_range[0]
        if op == ">":
            if big_diff < 0:
                if little_diff < 0:
                    return [self, None]
                else:
                    pass_range = deepcopy(self)
                    pass_range.data[attribute] = range(threshold + 1, the_range[-1])
                    fail_range = deepcopy(self)
                    fail_range.data[attribute] = range(the_range[0], threshold)
                    return [pass_range, fail_range]
            else:
                return [None, self]
        elif op == "<":
            if little_diff > 0:
                if big_diff > 0:
                    return [self, None]
                else:
                    pass_range = deepcopy(self)
                    pass_range.data[attribute] = range(the_range[0], threshold - 1)
                    fail_range = deepcopy(self)
                    fail_range.data[attribute] = range(threshold, the_range[-1])
                    return [pass_range, fail_range]
            else:
                return [None, self]
        else:
            print("Wut?")
    def show(self):
        print("x: ({},{})\nm: ({},{})\na: ({},{})\ns: ({},{})".format(self.data['x'][0], self.data['x'][1], self.data['m'][0], self.data['m'][1], self.data['a'][0], self.data['a'][1], self.data['s'][0], self.data['s'][1]))

rng = Ranges((0,10),(0,9),(1,7),(5,10))

chops = rng.chop('x', '>', 5)
for chop in chops:
    chop.show()

exit()


def setup(filename):
    lines = []
    index = None
    with open(filename) as source:
        for i, line in enumerate(source.readlines()):
            if line == "\n":
                break
            lines.append(line.replace("\n", ""))
    return lines

workflows = setup(filename)
start_range = (1,4000)
start = Ranges(start_range, start_range, start_range, start_range)

instructions = {}
for ins in workflows:
    name = ins.split("{")[0]
    process = ins.split("{")[1][:-1]
    instructions[name] = process.split(",")

""" for ins, val in instructions.items():
    print(ins, val) """

# Make a network of nodes
# Each node is an instruction
# Node receives a list of four ranges
# The node chops the ranges based on its rules, and forwards the ranges to other nodes
# Ranges that arrive at the A node are calculated.

class Instruction():
    def __init__(self, raw_instruction):
        self.parse(raw_instruction)
        #self.len
        #self.next_node
        #self.attribute
        #self.op
        #self.threshold
        
    def parse(self, raw):
        if ":" in raw:
            temp = raw.split(":")
            self.next_node = temp[1]
            self.attribute = raw[0]
            self.op = raw[1]
            self.threshold = temp[0][2:]
            self.len = 4
        else:
            self.next_node = raw
            self.len = 1

    def chop(self, a_range): 
    # In: a range
    # Out: a range that passes this instruction, a range that fails this instruction
        # Range pass
        test_range = a_range.data[self.attribute]
        low = test_range[0]
        high = test_range[1]
        # 1 - 4000
        # s < 1234
        # True: 1 - 1233
        # False: 1234 - 4000
        
        # 1 - 4000
        # s > 345
        # True: 346 - 4000
        # False: 1 - 345
                
        if len(self) == 1:
            return self
        
    def __len__(self): return self.len
            
""" inst = Instruction('m>2306:qkq')
print(len(inst)) """

class Node():
    def __init__(self, workflow):
        self.name = workflow.split("{")[0]
        self.instructions = self.gen_instructions(workflow.split("{")[1][:-1].split(","))
    def gen_instructions(self, raw_instructions):
        instructions = []
        for inst in raw_instructions:
            instructions.append(Instruction(inst))
        return instructions
    
    #Receive a range
    #Give range to each instruction in order
    #Ranges that don't 

node = Node(workflows[0])
print(node.instructions)

exit()
class Node():
    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions
    
    def parse_instruction(self, instruction): # Returns a tokenised form of the instruction, or the next instruction.
        if ">" in instruction or "<" in instruction:
            attribute = instruction[0]
            comparitor = instruction[1]
            result_index = instruction.index(":")
            comparison = instruction[2:result_index]
            result = instruction[result_index+1:]
            return [attribute, comparitor, comparison, result]
        else: # No comparison, just instruction
            return [instruction]
        
    def process_instruction(self, instruction, item):
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
    
    def process(self, range):
        pass
    
    
    
""" class Item():
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
            return self.s """
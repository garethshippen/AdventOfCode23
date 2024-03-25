from collections import deque

class Component():
    def __init__(self, name, output=None):
        self.name = name
        self.output = output
        self.state = -1
        
    def receive(self, *args):
        if self.output:
            return self.send(self.state)
    
    def send(self, out_signal):
        out = []
        for destination in self.output:
            out.append((destination, out_signal, self.name))
        return out

    def reset(self):
        pass

class FlipFlop(Component):
    def __init__(self, name, output):
        super().__init__(name, output)
    
    def receive(self, signal, *args):
        if signal == -1:
            self.state *= -1
            return self.send(self.state)
    
    def reset(self):
        self.state = -1

# This needs to know all its inputs from the beginning
class Conjunction(Component):
    def __init__(self, name, output):
        super().__init__(name, output)
        self.state = {}
    
    def receive(self, signal, sender):
        self.state[sender] = signal
        out_signal = 0
        if len(set(self.state.values())) == 1 and list(self.state.values())[0] == 1:
            out_signal = -1
        else:
            out_signal = 1
        return self.send(out_signal)
    
    def reset(self):
        self.state = {}


filename = "day19/input.txt"
#filename = "day19/testinput1.txt"
#filename = "day19/testinput2.txt"
def setup(filename):
    lines = []
    with open(filename) as source:
        for line in source.readlines():
            lines.append(line.replace("\n", "").replace(" ", ""))
    return lines
bits = setup(filename)

components = {"output":Component('output'), "rx":Component('rx')} ##################
conjs = []
for bit in bits:
    name, output = bit.split("->")
    output = output.split(",")
    if bit[0] == "%":
        components[name[1:]] = FlipFlop(name[1:], output)
    elif bit[0] == "&":
        conjs.append(name[1:])
        components[name[1:]] = Conjunction(name[1:], output)
    else:
        components[name] = Component(name, output)

for conj in conjs:
    for bit in bits:
        name, output = bit.split("->")
        output = output.split(",")
        if conj in output:
            components[conj].state[name[1:]] = -1
    
callstack = deque()

low_sigs = 0
high_sigs = 0
for i in range(1000):
    callstack.append(('broadcaster', -1, "button"))
    while callstack:
        destination, signal, source = callstack.popleft()
        if signal == -1:
            low_sigs += 1
        elif signal == 1:
            high_sigs += 1
        else:
            print(f"Something went wrong {signal}")
    
        comp = components[destination]
        new_signals = comp.receive(signal, source) 
        if new_signals:
            for new_sig in new_signals:
                if new_sig != None:
                    callstack.append(new_sig)
print(low_sigs * high_sigs)
# 856482136
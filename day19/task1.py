class FlipFlop():
    def __init__(self, output):
        self.state = -1
        self.output = output

    def process(self, signal):
        out = []
        if signal == -1:
            self.state *= signal
            for destination in self.output:
                out.append((destination, self.state))
        return out
    
    def reset(self):
        self.state = -1


class Conjunction():
    def __init__(self, output):
        self.states = {}
        self.output = output
        
    def receive(self, sender, signal):
        self.states[sender] = signal
    
    def proess(self):
        out = []
        if len(set(self.states.values())) == 1 and list(self.states.values())[0] == 1:
            out_signal = -1
        else:
            out_signal = 1
        for destination in self.output:
            out.append((destination, out_signal))
        return out
    
    def reset(self):
        self.states = {}
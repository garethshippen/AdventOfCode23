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


class Conjunction():
    def __init__():
        pass

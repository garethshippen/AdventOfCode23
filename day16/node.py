from math import inf, sqrt

class Node():
    def __init__(self, x, y, value, x_size, y_size):
        self.x = x
        self.y = y
        self.coord = (x,y)
        self.value = value
        self.x_size = x_size
        self.y_size = y_size
        self.f = inf
        self.g = inf
        self.h = self.set_h()
        self.neighbours = self.set_neighbours()
        self.open = True
        self.seen = False
        self.path = "yz"
        
    def set_h(self):
        return self.taxi()
        
    def taxi(self):
        return abs(self.x_size - self.x - 1) + abs(self.y_size - self.y - 1)
    
    def crow(self):
        return(sqrt((self.x_size - self.x - 1)**2 + (self.y_size - self.y - 1)**2))
    
    def update_g(self, value, path):
        if len(set(path[-4:])) != 1: # Not allowed to move more than three times in the same direction
            self.g = value
            self.f = self.g + self.h
            self.path = path
    
    def set_neighbours(self):
        directions = [((0, -1), "n"), ((1, 0),"e"), ((0, 1),"s"), ((-1, 0),"w")]
        neighbours = []
        for direction in directions:
            dx, dy = direction[0]
            if dx+self.x >= 0 and dx+self.x < self.x_size:
                if dy+self.y >= 0 and dy+self.y < self.y_size:
                    neighbours.append(((dx+self.x, dy+self.y),direction[1]))
        return neighbours
        
    def close(self):
        self.open = False
    
    def __lt__(self, other):
        return self.f < other.f
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
        
    def set_h(self):
        return(sqrt((self.x_size - self.x - 1)**2 + (self.y_size - self.y - 1)**2))
    
    def update_g(self, value):
        self.g = value
        self.f = self.g + self.h
    
    def set_neighbours(self):
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        neighbours = []
        for direction in directions:
            dx, dy = direction
            if dx+self.x >= 0 and dx+self.x < self.x_size:
                if dy+self.y >= 0 and dy+self.y < self.y_size:
                    neighbours.append((dx+self.x, dy+self.y))
        return neighbours
        
    def close(self):
        self.open = False
    
    def __lt__(self, other):
        return self.f < other.f
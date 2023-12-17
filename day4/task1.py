def load_data(filename):
    data = []
    with open(filename) as source:
        for line in source.readlines():
            line = [int(num) for num in line.split()]
            data.append(line)
    return data
    
def load_all(filenames):
    data = []
    for file in filenames:
        data.append(load_data(file))
    return data

sources = ["day4\\s2s.txt", "day4\\s2f.txt", "day4\\f2w.txt", "day4\\w2l.txt", "day4\\l2t.txt", "day4\\t2h.txt", "day4\\h2l.txt"]
seeds = [4239267129, 20461805, 2775736218, 52390530, 3109225152, 741325372, 1633502651, 46906638, 967445712, 47092469, 2354891449, 237152885, 2169258488, 111184803, 2614747853, 123738802, 620098496, 291114156, 2072253071, 28111202]

get_data = load_all(sources)
a2b = get_data[0]
b2c = get_data[1]
c2d = get_data[2]
d2e = get_data[3]
e2f = get_data[4]
f2g = get_data[5]
g2h = get_data[6]

class Ranges():
    def __init__(self, data):
        self.data = data
        self.ranges = []
        for row in data:
            source = range(row[1], row[1] + row[2])
            dest = range(row[0], row[0] + row[2])
            self.ranges.append((source, dest))
            
    def get_out(self, inp):
        for ranje in self.ranges:
            if inp in ranje[0]:
                diff = inp - ranje[0][0]
                out = diff + ranje[1][0]
                if out in ranje[1]:
                    return out
        return inp
            
            
first = Ranges(get_data[0])
second = Ranges(get_data[1])
third = Ranges(get_data[2])
fourth = Ranges(get_data[3])
fifth = Ranges(get_data[4])
sixth = Ranges(get_data[5])
seventh = Ranges(get_data[6])

locs = []
for seed in seeds:
    first_out = first.get_out(seed)
    second_out = second.get_out(first_out)
    third_out = third.get_out(second_out)
    fourth_out = fourth.get_out(third_out)
    fifth_out = fifth.get_out(fourth_out)
    sixth_out = sixth.get_out(fifth_out)
    locs.append(seventh.get_out(sixth_out))
    
print(sorted(locs)[0])
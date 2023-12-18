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

seed_ranges = []
for i in range(0, len(seeds), 2):
    seed_ranges.append(range(seeds[i], seeds[i] + seeds[i+1]))


get_data = load_all(sources)
a2b = get_data[6]
b2c = get_data[5]
c2d = get_data[4]
d2e = get_data[3]
e2f = get_data[2]
f2g = get_data[1]
g2h = get_data[0]

class Ranges():
    def __init__(self, data):
        self.data = data
        self.ranges = []
        for row in data:
            source = range(row[0], row[0] + row[2])
            dest = range(row[1], row[1] + row[2])
            self.ranges.append((source, dest))
    
    def get_output(self, inp):
        for ranje in self.ranges:
            if inp in ranje[0]:
                diff = inp - ranje[0][0]
                return ranje[1][0] + diff
        return inp
    
first = Ranges(a2b)
second = Ranges(b2c)
third = Ranges(c2d)
fourth = Ranges(d2e)
fifth = Ranges(e2f)
sixth = Ranges(f2g)
seventh = Ranges(g2h)

# Submitting the answer for task 1 into task 2 gives "answer too high", hence the upper limit. 

def main():
    for i in range(389056265):
        if i % 1000000 == 0:
            print(i)
        fst = first.get_output(i)
        snd = second.get_output(fst)
        trd = third.get_output(snd)
        frh = fourth.get_output(trd)
        fif = fifth.get_output(frh)
        six = sixth.get_output(fif)
        svn = seventh.get_output(six)
        
        for srange in seed_ranges:
            if svn in srange:
                print(i)
                return
            
main()
print("Done")
#137516820
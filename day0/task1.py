filename = "day0\\task1input.txt"

lines = []
with open(filename) as task:
    lines = [line for line in task]

outlines = []
for line in lines:
    numbers = "".join(c for c in line if c.isdigit())
    numbers = numbers[0] + numbers[-1]
    outlines.append(int(numbers))

            
print(sum(outlines))
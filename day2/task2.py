file_input = "input.txt"
#file_input = "testinput.txt"

lines = ["."*140]
with open(file_input) as source:
    for line in source.readlines(): 
        lines.append(list("." + line.replace("\n", "") + "."))
lines.append("."*140)

gears = []
for line in lines:
    row = []
    for i in range(len(line)):
        if line[i] == "*":
            row.append(i)
    gears.append(row)

digits = []
for line in lines:
    start_index = 0
    in_block = False
    row = []
    for i in range(len(line)):
        if line[i].isdigit():
            if in_block == False:
                start_index = i
                in_block = True
        else:
            if in_block:
                row.append(list(range(start_index, i)))
                in_block = False
    digits.append(row)
    

for i in range(len(digits)):
    if len(digits[i]) > 0:
        for block in digits[i]:
            num = ""
            for number in block:
                num += lines[i][int(number)]
            for number in block:
                index = int(number)
                lines[i][index] = num
                
matrix = {}
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        matrix[(i,j)] = c

products = []
for i,line in enumerate(lines):
    for j,c in enumerate(line):
        results = []
        if c == "*":
            results.append(matrix.get((i-1,j-1)))
            results.append(matrix.get((i-1, j)))
            results.append(matrix.get((i-1, j+1)))
            results.append(matrix.get((i, j-1)))
            results.append(matrix.get((i, j+1)))
            results.append(matrix.get((i+1, j-1)))
            results.append(matrix.get((i+1, j)))
            results.append(matrix.get((i+1, j+1)))

        nums = set([result for result in results if result.isdigit()]) # this'll be a problem if there are any squares
        if len(nums) == 2:
            a = list(nums)
            products.append(int(a[0]) * int(a[1]))

print(sum(products))

file_input = "input.txt"
#file_input = "testinput.txt"

lines = []
with open(file_input) as source:
    for line in source.readlines(): 
        lines.append("." + line.replace("\n", "") + ".")


WIDTH = len(lines[0])

no_punc = ""    
for line in lines:
    for c in line:
        if not c.isdigit() and c != ".":
            no_punc += c
SPEC_CHARS = set(no_punc)

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
    

def get_pre_row(cur_row):
    if cur_row <= 0:
        return None
    else:
        return lines[cur_row - 1]

def get_next_row(cur_row):
    if cur_row >= len(digits) - 1:
        return None
    else:
        return lines[cur_row + 1]
    
def get_back_index(cur_index):
    if cur_index <= 0:
        return None
    else:
        return cur_index - 1
    
def get_forward_index(cur_index):
    if cur_index >= len(lines[0]):
        return None
    else:
        return cur_index + 1

def get_include(prev_row, cur_row, next_row, back_index, cur_index, forward_index):
    if prev_row:
        if prev_row[cur_index] in SPEC_CHARS:
            return True
        if back_index:
            if prev_row[back_index] in SPEC_CHARS:
                return True
        if forward_index:
            if prev_row[forward_index] in SPEC_CHARS:
                return True

    if next_row:
        if next_row[cur_index] in SPEC_CHARS:
            return True
        if back_index:
            if next_row[back_index] in SPEC_CHARS:
                return True
        if forward_index:
            if next_row[forward_index] in SPEC_CHARS:
                return True
            
    if forward_index:
        if cur_row[forward_index] in SPEC_CHARS:
            return True
    
    if back_index:
        if cur_row[back_index] in SPEC_CHARS:
            return True
        
    return False

parts = []
for i, line in enumerate(lines):
    prev_line = get_pre_row(i)
    next_line = get_next_row(i)
    cur_line = line
    row = []
    for block in digits[i]:
        for number in block:
            back_index = get_back_index(number)
            forward_index = get_forward_index(number)
            include = get_include(prev_line, cur_line, next_line, back_index, number, forward_index)
            if include:
                row.append(block)
                break
    parts.append(row)


sum = 0
total = []
for i, row in enumerate(parts):
    line = []
    for block in row:
        number = ""
        for num in block:
            number += str(lines[i][num])
        line.append(int(number))
        sum += int(number)
    total.append(line)
    
print(sum)
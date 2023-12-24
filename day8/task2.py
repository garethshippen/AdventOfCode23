#inp = "21 32 43 50 52 63 128 354 980 2536 6198 14571 33400 75257 167315 367301 795349 1696172 3558635 7344376 14925482"
#inp = "0 3 6 9 12 15"

def conv_to_ints(sequence):
    nums = sequence.split(" ")
    ints = []
    for num in nums:
        ints.append(int(num))
    return ints

def calc_gaps(sequence):
    gaps = []
    for i in range(len(sequence)-1):
        gaps.append(sequence[i + 1] - sequence[i])
    return gaps

def check_not_zeros(sequence): # Returns true if there is a non-zero in the input
    for num in sequence:
        if num != 0:
            return True
    return False

def levels(sequence):
    if isinstance(sequence[0], str):
        sequence = conv_to_ints(sequence)
    rows = []
    rows.append(sequence)
    while(check_not_zeros(calc_gaps(sequence))):
        rows.insert(0,calc_gaps(sequence))
        sequence = calc_gaps(sequence)
    rows.insert(0,[0 for i in range(len(rows[0]) - 1)])
    return rows

def predict(rows):
    for i, row in enumerate(rows):
        if i == 0:
            rows[0].append(0)
        else:
            row.insert(0, row[0] - rows[i-1][0])
    return rows

def pipeline(sequence):
    l = levels(sequence)
    return predict(l)[-1][0]

filename = "day8\\input.txt"
#filename = "day8\\testinput.txt"

inp = []
with open(filename) as source:
    for line in source.readlines():
        inp.append(line.replace("\n", ""))

total = 0
for seq in inp:
    total += pipeline(seq)

print(total)

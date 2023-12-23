inp = "21 32 43 50 52 63 128 354 980 2536 6198 14571 33400 75257 167315 367301 795349 1696172 3558635 7344376 14925482"

def conv_to_ints(sequence):
    nums = sequence.split(" ")
    ints = []
    for num in nums:
        ints.append(int(num))
    return ints

def calc_gaps(sequence):
    gaps = []
    for i in range(len(sequence)-1):
        #print(sequence[i], sequence[i + 1], sequence[i+1] - sequence[i])
        gaps.append(sequence[i + 1] - sequence[i])
    return gaps

def levels(sequence):
    if isinstance(sequence[0], str):
        sequence = conv_to_ints(sequence)
    rows = []
    while(sum(calc_gaps(sequence))) != 0:
        rows.append(calc_gaps(sequence))
        sequence = calc_gaps(sequence)
    rows.append([0 for i in range(len(rows[-1]) - 1)])
    return rows


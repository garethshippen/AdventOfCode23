#filename = "day3\\testinput.txt"
#a, b, c, d = 10, 23, 25, 50

filename = "day3\\input.txt"
a, b, c, d = 10, 40, 42, 118

winning_nums = []
play_nums = []
with open(filename) as inp:
    for line in inp.readlines():
        winning_nums.append(line[a:b])
        play_nums.append(line[c:d])

for i in range(len(winning_nums)):
    temp_win = winning_nums[i].split(" ")
    temp_play = play_nums[i].split(" ")
    temp_win = [int(number) for number in temp_win if number != ""]
    temp_play = [int(number) for number in temp_play if number != ""]
    winning_nums[i] = temp_win
    play_nums[i] = temp_play

matches = []

for i in range(len(winning_nums)):
    win = set(winning_nums[i])
    play = set(play_nums[i])
    common = win.intersection(play)
    if len(common) > 0:
        matches.append(len(common))
    else:
        matches.append(0)
    
print(matches)

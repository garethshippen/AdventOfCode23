lines = []
with open("task1input.txt") as task:
    lines = [line for line in task]

num_words = {"one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9"}

rev_num = {"eno": "1",
            "owt": "2",
            "eerht": "3",
            "ruof": "4",
            "evif": "5",
            "xis": "6",
            "neves": "7",
            "thgie": "8",
            "enin": "9"}

def dig_ind_forward(word):
    for c in word:
        if c.isdigit():
            return word.index(c)

def dig_ind_back(word):
    for i in range(len(word)-1,-1,-1):
        if word[i].isdigit():
            return i

def early_index(sub):
    num = None
    index = 99
    for key in list(num_words.keys()):
        if key in sub:
            sub_index = sub.index(key)
            if sub_index < index:
                num = key
                index = sub_index
    return num

def late_index(sub):
    sub = sub[::-1]
    num = None
    index = 99
    for key in list(rev_num.keys()):
        if key in sub:
            sub_index = sub.index(key)
            if sub_index < index:
                num = key
                index = sub_index
    return num

def forward(word):
    index = dig_ind_forward(word)
    sub = word
    if index != None:
        sub = word[:index]
    num = early_index(sub)
    if num != None:
        return num_words[num]
    else:
        return word[index] 

def backwards(word):
    index = dig_ind_back(word)
    sub = word
    if index != None:
        sub = word[index+1:]
    num = late_index(sub)
    if num != None:
        return rev_num[num]
    else:
        return word[index]
    
def get_number(word):
    thing = ""
    thing += forward(word)
    thing += backwards(word)
    return int(thing)

total = 0
for line in lines:
    total += get_number(line)

print(total)
file = open("aoc_1_text.txt", "r")
all_lines = file.readlines()
num_as_word = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
    }

def words_to_nums(word):
    ret = ""
    for i in range(len(word)):
        if word[i].isdigit():
            ret+=str(word[i])
        if i+5<len(word):
            if word[i:i+5] in num_as_word:
                ret+=str(num_as_word[word[i:i+5]])
        if i+4<len(word):
            if word[i:i+4] in num_as_word:
                ret+=str(num_as_word[word[i:i+4]])
        if i+3<len(word):
            if word[i:i+3] in num_as_word:
                ret+=str(num_as_word[word[i:i+3]])
    return ret

def sum_digit_in_line(word):
    if len(word)==1:
        return 11*int(word)
    else:
        return 10*int(word[0])+int(word[-1])

tot = 0
for line in all_lines:
    line = words_to_nums(line)
    tot+=sum_digit_in_line(line)
print("part two " + str(tot))
tot = 0

def num_sum(word):
    ret = ""
    for i in range(len(word)):
        if word[i].isdigit():
            ret+=str(word[i])
    return ret

sum_all = 0
for line in all_lines:
    curr = num_sum(line)
    sum_all+=int(curr[0])*10 + int(curr[-1])
print("part one " + str(sum_all))

file.close()

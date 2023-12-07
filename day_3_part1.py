def find_dig(line):
    num_list = [0]
    for i in range(1,len(line[1])-1):
        if line[1][i] != "." and not line[1][i].isdigit():
            for j in range(3):
                for k in range(3):
                    if line[j][i-1+k].isdigit():
                        #check forward and backward for number, then add to return array
                        if num_list[-1] != add_num(line[j], i-2+k):
                            num_list.append(add_num(line[j], i-1+k))
    return num_list

def add_num(line, index):
    num = ""
    if line[index-1].isdigit() and line[index+1].isdigit():
        num = (line[index-1:index+2])
    elif line[index-1].isdigit():
        if index-2>0 and line[index-2].isdigit():
            num = (line[index-2:index+1])
        else:
            num = (line[index-1:index+1])
    elif line[index+1].isdigit():
        if index+2<len(line) and line[index+2].isdigit():
            num = (line[index:index+3])
        else:
            num = (line[index:index+2])
    else:
        num = (line[index])
    return num

file = open("aoc_3_text.txt", "r")
first_lines = file.readlines()
first, second, third = first_lines[0], first_lines[1], first_lines[2]
file.close()
file = open("aoc_3_text.txt", "r")

tot = 0
test = []
subtract = 0

temp = []
first = "." + first[:-1] + ".\n"
run = [first, second, third]
temp = find_dig(run)
for value in temp:
    test.append(int(value))
    subtract += int(value)

for line in file:
    temp = []
    first = "." + line[:-1] + ".\n"
    run = [first, second, third]
    temp = find_dig(run)
    for value in temp:
        test.append(int(value))
        tot += int(value)
    third = second
    second = first
file.close()
#value
print(tot-subtract)

#find if number of marbles is allowed
def is_possible(word, r, g, b):
    red = 0
    green = 0
    blue = 0
    for i in range(len(word)):
        if word[i].isdigit() and i>0 and not word[i-1].isdigit():
            dig = int(word[i])
            j = 1
            while word[i+j].isdigit():
                dig=dig*10+int(word[i+j])
                j+=1
            if i+6<len(word):
                if (word[i+2:i+7] == "green" or word[i+3:i+8] == "green"):
                    if dig>green:
                        green = dig
            if i+5<len(word):
                if (word[i+2:i+6] == "blue" or word[i+3:i+7] == "blue"):
                    if dig>blue:
                        blue = dig
            if i+4<len(word):
                if (word[i+2:i+5] == "red" or word[i+3:i+6] == "red"):
                    if dig>red:
                        red = dig
    return red <= r and green <= g and blue <= b

#find largest cube values by color
def minimum_cubes(word):
    red = 0
    green = 0
    blue = 0
    for i in range(len(word)):
        if word[i].isdigit() and i>0 and not word[i-1].isdigit():
            dig = int(word[i])
            j = 1
            while word[i+j].isdigit():
                dig=dig*10+int(word[i+j])
                j+=1
            if i+6<len(word):
                if (word[i+2:i+7] == "green" or word[i+3:i+8] == "green"):
                    if dig>green:
                        green = dig
            if i+5<len(word):
                if (word[i+2:i+6] == "blue" or word[i+3:i+7] == "blue"):
                    if dig>blue:
                        blue = dig
            if i+4<len(word):
                if (word[i+2:i+5] == "red" or word[i+3:i+6] == "red"):
                    if dig>red:
                        red = dig
    return [red, green, blue]

#1
file = open("aoc_2_text.txt", "r")
sum = 0
count = 1
for line in file:
    if is_possible(line, 12, 13, 14):
        sum+=count
    count+=1
print(sum)

file.close()

#2
file = open("aoc_2_text.txt", "r")
tot = 0
first, second = [], []
for line in file:
    largest_cubes = minimum_cubes(line)
    val = 1
    for num in largest_cubes:
        val*=num
    tot+=val
    first.append(tot)
print(tot)
file.close()

import re

input = open("input/day3", "r").read().splitlines()
multipSum = 0
multipSumWithFlags = 0
pattern = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
extendedPattern = re.compile(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)')
flag = True
for line in input:
    matches = pattern.findall(line)
    for match in matches:
        pair = [int(elem) for elem in (match[4:-1].split(","))]
        multipSum = multipSum + pair[0] * pair[1]
    extendedMatches = extendedPattern.findall(line)
    for match in extendedMatches :
        if (match == "do()"):
            flag = True
        elif (match == "don't()"):
            flag = False
        elif (flag) :
            pair = [int(elem) for elem in (match[4:-1].split(","))]
            multipSumWithFlags = multipSumWithFlags + pair[0] * pair[1]
print("The sum of correct multiplications is: " + str(multipSum))
print("The sum with flags = " + str(multipSumWithFlags))
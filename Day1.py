input = open("input/day1", "r")
list1 = []
list2 = []
for x in input:
    line = x.split()
    list1.append(int(line[0]))
    list2.append(int(line[1]))
list1.sort()
list2.sort()
sum = 0
simmilarityScore = 0
for i, val1 in enumerate(list1):
    sum += abs(val1 - list2[i])
    simmilarityScore += val1 * list2.count(val1)
print("The sum of distances is " + str(sum))
print("Simmilarity score "+ str(simmilarityScore))

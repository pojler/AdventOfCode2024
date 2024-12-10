import re
input = open("input/day7", "r")
records = [[int(elem) for elem in re.split(': | ', line)] for line in input]
correctSum = 0
correctSumWithNumberSplit = 0
flag = False
def validate(current, record):
    if(len(record) == 2 and current == record[1]):
        return True
    elif(len(record) == 2):
        return False
    return (current % record[-1] == 0 and validate(current/record[-1], record[0:-1])) or validate(current-record[-1], record[0:-1])

def validateWithNumberSplit(current, record):
    if(len(record) == 2 and current == record[1]):
        return True
    elif(len(record) == 2):
        return False
    strCheck = str(record[-1])
    strCurrent = str(current)
    strCurrentSplit = strCurrent[len(strCurrent)-len(strCheck):]
    goalSplit = 0
    if(strCheck == strCurrentSplit and strCurrent[0:-len(strCheck)] != ""):
        goalSplit = int(strCurrent[0:-len(strCheck)])
    return (current % record[-1] == 0 and validateWithNumberSplit(int(current/record[-1]), record[0:-1])) or (strCurrentSplit == strCheck and validateWithNumberSplit(goalSplit, record[0:-1])) or validateWithNumberSplit(current-record[-1], record[0:-1])

for record in records:
    if(validate(record[0], record)):
        correctSum = record[0] + correctSum
    if(validateWithNumberSplit(record[0], record)):
        correctSumWithNumberSplit = record[0] + correctSumWithNumberSplit
print(str(correctSum))
print(str(correctSumWithNumberSplit))
input = open("input/day2", "r").read().splitlines()

def validate(list):
    previous = 0
    i = 0
    while (i < len(list) - 1):
        diff = list[i] - list[i+1]
        if (abs(diff) > 3 or diff == 0 or previous * diff < 0) :
            return False
        i = i + 1
        previous = diff
    return True

reports = [[int(elem) for elem in line.split()] for line in input]
correct = len(reports)
additionalCorrect = 0
for report in reports:
    i = 0
    if (not validate(report)):
        correct = correct - 1
        while(i < len(report)):
            tempReport = [element for index, element in enumerate(report) if index != i]
            if(validate(tempReport)):
                additionalCorrect = additionalCorrect + 1
                break
            i = i + 1

print("There is " + str(correct)+ " correct reports")
print("There is " + str(correct + additionalCorrect)+ " correct reports with problem demptner")

input = open("input/day5", "r").read()
inputSplit = input.split("\n\n")
ruleSet = [[int(elem) for elem in line.split("|")]for line in inputSplit[0].split("\n")]
pageUpdates = [[int(elem) for elem in line.split(",")]for line in inputSplit[1].split("\n")]

def validate (update):
    for i in range(len(update) -1 ):
        if ([update[i], update[i+1]] not in ruleSet ) :
                return False
    return True

sumOfMidElementsInCorrectUpdates = 0
sumOfMidElementsInIncorrectUpdates = 0

incorrectUpdates = []

for update in pageUpdates :
    if(validate(update)):
        sumOfMidElementsInCorrectUpdates  = sumOfMidElementsInCorrectUpdates + update[(int(len(update)/2))]
    else:
         incorrectUpdates.append(update)

for update in incorrectUpdates:
    while(not validate(update)):
        for i in range(len(update) -1 ):
            if ([update[i], update[i+1]] not in ruleSet ) :
                temp = update[i+1]
                update[i+1] = update[i]
                update[i] = temp
    sumOfMidElementsInIncorrectUpdates  = sumOfMidElementsInIncorrectUpdates + update[(int(len(update)/2))]
print ("The sum of mid Page from correct update is: " + str(sumOfMidElementsInCorrectUpdates))
print ("The sum of mid Page from incorrect update is: " + str(sumOfMidElementsInIncorrectUpdates))

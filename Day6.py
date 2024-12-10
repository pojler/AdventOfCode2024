input = open("input/day6", "r").read().splitlines()

map = []

for line in input:
    map.append(list(line))

currentPosition = [0,0]
currentTurn = [-1,0]
startPosition = [0,0]
distinctPositions = 0
for i, row in enumerate(map):
    for j, element in enumerate(row):  
        if(element == "^"):
            startPosition =[i,j]
            break
currentPosition = startPosition
while (True):
    if(map[currentPosition[0]+currentTurn[0]][currentPosition[1]+currentTurn[1]] != "#"):
        map[currentPosition[0]+currentTurn[0]][currentPosition[1]+currentTurn[1]] ="X"
        currentPosition = [currentPosition[0]+currentTurn[0], currentPosition[1]+currentTurn[1]]
    else:
        if (currentTurn == [-1,0]):
            map[currentPosition[0]][currentPosition[1]] ="→"
            currentTurn = [0,1]
        elif (currentTurn == [0,1]):
            map[currentPosition[0]][currentPosition[1]] ="↓"
            currentTurn = [1,0]
        elif (currentTurn == [1,0]):
            map[currentPosition[0]][currentPosition[1]] ="←"
            currentTurn = [0,-1]
        elif (currentTurn == [0,-1]):
            map[currentPosition[0]][currentPosition[1]] ="↑"
            currentTurn = [-1,0]
    if(currentPosition[0] + currentTurn[0] == -1 or currentPosition[0] + currentTurn[0] >= len(map) or currentPosition[1] + currentTurn[1] == -1 or currentPosition[1] + currentTurn[1] >= len(map[0])):
        break

# for line in map:
#     print(line)

for line in map:
    for elem in line:
        if (elem == "X" or elem in ["→","↓","←","↑"] ):
            distinctPositions = distinctPositions + 1

possibleLoops = 0
for i in range(0, len(map)):
    for j in range(0, len(map[0])):
        copyMap = []
        if(map[i][j] in ["→","↓","←","↑","X"]):
            for line in map:
                copyMap.append(list(line))
            if([i,j] == startPosition):
                continue
            copyMap[i][j] = "#"
            currentPosition = startPosition
            currentTurn = [-1,0]
            # for line in copyMap:
            #     print(line)
            # print()
            positionWithTurn = []
            while(True):
                if(copyMap[currentPosition[0]+currentTurn[0]][currentPosition[1]+currentTurn[1]] != "#"):
                    currentPosition = [currentPosition[0]+ currentTurn[0], currentPosition[1]+currentTurn[1]]
                    if([currentPosition, currentTurn] in positionWithTurn):
                        possibleLoops = possibleLoops + 1
                        print("Loop found "+ str(possibleLoops))
                        break
                    else:
                        positionWithTurn.append([currentPosition, currentTurn])
                else:
                    if (currentTurn == [-1,0]):
                        currentTurn = [0,1]
                    elif (currentTurn == [0,1]):
                        currentTurn = [1,0]
                    elif (currentTurn == [1,0]):
                        currentTurn = [0,-1]
                    elif (currentTurn == [0,-1]):
                        currentTurn = [-1,0]
                if(currentPosition[0] + currentTurn[0] == -1 or currentPosition[0] + currentTurn[0] >= len(map) or currentPosition[1] + currentTurn[1] == -1 or currentPosition[1] + currentTurn[1] >= len(map[0])):
                    break                        



# def getAllParallelX(point, elem):
#     parallelPoints = []
#     if(elem == "→"):
#         for x in range(point[1], len(map[0])):
#             if(map[point[0]][x] == "↓"):
#                 parallelPoints.append(x)
#     if(elem == "↓"):
#         for x in range(0, point[1]):
#             if(map[point[0]][x] == "→"):
#                 parallelPoints.append(x)
#     if(elem == "←"):
#         for x in range(0, point[1]):
#             if(map[point[0]][x] == "↑"):
#                 parallelPoints.append(x)
#     if(elem == "↑"):
#         for x in range(point[1], len(map[0])):
#             if(map[point[0]][x] == "←"):
#                 parallelPoints.append(x)
#     return parallelPoints
           


# def getAllParallelY(point, elem):
#     parallelPoints = []
#     if(elem == "→"):
#         for y in range(point[0], len(map)):
#             if(map[y][point[1]] == "↑"):
#                 parallelPoints.append(y)
#     if(elem == "↑"):
#         for y in range(0, point[0]+1):
#             if(map[y][point[1]] == "→"):
#                 parallelPoints.append(y)
#     if(elem == "↓"):
#         for y in range(point[0], len(map)):
#             if(map[y][point[1]] == "←"):
#                 parallelPoints.append(y)
#     if(elem == "←"):
#         for y in range(0, point[0]+1):
#             if(map[y][point[1]] == "↓"):
#                 parallelPoints.append(y)
#     return parallelPoints

# def validateNoObstacles (currentY, currentX, newY, newX):
#     startY = min(currentY, newY)
#     stopY = max(currentY, newY)
#     startX = min(currentX, newX)
#     stopX = max(currentX, newX)

#     for y in range(startY, stopY):
#         if(map[y][newX] ==  "#"):
#             return False
#     for x in range(startX, stopX):
#         if(map[newY][x] == "#"):
#             return False
        
#     return True
 
# def vailidate8Loop(i, j):
#     parallelXPoints = []
#     parallelYPoints = []
#     for x in range(0, i):
#         if(map[i][x] == "→"):
#             parallelXPoints.append(x)
#     for x in range(i, len(map[0])):
#         if(map[i][x] == "→"):
#             parallelXPoints.append(x)

#     return True
    

# possibleLoops = []

# for i, line in enumerate(map) :
#     for j, elem in enumerate(line):
#         if (elem in ["→","↓","←","↑"]):
#            parallelX = getAllParallelX([i,j], elem)
#            parallelY = getAllParallelY([i,j], elem)
#            for x in parallelX:
#                for y in parallelY:
#                     print(str(y) + " " + str(x))
#                     if(validateNoObstacles(i, j, y, x)):
#                         print("true")
#                         possibleLoops.append([y,x])
#         if (elem == "X"):
                   


# for line in map:
#     print(line)
# print(possibleLoops)
print("Possible loops = " + str(possibleLoops))
print("There is " + str(distinctPositions) + " distinct positions guard will take")
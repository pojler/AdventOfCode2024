input = open("input/day4", "r").read().splitlines()
charactersArray = []
xmasOccurence = 0
masInShapeOfXOccurence = 0
for line in input:
    charactersArray.append(list(line))
for i, row in enumerate(charactersArray):
    for j, val in enumerate(row) :
        if (val == "X"):
            if ((j + 3) < len(row) and row[j+1] == "M" and  row[j+2] == "A" and  row[j+3] == "S") :
                xmasOccurence = xmasOccurence + 1
            if ((j - 3) > -1 and row[j-1] == "M" and  row[j-2] == "A" and  row[j-3] == "S") :
                xmasOccurence = xmasOccurence + 1
            if ((i + 3) < len(charactersArray) and charactersArray[i+1][j] == "M" and charactersArray[i+2][j] == "A" and charactersArray[i+3][j] == "S"):
                xmasOccurence = xmasOccurence + 1
            if ((i - 3) > -1 and charactersArray[i-1][j] == "M" and charactersArray[i-2][j] == "A" and charactersArray[i-3][j] == "S"):
                xmasOccurence = xmasOccurence + 1
            if ((i - 3) > -1 and (j + 3) < len (row)and charactersArray[i-1][j+1] == "M" and charactersArray[i-2][j+2] == "A" and charactersArray[i-3][j+3] == "S"):
                xmasOccurence = xmasOccurence + 1
            if ((i - 3) > -1 and (j - 3) > -1 and charactersArray[i-1][j-1] == "M" and charactersArray[i-2][j-2] == "A" and charactersArray[i-3][j-3] == "S"):
                xmasOccurence = xmasOccurence + 1 
            if ((i + 3) < len(charactersArray) and (j + 3) < len (row)and charactersArray[i+1][j+1] == "M" and charactersArray[i+2][j+2] == "A" and charactersArray[i+3][j+3] == "S"):
                xmasOccurence = xmasOccurence + 1
            if ((i + 3) < len(charactersArray) and (j - 3) > -1 and charactersArray[i+1][j-1] == "M" and charactersArray[i+2][j-2] == "A" and charactersArray[i+3][j-3] == "S"):
                xmasOccurence = xmasOccurence + 1  
        if (val == "A"):
            if (i-1 > -1 and i+1 < len(charactersArray) and j-1 > -1 and j+1 < len(row)):
                if ((charactersArray[i-1][j-1] == "M" and charactersArray[i+1][j+1] == "S") or (charactersArray[i-1][j-1] == "S" and charactersArray[i+1][j+1] == "M")):
                    if ((charactersArray[i-1][j+1] == "M" and charactersArray[i+1][j-1] == "S") or (charactersArray[i-1][j+1] == "S" and charactersArray[i+1][j-1] == "M")):
                        masInShapeOfXOccurence = masInShapeOfXOccurence + 1

            
print("There is " + str(xmasOccurence) + " XMAS Occurence" )
print("There is " + str(masInShapeOfXOccurence) + " MAS in shape of X occurences")
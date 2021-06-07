## am trying to find the solution for sorting the list using python

inputList = [21, 14, 8, 45, 26, 37, 48, 12, 14]
for x in range(len(inputList)) :
    minimum = inputList[x]
    for y in range(x, len(inputList)):
        if(minimum > inputList[y]) :
            minimum = inputList[y]
            temp = y
    inputList[x] , inputList[temp] = minimum, inputList[x]

print(inputList)

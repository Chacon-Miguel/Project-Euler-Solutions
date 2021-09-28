arr = []
grid = open("C:/Users/chaco/Desktop/test.txt", 'r')
for line in grid:
    arr.append([int(a) for a in line.split()])
grid.close()
Max = 0
currentPerm = 1
# Iterate through every row
for List in arr:
    for x in range(0, 17):
        for i in List[x:x+4]:
            currentPerm *= i
        if currentPerm > Max:
            Max, currentPerm = currentPerm, 1
        else:
            currentPerm = 1
# Iterate through every column
for column in range(20):
    for a in range(0, 17):
        for row in range(a, a + 4):
            currentPerm *= arr[row][column]
        if currentPerm > Max:
            Max = currentPerm
        currentPerm = 1
# Iterate through every diagonal that looks like a back slash
for x in range(17):
    for y in range(17):
        for a in range(4):
            currentPerm *= arr[a+x][a+y]
        if currentPerm > Max:
            Max = currentPerm
        currentPerm = 1
# Iterate through every diagonal that looks like a forward slash
for x in range(17):
    for y in range(19, 2, -1):
        for a in range(4):
            currentPerm *= arr[a+x][y-a]
        if currentPerm > Max:
            Max = currentPerm
        currentPerm = 1
print(Max)
"""
The original code was written in 2022

However the file has been accidently deleted and then rewritten through some dodgy screenshot and memory

May contain bugs

"""


import random

grid = [['*','*','*','*'],['*','*','*','*'],['*','*','*','*'],['*','*','*','*']]

def intTostr(grid):
    outGrid = [[],[],[],[]]
    for a in range(4):
        for b in range(4):
            outGrid[a].append(str(grid[a][b]))
    return outGrid

def printGrid(grid):
    mx = len(max((sub[sub.index(max(sub,key = len))] for sub in grid),key = len))
    for row in grid:
        print(" ".join(["{:<{mx}}".format(ele,mx=mx) for ele in row]))

def genNum():
    genList = [2,4]
    randNum = genList[random.randint(0,len(genList)-1)]
    return randNum

def genCoord(grid):
    x = random.randint(0,3)
    y = random.randint(0,3)
    occupied = True
    while occupied == True:
        if grid[x][y] == '*':   # This line reports index out of range occationally, it works about 50% of the time
            occupied = False
            return x,y
        else:
            x = random.randint(0,4)
            y = random.randint(0,4)

def checkRow(grid):
    flag = True
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j+1] and type(grid[i][j]) == int and type(grid[i][j+1]) == int:
                flag = False
                break
            break
    return flag

def checkCol(grid):
    flag = True
    for i in range(4):
        for j in range(3):
            if grid[j][i] == grid[j+1][i] and type(grid[j][i]) == int and type(grid[j+1][i]) == int:
                flag = False
                break
            break
    return flag

def lose(grid):
    starCount = 0
    for i in range(4):
        for j in range(4):
            if grid[i][j] == '*':
                starCount+=1
    if starCount == 0 and checkRow(grid) == True and checkCol(grid) == True:
        return True
    else:
        return False

def win(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 2048:
                return True
            else:
                return False

def left(grid):
    newGrid = []
    for i in range(4):
        newList = []
        compareNum = 0
        for j in range(4):
            if type(grid[i][j]) == int:
                if grid[i][j] != compareNum:
                    newList.append(grid[i][j])
                    compareNum = grid[i][j]
                else:
                    newList[len(newList)-1] = 2*grid[i][j]
                    compareNum = 0
        for _ in range(4-len(newList)):
            newList.append('*')
        newGrid.append(newList)
    return newGrid

def right(grid):
    newGrid = []
    for i in range(4):
        newList = []
        compareNum = 0
        for j in range(3,-1,-1):
            if type(grid[i][j]) == int:
                if grid[i][j] != compareNum:
                    newList.append(grid[i][j])
                    compareNum = grid[i][j]
                else:
                    newList[len(newList)-1] = 2*grid[i][j]
                    compareNum = 0
        for _ in range(4-len(newList)):
            newList.append('*')
        newList.reverse()
        newGrid.append(newList)
    return newGrid

def up(grid):
    newGrid = [[],[],[],[]]
    for i in range(4):
        newList = []
        compareNum = 0
        for j in range(4):
            if type(grid[j][i]) == int:
                if grid[j][i] != compareNum:
                    newList.append(grid[j][i])
                    compareNum = grid[j][i]
                else:
                    newList[len(newList)-1] = 2*grid[j][i]
                    compareNum = 0
        for _ in range(4-len(newList)):
            newList.append('*')
        for a in range(4):
            newGrid[a].append(newList[a])
    return newGrid

def down(grid):
    newGrid = [[],[],[],[]]
    for i in range(4):
        newList = []
        compareNum = 0
        for j in range(3,-1,-1):
            if type(grid[j][i]) == int:
                if grid[j][i] != compareNum:
                    newList.append(grid[j][i])
                    compareNum = grid[j][i]
                else:
                    newList[len(newList)-1] = 2*grid[j][i]
                    compareNum = 0
        for _ in range(4-len(newList)):
            newList.append('*')
        newList.reverse()
        for a in range(4):
            newGrid[a].append(newList[a])
    return newGrid

x,y = genCoord(grid)
grid[x][y] = genNum()
printGrid(intTostr(grid))
Continue = True
lFlag = False
while lFlag == False and Continue == True:
    move = input()
    if move == 'a':
        grid = left(grid)
    elif move == 'd':
        grid = right(grid)
    elif move == 'w':
        grid = up(grid)
    elif move == 's':
        grid = down(grid)
    x,y = genCoord(grid)
    grid[x][y] = genNum()
    lFlag = lose(grid)
    printGrid(intTostr(grid))
    if win(grid) == True:
        print('You win!')
        print('Continue? (Yes/No)')
        answer = input()
        if answer == 'Yes':
            Continue = True
        elif answer == False:
            Continue = False
print('Game over')
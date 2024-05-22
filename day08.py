import numpy as np

'''
--- Day 8: Treetop Tree House ---
In this day we have to find out the good spot for the tree house
The trees are in the input and you have to find out how many trees
can be seen out side the grid.

In part 2 basically we need to calculate the sceninc score of each spot.
The answer is the spot with heighest scenic score.
'''

filePath = '/Users/ali/Documents/programming-with-python-fork/aoc/day08.txt'
H = [[int(i) for i in list(line.strip())] for line in open(filePath)]


def ifUp(i, j, H):
    '''
    Input:  i: Row indes
            j: Column index
            H: data
    
    Output: Returns true if this tree can be seen from outside
            otherwise false.
    '''
    heightsUp = [H[k][j] for k in range(i) ][::-1]
    return all(_ < H[i][j] for _ in heightsUp)

def ifDown(i, j, H):
    '''
    Input:  i: Row indes
            j: Column index
            H: data
    
    Output: Returns true if this tree can be seen from outside
            otherwise false.
    '''
    m = len(H)
    heightsDown = [ H[k][j] for k in range(i+1,m)]
    return all(_ < H[i][j] for _ in heightsDown)
    
def ifRight(i, j, H):
    '''
    Input:  i: Row indes
            j: Column index
            H: data
    
    Output: Returns true if this tree can be seen from outside
            otherwise false.
    '''    
    heightsRight = H[i][j+1:]
    return all(_ < H[i][j] for _ in heightsRight)

def ifLeft(i, j, H):
    '''
    Input:  i: Row indes
            j: Column index
            H: data
    
    Output: Returns true if this tree can be seen from outside
            otherwise false.
    '''
    heightsLeft = H[i][::-1][len(H[i])-j:][::-1]
    return all(_ < H[i][j] for _ in heightsLeft)

def countVisible(H):
    '''
    Input:  H: data
    
    Output: The number of trees that are visible from
            the outside.
    '''
    outerTrees = len(H[0])*2 + ((len(H)-2)*2)
    count = 0
    for i in range(1,len(H[0])-1):
        for j in range(1,len(H)-1):

            if ifUp(i, j, H) or ifDown(i, j, H) or ifLeft(i, j, H) or ifRight(i, j, H):
                count+=1
    return count+outerTrees

print('Part One Solution: ', countVisible(H))

def distUp(i, j, H):
    '''
    Input:  i: Row indes
            j: Column index
            H: data
    
    Output: Returns distance which is the number 
            of trees that cant be seed from the
            specific spot from inside.
    '''
    dist = 0
    heightsUp = [H[k][j] for k in range(i)][::-1]
    for tree in heightsUp:
        if tree >= H[i][j] and dist == 0:
            return 1
        elif tree >= H[i][j] and dist > 0:
            return dist + 1 
        else:
            dist += 1
    return dist


def distDown(i, j, H):
    '''
    Input:  i: Row indes
            j: Column index
            H: data
    
    Output: Returns distance which is the number 
            of trees that cant be seed from the
            specific spot from inside.
    '''
    dist = 0
    m = len(H)
    heightsDown = [H[k][j] for k in range(i+1,m)]
    for tree in heightsDown:
        if tree >= H[i][j] and dist == 0:
            return 1
        elif tree >= H[i][j] and dist > 0:
            return dist + 1 
        else:
            dist += 1
    return dist


def distRight(i, j, H):
    '''
    Input:  i: Row indes
            j: Column index
            H: data
    
    Output: Returns distance which is the number 
            of trees that cant be seed from the
            specific spot from inside.
    '''
    dist = 0
    m = len(H)
    heightsRight = H[i][j+1:]
    for tree in heightsRight:
        if tree >= H[i][j] and dist == 0:
            return 1
        elif tree >= H[i][j] and dist > 0:
            return dist + 1 
        else:
            dist += 1
    return dist

def distLeft(i, j, H):
    '''
    Input:  i: Row indes
            j: Column index
            H: data
    
    Output: Returns distance which is the number 
            of trees that cant be seed from the
            specific spot from inside.
    '''
    dist = 0
    m = len(H)
    heightsLeft = H[i][::-1][len(H[i])-j:]
    for tree in heightsLeft:
        if tree >= H[i][j] and dist == 0:
            return 1
        elif tree >= H[i][j] and dist > 0:
            return dist + 1 
        else:
            dist += 1
    return dist

def getScenicScore(i,j):
    '''
    Calculates the scenic score for a specific position
    '''
    score = distUp(i, j, H) * distLeft(i, j, H) * distRight(i, j, H) * distDown(i, j, H)
    return score

def getMaxScenincScore(H):
    scenicScores = []
    for i in range(1,len(H[0])-1):
        for j in range(1,len(H)-1):
            scenicScores.append(getScenicScore(i,j))
    return max(scenicScores)

print('Part Two Solution: ', getMaxScenincScore(H))


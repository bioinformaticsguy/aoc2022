import string # We use this library to generate english alphabet.

'''
--- Day 12: Hill Climbing Algorithm ---
Today we have to find the shortest path by following certain rules.
You can only follow the path whose elevation level is equal or just one 
heigher than the current position.

In part two you have multiple starting points. You need to find out the path 
which takes the shortest among all the paths. 
'''

filePath = '/Users/ali/Documents/programming-with-python-fork/aoc/day12.txt'
rows = [[*line.strip()] for line in open(filePath)]

def getCharIndexes(char: str, rows: list) -> list[tuple]:
    '''This function takes a character and returns the 
    list with touples of all the positions of that soecific 
    character in the whole data '''
    indexList = []
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            if rows[i][j] == char:
                indexList.append((i,j))
    return indexList

def getelevationsDict() -> dict:
    '''This function simply returns the elevation 
    dictionary and also it has all the keys in lower
    case alphabets with the exception of S and E'''
    alphabet = list(string.ascii_lowercase)
    elevationDict = {}
    for i, letter in enumerate(alphabet):
        elevationDict[letter] = i
    elevationDict["S"] = elevationDict["a"]
    elevationDict["E"] = elevationDict["z"]
    return elevationDict

def getNeighbourHood(i:int, j:int) -> list[tuple]:
    '''
    This function generates the neighbourhood for
    a specific point. Neighbourhood contains 4 positons.
    up down, left and right.
    '''
    return [(i+1, j),
            (i-1, j),
            (i, j+1),
            (i, j-1)]

def findShortestPath(startChr:str, endChr:str, rows:list, part:int, startIndexesTouple:tuple=(0,0)) -> int:
    '''
    input:  This function takes 5 parameters.
            startChr: This is the starting point the path.
            endChr: This is the ending point of the path.
            rows: This is the list of lists which contains all the data.
            part: this stores the info about the part to switch some cases.
            startIndexesTouple: for the second part, you are not gonna start from (0,0)
            so this handles the starting position of current path finding.    
    
    Output: This returns the int which is the sum of the steps needed to find the shortest path.
    '''

    # If it is part one then the starting index is just gonna be the first 
    # element of the list returned by the getCharIndexes() so we index out 
    # first element and then we add the extra third element to the touple 
    # to store the depth of the current point which is initially equal 
    # to zero we will keep on updating it in the while loop.
    if part == 1:

        possibleMoves = [getCharIndexes(startChr, rows)[0] + (0,)]
        visitedSpots = {getCharIndexes(startChr, rows)[0]}

    elif part == 2:
        # Since we have checked in the part two that input starts with a 
        # and we need to start from finding the first a so our start index 
        # is equal to 0,0 which is default value of this functions parameter.
        possibleMoves = [startIndexesTouple + (0,)]
        visitedSpots = {startIndexesTouple}

    # A side note on the visited spots we have made this set to stop our while loop 
    # in ending up in the exponential blow up. So later on we will check if a certain point 
    # is already in the visited set we will not do anything with that point. Moreover, we made 
    # this a set because we dont want to have duplicated in this collection.


    elevLevel = getelevationsDict()

    # we get all the indexes of the end character and since we already know from the 
    # input that there could be just one end pos we take the first element form the list.
    endPos = getCharIndexes(endChr, rows)[0]

    # so we start out search from this while loop. We keep on looping until there are no 
    # possible moves left in the possibleMoves list of tuples.
    while len(possibleMoves) > 0:
        # We take the first elememnt form possible moves list and remove it from the list
        # pop function do two things at a time. Returns the first element if we call it with 
        # 0 and then also removed that element from the list.
        curElem = possibleMoves.pop(0)
        # we extract the info from our current element.  Where i is the row number, j is the
        # column number step is the number of steps that you have taken so far.
        i, j, step = curElem
        # We generate the neighbourhood for this point.
        neighbourHood = getNeighbourHood(i,j)
        
        for neighbour in neighbourHood:
            # ni represent the row index for the current neighbour.
            # nj represent the column index of the current neighbour.
            ni, nj = neighbour[0], neighbour[1]
            # First of all we chcek if we have already visited this neighbour.
            # we do not do any thing further in this iteration and move on the 
            # next iteration.
            if (ni, nj) in visitedSpots:
                continue
            # In this neighbour is our of bounds of our grid. 
            # it is less than 0 or the row index is greater or equal to the 
            # length of input. We do length minus one because the length function
            # starts counting from 1 and our indexes starts from 0.
            # if any of these conditions are true we continue to move on to the 
            # next iteration.
            if ni < 0 or nj < 0 or ni > len(rows)-1 or nj > len(rows[0])-1:
                continue
            
            # Since we are only allowed to move towords that direction 
            # where the next elevation level could only be just one 
            # heigher or should be queal to the previous one. 
            # so we cehcek if the differene is less greater than 1 we 
            # continue.
            if (elevLevel[rows[ni][nj]] - elevLevel[rows[i][j]]) > 1:
                continue
            # last but not the least as soon as we reach the end pos 
            # we know that we have found our destination 
            # we terminate the function by the return statement 
            # as we needed to find the steps needed to reach here we 
            # return the step number.
            if (ni, nj) == endPos:
                return step + 1
                
            # If none of the above if statements become true 
            # we know that this to our visited spots set and 
            # .
            visitedSpots.add((ni, nj))
            possibleMoves.append((ni, nj, step+1))

print('Part1 Solution: ', findShortestPath('S', 'E', rows, 1))

allAss = getCharIndexes('a', rows)
distances = [findShortestPath('a', 'E', rows, 2, i) for i in allAss]
b = [i for i in distances if i != None]

print('Part 2 Solution: ', min(b))
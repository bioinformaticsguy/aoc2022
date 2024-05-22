import numpy as np 
import matplotlib.pyplot as plt # This library was just to visualize.
from pprint import pprint as ppp # it is just for printing nicely.

'''
--- Day 14: Regolith Reservoir ---
The input was quite chellanging to parse and use it for finding the solution.
So basically in each row there are set of indexes and the indexes are seprated by
the -> signs. If we take the following example: 

498,4 -> 498,6 -> 496,6

Then we can have the following ranges:
498,4 to 498,6
498,6 to 496,6

The key thing to note here is that that in each range only one of the index, 
z or y changes. In other words these ranges are in straight lines. There could 
not be a range in both x and y are changing and that the line is diagonal. 
So rocks are aligned only horizontly or vertically.

so if we take 498,4 to 498,6 we can see that 498 stays the same i-e the x index
the y index changes from 4 to 6. So the all the positions where rock could be from 
this one pair are (498, 4), (498, 5) and (496, 6).

if we take a look at the second range 498,6 to 496,6 we can see that the range can 
be defined in reverse order as well. Like you can see that here y axis is fixed but the 
x axis is changing. Also pay attention that the y axix is going down or it is decreasing.
from 498 it decreases to 496. So the pairs for this range are going to be (498, 6), (498, 5)
and (498, 4).

once we fill our grid with the rocks we start to pour sand drops one by one from 500th x indx.
the sand will either goo down untill it hits rockbottom or it will try to to go left if that is not
possible too it will go to right it keeps on doing it untill it reaches the rockbottom or another 
sand particle. If it does not reach any of it it will fell down in the void. The solution of part one 
is to find out how many sand particles can come to a stand still.

Part2: In part two it is described that the rock bottom is infiniete on both ends but it is two levels
lower thatn the previous rockbottm (rockbottom is basically the lowest y in the data). Now when all the 
sand particles can come to a stop untill the opeing at 500 position is blocked then no new sand 
particle can come. We need to find out how many total particles can come in. 
'''


filePath = '/Users/ali/Documents/programming-with-python-fork/aoc/day14.txt'

rows = [line.strip().split(' -> ') for line in open(filePath)]

# print(rows[0])

def getStartStopXY(startingPair, endingPair):
    '''
    Given a pair it this function returns the starting and the stoping
    index for x and y. The starting index is simply the lowest value.
    The stoping index is onemore than the maximum value because in the 
    next function we are gonna loop over the range and we want to be 
    inclusive. 
    '''    
    allX = [int(startingPair[0]), int(endingPair[0])]
    allY = [int(startingPair[1]), int(endingPair[1])]
    return min(allX), min(allY), max(allX)+1 , max(allY)+1

def getListOfPairs(rowList):
    '''
    Input:  This function takes the list of lists of one row
    Output: It returns the list of will all the indexes 
            where there could be rocks for one row. 
    '''
    listOfRockPoints = []
    # we do len-1 in range because at the end our loop the second 
    # last element will be our starting pair and we will be 
    # accessing the next elemet by index+1 as the ending pair.
    for index in range(len(rowList)-1):
        # Since we have to find the ranges for all the combinations.
        # at ith position the the starting pair with be the ith pair 
        # the ending pair will be the next to it.
        startingPair = rowList[index].split(',')
        endingPair = rowList[index+1].split(',')
        # we get the starting and the stoping points from out previous function.
        startX, startY, stopX, stopY = getStartStopXY(startingPair, endingPair)
        # we will do a nested for loop to get all the 
        # combinations of the start and end of x and y.
        for xIndex in range(startX, stopX):
            for yIndex in range(startY, stopY):
                listOfRockPoints.append((xIndex, yIndex))
    return listOfRockPoints 

def getBigListOfRocPositions(rows):
    '''
    This is a simple collection combine for loop
    where we generate the list for each row and 
    then concatinate it with our big list
    in the end we return the big list.
    '''
    bigListOfRocks = []
    for row in rows:
        bigListOfRocks += getListOfPairs(row)
    return bigListOfRocks


def getRockBottom(bigListOfRocks):
    # This function gets the rock bottom which is basically 
    # the maximum value of the y or the second index in each pair.
    xes = [i[1] for i in bigListOfRocks]
    return max(xes)

def getFilledCaveGrid(bigListOfRocks):
    '''In this function we generate a zero numpy array 
    and then at all the indexes where rock could be 
    we set them to 1 and then return the updated
    array.'''
    ## This value 700 and 200 was narrowed down by 
    ## hit and trial and by manually visualizing the 
    ## grid. 
    caveGrid = np.zeros((700, 200))
    for rockPlace in bigListOfRocks:
        caveGrid[rockPlace] = 1
    return caveGrid


def sandDrop(grid, rockBottom, part):
    '''This function simulates droping the sand
    Input:      It basically takes three parameters.
                grid: the initial array.
                rockbottom: rockbottom the lowest level a sand stop can go.
                part: this one could be wither 1 or 2 to switch cases for part 1 or part 2.
    Output:     It can have different returns.
    '''

    x = 0
    y = 1
    sandPos = (500, 0)
    # if this function is used for part 2 we update the rockbottom.
    if part == 2: rockBottom += 2

    # We loop over unless the sand position do not reach rockbottom in part one
    # Otherwise, we loop over unless the sand particle starts to go below 
    # rockbottom.
    while sandPos[y] <= rockBottom if part == 1 else sandPos[y]+1 < rockBottom:
        if grid[sandPos[x], sandPos[y]+1] == 0: # Going Down Straight
            sandPos = (sandPos[0], sandPos[1]+1)
        elif grid[sandPos[x]-1, sandPos[y]+1] == 0: # Going Down Left
            sandPos = (sandPos[0]-1, sandPos[1])
        elif grid[sandPos[x]+1, sandPos[y]+1] == 0: # Going Down Right
            sandPos = (sandPos[0]+1, sandPos[1])
        else: # Reached Bottom
            return sandPos
    # if nothing works we return false in part one case because
    # we know that the snad is going in abys.
    # in part two we simply return the last sandposition.
    return False if part == 1 else sandPos # Nothing worked Sand in Abyss


def countSandParticles(filledGrid, rockBottom, part):
    """This function finds out the answer for our part 1 and 2"""
    # these new variables just make our code more readable.
    x = 0 # x is at 0 index 
    y = 1 # y is at 1 index
    count = 0
    # we get our first sand position.
    sandPos = sandDrop(filledGrid, rockBottom, part)
    # for part one we loop over unless the sand poss becomes false.
    # for part 2 we loop over unless the point where new sand comes 
    # become 1 or in other words it is filled as well.
    while sandPos if part == 1 else filledGrid[500, 0] == 0:
        # we update our grid or we add the sand at new positon
        filledGrid[sandPos[x], sandPos[y]] = 1
        count += 1
        # we drop andother sand particle
        sandPos = sandDrop(filledGrid, rockBottom, part)
    # we return the count which is answer to out puzzle.
    # filled grid is just for visualization purpose.
    return count, filledGrid

print('Part One: ', countSandParticles(
            getFilledCaveGrid(getBigListOfRocPositions(rows)), 
            getRockBottom(getBigListOfRocPositions(rows)), 
            1)[0])


print('Part Two: ', countSandParticles(
            getFilledCaveGrid(getBigListOfRocPositions(rows)), 
            getRockBottom(getBigListOfRocPositions(rows)), 
            2)[0])


# plt.imshow(maze)
# plt.show()

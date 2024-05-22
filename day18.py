import numpy as np
from pprint import pprint as ppp

'''
--- Day 18: Boiling Boulders ---
I would like to explain todays problem with the help of the following diagram:

        ^~::::::::::::::::::::::::::::::::::::::::::::::::!.          
        ~:                                                !.          
        ^:                                                !.          
        ^:                                                !.          
        ^:                                                !.          
        ^:                   ..::::::::::..               !.          
        ^:               .:^^::          ::^^.            !.          
        ^:             :^^                  .^^           !.          
        ^:           ^^:                      .~.         !.          
        ^:         :~:           .::^^::^^     .!         !.          
        ^:        ^^          .^^        .!     ~:        !.          
        ^:       ^^ #       .^  ####      !.    ~:        !.          
        ^:      :~  #      :~.  #  #     ^~     !.        !.          
        ^:      ~.  #     .!    ####   .^^     ^^         !.          
        ^:      !.  #     ^^    #  #   ^^.    :~          !.          
        ^:      ~:  ####  .~:.        .      ^^           !.          
        ^:      .!.         ::::::.. :     :~:            !.          
        ^:       .~:                    .:^:              !.          
        ^:         ^^:.             ..:^:.                !.          
        ^:           .:^^:::...:::^^::.                   !.          
        ^:               .........                        !.          
        ^:                                                !.          
        ~^                                                !.          
        :^::::::::::::::::::::::::::::::::::::::::::::::::~     

Let me explain this diagram. So there is a big grid in rectangle which is just for reference.
then we have the big cylender in which we have letter L written by hashes. This circle represents
the lava cubes. Inside lava we have small circle which is denoted by A that represents air.         

Part 1:
As in the diagram above we have represented it in 2d but the actual problem is in 3d.
For part one we need to find out the number of lava faces which could be facing the
rectangle or even air. This part can be solved by simply bruteforcing. So in the input
we are given the positios or he x, y and z axix for all the lava cubes. We loop ove the
lava points then we generate the neighbours. So we can check in the neighbours which will be 6 
since it is cube. We check weather the neighbour is already a lava cube if yes we skip ignore 
that neighbour otherwise we know that neighbout is facing air or the rectangle.

Part 2: For part two we need to exclude the faces that are facing towords the air. It is kind of 
a little bit trickey. But the idea is that we can start somewhere in the grid then we start our 
search. We generate the neighbours if the neighbour is a lava point we change it to lava face index or 2. 
Since we start  outside and the lava cylender is not broken and it makes a unbreakable wall between 
the air and the outer grid so we can never go inside the lava.
'''


filePath = '/Users/ali/Documents/programming-with-python-fork/aoc/day18.txt'
rows = [(int(line.strip().split(',')[0]),
         int(line.strip().split(',')[1]),
         int(line.strip().split(',')[2])) for line in open(filePath)]



def createDict(rows):
    D = {}
    for i, input in enumerate(rows):
        D[i] = {}

        D[i]['x'] = int(input[0])
        D[i]['y'] = int(input[1])
        D[i]['z'] = int(input[2])

    return D


def createList(rows):
    listOfLavaPos = []
    for input in rows:
        toup = (int(input[0]), int(input[1]), int(input[2]))
        listOfLavaPos.append(toup)

    return listOfLavaPos


def countFreeSpaces(dictOfLavaPos, listOfLavaPos):
    listofPossible = []
    for point in dictOfLavaPos.keys():
        x = dictOfLavaPos[point]['x']
        y = dictOfLavaPos[point]['y']
        z = dictOfLavaPos[point]['z']

        if (x+1,y,z) not in listOfLavaPos:
            val = (x+1,y,z)
            listofPossible.append(val)

        if (x,y+1,z) not in listOfLavaPos:
            val = (x,y+1,z)
            listofPossible.append(val)


        if (x,y,z+1) not in listOfLavaPos:
            val = (x,y,z+1)
            listofPossible.append(val)


        if (x-1,y,z) not in listOfLavaPos:
            val = (x-1,y,z)
            listofPossible.append(val)


        if (x,y-1,z) not in listOfLavaPos:
            val = (x,y-1,z)
            listofPossible.append(val)


        if (x,y,z-1) not in listOfLavaPos:
            val = (x,y,z-1)
            listofPossible.append(val)

    return len(listofPossible)


dictOfLavaPos = createDict(rows)
listOfLavaPos = createList(rows)
print('Part One Solution: ', countFreeSpaces(dictOfLavaPos, listOfLavaPos))


############################
## solve with numpy array ##
############################

def get3DZeroArray(rows):
    """This function takes the rows as input and 
    then finds out the mazimum values and generates
    a numpy array of zeros and returns it."""
    maxX, maxY, maxZ = getMaxXYZ(rows)
    threeDArray = np.zeros((maxX+2, maxY+2, maxZ+2))
    return threeDArray

def getMaxXYZ(rows):
    """This function simply finds out the 
    maximum values of x y and z and returns them."""
    maxX = max([touple[0] for touple in rows])
    maxY = max([touple[1] for touple in rows])
    maxZ = max([touple[2] for touple in rows])
    return (maxX, maxY, maxZ)

def getFilled3DArray(rows):
    '''this function takes the input. 
    Generated the zero array and then 
    filles up the array with 1's where
    we have x y and z coordinates from
    the input.'''
    array = get3DZeroArray(rows)
    for input in rows:
        array[input] = 1
    return array

def getNeighbourHood(point):
    '''`For a specufif point i-e x y and z axix
    this function generates 6 neighbours and returns the 
    list with touples in it.'''
    x,y,z = point
    return [(x+1, y, z),
            (x-1, y, z),
            (x, y+1, z),
            (x, y-1, z),
            (x, y, z+1),
            (x, y, z-1)]


def getSurfaceArea(rows):
    '''This function takes the input and then 
    returned the surface area i-e faces of lavacube 
    which are facing either air or rectangle. '''
    count = 0
    array = getFilled3DArray(rows)
    LAVA_POINT = 1
    # we loop over the input.
    for row in rows:
        # we generate the neighbouthood.
        neighborhood = getNeighbourHood(row)
        # we check if the neighbour is not a lavapoint.
        for neighbour in neighborhood:
            if array[neighbour] != LAVA_POINT:
                count += 1
    return count

print('Part One with 3D arrays: ', getSurfaceArea(rows))

def part2Solution(rows):
    # We keep a visited set to avoid exponentional blow up 
    # of the queue and avoid visiting same spot again.
    visited = set()

    filledArray = getFilled3DArray(rows)
    maxX, maxY, maxZ = getMaxXYZ(rows)
    # we start somewhere in the grid.
    queue = [(0,0,0)]

    # we loop over unless the queue is not empty.
    while queue:
            # remove the 0th index elemet and store it in point variable.
            point = queue.pop(0)
            # first of all we check if the current point is not int eh visited set
            if point not in visited: # so that we dont revisit points again
                neighbouthood = getNeighbourHood(point) # generating 6 neighbours
                # then we loop over the neighbours.
                for neighbour in neighbouthood:
                    nx, ny, nz = neighbour # gettig axix of the neighbour
                    # Trying to skip neighbour if it is outside of grid
                    if nx <= maxX+1 and ny <= maxY+1 and nz <= maxZ+1 and nx >= 0 and ny >= 0 and nz >= 0:
                        # we check if the neighbout is not already a lava point we add this 
                        # point to queue so that we can visit it again later because to its sides
                        # we could have another face point.
                        if filledArray[neighbour] != 1:
                            queue.append(neighbour)
                            # We also update it to lava face point or 2
                            filledArray[neighbour] = 2
                visited.add(point)
    return filledArray


def getSurfaceAreaPart2(array):
    '''In this function we simply count the 
    lava faces for part 2.'''
    count = 0
    for row in rows:
        # print(row)
        neighborhood = getNeighbourHood(row)

        for neighbour in neighborhood:
            if array[neighbour] == 2:
                count += 1
    return count



print('Part Two Solution: ', getSurfaceAreaPart2(part2Solution(rows)))
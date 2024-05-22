## Reference: https://www.youtube.com/watch?v=w7m48_uCvWI

'''
--- Day 15: Beacon Exclusion Zone ---
This problem is like a counting problem. Where we need to count the
number of spots in the row where we cant have the beacon. See the immage
below.

                1    1    2    2
       0    5    0    5    0    5
 9 ...#########################...
10 ..####B######################..
11 .###S#############.###########.

So we are given a target row and we only need to take care of that row. In toy example
that row is the 10th row. So we need to count the number of positions where beacon 
cant possible exist. In the toy example that happens to be 26 and it is not 27 because 
at one position we already have a beacon.
'''

filePath = '/Users/ali/Documents/programming-with-python-fork/aoc/day15.txt'

## we are just parcing the data and accessing the sensor and beacon x and y values.
#Sensor at x=2, y=18: closest beacon is at x=-2, y=15
listOfTouples = [(int(line.split()[2].split('=')[1].strip()[:-1]),
                  int(line.split()[3].split('=')[1][:-1]),
                  int(line.split()[8].split('=')[1].strip()[:-1]),
                  int(line.split()[9].split('=')[1].strip()))   
                            for line in open(filePath)]


def getManhatan(xSensor, xBeacon, ySensor, yBeacon):
    """This function simply returns the manhattan distance."""
    return abs(xSensor-xBeacon) + abs(ySensor-yBeacon)

def solvePart1(listOfTouples):
    '''This function takes the list of inputs i-e the touples
    that contain the x and y axis for the beacon and the sensors.
    '''
    emptyPoints = set()
    beakonPoints = set()
    for touple in listOfTouples:
        xSensor = touple[0]
        ySensor = touple[1]
        xBeacon = touple[2]
        yBeacon = touple[3]
        # For each input we calculate the manhatten distance. 
        dist = getManhatan(xSensor, xBeacon, ySensor, yBeacon)
        # then we get the vertical distsnce and the horizontal distance.
        verticalDist = abs(ySensor - 2000000)
        horizontalDist = dist - verticalDist
        ## As you can see in the diagram below we know that 
        ## the manhatten distance is rqual to a plus b.

        #                               .:~.                                          
        #                             .. .: ..                                        
        #            Start          ..   .:   ...       End                              
        #    SX-horizontalDist   ..       :      ..  SX+horizontalDist                                 
        #    .................:^!....a....SX........^::......................          
        #                   ...          .:          ...                              
        #                 ..             .:             ..                            
        #               ..               .B               ..                          
        #            ..                  .:                 ...                       
        #          ..                     :                    ..                     
        #       ...                     .~^                      ..                   
        #       ...                       S                      .:.                  
        #          ...                                        ...                     
        #             ...                                  ...                        
        #                ...                            ...                           
        #                   ...                      ...                              
        #                      ...                ...                                 
        #                         ...          ...                                    
        #                            ...     ..                                       
        #                               ....                                          
        #                                ..                                            
        #                                 .                                            
                                                                             
        ## So our starting point is the horiaontal distance minus because we want 
        ## to go left from the sensorX position
        ## end point will be plus because we want to go right from the sensorx position.
        start = xSensor - horizontalDist
        end = xSensor + horizontalDist
        ## so we count all the unique points in this range.
        for i in range(start, end+1):
            emptyPoints.add(i)
        
        ## we also count if there is already a unique beacon in this range.
        if yBeacon == 2000000:
            beakonPoints.add(xBeacon)

    # in torder to get the answer we subtract the beakon points from
    # empty places like in toy example we subtract 27-1
    return len(emptyPoints) - len(beakonPoints)

print('Part 1 Solution: ', solvePart1(listOfTouples))
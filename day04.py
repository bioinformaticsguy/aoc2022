'''
--- Day 4: Camp Cleanup ---
The input data is in the from of pairs of elves.
Each line of the data represents two elves. Elves are seprated
by comma. In the pair of elves each elve has a range. For example
take this following pair of elves:
2-4,6-8

The first elv have range 2-4 (i-e 2,3,4) and the second 
elv has the range 6-8 (i-e 6,7,8). 

Part1:  You basically need to find out all the pairs in which
        one of the elf can completely be also already present in 
        the other elv interval. Like 2345678, 2-8 can totally contain
        34567, 3-7 in it. 

Part 2: Rather than finding the full overlap in part two you need to 
        find out all the pairs that even slightly overlap.

Visualization Help:
.234.....  2-4
.....678.  6-8

.23......  2-3
...45....  4-5

....567..  5-7
......789  7-9

.2345678.  2-8
..34567..  3-7

.....6...  6-6
...456...  4-6

.23456...  2-6
...45678.  4-8

Input Explanation:
As you can see in the input below. Each line is sperated by the commna,
on each side of coma you have data of one elf. Lets call it left elf 
and right elf. So in the input in the first line you can see that the 
left elf is 2-4 and the right elf is gonna be 6-8. So 2-4 is the range 
it means that left elf will have the numbers 2, 3, 4 and the right elf will 
have 6, 7, 8.


2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8

'''


filename = '/Users/ali/Documents/programming-with-python-fork/aoc/day04.txt'
listOfAssiPairs = [line.strip() for line in open(filename)]


def getListOfIndices(pair):
    '''
    Input:  It takes the line from the input.
    Output: returns the pair in the form of a list
            that contains two touples. First touple
            represents the elf on the left side
            and the right touple represents the touple
            on the right side. 
    '''
    firstPart = pair.split(',')[0].split('-') 
    seconPart = pair.split(',')[1].split('-')
    toup1 = (int(firstPart[0]), int(firstPart[1]))
    toup2 = (int(seconPart[0]), int(seconPart[1]))
    pair = [toup1, toup2]
    return pair

def checkIfInsideInd(listPair):
    '''
    Input:  Takes the list of pair, which contains two touples.
    Output: Returns true if one of the pair completely contains the
            other's range.
    '''
    # Extracting the left and the right side.
    # or  two ranges.
    elem1 = listPair[0] 
    elem2 = listPair[1]

    # We check if left elements left number is less than 
    # or equal to the right elements left number and the 
    # right elements right number should be less than 
    # the left elements right number and vice versa.
    if elem1[0] <= elem2[0] and elem2[1] <= elem1[1]:
        return True
    if elem2[0] <= elem1[0] and elem1[1] <= elem2[1]:
        return True
    else:
        False

def getListOfNumbers(toup):
    '''
    Input:  It takes a touple which contains the 
            starting point and the ending point.
    Output: It returns the list of all the numbers that
            can appear in that range.
    '''

    listofNumbers = []
    elem1 = int(toup[0])
    elem2 = int(toup[1])
    for i in range(elem1, elem2+1):
        listofNumbers.append(i)
    return listofNumbers



def checkIfStartsInd(listPair):
    '''
    Input:  This function take the list pair
    Output: It returns true if there is overlap.
    '''

    list1 = getListOfNumbers(listPair[0])
    list2 = getListOfNumbers(listPair[1])
    return set(list1).intersection(list2)

def getCount(listOfAssiPairs, checkFun):
    '''
    Input:  it takes two paramerters.
            listOfAssiPairs: this is the list of pairs
            that is generated from the input.
            checkFun: this is the name of the functioin 
            that is going to be used in order to check 
            weather there is slight overlap (part2) or there is complete
            overlap (part1).
    Output: It returns the pairs that fulfill the certain critera according
            to part 1 or part 2.
    '''
    count = 0 
    for pair in listOfAssiPairs:
        listPair = getListOfIndices(pair)
        if checkFun(listPair):
            count += 1
    return count

print('Part 1: ', getCount(listOfAssiPairs, checkIfInsideInd))
print('Part 2: ', getCount(listOfAssiPairs, checkIfStartsInd))

## Reference
# https://www.geeksforgeeks.org/how-does-the-functools-cmp_to_key-function-works-in-python/
# 
from functools import cmp_to_key
from pprint import pprint as ppp
'''
--- Day 13: Distress Signal ---
Today we have to do the sorting of lists and then we need to find out the indexes of the 
elements which are already in the correct order. Once we have all those indices we 
then simply sum up those indices and that is our result.


In part two you need to sort all the packets or lists in the right order, but before starting, 
your sorting process you need to add two divider lists [[2]] and [[6]]. Once you sort all the 
lists in the input including the new divider lists that you just have added to your input 
yourself you get the indexes of those divider lists multipy them and you get your answer for 
part two.
'''

filePath = '/Users/ali/Documents/programming-with-python-fork/aoc/day13.txt'

def getInputDataInDict(filePath: str) -> dict:
    """This function takes the filepath and then it loopes over all the lines, 
    Then it pairs up the lines. As we know that in out input file two rows 
    which are next to each other and theat are not empty line are a pair of 
    lists that we need to sort.
    Input:  string that comprises of file path.
    Output: A dictionary where each key represents the unique pair number and the 
            value is a touple which consists of two lists list A and list B.
    """

    pairDict = {}
    pairNum = 1
    pair = ()
    with open(filePath) as file:
        for line in file:
            if line == "\n":
                pairDict['Pair'+str(pairNum)] = pair
                pairNum += 1
                pair = ()
            else:
                # Adding Second element to the touple.
                pair += (eval(line.strip()),)
        # adding the last pair to the dictionary that we found.
        pairDict['Pair'+str(pairNum)] = pair
    return pairDict

def getBiggerListLen(list1, list2):
    '''
    Input:      This fucntion takes two parameters as input.
                Both of them are lists.

    Output:     It returns the lenth of that list who is bigger.
    '''
    if len(list1) >= len(list2):
        return len(list1)
    else: 
        return len(list2)

def comparison(left, right):
    '''
    This is the main function which is the brains of solving todays problems.
    Input: it takes two lists left and right.
    Output: Returns 0 if both lists are equal.
            1 if left side is smaller than the right one.
            -1 if the right one is smaller than the left one.
    '''

    # This is a recursive solution our base case is simple.
    # if left and right both are int we check for three things.
    if isinstance(left, int) and isinstance(right, int):
        # if left is smaller we return 1 which means inputs are in right order.
        if left < right:
            # print('True -> Left side is smaller so inputs are in right order')
            return 1
        # if left is smaller we return -1 which mens that the imputs are not in right order.
        elif left > right:
            # print('True -> Left side is bigger so inputs are NOT in right order')
            return -1
        # if both are equal we return 0
        elif left == right:
            return 0
            
    # if left is int and right is list we convert left to a list and 
    # call the function again.
    if isinstance(left, int) and isinstance(right, list):
        return comparison([left], right)

    # if right is int and left is list we convert right to a list and 
    # call the function again.
    if isinstance(left, list) and isinstance(right, int):
        return comparison(left, [right])

    # if both are lists then we need to do something a little bit more complicated.
    if isinstance(left, list) and isinstance(right, list):
        # We will loop over the bigger list.
        for i in range(getBiggerListLen(left, right)):
            # When there is just one element in the left side
            # then we know that the lists are in the right order
            # so we return 1 because we know that the left list is 
            # finished and there are no more elements in the left list
            # we stop here and we do not need to study any further elements.
            if i == len(left):
                return 1
            # If the I becomes equal to or greater than the length of right 
            # list so it menas that the left list is longer so we return -1
            # and we do not need to study any further elements.
            if i >= len(right):
                return -1

            # if both of those cases do not work we can then store our result
            # for the ith elements in the lists.
            result = comparison(left[i], right[i])
            # Then we move on to check if the result is equal to 0 mens that both elements
            # are equal.
            if result == 0: 
                # then we move ahead to check if i is still less then the length of left list
                # we continue to the next element.
                if i < len(left):
                    continue
            # if the result is 1 means that the left element is smaller 
            # then we do not need to check the rest of the elements so we stop here.
            # and return 1
            if result == 1:
                return 1
            # if we get -1 we do not need to check any further elements and we return -1
            # means that the left list is not smaller than the right list.
            if result == -1:
                return -1


dataDict = getInputDataInDict(filePath)

def part1Solution(dataDict):
    '''This function keeps on collecting the indices of the list pairs, 
    where the left list is smaller than the right one. Then it 
    returns the sum of all those indices.'''
    indices = []
    for i in range(len(dataDict)):
        key = 'Pair' + str(i+1)
        left = dataDict[key][0]
        right = dataDict[key][1]
        comp = comparison(left, right)
        if comp == 1:
            indices.append(i+1)
    return sum(indices)


print('Part One Solution: ', part1Solution(dataDict))

## This time we do not need to make the pairs so we simply collect all the 
## lists and we just skip the new line characters.
rows = [eval(line.strip()) for line in open(filePath) if line != '\n']
rows.append([[2]]) # Adding divider elements as suggested in the problem.
rows.append([[6]])

## For part two we are gonna use the small python trick that is gonna make our life 
## way to much easier. So in the sorted function there is a parameter key which can be set 
## up to cmp_to_key(). 
##  This is a cool function that will only take a callable function of your choice.
## then it returns a unique key which helps to sort out the whole thing.
## since we have already developed the compare function above for part one.
## we can pass that function to cmp_to_key and then we will have the 
## sorted list according to our rules.
rows = sorted(rows, key=cmp_to_key(comparison), reverse=True)

## In the following for loop we simply get the indices of the divider elements
for i, element in enumerate(rows):
    if element == [[2]]:
        dividerPacket1 = i + 1
    if element == [[6]]:
        dividerPacket2 = i + 1

## the answer for the part two is the sum of the indices of those
##  two divider packets.
print('Part 2 Solution: ', dividerPacket1 * dividerPacket2)
'''
--- Day 10: Cathode-Ray Tube ---
In this day we have to find out the signal strengths at specific cycles.
Signal strength is considered as the value of X register into cycle number.

Part 2: We need to print the result on the screen after following certain 
        rules.
'''

filePath = '/Users/ali/Documents/programming-with-python-fork/aoc/day10.txt'

input = [line.strip().split(' ') for line in open(filePath)]


def getSum(programInput):
    '''
    Input:  This function takes the input from the file. 
    Output: It returns the sum of the signal strengths at
            20th, 60th, 100th, 140th, 180th, and 220th
    '''
    impCycleNumbers = [20,60,100, 140, 180, 220]
    # Initializing the dictionary where the key represents 
    # as the cycle number and then value is intially set to 
    # the identity value i-e 1. Later on we will keep on 
    # updating this dictionary.
    dictOfSignalStrengths = {key:1 for key in range(1,220+1)}
    # Initializig the cycle number and the register value with
    # the identity value i-e 1
    cycleNum = 1 
    registerVal = 1

    for instruction in programInput:
        # Since instructions are stored in the form of lists
        # having two elements at most. It has two elements 
        # when the instruction is add. So we check weather 
        # the length of instruction is greater then one. 
        # it is basically a way to set up the addx case.
        if len(instruction) > 1:
            # at the begining we increment the cycle number.
            cycleNum += 1
            # update the signal strength for that current cycle number
            dictOfSignalStrengths[cycleNum] = cycleNum * registerVal
            # increment the cycle number again the 2nd increment.
            cycleNum += 1
            # update the new register value and then update the 
            # signal strength again.
            registerVal += int(instruction[1])
            dictOfSignalStrengths[cycleNum] = cycleNum * registerVal

        # in case of noop instruction simply increment the cycle by one.
        elif len(instruction) == 1:
            cycleNum += 1
        
        # Updating the last value.
        dictOfSignalStrengths[cycleNum] = cycleNum * registerVal

    return sum([i[1]  for i in dictOfSignalStrengths.items() if i[0] in impCycleNumbers])


print('Part One Solution: ', getSum(input))


def printScreen(screen):
    '''This fucnction basically takes the screes which 
    is nothing more than a long list of string characters 
    of length 6*40 as the input and then it prints the 
    screen in the readable format.'''

    # list of indexes with step of 40
    indList = [i for i in range(0,len(screen),40)]
    for i, val in enumerate(indList):
        line = ''.join(screen[val:val+40]) 
        print(line, len(line))
instructions = [line.strip() for line in open(filePath)]

def updateScreen(instructions, screen):
    '''This function takes the screen and the set 
    of instructions and then returns the updated 
    screen'''
    spritePositioin = 1
    cycle = 0    
    # loop over all the instructions
    for instruction in instructions:
        # if instruction is not noop.
        if len(instruction.split()) > 1:
            # we looping over twice because in 
            # addx case we need run cycle twice.
            for i in range(2):
                # if there is overlap between the current sprite position 
                # and the cycle number.
                if cycle%40 in [spritePositioin-1,spritePositioin,spritePositioin+1]:
                    # Then sprite prints hash at the cycle position.
                    screen[cycle] = '#'
                cycle += 1 
            # it fetches the new position of the sprite 
            # and updates it
            value = int(instruction.split()[1])
            spritePositioin += value

        # when instruction is noop case.
        if len(instruction.split()) == 1:
            # we run it for one time and if it is overlapping sprite
            # prints #.
            if cycle%40 in [spritePositioin-1,spritePositioin,spritePositioin+1]:
                screen[cycle] = '#'
            cycle += 1

screen = [" " for i in range(6*40)]
updateScreen(instructions, screen)
print('Part Two solution is below:')
printScreen(screen)
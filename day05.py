'''
--- Day 5: Supply Stacks ---

Note: The input was quite complicated to parse. Especially
the crates. So I manually stored the crates in the form of
dictionary.

This problem basically applying the steps given in the input
and then arrange the crates. Eventually after applying all the 
steps you see which crates are on the top of the docks.

In second part if do not need to move multiple crates one by one
hence it changes the configuration. In the end we have to pick the 
top crates but this time the answer will be different as the 
configuration is also different.

Sample Input Explanation:
Initialy you have the setup of crates. You can see that we have three places
where we can put crates 1, 2, and 3. After the crates configuration you can see 
that you have the instructions. That you have to follow one by one. 


    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2

'''

filename = '/Users/ali/Documents/programming-with-python-fork/aoc/day05.txt'
instructionList = [[int(line.split()[1]), int(line.split()[3]), int(line.split()[5])] for line in open(filename)]

def moveItPartOne(cratesPos, nOfCrates, initialPos, finalPos):
    '''
    Input:  This takes 4 parapmeters.
            createpos:  this is the current positions of the crates which is the 
                        dictionary and it is created from the input.
            noOfCrates: this stores the number of crates that we hvae to move.
            initialPos: this the position of the starting.
            finalpos: This is the final position of the crates.

    Output: Returns the updated crates positions dictionary.
    '''

    # For loop to take one crate at a time.
    for _ in range(nOfCrates):
        # remove the crate from the orignal psition.
        popped = cratesPos[initialPos].pop(0)
        # update the create position in the dictionary
        cratesPos[finalPos] = [popped] + cratesPos[finalPos]
    return cratesPos

def moveItPart2(cratesPos, nOfCrates, initialPos, finalPos):
    '''
    Input:  This takes 4 parapmeters.
            createpos:  this is the current positions of the crates which is the 
                        dictionary and it is created from the input.
            noOfCrates: this stores the number of crates that we hvae to move.
            initialPos: this the position of the starting.
            finalpos: This is the final position of the crates.

    Output: Returns the updated crates positions dictionary.
    '''

    # Unlike the other function for part one
    # this does the job in one go
    # it takes the whole stack of crates 
    # removes from original position
    # then updates the dictionary of crates pos
    popped = cratesPos[initialPos][:nOfCrates]
    cratesPos[initialPos] = cratesPos[initialPos][nOfCrates:]    
    cratesPos[finalPos] = popped + cratesPos[finalPos]
 
    return cratesPos


def getResult(cratesPos):
    """
    Input:  This function simply takes the crate position dictionary
    Output: Returns the printable string which are all the top crates in the
            dictionary of create positons. 
    """
    return ''.join([cratesPos[i][0] for i in cratesPos.keys()])


def applyInstructions(instructionList, cratesPos, part):
    '''
    Input:  This takes theree parameters.
            instructionsList: Which is the list generated from the input.
            createPos: The initial position fo the crates
            part: this is a intger 1 for part one and 2 for part 2.
            basically it controls which movement function will be used.
            As this function can be used for solving both parts of day 5.
    Output: Returns the final positon of the crates in the form of a dictionary.
    '''
    for instruction in instructionList:
        nOfCrates = instruction[0]
        initialPos = instruction[1]
        finalPos = instruction[2]
        if part == 2:
            cratesPos = moveItPart2(cratesPos, nOfCrates, initialPos, finalPos)
        else:     
           cratesPos = moveItPartOne(cratesPos, nOfCrates, initialPos, finalPos)
    return cratesPos




cratesPos = {1: ['S', 'P', 'H', 'V', 'F', 'G'],
             2: ['M', 'Z', 'D', 'V', 'B', 'F', 'J', 'G'], 
             3: ['N', 'J', 'L', 'M', 'G'],
             4: ['P', 'W', 'D', 'V', 'Z', 'G', 'N'],
             5: ['B', 'C', 'R', 'V'],
             6: ['Z', 'L', 'W', 'P', 'M', 'S', 'R', 'V'],
             7: ['P', 'H', 'T'],
             8: ['V', 'Z', 'H', 'C', 'N', 'S', 'R', 'Q'],
             9: ['J', 'Q', 'V', 'P', 'G', 'L', 'F']}


finalCratesPosPart1 = applyInstructions(instructionList, cratesPos, 1)
print('Part1: ', getResult(finalCratesPosPart1))

cratesPos = {1: ['S', 'P', 'H', 'V', 'F', 'G'],
             2: ['M', 'Z', 'D', 'V', 'B', 'F', 'J', 'G'], 
             3: ['N', 'J', 'L', 'M', 'G'],
             4: ['P', 'W', 'D', 'V', 'Z', 'G', 'N'],
             5: ['B', 'C', 'R', 'V'],
             6: ['Z', 'L', 'W', 'P', 'M', 'S', 'R', 'V'],
             7: ['P', 'H', 'T'],
             8: ['V', 'Z', 'H', 'C', 'N', 'S', 'R', 'Q'],
             9: ['J', 'Q', 'V', 'P', 'G', 'L', 'F']}


finalCratesPosPart2 = applyInstructions(instructionList, cratesPos, 2)
print('Part2: ',getResult(finalCratesPosPart2))


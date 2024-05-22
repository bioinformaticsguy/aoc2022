"""
--- Day 3: Rucksack Reorganization ---
You basically again have to calculate some 
sort of score. In the input you are given
the lines of random alphabet. Each line can be split
into two euqal sections i-e compartment A and 
compartment B. 


Steps:
    1:  Find out the duplicate items. More specifically
        Where items being the same characters in compartment A
        and in the compartment B. 
    2:  Find out score for each rucksack (Score is equal to the alphabet 
        index of the item a-z = 1-26 and A-Z = 27-52).
    3:  Find out the sum of all scores.


Part 2: Basically is slight changes to the part one. Now the rucksacks
the rows are supposed to be considered in the form of groups of three.
Then you find the common item among that group. The score of that group 
is the score for that specific common item in the group. Eventually you 
return the sum of scores.

Expnantion With the sample Input:
S😀, as you can see that the lines contain just alphabets:

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


filename = '/Users/ali/Documents/programming-with-python-fork/aoc/day03.txt'
listOfRucksacks = [line.strip() for line in open(filename)]


def getduplicateItem(rucksack):
    '''
    Input:  Takes the rucksack which is simply one 
            row of the input. 
    Output: It then splits that row into equal parts
            eventually finding the common elements.
            Then returning the list with common elements.
    '''
    # We convert the elements of the compartment
    # to sets so that the duplicates are removed
    # if any.
    comp1 = set(rucksack[0:int(len(rucksack)/2)])
    comp2 = set(rucksack[int(len(rucksack)/2):])

    # Moreover as we have sets in the return statement
    # duplicate items can be found easily by just doing
    # the intersection of both sets. 
    return list(comp1.intersection(comp2))[0]

def getScore(letter):
    '''
    Input:  Takes one character as a string from enelish
            alphabet. It could be big or small.
    Output: Returns the score which is basically the 
            index of the long abcABC string. The index starts 
            from one.
    '''
    # Storing small abc in the variable and then
    # concatinating the big ABC.
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = alphabet + alphabet.upper()
    # Returning the index + 1 which is equal to 
    # the score. 
    return alphabet.find(letter) + 1 

def finalScore(listOfRucksacks):
    '''
    Input:  The list of the rucksacks
    Output: Returns the sum of score.
    '''
    score = 0
    for rucksack in listOfRucksacks:
      score += getScore(getduplicateItem(rucksack))  
    return score


def getduplicateItemAmongThree(rucksack1, rucksack2, rucksack3):
    """
    Input:  Takes three ruckscaks 1,2,3
    Output: Returns the common item among three.
    """
    return list(set(rucksack1).intersection(rucksack2).intersection(rucksack3))[0]

def badgeScore(listOfRucksacks):
    '''
    Input:  Takes the list of rucksacks.
    OutPut: Returns the final score after generating 
            the triades of the rucksacks. Finding the
            common thing among those three and then
            calculating the score and adding it to the 
            final score.
    '''

    score = 0
    for rucksack in range(0,len(listOfRucksacks),3):
        rucksack1 = listOfRucksacks[rucksack]
        rucksack2 = listOfRucksacks[rucksack+1]
        rucksack3 = listOfRucksacks[rucksack+2]
        letter = getduplicateItemAmongThree(rucksack1, rucksack2, rucksack3)
        score += getScore(letter)
    return score

print('Part 1: ', finalScore(listOfRucksacks))
print('Part 2: ', badgeScore(listOfRucksacks))


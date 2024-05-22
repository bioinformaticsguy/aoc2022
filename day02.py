"""
--- Day 2: Rock Paper Scissors ---
Basically two players are playing rock sizors game
in input column on the left represents the oponent 
coulumn on the right represents you. Your task is 
to follow rules for specific combinatios and find 
out the answer or the final score.

Part one and part two differes on the basis of the 
rules that are for calculating the score.

You calculate the score based on you win or loose or what you pick
the scores for win loose or draw are given below:

Loose           = 0 
Draw            = 3
Win             = 6

Sample Input Explanation:
In the input below. Left side represent your oponent and the right side
represents you. 

A Y
B X
C Z

The ABC and XYZ are associated with rock papers and 
sissors like below:

AX = ROCK       = 1
BY = PAPER      = 2
CZ = SICCSORS   = 3

"""


filename = '/Users/ali/Documents/programming-with-python-fork/aoc/day02.txt'

def getdata(filename):
    '''
    Input: Path of file
    Output: List of lists
    '''
    listOfLists = []
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            listOfLists.append(line.strip().split(" "))
    return listOfLists

def getScore(first, second):
    '''
    Input:  Player one and player two current selection.
            Where player first is oponent and 
            second is you. Also remember the left and 
            right conditions.
    Output: Score for that given condition.
    '''
    # X scores 1 and Draw Scores 3 
    if first == 'A' and second == 'X':
        return 1 + 3
    # Y scores 2 and Win Scores 6
    elif first == 'A' and second == 'Y':
        return 2 + 6
    # Z scores 3 and Loose scores 0
    elif first == 'A' and second == 'Z':
        return 3 + 0
    # X scores 1 and Loose scores 0
    elif first == 'B' and second == 'X':
        return 1 + 0
    # Y scores 2 and Draw scores 3
    elif first == 'B' and second == 'Y':
        return 2 + 3
    # Z scores 3 and Win scores 6
    elif first == 'B' and second == 'Z':
        return 3 + 6
    # X scores 1 and Win scores 6
    elif first == 'C' and second == 'X':
        return 1 + 6
    # Y scores 2 and Loose scores 0
    elif first == 'C' and second == 'Y':
        return 2 + 0
    # Z scores 3 and Draw scores 3
    elif first == 'C' and second == 'Z':
        return 3 + 3
    

def getFinalSum(listOfTurns, func):
    """
    Input:  listOfTurns: Just a simple list
            with instructions.
            func: name of the function i-e
            there are different functions
            for part one and for part 2.
    Output: Returns the sum of all the scores i-e
            the final score.
    """
    score = 0 
    for turn in listOfTurns:
        tempScpre = func(turn[0], turn[1])
        score += tempScpre
    return score


# print(getScore('C', 'Z'))


def getScoreUpdated(first, second):
    '''
    Input:  First is the oponents Pick
    Output: loose, draw or win.
    
    It is a little bit twisted this time.
    Now, X, Y, Z represent loose, draw and 
    win respectively. See as follow:

    X -> Loose
    Y -> Draw   
    Z -> Win    
     
    So the first number in 
    the return statement is the score that 
    you get as a result of picking rock, 
    papers and sizors (i-e, A, B and C).
    Second number is the number from the 
    result of the specific round. Which could be 
    either X, Y or Z.    
    '''

    # You pick C=3 in order to loose=0 
    if first == 'A' and second == 'X':
        return 3 + 0
    # You pick A=1 in order to draw=3
    elif first == 'A' and second == 'Y':
        return 1 + 3
    # You pick B=2 in order to win=6
    elif first == 'A' and second == 'Z':
        return 2 + 6
    # You pick A=1 in order to loose=0
    elif first == 'B' and second == 'X':
        return 1 + 0
    # You pick B=2 in order to draw=3
    elif first == 'B' and second == 'Y':
        return 2 + 3
    # You pick C=3 in order to win=6
    elif first == 'B' and second == 'Z':
        return 3 + 6
    # You pick B=2 in order to loose=0
    elif first == 'C' and second == 'X':
        return 2 + 0
    # You pick C=3 in order to draw=3
    elif first == 'C' and second == 'Y':
        return 3 + 3
    # You pick X=1 in order to win=6
    elif first == 'C' and second == 'Z':
        return 1 + 6


listOfTurns = getdata(filename)
print('Part One:  ', getFinalSum(listOfTurns, getScore))
print('Part Two: ', getFinalSum(listOfTurns, getScoreUpdated))


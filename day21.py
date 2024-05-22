import operator

'''
--- Day 21: Monkey Math ---
This problem we have to find out the value of root. The value 
of root could depend on other monkeys. so this problem could be 
solved with the help of recursion.
'''

filePath = '/Users/ali/Documents/programming-with-python-fork/aoc/day21.txt'


def makeDictionary():
    '''This function generates the dictionary for the
    input where the keys are the names of the monkeys
    since the monkeys are unique and the values
    are either the value of the monkey or it is the
    expression to find out the value of the 
    monkey.'''
    input = [line.strip() for line in open(filePath)]
    dictionary = {}
    for i in input:
        i = i.split(' ') 
        key = i[0][:-1]
        value = i[1:]
        dictionary[key] = value
    return dictionary

def getOpsDict():
    '''This function simply returns the dictionary 
    for the operations so that we dont not have to 
    use several if statements. The keys are the string
    representaions of the operators and the values are 
    the operators itself.'''
    return { "+": operator.add, 
             "-": operator.sub,
             '*' : operator.mul,
             '/' : operator.truediv } # etc.

def rootYells(monkey):
    monkStor = makeDictionary()
    ops = getOpsDict()

    # base case when we already have the value of that monkey 
    # in the dictionary.
    if len(monkStor[monkey]) <= 1:
        return int(monkStor[monkey][0])

    # in the recursive case we access the left and right monkeys and the operator
    # then we call the function on each monkey with the operator.
    else:
        monkey1 = monkStor[monkey][0]
        operator = monkStor[monkey][1]
        monkey2 = monkStor[monkey][2]
        
        return ops[operator](rootYells(monkey1),rootYells(monkey2))
 
print('Part one solution: ', rootYells('root'))






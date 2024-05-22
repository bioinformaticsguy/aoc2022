from pprint import pprint as ppp ## this is just for debugging
import operator ## this is to perform the operator functions
import heapq ## To get two largest numbers from a li

'''
--- Day 11: Monkey in the Middle ---
This problem is about finding out the score. The score happens to be equal to the 
total number of items a monkey inspects over the span of twenty rounds. There are 
certain ground rules for each round.
'''

filePath = '/Users/ali/Documents/programming-with-python-fork/aoc/day11.txt'

def getMonkeyDataInLists(filePath):
    '''
    Input:   This funtion takes the file path.
    Output:  Returns the list of lists in which
             sublists contains the data about one 
             monkey.
    '''
    input = [line.strip() for line in open(filePath)]
    monkeyDataLists = []
    monkeyName = None
    for line in input:
        # Case when you find a new monkey
        if line[:6] == 'Monkey':
            ## If you already have the monkey name 
            ## means you also have all the lines of that 
            ## specific monkey so you add that monkey list 
            ## to the big list.
            if monkeyName:
                monkeyDataLists.append([monkeyName]+monkeySet[:-1])
            ## Otherwise we will rest the list and update the monkey
            ## name to the new name.
            monkeyName = line
            monkeySet = []
        # In this case we know that this current line is the 
        # instruction like so we will keep on adding
        # it to the monkey data list.
        else:
            monkeySet.append(line)
    ## Here we add the data of the last monkey to the
    ## big list.
    monkeyDataLists.append([monkeyName]+monkeySet)
    return monkeyDataLists

def getDataDict(monkeyDataLists):
    '''
    This function takes the input in the form of the list 
    of lists. Then it generates the dictionary where the key
    of the key represents the monkeys because all the monkeys
    are unique the value of the key is also a dictionary that
    stores the following details about that specific monkey.
    
    InspectCount:   Stores the int which is the count of the 
                    total items inspected by that monkey.
    
    Items:          Stores the list of items that monkey has.

    Operator:       It is the sign "+", "-", '*' or '/'

    OperatorNum:    This is the number for updating the 
                    worry level.

    divTestNum:     Number to divide for the test which decides
                    to which monkey the item will go.

    
    ifTrue:         This stores number of the monkey if the 
                    test passes.

    ifFalse:        This stores the number of the monkey 
                    if the test fails.
    '''
    dataDict = {}
    for monkeyDataList in monkeyDataLists:
        for line in monkeyDataList:
            if line.startswith('Monkey'):
                monkeyName = line[:-1]
                dataDict[monkeyName] = {'inspectCount' : 0}
            if line.startswith('Starting items'):
                items = [int(i) for i in line.split(':')[1].strip().split(', ')]
                dataDict[monkeyName]['items'] = items
            if line.startswith('Operation'):
                operator = line.split('=')[1].split(' ')[2]
                operatorNum = line.split('=')[1].split(' ')[3]
                dataDict[monkeyName]['operator'] = operator
                dataDict[monkeyName]['operatorNum'] = operatorNum
            if line.startswith('Test'):
                divTestNum = line.split(':')[1].split()[2]
                dataDict[monkeyName]['divTestNum'] = divTestNum
            if line.startswith('If true'):
                ifTrue = line.split(':')[1].split()[3]
                dataDict[monkeyName]['ifTrue'] = ifTrue
            if line.startswith('If false'):
                ifFalse = line.split(':')[1].split()[3]
                dataDict[monkeyName]['ifFalse'] = ifFalse
    return dataDict

def getOpsDict():
    '''This is simple function that just returns the dictionary
       with the operator strings as the keys and the 
       operator function as the value.'''
    return { "+": operator.add, 
             "-": operator.sub,
             '*' : operator.mul,
             '/' : operator.truediv }

def applyOperation(old, operator, new):
    '''
    Input:      It takes three parameters.
                Old: This is the old worry level.
                Operator: String which could be "+", "-", '*' or '/'.
                New: this is the new oerry level to operate with.

    Return:     It returns the updated worry level.
    '''
    if new == 'old':
        return getOpsDict()[operator](int(old),int(old))
    else:
        return getOpsDict()[operator](int(old),int(new))

def test(afterBored, divTestNum):
    '''
    Input:      This takes two inputs.
                afterBored: this is the number which represents the 
                worry level after the monkey gets bored with that specific item.
                divTestNum: this is the number that is used to perform the test 
                which later on decides to which monkey this item will go next. 
    '''
    if (int(afterBored)%int(divTestNum)) == 0:
        return True
    else:
        return False


def round(dataDict, part):
    '''
    This is the main beafy function that works as the brains of solving this days problem.
    Inpout:     We have two inputs.
                dataDict: This dictionary whcich contains the info abut the monkeys.
                part: this is just an integer which could be either 1 or 2 it is to 
                switch between some cases in case of using this function for part 1 or 
                for part two.
    Output:     This returns the updated dataDict. By updated we mean the changes in the 
                inspection count, current list of items.
    '''
  
    for monkeyNum in range(len(dataDict)):
        # print('Monkey ' + str(monkeyNum) + ':')
        curMonkeyDict = dataDict['Monkey '+ str(monkeyNum)]
        items = curMonkeyDict['items']
        operator = curMonkeyDict['operator']
        operatorNum = curMonkeyDict['operatorNum']
        divTestNum = curMonkeyDict['divTestNum']
        for item in items:
            curMonkeyDict['inspectCount'] += 1
            # print("   Monkey inspects an item with a worry level of" ,item)
            updatedItem = applyOperation(item, operator, operatorNum)
            # print("       Worry level is multiplied by ", operatorNum, 'to', updatedItem)
            # if wDiv <= 1:
            #     afterBored = int(updatedItem//100)
            # if we are solving it according to the part one rules we simply divide it by 
            # 3 and get the after bored value.
            if part == 'part1':
                afterBored = updatedItem//3
            # In part too technically we do not need to do anything at this step. But 
            # the problem with doing nothing is that the numbers become so huge that 
            # it becomes impossible to get the answer in timly manner. So we take modulo of it 
            # highest common factor so that we get such a number which gets same remainder 
            # when we do the monkey test and the item is thrown to correct monkey.
            elif part == 'part2':
                afterBored = updatedItem%getHCF(dataDict)
            # print("       Monkey gets bored with item. Worry level is divided by 3 to ", int(updatedItem/3))
            # print('Monkey ', monkeyNum, 'item', item, 'Updated Item', updatedItem, 'aferBored', afterBored)

            # in case of the test is true item is thrown to next monkey.
            if test(afterBored, divTestNum):
                newMonkey = 'Monkey ' + curMonkeyDict['ifTrue']
                curMonkeyDict['items'] = curMonkeyDict['items'][1:]
                dataDict[newMonkey]['items'] += [afterBored]
                # print('       Current Worry Level is divisible by ', divTestNum)
                # print('       Item with worry level ', afterBored, ' is thrown to monkey', curMonkeyDict['ifFalse'])

            # in case of the test is false item is thrown to next monkey.
            else:
                newMonkey = 'Monkey ' + curMonkeyDict['ifFalse']
                curMonkeyDict['items'] = curMonkeyDict['items'][1:]            
                dataDict[newMonkey]['items'] += [afterBored]
                # print('       Current Worry Level is not divisible by ', divTestNum)
                # print('       Item with worry level ', afterBored, ' is thrown to monkey', curMonkeyDict['ifFalse'])

    return dataDict


def getHCF(dataDict):
    ''' This function calculates the Heighest Common Factor
        This is useful for part two.
    '''
    hcf = 1
    for monkey in dataDict:
        hcf *= int(dataDict[monkey]['divTestNum'])
    return hcf

def getInspectionCounts(roundData):
    '''
    This cunction simply fetches the number which happens to be 
    the answer for this days problems. Actually this function takes 
    the data in the form of the dictionary. Loopes over all the 
    entries and then collects the inspection counts in the list. 
    Finally it returns the product of two maximum numbers.
    '''
    scores = []
    for monkeyDict in roundData:
        scores.append(roundData[monkeyDict]['inspectCount'])
    max1, max2 = heapq.nlargest(2, scores)
    return max1*max2

def getNRounds(initialData, N, part):
    '''This function does the same thing as the getNRoundsLoop function but 
    this one uses recursion which is not so helpful for part two. So the optimized 
    version of this function is by using the for loop'''
    if N <= 0:
        return initialData
    else:
        return getNRounds(round(initialData, part), N-1, part)


def getNRoundsLoop(initialData, N, part):
    '''
    Input:  This function takes the intial data total number of rounds you wanna run,
            and the part which could be one or two. 

    Output: It keeps one getting the updated dictionary for each round. Then it eventually
            returns the last dictionary which represents the data after N number of rounds. 
    '''
    roundsdict = {}
    for i in range(1,N+1):
        if i == 1:
            roundsdict[i] = round(initialData, part)
        elif i > 1:
            roundsdict[i] = round(roundsdict[i-1], part)
    return roundsdict[N]

monkeyDataLists = getMonkeyDataInLists(filePath)


par1Data = getDataDict(monkeyDataLists)
par2Data = getDataDict(monkeyDataLists)

twentyDicts = getNRoundsLoop(par1Data, 20, 'part1')
tenthousandDicts = getNRoundsLoop(par2Data, 10000, 'part2')

print('Part one answer: ',getInspectionCounts(twentyDicts))
print('Part two answer: ',getInspectionCounts(tenthousandDicts))
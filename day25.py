'''
--- Day 25: Full of Hot Air ---
Today we have to do some base 5 conversion with a little twist.
Initially we have to convert snafu to decimal which is pretty straight
forword base 5 conversion. Then we need to sum up the input and then 
change back that decimal to SNAFU.

Another approach to solve part one could be to directly add the snafu 
numbers in snafu format.
'''

filepath = '/Users/ali/Documents/programming-with-python-fork/aoc/day25.txt'


SNAFUCodes = [line.strip() for line in open(filepath)]

def getToDecimalDict():
    return {"=": -2, 
            '-':-1,
            '0':0,
            '1':1,
            '2':2}

def getToSNAFUDict():
    return {-2:'=', 
            -1:'-',
            0:'0',
            1:'1',
            2:'2'}

def get_decimal_from_snafu(snafu):
    """
    This function simply converts that snafu to decimal 
    and then adds up all the numbers.
    """
    SNAFUDict = getToDecimalDict()
    # we start from reverse as in the base 5 
    # we start with 5^0, and then go like this
    # 5^1, 5^2, 5^3 and so on.
    snafu = snafu[::-1]
    decimal = 0
    for i, val in enumerate(snafu):
        curAdd =  (5**int(i))*SNAFUDict[val]
        decimal += curAdd
    return decimal


decimalToConvert = sum([get_decimal_from_snafu(snafu) for snafu in SNAFUCodes])

def getRemainderNumber(decimal):
    '''This function simply converts the 
    decimal to base 5 number.'''
    rem = ''
    num = decimal
    while num > 1:
        rem += str(num % 5)
        num = num // 5
    rem += str(num)
    return rem[::-1]

remainderNumber = getRemainderNumber(decimalToConvert)

def toSNAFU(remainderNumber):
    '''
    1342320332423220023
    134232033242322003
    13423203324232201
    1342320332423220
    134232033242322
    13423203324232
    1342320332423
    134232033243
    13423203325
    1342320333
    134232034
    13423204
    1342321
    134232
    13423
    1343
    135
    14
    2

    '''
    snafuDict = getToSNAFUDict()
    snafu = ''

    # we loop over until we reach only one 
    # digit.
    while len(remainderNumber) >= 1:
        # we take the last element from the number.
        curElem = int(remainderNumber[-1])
        # we check if the number is greater than 2 
        # because all the other numbers are just like 
        # normal base 5 conversion so we do now need to 
        # do anything in that case.
        if curElem > 2:
            if curElem == 3: # -2%5 = 3
                snafu += snafuDict[-2]
            elif curElem == 4: # -1%5 = 4
                snafu += snafuDict[-1]
            elif curElem == 5: # 0%5 = 5
                snafu += snafuDict[0]

            remainderNumber = str(int(remainderNumber[:-1])+1)

        elif curElem <= 2:   
            snafu += snafuDict[curElem]
            remainderNumber = remainderNumber[:-1]
    
    return snafu[::-1]

print('Part One Solution: ', toSNAFU(remainderNumber))
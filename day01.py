'''
--- Day 1: Calorie Counting ---
In this problem the input is basically the collection
of items each elve has seprated by the new line character.

In part one we need to get the sums of all the elves and the answer
is just the elve having maximum calories. 

In part two we need to get top three elves having moost calories then 
sum up those three elves calories to get the final answer.

Example Output Explanation:
The example output is like this where in each line there is the calorie count 
for the food item of a spacific elf. The items in one group (i-e groups seprated
by the new line characters.)

1000
2000
3000

4000

5000
6000

7000
8000
9000

10000

'''

filename = '/Users/ali/Documents/programming-with-python-fork/aoc/day01.txt'

def readFile(filename):
    '''
    Input:  Directory of the file.
    Output: A list which contains the calorie count of 
            each elve in the order they appear in the 
            file. 
    '''
    listOfSums = []
    sum = 0 
    with open(filename) as file:
        for line in file:
            # Newline case. As long as we hit
            # newline we know new elf data 
            # if gonna start from the next 
            # line so we append and then 
            # reset the sum.
            if line == '\n':
                listOfSums.append(sum)
                sum = 0
            # Inside Case: When you are in 
            # the middle of the current elf data
            else:
                sum += int(line.strip())

    return listOfSums


sums = readFile(filename)

print('Part One: ', max(sums))
print('Part Two: ', sum(sums[:3]))
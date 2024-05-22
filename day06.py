'''
--- Day 6: Tuning Trouble ---
This is basically pattern matching problem.
Input is very simple and it is just one line.
You keep on searching for the the kmers in the line. 
As soon as you get the kmer which has no duplicate characters
you return the ending index of that kmer.

Part 1: kmer size is 4
Pert 2: kmer size is 14

Explanation of Sample Input:
As you can see in the input below you just have one lone line.

mjqjpqmgbljsphdztnvjfqwrcgsmlb

'''


filename = '/Users/ali/Documents/programming-with-python-fork/aoc/day06.txt'
datastream = [line.strip() for line in open(filename)][0]

def findLastIndex(datastream, k):
    """
    Input:  This function takes two parameters.
            datastream: which is simply long input string.
            k: length of the kmer that you are looking for.

    Output: It returns the indesx where the first unique kmer ends.
    """
    for i in range(len(datastream)-k):
        kmer = datastream[i:i+k]
        ifUnique = len(set(kmer)) == k
        if ifUnique:
            return i+k

print('part1: ', findLastIndex(datastream, 4))
print('part2: ', findLastIndex(datastream, 14))
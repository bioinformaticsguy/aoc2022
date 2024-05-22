'''
--- Day 7: No Space Left On Device ---
This is basically parsing the directories. Which can 
be nested as well. 

Part 1: You need to find out the total size of the root
        directory or in other words you need to find out 
        sum of the size of all the directories.

Part 2: In part 2 you need to find out the directory that 
        you can delete and that directory should be 
        able to free up enough space. That is needed to 
        run the system properly.

Explanation of the sample Input:

As you can see below the sample input is just like we are using the linux terminal.
In each line you either have the command which starts with the $ sign or you will have the
name of the directory which starts with dir or you will have the file which srtarts with 
a number as the size of the file is mentioned first then the name of the line which is seprate
by the space character. 


$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k



'''


filePath = '/Users/ali/Documents/programming-with-python-fork/aoc/day07.txt'
inputs = [line.strip() for line in open(filePath)]

def getDirectories(inputs):
    '''
    Input:  It takes the input as list of strings.
    Output: Returns the dictionary with the name of
            the directory as the key the size of that 
            directory as the value.
    '''

    # initializing the dictionary with the root directory
    # the sise of the root directory is set to zero.
    # Initializing the current directory as the root 
    # directory as well because the first directory in the
    # input is also root directory.

    dataDict = {'/~': 0}
    curDir = '/~'

    ## Start by looping over the input.
    for input in inputs:
        # When input is a command
        if input.startswith('$'):
            # When input is a change directory but not list directory
            if input.startswith('$ cd') and not input.endswith('ls'):
                # If changing the directory to root we will 
                # update our current directory to root as well.
                if input.startswith('$ cd /'):
                    curDir = '/~'
                # If we are going back in the directory then 
                # we will update our current directory one step back
                elif input.endswith('..'):
                    # but before that we will check if we are outside the
                    # root directory already.
                    if curDir.count('/') > 1:
                        curDir = curDir[0:curDir.rfind('/')]
                # Incase of new directory we update to a new directory
                else:
                    curDir = curDir + '/' + input[5:]
                    dataDict[curDir] = 0

        # When input is not a command then it is the file or a folder
        # with the help of if statement we rule out the folder option. 
        elif not input.startswith("dir"):
            # Get size of the file             
            bytesSize = int(input.split()[0])
            slashLevel = curDir.count('/')
            tempDir = curDir
            # We update all the previuous directories. 
            # we go back one directory at a time
            # update the size of that directory.
            for i in range(slashLevel):
                dataDict[tempDir] += bytesSize
                tempDir = tempDir[:tempDir.rfind('/')]
    return dataDict

def getPartOneAnswer(folders):
    """
    Input:  It takes the folders dictionary
    Output: It returns the sum of folder
            sizes which are less then or 
            equal to 100000.     
    """
    answer = 0
    for folder in folders:
        if folders[folder] <= 100000:
            answer += folders[folder]
    return answer

folders = getDirectories(inputs)

def getPartTwoAnswer(folders):
    ''' 
    Input: Dictionary of folders containg the names and sizes.
    Output: it returns the smallest directory which is bigger than
    the considerable size.
    '''
    possibleDirectories = []
    usedSpace = folders['/~']
    unUsedSpace = 70000000 - usedSpace
    consider = 30000000 - unUsedSpace
    for folder in folders:
        if folders[folder] >= consider:
            possibleDirectories.append(folders[folder])
    return min(possibleDirectories)

print('Part One Answer: ', str(getPartOneAnswer(folders)))
print('Part Two Answer: ', str(getPartTwoAnswer(folders)))

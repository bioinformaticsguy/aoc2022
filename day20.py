## Reference: https://www.youtube.com/watch?v=Tv9tPOZ0x9g

'''
--- Day 20: Grove Positioning System ---
Today we will have to re arrange a huge list acording to certain rules. 
The list is a circular list so if you have an element at the front and you 
move it one point back it will not just go one point back it will go past 
that point because it is circular. The numbers should be moved in the order 
that they appear. This is implemented by using Doubly Linked List Data Structure.
Part2: We have to do 10 rounds and multiply each value by a huge number.
'''

filePath = '/Users/ali/Documents/programming-with-python-fork/aoc/day20.txt'

class DoublyPoint:
    '''This is a simple point class 
    that has the value and the left and the 
    right pointer.'''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def addLeftRight(listofPoints):
    '''
    In this we just update the left and the right 
    pointer of each value. So we iterate over the list of the points.
    For each kth point the point on the left is gonna be k-1 and the point
    on the right is gonna be k+1. So we set the value of the left and right 
    to the corresponding pointer. Then eventually we return the list of points.
    '''
    for i in range(len(listofPoints)):
        listofPoints[i].right = listofPoints[(i + 1) % len(listofPoints)]
        listofPoints[i].left = listofPoints[(i - 1) % len(listofPoints)]
    return listofPoints


def solve(doublyPoints, part=1):
    ## By default this function solves part 1 
    ## and runs for just one round. But if the 
    ## optional part parameter is given then it 
    ## will run 10 times.
    if part == 2:
        rounds = 10
    elif part == 1:
        rounds = 1

    ## This is the value by which we take the modulo
    ## there is minus one because if we move upto the 
    ## length of the list we would move but if we move
    ## one less that the length then it would not move us.
    ## so we can take modulo and our answer will not be changed.
    m = len(doublyPoints) - 1

    for _ in range(rounds):
        for point in doublyPoints:
            # this is the zero position that 
            # we are gonna use to exteract the 
            # answer. According to the problem statement
            # 0 element do not move ever because it is zero
            # also it is important to note down this point because
            # in order to get the answer you need to see the element 
            # which is after 1000, 2000 and 3000 posiitons after 0 point
            # That is why we store this point in a seprate variable. Now if 
            # you will think that we can access the 0 randomly from the list then 
            # you need to consider that our list contains objects which has limited
            # functionality developed by us so it is not possible to find the element
            # directly.
            if point.value == 0:
                zeroData = point
                continue

            # we create the temp point to do the swaping.
            tempPoint = point
            # We check if the point value is greater than 0.
            if point.value > 0:
                ## if we reach the same spot we just continue.
                ## we take the modulo of the point value with 
                ## m (total number of points - 1). We do this modulo so that
                # we just get the remainder . Let me explain this in a bit more detail
                # lets assume you have a list of five numbers and this is a circular list
                # if you will move it upto the length of the list then you will move it 
                # one position ahead. If you will move it one position less then the length 
                #  of the list then you will end up again in the same poition. That 
                # is why we take modulo with len-1. Lets say that our current number is 18 
                # and our list is of just 5 elememnts so we will take 9%4 and get 1. So will
                # start moving the number you will move it 4 times and then you will end up at
                # the same position then you will move 4 times again and you will be at same 
                # position again now you have moved 8 positions one is still left so then you 
                # will move just one position and you will be at the correct position. By taking
                # the modulo we are actually removing all the extra revolutions we will just move
                # 9 one position and we will be good to go...... 

                for _ in range(point.value % m):
                    tempPoint = tempPoint.right

                # this is when we reach the same point or when we get 0 after doing the 
                # modulo then we know that we do not need to swap that is why we simply 
                # continue. 
                if point == tempPoint:
                    continue

                # If the points are not same we swap and we have to follow a few steps 
                # while swaping.

                # The following two lines just remove the current point
                # basically we are pointing it to over to the current point.
                point.right.left = point.left
                point.left.right = point.right

                # Now we need to insert the removed point to its new neighbour
                # which is called as temp point. So in order to do that we will
                # insert to the right of neighbour so we will join its left 
                # with the removed point.  
                tempPoint.right.left = point
                # now we also have to join the removed point to the neighbour we do that 
                # below.
                point.right = tempPoint.right

                # Then we have to do the same thing on the other side.
                tempPoint.right = point
                point.left = tempPoint
            else: ## When point value is less then 0. Then we will move towords 
                ## left.

                ## if we reach the same spot we just continue.
                for _ in range(-point.value % m):
                    tempPoint = tempPoint.left
                if point == tempPoint:
                    continue
                # otherwise we swap and this time we will remove the point to 
                # the left.
                point.left.right = point.right
                point.right.left = point.left
                tempPoint.left.right = point
                point.left = tempPoint.left
                tempPoint.left = point
                point.right = tempPoint
    return zeroData

def getanswer(zeroData):
    '''This function loops over the datapoints
    1000, 2000 and 3000 times after the 0th 
    value and then sums up.'''
    count = 0
    for _ in range(3):
        for _ in range(1000):
            zeroData = zeroData.right
        count += zeroData.value
    return count


listofPoints = [DoublyPoint(int(x)) for x in open(filePath)]
doublyPoints = addLeftRight(listofPoints)
zeroData = solve(doublyPoints,1)
print('Part One Solution: ', getanswer(zeroData))

## We multiply it with the number given in the problem statement.
listofPoints = [DoublyPoint(int(x) * 811589153) for x in open(filePath)]
doublyPoints = addLeftRight(listofPoints)
# part two ensures that we run this problem 10 times.
zeroData = solve(doublyPoints,2)
print('Part One Solution: ', getanswer(zeroData))
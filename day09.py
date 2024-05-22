import numpy as np

"""
--- Day 9: Rope Bridge ---

In this problem we have to follow the knots. In the problem we are given
head and tail. But we can consider both as same things. Then you need 
to just check the difference of positions and then update the following 
point. This works elegently when we consider one point in hand as the 
head and the other point as the tail. 

Like in part two when you have multiple tails you can start with the first
knot which is known as head we will move it and then update the tail postion
Once we have updated the tail position. Our tail will become the new head 
and the new tail will be the one previous to the head.
"""



filePath = '/Users/ali/Documents/programming-with-python-fork/aoc/day09.txt'
input = [(line.strip().split(' ')[0], int(line.strip().split(' ')[1]))  for line in open(filePath)]


# from math import sqrt
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x, self.y = float(x), float(y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def x_y_greater_than1(self, other):
        """
        Input: Takes two points. x, x' and y, y'.
        output: Returns True if the differneces of x or y is greater then 1.
        """
        return abs(self.x - other.x) > 1 or abs(self.y - other.y) > 1
    
    def move_up(self):
        return Point(self.x, self.y+1)

    def move_down(self):
        return Point(self.x, self.y-1)

    def move_right(self):
        return Point(self.x+1, self.y)

    def move_left(self):
        return Point(self.x-1, self.y)

    def get_new_position(self, other):
        """
        np.sign returns -1 if x < 0, 0 if x==0, 1 if x > 0. 
        So we will check the difference of the positions and 
        if the difference is negative we will subtract -1 from 
        the index and if the difference is 0 then we do not make any 
        change. If the difference is positive we will add +1 to that
        index. We are not adding or subtracting more than 1 because
        we update the position of the tail in each iteration. That 
        is why tail can never be more far away so that it is needed 
        to move more than one position.
        
        """
        newX = other.x + np.sign(self.x - other.x)
        newY = other.y + np.sign(self.y - other.y)
        return Point(newX, newY)



def get_visited_positions(input, length):
    knot_positions = []
    visited_positions = set()

    # this loop will add points 0, 0 to the list
    # which will be equal to length. 
    for i in range(length):
        knot_positions.append(Point(0,0))

    # we add the last knot to the visited positions as we consider that 
    # as head.
    # print(knot_positions[0])
    visited_positions.add((knot_positions[-1].x, knot_positions[-1].y))
    # print(visited_positions)

    for instruction in input:
        move_direction = instruction[0]
        move_length = instruction[1]
        # print(move_direction, move_length)
        for _ in range(move_length):
            # print(move_index)
            if move_direction == 'U':
                knot_positions[0] = knot_positions[0].move_up()
            elif move_direction == 'D':
                knot_positions[0] = knot_positions[0].move_down()                
            elif move_direction == 'L':
                knot_positions[0] = knot_positions[0].move_left()                
            elif move_direction == 'R':
                knot_positions[0] = knot_positions[0].move_right()
            
            for k in range(length-1):
                if knot_positions[k].x_y_greater_than1(knot_positions[k+1]):
                    knot_positions[k+1] = knot_positions[k].get_new_position(knot_positions[k+1])
                    # print(knot_positions[k+1], knot_positions[k])
                    
                    visited_positions.add((knot_positions[-1].x, knot_positions[-1].y))

    # print(knot_positions)
    return (len(visited_positions))


print('Part 1 Soultion: ', get_visited_positions(input, 2))
print('Part 2 Soultion: ', get_visited_positions(input, 10))

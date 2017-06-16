"""
Solar Doomsday
==============

Who would've guessed? Doomsday devices take a LOT of power. Commander Lambda wants to supplement the LAMBCHOP's quantum antimatter reactor core with solar arrays, and she's tasked you with setting up the solar panels.

Due to the nature of the space station's outer paneling, all of its solar panels must be squares. Fortunately, you have one very large and flat area of solar material, a pair of industrial-strength scissors, and enough MegaCorp Solar Tape(TM) to piece together any excess panel material into more squares. For example, if you had a total area of 12 square yards of solar material, you would be able to make one 3x3 square panel (with a total area of 9). That would leave 3 square yards, so you can turn those into three 1x1 square solar panels.

Write a function answer(area) that takes as its input a single unit of measure representing the total area of solar panels you have (between 1 and 1000000 inclusive) and returns a list of the areas of the largest squares you could make out of those panels, starting with the largest squares first. So, following the example above, answer(12) would return [9, 1, 1, 1].

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) area = 12
Output:
    (int list) [9, 1, 1, 1]

Inputs:
    (int) area = 15324
Output:
    (int list) [15129, 169, 25, 1]


Time to solve: 48 hours.
"""

# But, if we are going to use this function for many-many different areas in a row (imagine that we are not sure how many space stations we need to cover with solar panels) better solution would be to prepare list of all squares for numbers 1..1000 (because 1000 is a square root of 1000000) and use binary search in that array to get proper numbers faster.
# As soon as lower bound of area is 1, I do not need to cover case with area equal to 0
def answer(area):
    res = []
    while (area > 0):
        biggest_square_side = int(area ** 0.5)
        biggest_square = biggest_square_side ** 2
        area -= biggest_square
        res.append(biggest_square)
    return res


T = int(input())

for t in range(T):
    s = int(input())
    answer_in = [int(x) for x in input().split()]
    answer_my = answer(s)
    print("area: {}".format(s))
    print("answer_in: {}".format(answer_in))
    print("answer_my: {}".format(answer_my))
    print(len(answer_in) == len(answer_my) and all(map(lambda v: v in answer_in, answer_my)))






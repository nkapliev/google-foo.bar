"""
Gearing Up for Destruction
==========================

As Commander Lambda's personal assistant, you've been assigned the task of configuring the LAMBCHOP doomsday device's axial orientation gears. It should be pretty simple - just add gears to create the appropriate rotation ratio. But the problem is, due to the layout of the LAMBCHOP and the complicated system of beams and pipes supporting it, the pegs that will support the gears are fixed in place.

The LAMBCHOP's engineers have given you lists identifying the placement of groups of pegs along various support beams. You need to place a gear on each peg (otherwise the gears will collide with unoccupied pegs). The engineers have plenty of gears in all different sizes stocked up, so you can choose gears of any size, from a radius of 1 on up. Your goal is to build a system where the last gear rotates at twice the rate (in revolutions per minute, or rpm) of the first gear, no matter the direction. Each gear (except the last) touches and turns the gear on the next peg to the right.

Given a list of distinct positive integers named pegs representing the location of each peg along the support beam, write a function answer(pegs) which, if there is a solution, returns a list of two positive integers a and b representing the numerator and denominator of the first gear's radius in its simplest form in order to achieve the goal above, such that radius = a/b. The ratio a/b should be greater than or equal to 1. Not all support configurations will necessarily be capable of creating the proper rotation ratio, so if the task is impossible, the function answer(pegs) should return the list [-1, -1].

For example, if the pegs are placed at [4, 30, 50], then the first gear could have a radius of 12, the second gear could have a radius of 14, and the last one a radius of 6. Thus, the last gear would rotate twice as fast as the first one. In this case, pegs would be [4, 30, 50] and answer(pegs) should return [12, 1].

The list pegs will be given sorted in ascending order and will contain at least 2 and no more than 20 distinct positive integers, all between 1 and 10000 inclusive.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) pegs = [4, 30, 50]
Output:
    (int list) [12, 1]

Inputs:
    (int list) pegs = [4, 17, 50]
Output:
    (int list) [-1, -1]


Time to solve: 72 hours.
"""


from fractions import Fraction

def answer (pegs):
    last_gear_radius = 0
    for i in range(len(pegs) - 1):
        dist = pegs[i + 1] - pegs[i]
        last_gear_radius += ((-1) ** i) * dist
    first_gear_radius = last_gear_radius * 2
    divisor = 1

    if len(pegs) % 2 == 0:
        if first_gear_radius % 3 == 0:
            first_gear_radius /= 3
        else:
            divisor = 3

    is_all_gear_fit = True

    prev_gear_radius = Fraction(first_gear_radius) / Fraction(divisor)
    for i in range(len(pegs) - 1):
        dist = pegs[i + 1] - pegs[i]
        next_gear_radius = Fraction(dist) - prev_gear_radius
        if next_gear_radius < 1:
            is_all_gear_fit = False
            break
        prev_gear_radius = next_gear_radius

    return [ first_gear_radius, divisor ] if is_all_gear_fit else [ -1, -1 ]


T = int(raw_input())

for t in range(T):
    pegs = list(map(int, raw_input().split()))
    print("pegs: {}".format(pegs))
    answer_in = list(map(int, raw_input().split()))
    answer_my = answer(pegs)
    print("answer_in: {}".format(answer_in))
    print("answer_my: {}".format(answer_my))
    print(answer_in == answer_my)

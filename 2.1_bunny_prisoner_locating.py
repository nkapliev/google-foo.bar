"""
Bunny Prisoner Locating
=======================

Keeping track of Commander Lambda's many bunny prisoners is starting to get tricky. You've been tasked with writing a program to match bunny prisoner IDs to cell locations.

The LAMBCHOP doomsday device takes up much of the interior of Commander Lambda's space station, and as a result the prison blocks have an unusual layout. They are stacked in a triangular shape, and the bunny prisoners are given numerical IDs starting from the corner, as follows:

| 7
| 4 8
| 2 5 9
| 1 3 6 10

Each cell can be represented as points (x, y), with x being the distance from the vertical wall, and y being the height from the ground.

For example, the bunny prisoner at (1, 1) has ID 1, the bunny prisoner at (3, 2) has ID 9, and the bunny prisoner at (2,3) has ID 8. This pattern of numbering continues indefinitely (Commander Lambda has been taking a LOT of prisoners).

Write a function answer(x, y) which returns the prisoner ID of the bunny at location (x, y). Each value of x and y will be at least 1 and no greater than 100,000. Since the prisoner ID can be very large, return your answer as a string representation of the number.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) x = 3
    (int) y = 2
Output:
    (string) "9"

Inputs:
    (int) x = 5
    (int) y = 10
Output:
    (string) "96"


Time to solve: 72 hours.
"""


def answer(x, y):
    base = sum(xx + 1 for xx in range(x))
    tail = sum(yy for yy in range(x, x + y - 1))
    return base + tail


T = int(raw_input())

for t in range(T):
    x, y = map(int, raw_input().split())
    answer_in = int(raw_input())
    answer_my = answer(x, y)
    print("x, y: {}, {}".format(x, y))
    print("answer_in: {}".format(answer_in))
    print("answer_my: {}".format(answer_my))
    print(answer_in == answer_my)


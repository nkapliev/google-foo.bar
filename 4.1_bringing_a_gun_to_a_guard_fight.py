"""
Bringing a Gun to a Guard Fight
===============================

Uh-oh - you've been cornered by one of Commander Lambdas elite guards! Fortunately, you grabbed a beam weapon from an abandoned guardpost while you were running through the station, so you have a chance to fight your way out. But the beam weapon is potentially dangerous to you as well as to the elite guard: its beams reflect off walls, meaning youll have to be very careful where you shoot to avoid bouncing a shot toward yourself!

Luckily, the beams can only travel a certain maximum distance before becoming too weak to cause damage. You also know that if a beam hits a corner, it will bounce back in exactly the same direction. And of course, if the beam hits either you or the guard, it will stop immediately (albeit painfully).

Write a function answer(dimensions, your_position, guard_position, distance) that gives an array of 2 integers of the width and height of the room, an array of 2 integers of your x and y coordinates in the room, an array of 2 integers of the guard's x and y coordinates in the room, and returns an integer of the number of distinct directions that you can fire to hit the elite guard, given the maximum distance that the beam can travel.

The room has integer dimensions [1 < x_dim <= 1000, 1 < y_dim <= 1000]. You and the elite guard are both positioned on the integer lattice at different distinct positions (x, y) inside the room such that [0 < x < x_dim, 0 < y < y_dim]. Finally, the maximum distance that the beam can travel before becoming harmless will be given as an integer 1 < distance <= 10000.

For example, if you and the elite guard were positioned in a room with dimensions [3, 2], you_position [1, 1], guard_position [2, 1], and a maximum shot distance of 4, you could shoot in seven different directions to hit the elite guard (given as vector bearings from your location): [1, 0], [1, 2], [1, -2], [3, 2], [3, -2], [-3, 2], and [-3, -2]. As specific examples, the shot at bearing [1, 0] is the straight line horizontal shot of distance 1, the shot at bearing [-3, -2] bounces off the left wall and then the bottom wall before hitting the elite guard with a total shot distance of sqrt(13), and the shot at bearing [1, 2] bounces off just the top wall before hitting the elite guard with a total shot distance of sqrt(5).

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) dimensions = [3, 2]
    (int list) captain_position = [1, 1]
    (int list) badguy_position = [2, 1]
    (int) distance = 4
Output:
    (int) 7

Inputs:
    (int list) dimensions = [300, 275]
    (int list) captain_position = [150, 150]
    (int list) badguy_position = [185, 100]
    (int) distance = 500
Output:
    (int) 9


Time to solve: 360 hours.
"""


import math


def gcd(a, b):
    a, b = abs(a), abs(b)
    while b > 0:
        a, b = b, a % b
    return a


def get_mirror_coord(dimension, room_number, original_coord):
    if room_number == 0:
        mirror_coord = 0
    elif room_number > 0:
        mirror_coord = dimension * (room_number - 1) + ((dimension - original_coord) * 2 if room_number % 2 == 1 else dimension)
    else:
        mirror_coord = dimension * (room_number + 1) - (original_coord * 2 if room_number % 2 == 1 else dimension)
    return mirror_coord


def get_mirror_vector(dimensions, new_col, new_row, original_position):
    return get_mirror_coord(dimensions[0], new_col, original_position[0]), \
           get_mirror_coord(dimensions[1], new_row, original_position[1])


def get_canonical_vector(mirror_vector):
    if mirror_vector[0] == 0 and mirror_vector[1] == 0:
        return 0, 0
    elif mirror_vector[0] == 0:
        return 0, 1 if mirror_vector[1] > 0 else -1
    elif mirror_vector[1] == 0:
        return 1 if mirror_vector[0] > 0 else -1, 0
    else:
        vector_gcd = gcd(*mirror_vector)
        return mirror_vector[0] / vector_gcd, mirror_vector[1] / vector_gcd


def get_distance(vector):
    return math.hypot(*vector)  # (vector[0] ** 2 + vector[1] ** 2) ** 0.5


def get_vector_value(vector):
    return max(abs(vector[0]), abs(vector[1]))  # get_distance(vector)


def answer(dimensions, captain_position, badguy_position, distance):
    distance_to_badguy = get_distance([captain_position[0] - badguy_position[0], captain_position[1] - badguy_position[1]])
    if distance < distance_to_badguy:
        return 0
    elif distance == distance_to_badguy:
        return 1

    rows = distance / dimensions[1] + 3
    cols = distance / dimensions[0] + 3
    captain_to_badguy_diff = [badguy_position[0] - captain_position[0], badguy_position[1] - captain_position[1]]
    shoot_vectors = dict()

    for row in xrange(-rows, rows):
        for col in xrange(-cols, cols):
            captain_mirror_vector = get_mirror_vector(dimensions, col, row, captain_position)

            if get_distance(captain_mirror_vector) <= distance:
                captain_canonical_vector = get_canonical_vector(captain_mirror_vector)
                captain_mirror_vector_value = get_vector_value(captain_mirror_vector)
                if captain_canonical_vector in shoot_vectors:
                    if shoot_vectors[captain_canonical_vector][1] > captain_mirror_vector_value:
                        shoot_vectors[captain_canonical_vector] = False, captain_mirror_vector_value
                else:
                    shoot_vectors[captain_canonical_vector] = False, captain_mirror_vector_value

            badguy_mirror_vector = get_mirror_vector(dimensions, col, row, badguy_position)
            badguy_mirror_relative_vector = badguy_mirror_vector[0] + captain_to_badguy_diff[0], \
                                            badguy_mirror_vector[1] + captain_to_badguy_diff[1]

            if get_distance(badguy_mirror_relative_vector) <= distance:
                badguy_canonical_vector = get_canonical_vector(badguy_mirror_relative_vector)
                badguy_mirror_relative_vector_value = get_vector_value(badguy_mirror_relative_vector)
                if badguy_canonical_vector in shoot_vectors:
                    if shoot_vectors[badguy_canonical_vector][1] > badguy_mirror_relative_vector_value:
                        shoot_vectors[badguy_canonical_vector] = True, badguy_mirror_relative_vector_value
                else:
                    shoot_vectors[badguy_canonical_vector] = True, badguy_mirror_relative_vector_value

    #print("shoot_vectors: {}".format(shoot_vectors))

    counter = 0
    for key, value in shoot_vectors.iteritems():
        if value[0]:
            counter += 1

    return counter


T = int(raw_input())

for t in range(T):
    dim = [int(x) for x in raw_input().split()]
    cap = [int(x) for x in raw_input().split()]
    bad = [int(x) for x in raw_input().split()]
    dist = int(raw_input())
    print("dim, cap, bad, dist: {}, {}, {}, {}".format(dim, cap, bad, dist))
    answer_in = int(raw_input())
    answer_my = answer(dim, cap, bad, dist)
    print("answer_in: {}".format(answer_in))
    print("answer_my: {}".format(answer_my))
    print(answer_in == answer_my)

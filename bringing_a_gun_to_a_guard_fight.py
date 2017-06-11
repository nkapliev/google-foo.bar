def gcd(a,b):
    a, b = abs(a), abs(b)
    while b > 0:
        a, b = b, a % b
    return a

def get_mirror_vector(dimensions, new_col, new_row, original_position):
    def get_mirror_coord(dimension, room_number, original_coord):
        if room_number == 0:
            return 0
        else:
            mirror_coord = dimension * (abs(room_number) - 1)
            if room_number > 0:
                mirror_coord += (dimension - original_coord) * 2 if room_number % 2 == 1 else dimension
            else:
                mirror_coord += original_coord * 2 if room_number % 2 == 1 else dimension
                mirror_coord *= -1
        return mirror_coord

    return [
        get_mirror_coord(dimensions[0], new_col, original_position[0]),
        get_mirror_coord(dimensions[1], new_row, original_position[1])
    ]

def get_canonical_key(col, row, mirror_vector):
    if mirror_vector[0] == 0 and mirror_vector[1] == 0:
        canonical_vector = [0, 0]
    elif mirror_vector[0] == 0:
        canonical_vector = [0, 1 if mirror_vector[1] > 0 else -1]
    elif mirror_vector[1] == 0:
        canonical_vector = [1 if mirror_vector[0] > 0 else -1, 0]
    else:
        #print("mirror_vector, gcd: {}, {}".format(mirror_vector, gcd(*mirror_vector)))
        vector_gcd = gcd(*mirror_vector)
        canonical_vector = [mirror_vector[0] / vector_gcd, mirror_vector[1] / vector_gcd]
    return str(canonical_vector)

def answer(dimensions, captain_position, badguy_position, distance):
    distance_to_badguy = ((captain_position[0] - badguy_position[0]) ** 2 + (captain_position[1] - badguy_position[1]) ** 2) ** 0.5
    if distance < distance_to_badguy: 
        return 0
    elif distance == distance_to_badguy:
        return 1

    rows = distance / dimensions[1] + 1
    cols = distance / dimensions[0] + 1
    captain_to_badguy_diff = [badguy_position[0] - captain_position[0], badguy_position[1] - captain_position[1]]
    badguy_vectors = dict()
    captain_vectors = dict()
    for row in xrange(-rows, rows):
        if row % 100 == 0:
            print("row: {}".format(row))
        for col in xrange(-cols, cols):
            #print("col, row: {}, {}".format(col, row))

            captain_mirror_vector = get_mirror_vector(dimensions, col, row, captain_position)
            canonical_captain_key = get_canonical_key(col, row, captain_mirror_vector)
            #print("captain_mirror_vector, key: {}, {}".format(captain_mirror_vector, canonical_captain_key))

            badguy_mirror_vector = get_mirror_vector(dimensions, col, row, badguy_position)
            badguy_mirror_relative_vector = [badguy_mirror_vector[0] + captain_to_badguy_diff[0], badguy_mirror_vector[1] + captain_to_badguy_diff[1]]
            canonical_badguy_key = get_canonical_key(col, row, badguy_mirror_relative_vector)
            #print("badguy_mirror_vector, key: {}, {}".format(badguy_mirror_relative_vector, canonical_badguy_key))

            if canonical_captain_key in captain_vectors:
                if abs(captain_vectors[canonical_captain_key][0]) > abs(captain_mirror_vector[0]) or abs(captain_vectors[canonical_captain_key][1]) > abs(captain_mirror_vector[1]):
                    captain_vectors[canonical_captain_key] = captain_mirror_vector
            else:
                captain_vectors[canonical_captain_key] = captain_mirror_vector
            #if canonical_badguy_key in captain_vectors:
            #    if abs(captain_vectors[canonical_badguy_key][0]) > abs(badguy_mirror_relative_vector[0]) or abs(captain_vectors[canonical_badguy_key][1]) > abs(badguy_mirror_relative_vector[1]):
            #        pass # or `del captain_vectors[canonical_badguy_key]`
            if canonical_badguy_key in badguy_vectors:
                if abs(badguy_vectors[canonical_badguy_key][0]) > abs(badguy_mirror_relative_vector[0]) or abs(badguy_vectors[canonical_badguy_key][1]) > abs(badguy_mirror_relative_vector[1]):
                    badguy_vectors[canonical_badguy_key] = badguy_mirror_relative_vector
            else:
                badguy_vectors[canonical_badguy_key] = badguy_mirror_relative_vector

            if canonical_captain_key in badguy_vectors:
                if abs(badguy_vectors[canonical_captain_key][0]) > abs(captain_mirror_vector[0]) or abs(badguy_vectors[canonical_captain_key][1]) > abs(captain_mirror_vector[1]):
                    del badguy_vectors[canonical_captain_key]

    #print("captain_vectors: {}".format(captain_vectors))
    #print("badguy_vectors: {}".format(badguy_vectors))

    counter = 0
    for key, succ_shoted_badguy in badguy_vectors.iteritems():
        succ_shot_distance = (succ_shoted_badguy[0] ** 2 + succ_shoted_badguy[1] ** 2) ** 0.5
        #print("succ_shoted_badguy, succ_shot_distance: {}, {}".format(succ_shoted_badguy, succ_shot_distance))
        if succ_shot_distance <= distance:
            counter += 1

    return counter


T = int(raw_input())
#T = 0

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

#dim = [4, 3]
#rooms_limit = 3
#orig = [1,1]
#for row in range(-rooms_limit, rooms_limit):
#    for col in range(-rooms_limit, rooms_limit):
#        print("room, vector: {}, {}".format([col, row], get_mirror_vector(dim, col, row, orig)))



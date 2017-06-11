
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






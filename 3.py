def answer (pegs):
    if len(pegs) == 2:
        numerator = (pegs[1] - pegs[0]) * 2
        denominator = 1

        if numerator % 3 == 0:
            numerator /= 3
        else:
            denominator = 3
    else:
        dist = pegs[2] - pegs[1]
        prev_dist = pegs[1] - pegs[0]
        prev_prev_dist = 0
        if dist < 2 or prev_dist < 2:
            return [-1, -1]
        last_peg_radius = prev_dist - dist
        for i in range(2, len(pegs) - 1):
            prev_prev_dist = prev_dist
            prev_dist = dist
            dist = pegs[i + 1] - pegs[i]
            last_peg_radius += ((-1) ** i) * dist
            if dist < 2 or (prev_dist > dist + prev_prev_dist - 2):
                return [-1, -1]

            print(dist, last_peg_radius)

        numerator = last_peg_radius * 2
        denominator = 1

        if len(pegs) % 2 == 0:
            if numerator % 3 == 0:
                numerator /= 3
            else:
                denominator = 3

    print("num, denom: {}, {}".format(numerator, denominator))

    if (numerator < 1) or (numerator < denominator):
        return [-1, -1]
    else:
        return [numerator, denominator]


T = int(raw_input())

for t in range(T):
    pegs = list(map(int, raw_input().split()))
    print("pegs: {}".format(pegs))
    answer_in = list(map(int, raw_input().split()))
    answer_my = answer(pegs)
    print("answer_in: {}".format(answer_in))
    print("answer_my: {}".format(answer_my))
    print(answer_in == answer_my)

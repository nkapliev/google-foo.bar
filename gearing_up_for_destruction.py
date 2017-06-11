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

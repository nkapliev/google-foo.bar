# https://math.stackexchange.com/questions/2052179/how-to-find-sum-i-1n-left-lfloor-i-sqrt2-right-rfloor-a001951-a-beatty-s

max_n = 10 ** 100
seed = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727
# seed = math.floor((2 ** 0.5 - 1) * max_n)


def sum_to_x(x):
    return x * (x + 1) / 2


def kappa(n):
    if n <= 1:
        return n

    next_n = (n * seed) // max_n
    return next_n * n + sum_to_x(n) - sum_to_x(next_n) - kappa(next_n)


def answer(str_n):
    return str(kappa(long(str_n)))


T = int(raw_input())

for t in range(T):
    str_n = raw_input()
    print("str_n: {}".format(str_n))
    answer_in = raw_input()
    answer_my = answer(str_n)
    print("answer_in: {}".format(answer_in))
    print("answer_my: {}".format(answer_my))
    print(answer_in == answer_my)

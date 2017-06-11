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


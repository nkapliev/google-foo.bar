def answer (M, F):
    def helper (ma, mi, counter):
        print(ma, mi)
        if mi == 1:
            return counter + ma - 1
        elif ma == 1 and mi == 1:
            return counter
        elif ma == mi or ma % mi == 0:
            return 'impossible'
        else:
            div = ma / mi
            print("div, counter: {}, {}".format(div, counter))
            ma -= div * mi
            counter += div
            return helper(mi, ma, counter)

    M, F = int(M), int(F)
    return helper(max(M, F), min(M, F), 0)


T = int(raw_input())

for t in range(T):
    M, F = raw_input().split()
    print("M, F: {}, {}".format(M, F))
    answer_in = raw_input()
    answer_my = str(answer(M, F))
    print("answer_in: {}".format(answer_in))
    print("answer_my: {}".format(answer_my))
    print(answer_in == answer_my)


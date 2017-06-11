def answer(n):
    rest = 0
    n = bin(int(n))[2:]
    counter = 0
    print(n)
    for i in xrange(len(n) - 1, 0, -1):
        if n[i] == '0' and rest == 0:
            print('case 1')
            counter += 1
        elif n[i] == '0' and rest == 1:
            print('case 2')
            counter += 2
            if i == 1 or n[i - 1] == '0':
                rest = 0
        elif n[i] == '1' and rest == 0:
            print('case 3')
            counter += 2
            if i > 1 and n[i - 1] == '1':
                rest = 1
        else:
            print('case 4')
            counter += 1
    return counter + rest

T = int(raw_input())

for t in range(T):
    n = raw_input()
    print("n: {}".format(n))
    answer_in = int(raw_input())
    answer_my = answer(n)
    print("answer_in: {}".format(answer_in))
    print("answer_my: {}".format(answer_my))
    print(answer_in == answer_my)



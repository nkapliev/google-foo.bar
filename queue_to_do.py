def answer(start, length):
    # @return s ^ (s+1) ^ (s+2) ^ ... ^ (f-1) ^ f
    def range_xor(s, f):
        def helper(x):
            res = [x, 1, x + 1, 0]
            return res[x % 4]
        return helper(f) ^ helper(s - 1)
    res = 0
    for row in range(length):
        col_start = start + length * row
        col_end = col_start + length - row - 1
        print("col_start, col_end: {}, {}".format(col_start, col_end))
        res ^= range_xor(col_start, col_end)

    return res

T = int(raw_input())

for t in range(T):
    s, l = [int(x) for x in raw_input().split()]
    print("start, length: {}, {}".format(s, l))
    answer_in = int(raw_input())
    answer_my = answer(s, l)
    print("answer_in: {}".format(answer_in))
    print("answer_my: {}".format(answer_my))
    print(answer_in == answer_my) 


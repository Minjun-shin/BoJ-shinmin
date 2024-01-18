# Try 1
board = [[2, 1, 3, 1, 1, 5]]

one_block = [
    [46, 46, 43, 45, 45, 45, 43],
    [46, 47, 32, 32, 32, 47, 124],
    [43, 45, 45, 45, 43, 32, 124],
    [124, 32, 32, 32, 124, 32, 43],
    [124, 32, 32, 32, 124, 47, 46],
    [43, 45, 45, 45, 43, 46, 46]
    ]

res = [[46]]
curr_floor = 0

for idx, row in enumerate(board):
    for i in range(len(res)):
        res[i] = [46, 46] + res[i]
    res += [[46] * len(res[0]) for _ in range(2)]
    for num in row:
        if idx == 0:
            for i in range(len(res)):
                res[i] += [46, 46, 46, 46]

        res = [[46] * len(res[0]) for _ in range(3 * (num - curr_floor))] + res
        curr_floor = max(num, curr_floor)

        for block in range(num):
            for i in range(1, 7):
                for j in range(1, 8):
                    res[-i - 3 * block][-j] = one_block[-i][-j] if one_block[-i][-j] != 46 else res[-i - 3 * block][-j]

for row in res:
    print(''.join(map(chr, row)))
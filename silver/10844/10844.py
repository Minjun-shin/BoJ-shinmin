N = int(input())
res = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
for _ in range(N-1):
    tmp = [0] * 10
    tmp[0], tmp[-1] = res[-1][1], res[-1][8]
    for i in range(1, 9):
        tmp[i] = res[-1][i-1] + res[-1][i+1]

    res.append(tmp)

print(sum(res[-1]) % 1000000000)
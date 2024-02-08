N = int(input())

infos = [tuple(map(int, input().split())) for _ in range(N)]
res = [0] * N

for i in range(N):
    tmp = 0
    for j in range(N):
        if infos[i][0] < infos[j][0] and infos[i][1] < infos[j][1]:
            tmp += 1

    res[i] = tmp + 1

print(*res)
N, M = map(int, input().split())
infos = [[0] * N for _ in range(N)]

for _ in range(M):
    heavy, light = map(int, input().split())
    infos[heavy-1][light-1] = -1
    infos[light-1][heavy-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if infos[i][k] == infos[k][j] != 0:
                infos[i][j] = infos[i][k]

cnt = 0
for r in range(N):
    p_num, n_num = 0, 0
    for c in range(N):
        if infos[r][c] > 0:
            p_num += 1
        elif infos[r][c] < 0:
            n_num += 1
    if max(p_num, n_num) > N // 2:
        cnt += 1

print(cnt)
N = int(input())
res = [[float('inf')] * 3 for _ in range(3)]
num_list = list(map(int, input().split()))
for i in range(3):
    res[i][i] = num_list[i]

for idx in range(1, N):
    num_list = list(map(int, input().split()))
    tmp_list = [ele.copy() for ele in res]

    for i in range(3):
        for j in range(3):
            tmp = float('inf')
            for k in range(3):
                if k == i:
                    continue
                tmp = min(tmp, tmp_list[k][j])
            res[i][j] = tmp + num_list[i]

ans = float('inf')
for i in range(3):
    for j in range(3):
        if i == j:
            continue
        ans = min(ans, res[i][j])

print(ans)
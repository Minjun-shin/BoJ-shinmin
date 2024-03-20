N = int(input())
res = [0]

for i in range(N):
    num_list = [0] + list(map(int, input().split()))
    if not res:
        res = [0] + num_list.copy()
        continue
    res.append(0)
    for j in range(i+1, 0, -1):
        res[j] = max(res[j], res[j-1]) + num_list[j]

print(max(res))
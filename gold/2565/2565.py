N = int(input())
connections = {}
num_list = []

for _ in range(N):
    s, e = map(int, input().split())
    connections[e] = s
    num_list.append(e)

num_list.sort(key=lambda x: connections[x])

res = [1] * N
for i in range(1, N):
    for j in range(i):
        if num_list[i] > num_list[j]:
            res[i] = max(res[i], res[j] + 1)

print(N - max(res))
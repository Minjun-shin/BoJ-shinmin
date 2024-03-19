from collections import deque


N, M = map(int, input().split())
res = [0] * 100
connects = {}
for _ in range(N + M):
    s, e = map(int, input().split())
    connects[s-1] = e-1

dQ = deque()
dQ.append(0)

while dQ and res[-1] == 0:
    curr = dQ.popleft()

    for i in range(1, 7):
        n_c = curr + i

        if 0 <= n_c < 100 and res[n_c] == 0:
            res[n_c] = res[curr] + 1
            if n_c in connects.keys():
                if res[connects[n_c]] == 0:
                    res[connects[n_c]] = res[n_c]
                    dQ.append(connects[n_c])
            else:
                dQ.append(n_c)

print(res[-1])
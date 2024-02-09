from collections import deque


N, K = map(int, input().split())
ch = [-1] * 100001
ch[N] = 0
dQ = deque([N])

while ch[K] == -1:
    curr = dQ.popleft()
    if 0 <= curr-1 and ch[curr - 1] == -1:
        ch[curr - 1] = ch[curr] + 1
        dQ.append(curr - 1)

    if curr + 1 <= 100000 and ch[curr + 1] == -1:
        ch[curr + 1] = ch[curr] + 1
        dQ.append(curr + 1)

    if curr * 2 <= 100000 and ch[curr * 2] == -1:
        ch[curr * 2] = ch[curr] + 1
        dQ.append(curr * 2)

print(ch[K])
from heapq import heappop, heappush


N, K = map(int, input().split())
ch = [float('inf')] * (2*max(N, K)+1)
ch[K] = 0
pQ = []
heappush(pQ, (0, K))

while pQ:
    time, curr = heappop(pQ)

    if time > ch[curr] or curr == N:
        continue

    if curr - 1 >= 0 and ch[curr-1] > ch[curr] + 1:
        ch[curr-1] = ch[curr] + 1
        heappush(pQ, (ch[curr] + 1, curr-1))

    if curr + 1 <= 2*max(N, K) and ch[curr+1] > ch[curr] + 1:
        ch[curr+1] = ch[curr] + 1
        heappush(pQ, (ch[curr] + 1, curr+1))

    if curr % 2 == 0 and ch[curr//2] > ch[curr]:
        ch[curr//2] = ch[curr]
        heappush(pQ, (ch[curr], curr//2))

print(ch[N])
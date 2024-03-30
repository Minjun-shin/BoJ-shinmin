from heapq import heappop, heappush


N, K = map(int, input().split())
ch = [float('inf')] * 200001
ch[K] = 0
pQ = []
heappush(pQ, (0, K))
cnt = 0

while pQ:
    time, curr = heappop(pQ)

    if time > ch[curr]:
        continue

    if curr == N and time == ch[curr]:
        cnt += 1
        continue

    if curr - 1 >= 0:
        ch[curr-1] = min(ch[curr-1], ch[curr] + 1)
        heappush(pQ, (ch[curr] + 1, curr-1))

    if curr + 1 <= 200000:
        ch[curr+1] = min(ch[curr+1], ch[curr] + 1)
        heappush(pQ, (ch[curr] + 1, curr+1))

    if curr % 2 == 0:
        ch[curr//2] = min(ch[curr//2], ch[curr] + 1)
        heappush(pQ, (ch[curr] + 1, curr//2))

print(ch[N], cnt, sep='\n')
import sys
input = sys.stdin.readline


N = int(input())

times = [tuple(map(int, input().split())) for _ in range(N)]
times.sort(key=lambda x : (x[1], x[0]))

res = [times[0][1]]
for s, e in times[1:]:
    if s >= res[-1]:
        res.append(e)

print(len(res))
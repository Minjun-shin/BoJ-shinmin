import sys
input = sys.stdin.readline


days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
N = int(input())
periods = []

for _ in range(N):
    sm, sd, em, ed = map(int, input().split())
    periods.append((sum(days[:sm-1])+sd, sum(days[:em-1])+ed))

periods.sort()

curr = sum(days[:2])+1
cnt = 0
tmp = 0
for s, e in periods:
    if s > curr:
        cnt += 1
        curr = tmp
        if s > curr:
            break
    tmp = max(tmp, e)
    
if curr < sum(days[:11])+1:
    curr = tmp
    cnt += 1

print(cnt if curr >= sum(days[:11])+1 else 0)
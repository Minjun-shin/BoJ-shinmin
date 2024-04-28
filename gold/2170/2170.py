import sys
input = sys.stdin.readline


N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]
lines.sort()
res = []

for s, e in lines:
    if not res or res[-1][-1] < s:
        res.append([s, e])
    else:
        res[-1][-1] = max(e, res[-1][-1])
     
ans = 0   
for s, e in res:
    ans += e - s
    
print(ans)
N = int(input())
res = [list(map(int, input().split()))]

for _ in range(N-1):
    curr = list(map(int, input().split()))

    curr = [curr[0] + min(res[-1][1], res[-1][2]), curr[1] + min(res[-1][0], res[-1][2]), curr[2] + min(res[-1][0], res[-1][1])]

    res.append(curr)

print(min(res[-1]))
M, N = map(int, input().split())

T = int(input())

res = [[0, N], [0, M]]
for _ in range(T):
    vh, num = map(int, input().split())
    if vh == 0:
        res[0].append(num)

    else:
        res[1].append(num)

res[0].sort()
res[1].sort()

ver, hor = 0, 0

for i in range(len(res[0])-1):
    ver = max(res[0][i+1]-res[0][i], ver)

for i in range(len(res[1])-1):
    hor = max(res[1][i+1]-res[1][i], hor)

print(ver * hor)
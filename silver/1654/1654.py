K, N = map(int, input().split())

lines = [int(input()) for _ in range(K)]

s, e = 1, sum(lines) // N

res = 0
while s <= e:
    tmp = 0
    middle = (s + e) // 2
    for line in lines:
        tmp += line // middle

    if tmp >= N:
        res = max(res, middle)
        s = middle + 1
    
    else:
        e = middle - 1

print(res)
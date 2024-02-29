M = int(input())

left, right = 0, M * 5
res = float('inf')

while left <= right:
    middle = (left + right) // 2
    num = middle
    tmp = 0
    while num >= 5:
        tmp += num // 5
        num //= 5

    if tmp == M:
        res = min(res, middle)
        right = middle - 1

    elif tmp > M:
        right = middle - 1

    else:
        left = middle + 1

print(-1 if res == float('inf') else res)
N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort(reverse=True)

left, right = 0, max(num_list)
res = 0
while left <= right:
    middle = (left + right) // 2

    total = 0
    for num in num_list:
        if num > middle and total < M:
            total += num-middle
        else:
            break

    if total >= M:
        res = max(res, middle)
        left = middle + 1

    else:
        right = middle - 1

print(res)
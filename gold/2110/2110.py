import sys
input = sys.stdin.readline


N, C = map(int, input().split())
num_list = [int(input()) for _ in range(N)]
num_list.sort()

l, r = 0, num_list[-1] - num_list[0]
res = 0

while l <= r:
    middle = (l + r) // 2
    prev = num_list[0]
    cnt = 1
    for i in range(1, N):
        if num_list[i] >= prev + middle:
            cnt += 1
            prev = num_list[i]
    if cnt >= C:
        res = max(res, middle)
        l = middle + 1
    else:
        r = middle - 1

print(res)
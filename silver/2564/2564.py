def mkcorr(direction, num):
    if direction == 1:
        return (num, 0)

    elif direction == 2:
        return (num, N)

    elif direction == 3:
        return (0, num)

    else:
        return (M, num)


M, N = map(int, input().split())

num = int(input())

corr_list = [tuple(map(int, input().split())) for _ in range(num)]

curr = tuple(map(int, input().split()))

res = 0
for corr in corr_list:
    if corr[0] == curr[0]:
        res += abs(corr[1] - curr[1])

    elif corr[0] in [1, 2] and curr[0] in [1, 2]:
        tmp = corr[1] + curr[1] + N
        res += min(tmp, (N + M) * 2 - tmp)

    elif corr[0] in [3, 4] and curr[0] in [3, 4]:
        tmp = corr[1] + curr[1] + M
        res += min(tmp, (N + M) * 2 - tmp)

    else:
        new_curr = mkcorr(*curr)
        corr = mkcorr(*corr)
        res += abs(new_curr[0] - corr[0]) + abs(new_curr[1] - corr[1])

print(res)
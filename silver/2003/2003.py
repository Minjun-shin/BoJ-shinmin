N, M = map(int, input().split())
num_list = list(map(int, input().split())) + [0]

s, e = 0, 1
total = num_list[0]

res = 0
while e <= N:
    if total > M:
        total -= num_list[s]
        s += 1

    elif total < M:
        total += num_list[e]
        e += 1

    else:
        res += 1
        total += num_list[e]
        e += 1

print(res)
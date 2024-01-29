N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
X = int(input())

res = 0
s, e = 0, N-1
while s < e:
    if num_list[s] + num_list[e] > X:
        e -= 1

    elif num_list[s] + num_list[e] < X:
        s += 1

    else:
        s += 1
        res += 1

print(res)
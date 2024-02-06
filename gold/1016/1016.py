min_value, max_value = map(int, input().split())
sqrt = int(max_value ** (1/2)) + 1

ch = [0] * (sqrt + 1)
res = [1] * (max_value - min_value + 1)

ch[0], ch[1] = 1, 1

for i in range(2, sqrt+1):
    if ch[i] == 0:
        for j in range(2*i, sqrt+1, i):
            ch[j] = 1

        for j in range(((i**2) - (min_value % (i**2))) % (i**2), max_value - min_value + 1, i**2):
            res[j] = 0

print(sum(res))
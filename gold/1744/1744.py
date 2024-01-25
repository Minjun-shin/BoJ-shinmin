N = int(input())
minus = []
plus = []
iszero = False
res = 0

for _ in range(N):
    n = int(input())
    if n == 0:
        iszero = True

    elif n == 1:
        res += 1

    elif n > 0:
        plus.append(n)

    else:
        minus.append(n)

plus.sort(reverse=True)
minus.sort()

tmp = []
for num in plus:
    tmp.append(num)
    if len(tmp) == 2:
        a, b = tmp
        tmp = []
        res += a * b

if tmp:
    res += tmp[0]

tmp = []
for num in minus:
    tmp.append(num)
    if len(tmp) == 2:
        a, b = tmp
        tmp = []
        res += a * b

if tmp and not iszero:
    res += tmp[0]

print(res)
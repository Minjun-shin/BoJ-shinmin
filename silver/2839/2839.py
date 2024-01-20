N = int(input())

num5 = N // 5
num3 = 0
judge = True

while num5 >= 0:
    num3 = (N - 5 * num5) // 3
    if (N - 5 * num5) % 3 == 0:
        break
    num5 -= 1

else:
    judge = False

if judge:
    print(num5 + num3)
else:
    print(-1)
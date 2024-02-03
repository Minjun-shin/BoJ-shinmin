N = int(input())

num = 1
for i in range(2, N+1):
    num *= i

res = 0
while num % 10 == 0:
    res += 1
    num //= 10

print(res)
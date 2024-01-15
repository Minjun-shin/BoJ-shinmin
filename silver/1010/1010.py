from math import factorial


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(factorial(M) // factorial(N) // factorial(M-N))
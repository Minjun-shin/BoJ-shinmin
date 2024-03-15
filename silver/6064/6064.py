import sys
input = sys.stdin.readline


T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    limit = M * N

    while x <= limit:
        if (x % N) == (y % N):
            break

        x += M

    else:
        x, y = -1, -1

    print(x)
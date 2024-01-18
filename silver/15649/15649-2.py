from itertools import permutations as perm


N, M = map(int, input().split())
for nums in perm(range(1, N+1), M):
    print(*nums)
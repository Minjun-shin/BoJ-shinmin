from itertools import combinations as comb


N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

for nums in comb(num_list, M):
    print(*nums)
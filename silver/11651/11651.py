import sys
input = sys.stdin.readline


N = int(input())
corr_list = [tuple(map(int, input().split())) for _ in range(N)]
corr_list.sort(key=lambda x : (x[1], x[0]))

for corr in corr_list:
    print(*corr)
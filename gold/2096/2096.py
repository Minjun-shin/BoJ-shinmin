import sys
input = sys.stdin.readline


N = int(input())
res = [[0, 0] for _ in range(3)]
tmp = [[0, 0] for _ in range(3)]

for i in range(N):
    num_list = list(map(int, input().split()))
    tmp[0][0] = min(res[0][0], res[1][0]) + num_list[0]
    tmp[0][1] = max(res[0][1], res[1][1]) + num_list[0]
    tmp[1][0] = min(res[0][0], res[1][0], res[2][0]) + num_list[1]
    tmp[1][1] = max(res[0][1], res[1][1], res[2][1]) + num_list[1]
    tmp[2][0] = min(res[1][0], res[2][0]) + num_list[2]
    tmp[2][1] = max(res[1][1], res[2][1]) + num_list[2]
    res = [tmp_e.copy() for tmp_e in tmp]

print(max(res[0][1], res[1][1], res[2][1]), min(res[0][0], res[1][0], res[2][0]))
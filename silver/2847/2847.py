N = int(input())

res = 0
num_list = [int(input()) for _ in range(N)]

for _ in range(N-1):
    num = num_list.pop()
    if num_list[-1] >= num:
        res += num_list[-1] - num + 1
        num_list[-1] = num - 1

print(res)
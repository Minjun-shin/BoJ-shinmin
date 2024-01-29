N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

res = 0
for i in range(N):
    res += num_list[i] * (N - i)

print(res)
N, K = map(int, input().split())
num_list = list(map(int, input().split()))

left, right = 0, K
total = sum(num_list[:K])
res = total

for _ in range(N-K):
    total = total + num_list[right] - num_list[left]
    res = max(res, total)
    left += 1
    right += 1

print(res)
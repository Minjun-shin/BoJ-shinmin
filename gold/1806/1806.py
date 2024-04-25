N, S = map(int, input().split())
num_list = list(map(int, input().split()))

l, r, tmp_sum = 0, 0, num_list[0]

res = float('inf')
while l <= r < N:
    if tmp_sum < S:
        r += 1
        if r < N:
            tmp_sum += num_list[r]
    else:
        res = min(res, r-l+1)
        tmp_sum -= num_list[l]
        l += 1
    
print(0 if res == float('inf') else res)
H, W = map(int, input().split())
num_list = list(map(int, input().split()))

res = [H] * W

h = num_list[0]
for i in range(W):
    if num_list[i] > h:
        res[i] = 0
        h = num_list[i]
    
    else:
        res[i] = min(res[i], h - num_list[i])
        
h = num_list[-1]
for i in range(W-1, -1, -1):
    if num_list[i] > h:
        res[i] = 0
        h = num_list[i]
    
    else:
        res[i] = min(res[i], h - num_list[i])

print(sum(res))
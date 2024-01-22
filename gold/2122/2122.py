N, K = int(input()), int(input())
num_list = list(map(int, input().split()))
num_list.sort()

tmp_list = []

for i in range(N-1):
    tmp_list.append(num_list[i+1] - num_list[i])
    
tmp_list.sort()

print(sum(tmp_list[:N-K]))
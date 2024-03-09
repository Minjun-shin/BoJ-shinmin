N = int(input())
num_list = list(map(int, input().split()))

sort_list = sorted(set(num_list))
num_dict = {sort_list[i]:i for i in range(len(sort_list))}
res = []

for num in num_list:
    res.append(num_dict[num])

print(*res)
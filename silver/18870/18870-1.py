def bin_search(num):
    left = 0
    right = len(sort_list)
    while left <= right:
        middle = (left + right) // 2
        if sort_list[middle] == num:
            return middle
        elif sort_list[middle] < num:
            left = middle + 1
        else:
            right = middle - 1


N = int(input())
num_list = list(map(int, input().split()))

sort_list = sorted(set(num_list))
res = []

for num in num_list:
    res.append(bin_search(num))

print(*res)
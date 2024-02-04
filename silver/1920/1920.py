def bin_search(num):
    s, e = 0, N-1
    while s <= e:
        middle = (s + e) // 2
        if num_list[middle] > num:
            e = middle - 1

        elif num_list[middle] < num:
            s = middle + 1

        else:
            return 1
    
    return 0


N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

M = int(input())
targets = list(map(int, input().split()))

for target in targets:
    print(bin_search(target))
def hanoi(n, stick_nums):
    global res
    if n == 1:
        res.append([stick_nums[0], stick_nums[2]])
        return

    hanoi(n-1, [stick_nums[0], stick_nums[2], stick_nums[1]])
    res.append([stick_nums[0], stick_nums[2]])
    hanoi(n-1, [stick_nums[1], stick_nums[0], stick_nums[2]])

N = int(input())
res = []

hanoi(N, [1, 2, 3])

print(len(res))
for each_res in res:
    print(*each_res)
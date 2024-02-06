N = int(input())
num_dict = {}
for num in map(int, input().split()):
    num_dict[num] = num_dict.get(num, 0) + 1

M = int(input())
print(*[num_dict.get(x, 0) for x in map(int, input().split())])
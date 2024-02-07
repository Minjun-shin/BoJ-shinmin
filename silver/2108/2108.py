import sys
input = sys.stdin.readline


def arithmetic(arr):
    return round(sum(arr) / len(arr))


def median(arr):
    return arr[len(arr) // 2]


def mode(arr):
    res = (0, [0])
    for num in arr.keys():
        if res[0] < arr[num]:
            res = (arr[num], [num])

        elif res[0] == arr[num]:
            res[1].append(num)

    return sorted(res[1])[1] if len(res[1]) > 1 else res[1][0]


def scope(arr):
    return arr[-1] - arr[0]


N = int(input())
num_list = []
num_dict = {}

for _ in range(N):
    num = int(input())
    num_list.append(num)
    num_dict[num] = num_dict.get(num, 0) + 1

num_list.sort()

print(arithmetic(num_list))
print(median(num_list))
print(mode(num_dict))
print(scope(num_list))

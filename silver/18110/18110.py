import sys
input = sys.stdin.readline


def round(num):
    if num - int(num) >= .5:
        return int(num) + 1
    
    else:
        return int(num)


N = int(input())
if N == 0:
    print(0)

else:
    out = round(N * 15 / 100)

    num_list = [int(input()) for _ in range(N)]
    num_list.sort()

    if out != 0:
        print(round(sum(num_list[out:-out]) / (N - 2 * out)))
    else:
        print(round(sum(num_list) / N))
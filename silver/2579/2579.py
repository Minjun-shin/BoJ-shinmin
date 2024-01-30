N = int(input())
num_list = [int(input()) for _ in range(N)]

ch = [[0, 0] for _ in range(N)]
if N <= 2:
    print(sum(num_list))

else:
    ch[0] = [num_list[0], num_list[0]]
    ch[1] = [num_list[0] + num_list[1], num_list[1]]

    for i in range(2, N):
        ch[i] = [ch[i-1][1] + num_list[i], max(ch[i-2]) + num_list[i]]

    print(max(ch[-1]))
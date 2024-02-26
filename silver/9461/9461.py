num_list = [1, 1, 1, 2, 2]

T = int(input())
for _ in range(T):
    N = int(input())
    if N <= len(num_list):
        print(num_list[N-1])
    else:
        while N > len(num_list):
            num_list.append(num_list[-1] + num_list[-5])
        print(num_list[-1])
import sys
input = sys.stdin.readline


T = int(input())

for test_case in range(T):
    N = int(input())
    arr = [0] * (N+1)

    for _ in range(N-1):
        s, e = map(int, input().split())
        arr[e] = s

    A, B = map(int, input().split())
    a_list, b_list = [], []

    while A:
        a_list.append(A)
        A = arr[A]

    while B:
        b_list.append(B)
        B = arr[B]

    for i in range(-1, -min(len(a_list), len(b_list))-1, -1):
        if a_list[i] != b_list[i]:
            break

    print(a_list[i] if i == -min(len(a_list), len(b_list)) else a_list[i+1])
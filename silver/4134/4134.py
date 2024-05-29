import sys
input = sys.stdin.readline


def isprime(num):
    for i in range(int(num ** (1/2))+1):
        if prime[i]:
            continue
        if num % i == 0:
            return False
    return True


T = int(input())
num_list = [int(input()) for _ in range(T)]
max_val = max(num_list)

N = int(1.5 * max_val ** (1/2))
prime = [0] * (N + 1)
prime[0], prime[1] = 1, 1

for i in range(N+1):
    if prime[i] == 0:
        for j in range(2*i, N+1, i):
            prime[j] = 1

for num in num_list:
    if num <= 1:
        print(2)
        continue

    while True:
        if isprime(num):
            print(num)
            break
        num += 1
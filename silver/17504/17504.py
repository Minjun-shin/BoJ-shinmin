from math import gcd


def calc(numbers):
    if len(numbers) == 1:
        return 1, numbers[0]
    
    num = numbers.pop()
    P, Q = calc(numbers)
    return Q, P + num * Q


N = int(input())
num_list = list(map(int, input().split()))[::-1]
P, Q = calc(num_list)
print((Q - P) // gcd(P, Q), Q // gcd(P, Q))
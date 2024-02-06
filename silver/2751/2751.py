import sys
input = sys.stdin.readline


N = int(input())
num_list = [int(input()) for _ in range(N)]
print(*sorted(num_list), sep='\n')
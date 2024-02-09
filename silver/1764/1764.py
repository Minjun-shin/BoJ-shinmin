import sys
input = sys.stdin.readline


N, M = map(int, input().split())
A = set([input().strip() for _ in range(N)])
B = set([input().strip() for _ in range(M)])

print(len(A & B))
print(*sorted(A & B), sep='\n')
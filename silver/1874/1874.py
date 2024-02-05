import sys
input = sys.stdin.readline


N = int(input())
num_list = [float('inf')] + list(range(N, 0, -1))

stack = [0]
res = []

for _ in range(N):
    num = int(input())
    if (num > stack[-1]) and (num < num_list[-1]):
        print('NO')
        break

    while num >= num_list[-1]:
        number = num_list.pop()
        stack.append(number)
        res.append('+')
    
    while num <= stack[-1]:
        stack.pop()
        res.append('-')

else:
    print(*res, sep='\n')
import sys
input = sys.stdin.readline


N = int(input())
stack = []

for _ in range(N):
    command = input().strip()
    if command.startswith('push'):
        _, num = command.split()
        num = int(num)
        stack.append(num)

    elif command == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif command == 'size':
        print(len(stack))

    elif command == 'empty':
        print(int(not bool(stack)))

    else:
        print(stack[-1] if stack else -1)
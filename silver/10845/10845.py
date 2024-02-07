from collections import deque
import sys
input = sys.stdin.readline


N = int(input())

Queue = deque()
for _ in range(N):
    order = input().split()
    if order[0] == 'push':
        Queue.append(int(order[1]))

    elif order[0] == 'pop':
        if Queue:
            print(Queue.popleft())
        else:
            print(-1)

    elif order[0] == 'size':
        print(len(Queue))

    elif order[0] == 'empty':
        print(int(not Queue))

    elif order[0] == 'front':
        if Queue:
            print(Queue[0])
        
        else:
            print(-1)

    else:
        if Queue:
            print(Queue[-1])
        
        else:
            print(-1)
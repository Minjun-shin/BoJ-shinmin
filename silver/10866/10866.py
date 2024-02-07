from collections import deque
import sys
input = sys.stdin.readline


N = int(input())

Deque = deque()
for _ in range(N):
    order = input().split()
    if order[0] == 'push_front':
        Deque.appendleft(int(order[1]))

    elif order[0] == 'push_back':
        Deque.append(int(order[1]))

    elif order[0] == 'pop_front':
        if Deque:
            print(Deque.popleft())

        else:
            print(-1)
    
    elif order[0] == 'pop_back':
        if Deque:
            print(Deque.pop())
            
        else:
            print(-1)

    elif order[0] == 'size':
        print(len(Deque))

    elif order[0] == 'empty':
        print(int(not Deque))

    elif order[0] == 'front':
        if Deque:
            print(Deque[0])
        
        else:
            print(-1)

    else:
        if Deque:
            print(Deque[-1])
        
        else:
            print(-1)
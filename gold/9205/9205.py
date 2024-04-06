from collections import deque


def dist(corr1, corr2):
    return abs(corr1[0] - corr2[0]) + abs(corr1[1] - corr2[1])


T = int(input())
Limit = 20 * 50

for _ in range(T):
    N = int(input())
    S = tuple(map(int, input().split()))
    stores = [tuple(map(int, input().split())) for _ in range(N)]
    E = tuple(map(int, input().split()))

    visited = [0] * N
    dQ = deque()
    dQ.append(S)

    while dQ:
        curr = dQ.popleft()

        if dist(curr, E) <= Limit:
            print('happy')
            break

        for idx, store in enumerate(stores):
            if visited[idx] == 0 and dist(curr, store) <= Limit:
                visited[idx] = 1
                dQ.append(store)
    
    else:
        print('sad')
from collections import deque
import sys
input = sys.stdin.readline


test_case = 0
while True:
    test_case += 1
    N, M = map(int, input().split())
    if N == M == 0:
        break

    graphs = [[] for _ in range(N)]
    visited = [0] * N

    for _ in range(M):
        s, e = map(int, input().split())
        graphs[s-1].append(e-1)
        graphs[e-1].append(s-1)

    res = 0
    for i in range(N):
        if visited[i] == 0:
            res += 1
            status = False
            visited[i] = 1
            dQ = deque([(-1, i)])

            while dQ:
                prev, curr = dQ.popleft()

                for num in graphs[curr]:
                    if visited[num] == 0:
                        visited[num] = 1
                        dQ.append((curr, num))
                    elif num != prev:
                        status = True

            if status:
                res -= 1

    if res == 0:
        print(f'Case {test_case}: No trees.')
    elif res == 1:
        print(f'Case {test_case}: There is one tree.')
    else:
        print(f'Case {test_case}: A forest of {res} trees.')
def bellman_ford():
    dists = [1e9] * N
    dists[0] = 0
    for i in range(N):
        for start, end, weight in graphs:
            if dists[end] > dists[start] + weight:
                dists[end] = dists[start] + weight
                if i == N-1:
                    return True
    return False


T = int(input())
for _ in range(T):
    N, M, W = map(int, input().split())
    graphs = []

    for _ in range(M):
        s, e, w = map(int, input().split())
        graphs.append((s-1, e-1, w))
        graphs.append((e-1, s-1, w))
    for _ in range(W):
        s, e, w = map(int, input().split())
        graphs.append((s-1, e-1, -w))

    if bellman_ford():
        print('YES')
    else:
        print('NO')
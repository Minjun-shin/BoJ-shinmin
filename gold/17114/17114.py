from collections import deque
import sys
input = sys.stdin.readline


def is_inrange(w, v, u, t, s, r, q, p, o, n, m):
    return 0 <= w < W and 0 <= v < V and 0 <= u < U and 0 <= t < T and 0 <= s < S and 0 <= r < R and 0 <= q < Q and 0 <= p < P and 0 <= o < O and 0 <= n < N and 0 <= m < M


M, N, O, P, Q, R, S, T, U, V, W = map(int, input().split())
board = [[[[[[[[[[list(map(int, input().split())) for _ in range(N)] for _ in range(O)] for _ in range(P)] for _ in range(Q)] for _ in range(R)] for _ in range(S)] for _ in range(T)] for _ in range(U)] for _ in range(V)] for _ in range(W)]

dm = [1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
dn = [0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
do = [0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
dp = [0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
dq = [0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
dr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ds = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0]
dt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0]
du = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0]
dv = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0]
dw = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1]

dQ = deque()

cnt = 0
for m in range(M):
    for n in range(N):
        for o in range(O):
            for p in range(P):
                for q in range(Q):
                    for r in range(R):
                        for s in range(S):
                            for t in range(T):
                                for u in range(U):
                                    for v in range(V):
                                        for w in range(W):
                                            if board[w][v][u][t][s][r][q][p][o][n][m] == 1:
                                                dQ.append((w, v, u, t, s, r, q, p, o, n, m))
                                            elif board[w][v][u][t][s][r][q][p][o][n][m] == 0:
                                                cnt += 1

res = 0
while dQ:
    res += 1
    for _ in range(len(dQ)):
        w, v, u, t, s, r, q, p, o, n, m = dQ.popleft()

        for i in range(22):
            n_w = w + dw[i]
            n_v = v + dv[i]
            n_u = u + du[i]
            n_t = t + dt[i]
            n_s = s + ds[i]
            n_r = r + dr[i]
            n_q = q + dq[i]
            n_p = p + dp[i]
            n_o = o + do[i]
            n_n = n + dn[i]
            n_m = m + dm[i]

            if is_inrange(n_w, n_v, n_u, n_t, n_s, n_r, n_q, n_p, n_o, n_n, n_m) and board[n_w][n_v][n_u][n_t][n_s][n_r][n_q][n_p][n_o][n_n][n_m] == 0:
                board[n_w][n_v][n_u][n_t][n_s][n_r][n_q][n_p][n_o][n_n][n_m] = 1
                dQ.append((n_w, n_v, n_u, n_t, n_s, n_r, n_q, n_p, n_o, n_n, n_m))
                cnt -= 1

if cnt:
    print(-1)
else:
    print(res-1)
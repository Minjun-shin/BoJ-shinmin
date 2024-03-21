blocks = [
    [
        [1],
        [1],
        [1],
        [1]
    ],
    [
        [1, 1, 1, 1]
    ],
    [
        [1, 1],
        [1, 1]
    ],
    [
        [1, 1, 1],
        [0, 1, 0]
    ],
    [
        [0, 1, 0],
        [1, 1, 1]
    ],
    [
        [1, 0],
        [1, 1],
        [1, 0]
    ],
    [
        [0, 1],
        [1, 1],
        [0, 1]
    ],
    [
        [1, 0],
        [1, 0],
        [1, 1]
    ],
    [
        [1, 1],
        [0, 1],
        [0, 1]
    ],
    [
        [1, 1, 1],
        [1, 0, 0]
    ],
    [
        [0, 0, 1],
        [1, 1, 1]
    ],
    [
        [0, 1],
        [0, 1],
        [1, 1]
    ],
    [
        [1, 1],
        [1, 0],
        [1, 0]
    ],
    [
        [1, 1, 1],
        [0, 0, 1]
    ],
    [
        [1, 0, 0],
        [1, 1, 1]
    ],
    [
        [1, 0],
        [1, 1],
        [0, 1]
    ],
    [
        [0, 1, 1],
        [1, 1, 0]
    ],
    [
        [0, 1],
        [1, 1],
        [1, 0]
    ],
    [
        [1, 1, 0],
        [0, 1, 1]
    ]
]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
res = 0

for block in blocks:
    n, m = len(block), len(block[0])
    for r in range(N-n+1):
        for c in range(M-m+1):
            tmp = 0

            for dr in range(n):
                for dc in range(m):
                    tmp += board[r+dr][c+dc] * block[dr][dc]

            res = max(res, tmp)

print(res)
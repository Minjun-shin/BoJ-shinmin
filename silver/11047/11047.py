N, M = map(int, input().split())
coins = []

for _ in range(N):
    coins.append(int(input()))

coins.sort(reverse=True)
res = 0

for coin in coins:
    if coin <= M:
        res += M // coin
        M -= (M // coin) * coin

print(res)
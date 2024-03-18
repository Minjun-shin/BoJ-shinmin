number = int(input())
N = int(input())
banned = set(input().split()) if N else set()

res = abs(number - 100)
for num in range(1000001):
    if set(str(num)) & banned:
        continue
    res = min(res, len(str(num)) + abs(number - num))
print(res)
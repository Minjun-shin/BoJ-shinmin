T = int(input())

for _ in range(T):
    N = int(input())
    cloth_dict = {}

    for _ in range(N):
        _, cloth = input().split()
        cloth_dict[cloth] = cloth_dict.get(cloth, 1) + 1

    res = 1
    for cloth in cloth_dict:
        res *= cloth_dict[cloth]

    print(res - 1)
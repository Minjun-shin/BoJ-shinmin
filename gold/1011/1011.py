T= int(input())

for _ in range(T):
    s, e = map(int, input().split())
    dist = e - s
    n = 1
    length = 1
    
    while length < dist:
        n += 1
        length += (n + 1) // 2
    
    print(n)
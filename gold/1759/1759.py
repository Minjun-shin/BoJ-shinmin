def DFS(n, result, idx=-1):
    if n == M:
        total = 0
        for letter in ['a', 'e', 'i', 'o', 'u']:
            if letter in result:
                total += 1

        if 1 <= total <= M-2:
            print(''.join(result))
        return
    
    for i in range(idx+1, N):
        DFS(n+1, result+(letters[i],), i)


M, N = map(int, input().split())
letters = list(input().split())
letters.sort()

DFS(0, ())
def is_prime(num):
    length = int(num ** (1/2)) + 1
    ch = [1] * length
    ch[0], ch[1] == 1
    for n in range(2, length):
        if ch[n]:
            if num % n == 0:
                return False
            else:
                for i in range(n, length, n):
                    ch[i] = 0
    return True


N = int(input())

starts = [2, 3, 5, 7]
middles = [1, 3, 7, 9]

curr = starts.copy()

for _ in range(N-1):
    prev = curr.copy()
    curr = []

    for num in prev:
        for plus in middles:
            new = num * 10 + plus
            if is_prime(new):
                curr.append(new)

print(*curr, sep='\n')
N = int(input())
L = int(input())
S = input().strip()

prev = ''
tmp = 0
res = 0
for letter in S:
    if (not tmp and letter == 'I') or (prev == 'I' and letter == 'O') or (prev == 'O' and letter == 'I'):
        tmp += 1
    else:
        if letter == 'I':
            tmp = 1
        else:
            tmp = 0

    prev = letter

    if tmp >= 2 * N + 1 and tmp % 2 == 1:
        res += 1

print(res)
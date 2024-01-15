N = int(input())
# Upper
for i in range(N-1):
    print(' ' * i + '*', end='')
    if i == 0:
        print('*' * (N-2), end='')
    else:
        print(' ' * (N-2), end='')
    print('*', end='')
    print(' ' * (2 * (N - i) - 3), end='')
    print('*', end='')
    if i == 0:
        print('*' * (N-2), end='')
    else:
        print(' ' * (N-2), end='')
    print('*', end='')
    print()

# Middle
print(' ' * (N-1) + '*' + ' ' * (N-2) + '*' + ' ' * (N-2) + '*')

# Bottom
for i in range(N-1):
    print(' ' * (N-2-i) + '*', end='')
    if i == N-2:
        print('*' * (N-2), end='')
    else:
        print(' ' * (N-2), end='')
    print('*', end='')
    print(' ' * (2 * i + 1), end='')
    print('*', end='')
    if i == N-2:
        print('*' * (N-2), end='')
    else:
        print(' ' * (N-2), end='')
    print('*', end='')
    print()
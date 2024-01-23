T = int(input())
for _ in range(T):
    s = input()
    stack = []
    for letter in s:
        if letter == '(':
            stack.append(letter)

        else:
            if not stack:
                print('NO')
                break
            stack.pop()
    else:
        if stack:
            print('NO')
        else:
            print('YES')
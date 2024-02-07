import sys
input = sys.stdin.readline


while True:
    S = input().rstrip()
    if S == '.':
        break

    stack = []

    for letter in S:
        if letter in ['(', '[']:
            stack.append(letter)

        elif letter == ')':
            if stack and stack[-1] == '(':
                stack.pop()

            else:
                print('no')
                break

        elif letter == ']':
            if stack and stack[-1] == '[':
                stack.pop()

            else:
                print('no')
                break

    else:
        if stack:
            print('no')
        else:
            print('yes')
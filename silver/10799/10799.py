S = input().strip()
stack = []
prev = ''
res = 0

for letter in S:
    if letter == '(':
        stack.append(letter)

    elif letter == ')':
        if prev == '(':
            stack.pop()
            res += len(stack)

        elif prev == ')':
            stack.pop()
            res += 1

    prev = letter

print(res)
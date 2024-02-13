def mkpostfix(S):
    prior = {'+':1, '-':1, '*':2, '/':2, '(':0}
    stack = []
    res = []
    for letter in S:
        if letter.isalpha():
            res.append(letter)

        else:
            if not stack or letter == '(':
                stack.append(letter)

            elif letter == ')':
                while stack[-1] != '(':
                    res.append(stack.pop())
                stack.pop()

            else:
                while stack and prior[stack[-1]] >= prior[letter]:
                    res.append(stack.pop())
                stack.append(letter)

    while stack:
        res.append(stack.pop())

    return ''.join(res)

print(mkpostfix(input().strip()))

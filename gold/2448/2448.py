def calc():
    for i in range(len(triangle)):
        triangle.append(triangle[i] + ' ' + triangle[i])
        triangle[i] = '   ' * cnt + triangle[i] + '   ' * cnt


N = int(input())
N //= 3
cnt = 1
triangle = ['  *  ', ' * * ', '*****']

while N > cnt:
    calc()
    cnt *= 2

print(*triangle, sep='\n')
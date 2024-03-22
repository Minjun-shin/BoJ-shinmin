num_dict = {2:'1', 3:'7', 4:'4', 5:'2', 6:'6'}

T = int(input())
for _ in range(T):
    N = int(input())
    num8 = N // 7
    rest8 = N % 7
    if rest8 == 0:
        print('8' * num8, end=' ')

    elif rest8 == 1:
        print('10' + '8' * (num8-1), end=' ')

    elif rest8 >= 5 or rest8 == 2:
        print(num_dict[rest8] + '8' * num8, end=' ')

    elif num8 == 0:
        print(num_dict[rest8], end=' ')

    elif rest8 == 3:
        if num8 >= 2:
            print('200' + '8' * (num8-2), end=' ')
        else:
            print('22' + '8' * (num8-1), end=' ')

    else:
        print('20' + '8' * (num8-1), end=' ')

    num1 = N // 2
    rest1 = N % 2

    if rest1 == 0:
        print('1' * num1)

    else:
        print('7' + '1' * (num1-1))
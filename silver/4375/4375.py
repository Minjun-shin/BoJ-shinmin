while True:
    try:
        res = 1
        tmp = '1'
        N = int(input())

        while int(tmp) % N:
            tmp += '1'
            res += 1

        print(res)
    
    except:
        break
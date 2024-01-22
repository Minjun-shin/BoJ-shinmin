def fibonacci(n):
    global res0, res1
    if n == 0:
        res0 += 1
        return
    
    if n == 1:
        res1 += 1
        return
    
    return fibonacci(n-1), fibonacci(n-2)


if __name__=="__main__":
    T = int(input())

    for _ in range(T):
        res0, res1 = 0, 0
        N = int(input())
        
        fibonacci(N)
        print(res0, res1)
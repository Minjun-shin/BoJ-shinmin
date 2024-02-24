import math


def BF(N):
    if int(math.sqrt(N)) == math.sqrt(N):
        return 1
    
    for i in range(1, int(math.sqrt(N))+1):
        if int(math.sqrt(N - i**2)) == math.sqrt(N - i**2):
            return 2
        
    for i in range(1, int(math.sqrt(N))+1):
        for j in range(1, int(math.sqrt(N-i**2))+1):
            if int(math.sqrt(N - i**2 - j**2)) == math.sqrt(N - i**2 - j**2):
                return 3
            
    return 4

N = int(input())
print(BF(N))
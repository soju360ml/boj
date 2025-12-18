import math

M = input()
N = input()

def is_prime_number(a):
    x = set()   
    tmp_sqrt = math.floor(math.sqrt(a))

    for i in range(1, tmp_sqrt + 1):
        if a % i == 0:
            x.add(i)
            x.add(a // i)
            if len(x) > 2:
                return False
    if len(x) == 2:
        return True
    else:
        return False
    
def MtoN(M, N):
    sum = 0
    min_primes = None

    for i in range(M, N + 1):
        if is_prime_number(i):
            sum += i
            if min_primes == None:
                min_primes = i
    if min_primes == None:
        return -1
    
    return sum, min_primes

result = MtoN(int(M), int(N))

if result == -1:
    print(-1)
else:
    sum = result[0]
    min = result[1]

    print(sum)
    print(min)
from math import sqrt
def isprime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, round(sqrt(n)+1), 2):
        if n%i == 0:
            return False
    return True

def additive(n):
    s = 0
    while True:
        r = n % 10
        s += r
        n = n // 10
        if n == 0:
            if s < 10:
                if isprime(s):
                    return True
                else:
                    return False
            if s >= 10:
                n = s
                s = 0
            # else:
            #     return True

def isAdditivePrime(n):
    if n < 10 and isprime(n):
        return True
    
    elif n < 10 and not isprime(n):
        return False
    
    elif additive(n):
        return True

    else:
        return False

print(isAdditivePrime(int(input())))
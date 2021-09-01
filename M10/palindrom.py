def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, round(n**0.5)+1, 2):
        if n%i==0:
            return False
    return True

def IsPalindromicPrime(n):
    s = 0
    x = n
    while True:
        r = x % 10
        s = s*10 + r
        x = x // 10
        if x == 0:
            if s == n:
                return True
            else:
                return False            

def PalindromicPrime(n):
    if isPrime(n) and IsPalindromicPrime(n):
        return True
    else:
        return False

print(PalindromicPrime(int(input())))
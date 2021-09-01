# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def digisum(n):
    if n < 10:
        return n
    sum = 0
    while(n >0):
        d = n % 10
        n = n // 10
        sum += d
    return sum

def isSmith(n) :
    sum = digisum(n)
    sum1 = 0
    for i in range(2, n):
        if n % i == 0:
            if(isPrime(i)):
                sd = digisum(i)
                factor = 0
                num = n
                while(num%i==0):
                    factor += 1
                    num = num // i           
                sum1 += factor * sd
            
    if sum == sum1:
        return True
    else:
        return False

def fun_nth_smithnumber(n):
    if n == 0:
        return 4
    m = 10 ** 10
    count = 0
    for i in range(5, m):
        if(isPrime(i) == False):
            if(isSmith(i)):
                count += 1
        if count == n:
            return i
    return 1
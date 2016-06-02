import PrimeHandler as PH

def isPrime(x):
    i = 0
    while primes[i] < x:
        i += 1
    if primes[i]==x:
        return True
    return False

global primes
primes = PH.readPrimes()[1]
smallPrimes = PH.readPrimes(1000)[1]

maxNum = 0
prod = 0

for a in range(-999,1000,2):
    for b in smallPrimes:
        for j in range(2):
            n = 0
            if (j==0):
                sign = 1
            else:
                sign = -1
            if b==2:
                aodd = 1
            else:
                aodd = 0
            while isPrime(n*(n+a+aodd)+sign*b):
                n += 1
            if (n > maxNum):
                maxNum = n
                prod = (a+aodd)*b*sign

print(prod)

##for a in range(-999,1000):
##    print(a)
##    for b in smallPrimes:
##        num = numPrimes(a,b)
##        if num>maxNum:
##            maxNum = num
##            prod = a*b
##        num = numPrimes(a,-b)
##        if num>maxNum:
##            maxNum = num
##            prod = -a*b
##print("")
##print(prod)
            

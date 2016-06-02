import PrimeHandler as PH

def findNumberFactors(N):
    numFact = 1

    for p in primes:
        num = 1
        power = p
        if (N<=1):
            break
        if (N%p==0):
            while (N%(power*p)==0):
                num += 1
                power *= p
            N = N//power
            numFact *= (num+1)
    return numFact

global primes

primes = (PH.readPrimes())[1]

print('running')

tri = 1
n = 2

cap = 500

print(findNumberFactors(28))

while (findNumberFactors(tri)<cap):
    tri += n
    n += 1
    if (n%100==0):
        print(n,tri)
    #print(tri)

print(tri)

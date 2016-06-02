import PrimeHandler as PH

def isAbundant(x):
    return sum(PH.genFactors(x,primes,False))>x

global primes
primes = PH.readPrimes(28123)[1]
A = []

for i in range(2,28123):
    if isAbundant(i):
        A.append(i)

sums = set()
for i in range(len(A)):
    for j in range(i,len(A)):
        val = A[i]+A[j]
        if val<28123:
            sums.add(val)
        else:
            break

sums = list(sums)

print((28122*28123)//2 - sum(sums))

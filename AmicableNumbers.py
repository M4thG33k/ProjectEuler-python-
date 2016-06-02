import PrimeHandler as PH

#finds the potential amicable partner for x
def findAmicablePartner(x):
    return sum(PH.generateFactors(list(PH.findPrimeFactorTuples(x,primes)),False))


global primes
primes = (PH.readPrimes(10000))[1]

total = 0
aNums = 10000*[0]

aNums[0] = -1
aNums[1] = -1

for i in range(2,10000):
    aNums[i] = findAmicablePartner(i)
            
for i in range(2,10000):
    if (aNums[i]<10000 and i!=aNums[i] and i==aNums[aNums[i]]):
        print(i)
        total += i

print('\t',total)

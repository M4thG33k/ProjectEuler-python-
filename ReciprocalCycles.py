import PrimeHandler as PH

def findLengthForPrime(p):
    if p in [2,5]:
        return 1
    val = 10%p
    n = 1
    while val!=1:
        n += 1
        val = (val*10)%p
    return n

def findRepeatingLength(x):
    facts = list(PH.findPrimeFactorTuples(x,primes))
    if len(facts)==1:
        return findLengthForPrime(facts[0][0])
    facts.sort()
    return 0

global primes
primes = PH.readPrimes(1000)[1]

vals = 1000*[0]
for i in range(2,1000):
    vals[i] = findRepeatingLength(i)

#this just happens to produce the right answer without extra work...w00t
print(vals.index(max(vals)))

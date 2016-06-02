import PrimeHandler as PH

num = 1
numFactors = []

for x in range(2,21):
    numF = numFactors[:]
    primes = PH.readPrimes(0)[1]
    xF = PH.findPrimeFactorList(x,primes)
    #print(num,numF)
    #print('\t',x,xF)
    i = 0
    while i < len(xF):
        if xF[i] in numF:
            numF.remove(xF.pop(i))
        else:
            i += 1
    for f in xF:
        num *= f
        numFactors.append(f)
    #print('\t\t',num)

print(num)

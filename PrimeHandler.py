import os.path

def findFirstNPrimes(N):
    slicer = 100000
    if (grabMaxVal()>=N):
        return readPrimes(N)[1]
    if (N<=slicer):
        return findPrimesUpTo(N)
    p = findPrimesUpTo(N)
    minMax = slicer
    writePrimes(p,minMax)

    i = 2
    while minMax!=N:
        minMin = minMax+1
        minMax = min(N,slicer*i)

        newPrimes = findPrimesBetween(minMin,minMax)
        p = p + newPrimes
        writePrimes(p,minMax)
        i += 1

    return p

#uses the sieve of Eratosthenes to calculate the primes up
#to and including the given value
def findPrimesUpTo(N):
    if (grabMaxVal()>=N):
        return readPrimes(N)[1]
    A = [True]*(N+1)
    primes = []

    for i in range(2,int(N**0.5)+1):
        if A[i]:
            j = i*i
            while (j<=N):
                A[j] = False
                j += i
    for i in range(2,N+1):
        if A[i]:
            primes.append(i)
    writePrimes(primes,N)
    return primes

#uses the sieve of Eratosthenes to calculate the primes between
#the two input values (inclusive). (The smaller primes must already
#exist in the primeList.txt file.)
def findPrimesBetween(M,N):

    if (grabMaxVal() >= M):
        maxRead = min(grabMaxVal(),N)
    else:
        maxRead = M

    smallerPrimes = readPrimes(maxRead)[1]

    M = maxRead+1

##    A = []
##    vals = []
##
##    for i in range(M,N+1):
##        A.append(True)
##        vals.append(i)

    A = [True]*(N-M+1)

    newPrimes = []

    maxScan = int(N**0.5)+1
    for val in smallerPrimes:
        if (val<=maxScan):
            j = val*val
            while (j < M):
                j += val
            while (j<=N):
                A[j-M] = False
                j += val

    for i in range(N-M+1):
        if A[i]:
            val = i+M
            j = val*val
            while (j<=N):
                A[j] = False
                j += val
    
    for i in range(N-M+1):
        if A[i]:
            newPrimes.append(i+M)
    return newPrimes

#grabs the first line of the primeList and returns it
#returns 0 if no file is found
def grabMaxVal():
    if (os.path.isfile("primeList.txt")):
        f = open("primeList.txt",'r')
        for line in f:
            return int(line[:-1])
    return 0

#reads primes from a file and returns them as a list
#if a parameter N>1 is passed in, it will stop reading
#once it reaches a value greater than N
def readPrimes(N=0):
    print("Reading primes from file")
    primes = []
    if (os.path.isfile("primeList.txt")):
        f = open("primeList.txt",'r')
        maxFound = False
        for line in f:
            if not maxFound:
                maxVal = int(line[:-1])
                maxFound = True
                continue
            if (line[-1] == "\n"):
                line = line[:-1]
            line= int(line)
            if line > N and N!=0:
                break
            primes.append(line)
        f.close()
    print("Finished reading primes")
    return [maxVal,primes]

#writes the input array into the primeList.txt file
#the first line indicates the maximum value that has
#been searched for previously
def writePrimes(primes,maxVal):
    f = open("primeList.txt",'w')
    f.write(str(maxVal)+"\n")
    for i in range(len(primes)-1):
        f.write(str(primes[i])+"\n")
    f.write(str(primes[-1]))
    f.close()

#finds and returns a list of all prime factors of the number N
#including their multiplicities
def findPrimeFactorList(N,primes):
    tuples = findPrimeFactorTuples(N,primes)
    factors = []
    for t in tuples:
        factors = factors + t[1]*[t[0]]
    factors.sort()
    return factors

#finds and returns a set of all prime factors of the number N
def findPrimeFactorSet(N,primes):
    tuples = findPrimeFactorTuples(N,primes)
    theSet = set()
    for t in tuples:
        theSet.add(t[0])
    return theSet

#find and returns a set of tuples where the first entry is a prime factor
#and the second is the number of times that prime is a factor
def findPrimeFactorTuples(N,primes):
    tuples = set()

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
            tuples.add((p,num))
    return tuples

#finds and returns the number of (not necessarily prime) factors
#of a number (including 1 and itself)
def findNumberFactors(N):
    tuples = findPrimeFactorTuples(N)

    num = 1

    for t in tuples:
        num *= (1+t[1])

    return num

#takes in a list of tuples of prime factorization and returns
#a set of all factors that can be created
#if flag = FALSE, then we will only look at proper factors
def generateFactors(tuples,flag=True):
    facts = []
    if (len(tuples)==1):
        facts = [1]
        for i in range(1,tuples[0][1]+1):
            facts.append(facts[-1]*tuples[0][0])
    else:
        n = len(tuples)//2
        A = generateFactors(tuples[:n])
        B = generateFactors(tuples[n:])
        for valA in A:
            for valB in B:
                facts.append(valA*valB)

    facts.sort()
    if not flag:
        facts = facts[:-1]
    return facts
#same as above, but does some grunt work
def genFactors(N,primes,flag=True):
    tuples = list(findPrimeFactorTuples(N,primes))
    return generateFactors(tuples,flag)

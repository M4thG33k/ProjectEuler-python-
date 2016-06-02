def findPrimesUpTo(N):
    if N<2:
        return []
    primes = [2]

    for n in range(3,N+1):
        works = True
        for p in primes:
            if not works:
                break
            if p > n**0.5:
                primes.append(n)
                break
            if n%p==0:
                works = False
                break

    return primes

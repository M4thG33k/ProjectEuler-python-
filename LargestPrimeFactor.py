import PrimeHandler as PH

primes = PH.findPrimesUpTo(int(600851475143**0.5))

index = -1
value = 600851475143

while (value>1):
    index += 1
    prime = primes[index]
    while (value%prime==0):
        value = value//prime

print(primes[index])

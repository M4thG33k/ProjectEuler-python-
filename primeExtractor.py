fname = input("Filename: ")

f = open(fname,'r')

primes = []
firstLine = True
for line in f:
    if (firstLine):
        firstLine = False
        continue

    line = line.strip()

    line = line.split()

    for i in range(len(line)):
        try:
            line[i] = int(line[i])
        except ValueError:
            continue
        primes.append(line[i])

f.close()

f = open('primeList.txt','w')
f.write(str(primes[-1])+'\n')
for i in range(len(primes)-1):
    f.write(str(primes[i])+'\n')
f.write(str(primes[-1]))
f.close()

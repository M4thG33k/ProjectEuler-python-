pows = []
for i in range(10):
    pows.append(i**5)

#for all integers a >= 999999, the sum of the fifth powers of their digits will
#always be less than the original number, so we have a maximum

total = 0
for n in range(2,999999):
##    if (n%100==0):
##        print(n)
    s = 0
    val = n
    r = val%10
    while val != 0:
        s += pows[r]
        val = val//10
        r = val%10
    if s==n:
        total += n
print("")
print(total)

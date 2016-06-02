def seqLength(x):
    if x not in ChainLength.keys():
        if (x%2==0):
            ChainLength[x] = 1+seqLength(x//2)
        else:
            ChainLength[x] = 1+seqLength(3*x+1)
    return ChainLength[x]

global ChainLength

ChainLength = dict()
ChainLength[1]=1

maximum = 0
maxVal = 0

for x in range(1,1000000):
    val = seqLength(x)
    if (val>maximum):
        maximum = val
        maxVal = x

print(maxVal)

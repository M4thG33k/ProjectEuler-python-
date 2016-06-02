f = open('LargeSum.txt','r')

total = 0
for line in f:
    line = line.strip()
    line = int(line[:13])
    total += line
f.close()

total = str(total)[:10]
print(total)

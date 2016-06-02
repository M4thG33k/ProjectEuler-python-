def getNameNumber(name):
    total = -64*len(name)
    for i in range(len(name)):
        total += ord(name[i])
    return total

names = []
f = open('p022_names.txt','r')
for line in f:
    line = line.split('"')
    line = "".join(line)
    names = line.split(',')
f.close()

names.sort()

total = 0
place = 1
for name in names:
    total += (place * getNameNumber(name))
    place += 1
print(total)

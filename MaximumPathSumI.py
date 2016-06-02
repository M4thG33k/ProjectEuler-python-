f = open('MaximumPathSumI.txt','r')

data = []
for line in f:
    line = line.strip()

    line = line.split()

    if line != []:
        for i in range(len(line)):
            line[i] = int(line[i])
        data.append(line[:])

f.close()

for i in range(len(data)-2,-1,-1):
    for j in range(len(data[i])):
        maxVal = max(data[i+1][j:j+2])
        data[i][j] += maxVal
print(data[0][0])

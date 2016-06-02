

f = open('LargestProductInAGrid.txt','r')
data = []
n = 4
maxProd = 0

for line in f:
    if (line[-1]=='\n'):
        line = line[:-1]
    line = line.split(' ')
    for i in range(len(line)):
        line[i] = int(line[i])
    data.append(line[:])

for row in range(20):
    for col in range(20):
        hor = vert = dleft = dright = data[row][col]
        fleft = fright = fdown = True
        if (col<n-1):
            fleft = False
        if (col+n>20):
            fright = False
        if (row+n>20):
            fdown = False
        for i in range(1,n):
            if (fright):
                hor *= data[row][col+i]
                if (fdown):
                    dright *= data[row+i][col+i]
            if (fdown):
                vert *= data[row+i][col]
                if (fleft):
                    dleft *= data[row+i][col-i]
        #print(row,col,[maxProd,hor,vert,dleft,dright])
        #blah = input("")
        maxProd = max([maxProd,hor,vert,dleft,dright])
print(maxProd)
                
            
            

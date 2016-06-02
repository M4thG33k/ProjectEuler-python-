def findProduct(string):
    total = 1
    for i in range(len(string)):
        total *= int(string[i])
    return total

n = 13
f = open('LargestProductInSeries.txt','r')

for line in f:
    num = line

f.close()

maxProd = findProduct(num[:n])
currentProd = maxProd

for i in range(n,len(num)-1):
    #print(currentProd)
    #print('\t',i,num[i-n],num[n],num[i-n+1:n+1])
    #print('\t',maxProd)
    if (num[i-n]=='0'):
        currentProd = findProduct(num[i-n+1:i+1])
    else:
        currentProd = (currentProd // int(num[i-n])) * int(num[i])
    if currentProd > maxProd:
        maxProd = currentProd
    #temp = input("")
print(maxProd)

sumOfSquares = 0
sumTotal = 0

for i in range(1,101):
    sumTotal += i
    sumOfSquares += i*i

print(sumTotal**2 - sumOfSquares)

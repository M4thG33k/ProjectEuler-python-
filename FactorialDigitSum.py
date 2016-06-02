def factorial(n):
    f = 1
    for x in range(2,n+1):
        f *= x
    return f

total = 0
string = str(factorial(100))
for i in range(len(string)):
    total += int(string[i])
print(total)

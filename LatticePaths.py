def factorial(n):
    val = 1
    for i in range(2,n+1):
        val *= i
    return val

def choose(n,k):
    return factorial(n)//(factorial(n-k)*factorial(k))

#since we have to travel exactly 40 units and exactly 20 of them must be to the right,
#the total number of routs is "40 choose 20"

print(choose(40,20))

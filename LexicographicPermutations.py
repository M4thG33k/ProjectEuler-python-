def factorial(n):
    val = 1
    for i in range(2,n+1):
        val *= i
    return val

#find the Nth permutation of the string STRING with 1-indexing
def findNthPermutation(string,n):
    n -= 1
    ans = ""
    while n>0:
        f = factorial(len(string)-1)
        val = n//f
        ans += string[val]
        string = string[:val]+string[val+1:]
        n -= val*f
    ans += string
    return ans

print(findNthPermutation("0123456789",1000000))

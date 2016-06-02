def lengthOf(x):
    return len(str(x))

#we are starting with n=3
F_Nminus2 = 1
F_Nminus1 = 1
F_N = 2
n = 3

while (lengthOf(F_N)<1000):
    F_Nminus2 = F_Nminus1
    F_Nminus1 = F_N
    F_N = F_Nminus2+F_Nminus1
    n += 1

print(n)

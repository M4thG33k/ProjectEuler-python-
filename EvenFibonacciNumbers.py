F = [1, 2, 3]
total = 2


while F[2]<= 4000000:
    if (F[2]%2==0):
        total += F[2]
    F[0] = F[1]
    F[1] = F[2]
    F[2] = F[0]+F[1]

print(total)

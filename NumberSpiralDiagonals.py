total = 1

#note that the upper-right diagonal is made up of the numbers
#(2n+1)^2 where n is the number of rows above the center at
#which we are looking; call this number D_n. The number
#along the upper-left diagonal along the same row is D_n-(2n)
#The other two diagonal entries can be found by repeatedly
#subtracting (2n). That means the sum of each square is given
#by D_n+(D_n-(2n))+(D_n-2(2n))+(D_n-3(2n))
# = 4D_n-6(2n) = 4(2n+1)^2-12n which leads to:

sideLength = 1001

for n in range(1,sideLength//2+1):
    total += (4*(2*n+1)**2-12*n)
print(total)

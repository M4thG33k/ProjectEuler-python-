#hard-code the values for 0-20, since teens screw up everything
Counts = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8,6]

#use this to help with double-digit numbers ie: "twenty" has length
#six so if a 2 is in the ten's place, then "twenty" appears in its spelling
tens = dict()
tens[2] = 6
tens[3] = 6
tens[4] = 5
tens[5] = 5
tens[6] = 5
tens[7] = 7
tens[8] = 6
tens[9] = 6

#take care of all two-digit numbers
for val in range(21,100):
    Counts.append(tens[val//10]+Counts[val%10])

#take care of all three-digit numbers
for val in range(100,1000):
    Counts.append(Counts[val//100]+7)
    #check if an even hundred
    if (val%100!=0):
        #if it isn't an even hundred, then we have "and" plus the letters
        #needed to write the two-digit number (already computed)
        Counts[val] += 3+Counts[val%100]

#take care of 1000
Counts.append(3+8)

print(sum(Counts))

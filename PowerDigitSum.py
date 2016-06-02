string = str(2**1000)

total = 0
for i in range(len(string)):
    total += int(string[i])

print(total)

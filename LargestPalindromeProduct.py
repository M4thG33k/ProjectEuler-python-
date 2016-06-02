maxVal = 0
for i in range(100,1000):
    for j in range(i,1000):
        val = i*j
        if (val) > maxVal:
            if (str(val) == str(val)[-1::-1]):
                maxVal = val

print(maxVal)
            

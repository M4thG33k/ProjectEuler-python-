
dictionary = dict()
dictionary[1] = 1
dictionary[2] = 2
dictionary[5] = 4
dictionary[10] = (dictionary[5])**2+2
dictionary[20] = (dictionary[10])**2+1
dictionary[50] = ((dictionary[20])**2)*(dictionary[10])+1
dictionary[100] = (dictionary[50])**2+1
dictionary[200] = (dictionary[100])**2+1

print(dictionary[200])

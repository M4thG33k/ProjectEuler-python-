for a in range(1,333):
    for b in range(a+1,(1000-a)//2+1):
        if (a**2+b**2==(1000-a-b)**2):
            print([a,b,1000-a-b])
            print(a*b*(1000-a-b))

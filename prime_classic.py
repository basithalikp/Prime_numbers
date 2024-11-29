def prime(j):
    c,isPrime=0,True
    for i in range(1,j+1):
        if j%i==0:
            c+=1
    if c<=2:
        isPrime=False
    return isPrime
def prime(j):
    c=0
    for i in range(1,j+1):
        if j%i==0:
            c+=1
    if c<=2:
        return False
    return True

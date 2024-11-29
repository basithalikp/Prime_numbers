def prime(j):
    i=2
    while i*i<j:
        if j%i==0:
            return False
        i+=1
    return True
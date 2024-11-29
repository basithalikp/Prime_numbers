def prime(n):
    is_prime=True
    for i in range(2,(n//2)+1):
        if n%i==0:
            is_prime=False
            break
    return is_prime
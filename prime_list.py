import time
from prime_ampere2 import prime
start_time = time.time()
def prime_list(n):
    values=[]
    if n <= 1:
        print("Invalid upper limit")
    else:
        for j in range(2,n):
            if prime(j)==True:
                values.append(j)
    print(values)

prime_list(12345)
print("--- %s seconds ---" % (time.time() - start_time))
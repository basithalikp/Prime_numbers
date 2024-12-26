import time
from prime_locals import prime

def prime_list(time_limit):
    start_time = time.time()
    values = []
    j=2
    while time.time() - start_time < time_limit:
        if prime(j):
            values.append(j)
        j+=1

    print(values)
    print(f"--- {time.time() - start_time} seconds ---")

# Example usage
time_limit = 1  # Set the time limit in seconds
prime_list(time_limit)
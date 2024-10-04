import sys

def is_prime(limit):
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False
    
    for start in range(2, int(limit**0.5) + 1):
        if prime[start]:
            for i in range(start*start, limit + 1, start):
                prime[i] = False
    return prime

MAX_LIMIT = 1000000
primes = is_prime(MAX_LIMIT)

while True:
    n = int(sys.stdin.readline())
    
    if n == 0:
        break
    
    for i in range(3, int(n/2)+1, 2): 
        if primes[i] and primes[n-i]:
            print(f"{n} = {i} + {n-i}")
            break

    else:
        print("Goldbach's conjecture is wrong.")

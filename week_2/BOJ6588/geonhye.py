# 골드바흐의 추측 / 1h 40m
import sys

def findPrime(n):
    prime = [True] * (n + 1)
    p = 2
    while p*p <= n:
        if prime[p] == True:
            for i in range(2 * p, n+1, p):
                prime[i] = False
        p += 1
    return prime

def main():
    global prime
    prime = findPrime(1000001)
    while True:
        n = int(sys.stdin.readline().strip())
        if n == 0:
            break
        else:
            print(solution(n))

def solution(n):
    for i in range(2, int(n*(1/2))+1):
        if prime[i] and prime[n-i]:
            return f"{n} = {i} + {n-i}"
    return "Goldbach's conjecture is wrong."

if __name__ == "__main__":
    main()
# 중복 조합 사용 / 1h

import math

def uphill(n):
    return math.comb(n+9, 9) % 10007

def factorial(k):
    result = 1
    for x in range(1, k+1):
        result *= x
    return result
    
def uphill_(n):
    result = factorial(9+n) // (factorial(9) * factorial(n))
    return result % 10007
    
def main():
    n = int(input())
    print(uphill_(n))

if __name__=="__main__":
    main()

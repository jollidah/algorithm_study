#32m
from bisect import bisect_left
import sys
input = sys.stdin.readline

def main():
    T = int(input()) 
    results = []
    
    for _ in range(T):
        N, M = map(int, input().split())  
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        A.sort()
        B.sort()
        
        count = 0
        for a in A:
            count += bisect_left(B, a)
        
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()

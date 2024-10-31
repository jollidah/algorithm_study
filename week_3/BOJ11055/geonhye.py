# 가장 큰 증가하는 부분 수열 

import sys
input = sys.stdin.readline

def main(): 
    n = int(input().strip())
    ls = list(map(int, input().strip().split()))
    
    d = [0] * n
    d[0] = ls[0]

    for i in range(n):
        for j in range(i):
            if ls[i] > ls[j]:
                d[i] = max(d[i], d[j] + ls[i])
            else:
                d[i] = max(d[i], ls[i])
    print(max(d))

if __name__ == '__main__':
    main()
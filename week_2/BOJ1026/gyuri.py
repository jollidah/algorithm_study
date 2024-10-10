import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


A.sort() 
BC = [i for i in range(n)]
BC = sorted(BC, key=lambda x: B[x], reverse=True)

result = 0
for i in range(n):
    result += A[i] * B[BC[i]] 

print(result)
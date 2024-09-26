import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())
cnt = 0

while a!=b:
    a -= a//2
    b -= b//2
    cnt+=1

if cnt == 0:
    print(-1)
else:
    print(cnt)
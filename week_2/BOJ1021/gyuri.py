import sys
input = sys.stdin.readline
n, m = map(int, input().split())
data = list(map(int, input().split()))
dq = [i for i in range(1, n+1)]
cnt = 0

for i in data:
    while True:
        if dq[0] == i:
            dq = dq[1:]
            break
        else:
            if dq.index(i) < len(dq)/2:
                while dq[0] != i:
                    dq.append(dq[0])
                    dq = dq[1:]
                    cnt += 1
            else:
                while dq[0] != i:
                    dq = [dq.pop()] + dq
                    cnt += 1
print(cnt)
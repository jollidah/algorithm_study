import sys

n = int(input())
l = [int(sys.stdin.readline()) for _ in range(n)]
answer = -1
    
l.sort(reverse = True)

for i in range(n-2):
    if l[i] < l[i + 1] + l[i + 2]:
        answer = l[i] + l[i + 1] + l[i + 2]
        break
    
print(answer)

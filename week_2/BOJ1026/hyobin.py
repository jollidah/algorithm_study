n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()

answer = 0

for i in range(n):
    b_max = max(b)
    answer += a[i] * b_max
    b.remove(b_max)
    
print(answer)

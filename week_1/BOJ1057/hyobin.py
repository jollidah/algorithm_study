a, b, c = map(int, input().split())

count = 0

while b != c:
    b -= b//2
    c -= c//2
    count += 1
    
print(count)
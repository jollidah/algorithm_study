n, a, b = map(int, input().split())
times = 0

while a != b:
    n = n//2 + n%2
    a = a//2 + a%2
    b = b//2 + b%2
    times += 1

print(times)
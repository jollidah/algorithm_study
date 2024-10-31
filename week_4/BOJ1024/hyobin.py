def search_sum(n, l):
    while l <= 100:
        if (n - (l * (l - 1)) // 2) % l == 0:
            start = (n - (l * (l - 1)) // 2) // l
            
            if (n - (l * (l - 1)) // 2) >= -1:
                return [start + i for i in range(l)]
        
        l += 1
    
    return None

n, l = map(int, input().split())

result = search_sum(n, l)
if result:
    print(*result)
else:
    print(-1)

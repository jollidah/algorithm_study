def check_order(a, b):
    if len(a) > len(b):
        return True
        
    elif len(a) < len(b):
        return False
        
    else:
        if check_num(a) > check_num(b):
            return True
            
        elif check_num(a) < check_num(b):
            return False
            
        else:
            for x, y in zip(a, b):
                if x > y:
                    return True
                    
                elif x < y:
                    return False
    return False
        
        
def check_num(a):
    s = 0
    for i in range(len(a)):
        if '0' <= a[i] <= '9':
            s += int(a[i])
    return s
    
    
n = int(input())
arr = []
arr = [input() for _ in range(n)]
    

# 버블정렬
for i in range(n):
    for j in range(0, n - i - 1):
        if check_order(arr[j], arr[j + 1]):
            arr[j], arr[j + 1] = arr[j + 1], arr[j]


print('\n'.join(arr))

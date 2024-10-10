n = int(input())

a = list(map(int, input().split()))

sum_list = [0] * n
sum_list[0] = a[0]

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            sum_list[i] = max(sum_list[i], sum_list[j] + a[i])
        
        else:
            sum_list[i] = max(sum_list[i], a[i])
    
print(max(sum_list))

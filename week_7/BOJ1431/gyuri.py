import sys
input = sys.stdin.readline
n = int(input())
data = []
for _ in range(n):
    data.append(input().strip())

for i in range(n-1):
    for j in range(i+1, n):
        if len(data[i]) > len(data[j]):
            data[i], data[j] = data[j], data[i]
        elif len(data[i]) == len(data[j]):
            cnt_1=0
            cnt_2=0
            for x,y in zip(data[i],data[j]):
                if x.isdigit():
                    cnt_1+=int(x)
                if y.isdigit():
                    cnt_2+=int(y)
            if cnt_1 > cnt_2:
                data[i],data[j] = data[j], data[i]

            elif cnt_1 == cnt_2:
                for x,y in zip(data[i], data[j]):
                    if x > y:
                        data[i],data[j] = data[j], data[i]
                        break
                    elif x < y:
                        break

for i in data:
    print(i)
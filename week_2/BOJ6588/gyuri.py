import sys

case = sys.stdin.read().splitlines()
case = case[:-1]

num = [True] * 1000001
for i in range(2, int(len(num)**0.5) + 1):
    if num[i]:
        for j in range(2*i, 1000001, i):
            num[j] = False


for data in case:
    n = int(data)
    
    for i in range(n - 3, 2, -2):
        if num[i] and num[n - i]:
            print(f"{n} = {n - i} + {i}")
            break
    else:
        print("Goldbach\'s conjecture is wrong.")
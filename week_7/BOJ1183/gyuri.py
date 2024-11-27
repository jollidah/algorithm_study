# 이해력이 딸려서 이해를 못했습니다...
# 참고 : https://v3.leedo.me/devs/58 

import sys
input = sys.stdin.readline

n = int(input())
numbers = list()
for _ in range(n):
    a, b = map(int, input().split())
    numbers.append(b - a)

numbers = sorted(numbers)

answer = 0
if len(numbers) % 2 == 0:
    start = len(numbers) // 2 - 1
    answer = numbers[start + 1] - numbers[start] + 1
else:
    answer = 1

print(answer)
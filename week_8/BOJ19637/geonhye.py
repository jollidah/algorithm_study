# IF문 좀 대신 써줘 / 40m

import sys
from bisect import bisect_left
input = sys.stdin.readline

def solution():
    title = []
    value = []
    for _ in range(n):
        a, b = input().rstrip().split()
        title.append(a)
        value.append(int(b))

    character = [int(input().rstrip()) for i in range(m)]

    for i in range(m):
        idx = bisect_left(value, character[i])
        print(title[idx])

if __name__ == '__main__':
    n, m = map(int, input().rstrip().split())
    solution()
#47m
from bisect import bisect_left
import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())  
    titles = []
    limit = []

    for _ in range(N):
        title, power = input().split()
        titles.append(title)
        limit.append(int(power))
    
    data = []
    for _ in range(M):
        tmp = int(input())
        data.append(tmp)
    for i in data:
        index = bisect_left(limit, i)
        print(titles[index])

if __name__ == "__main__":
    main()

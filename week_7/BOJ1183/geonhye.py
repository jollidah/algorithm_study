from itertools import combinations
import sys
input = sys.stdin.readline

def solution(ls):
    if len(ls) % 2 == 1:
        return 1
    else:
        ls.sort()
        mid = len(ls) // 2 -1
        return ls[mid+1] - ls[mid] + 1

if __name__ == "__main__":
    n = int(input().strip())
    ls = []
    for _ in range(n):
        a, b = map(int, input().strip().split())
        ls.append(b - a)
    print(solution(ls))
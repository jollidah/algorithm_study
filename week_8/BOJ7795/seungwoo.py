import sys
from bisect import bisect_left

def solution():
    inp = sys.stdin.readline
    for _ in range(int(inp())):
        inp()
        a_list , b_list = sorted(map(int, inp().split())), sorted(map(int, inp().split()))
        idx, sum = 0, 0
        for a in a_list:
            sum += (idx := bisect_left(b_list, a, idx))
        print(sum)

if __name__ == "__main__":
    solution()

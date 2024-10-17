import sys
from bisect import bisect_left

def solution(): 
    inp = sys.stdin.readline
    n, n_list, cnt_list = int(inp()), list(map(int, inp().split())), [0 for _ in range(1001)]
    sorted_n_list = sorted(n_list)
    for n in n_list:
        print(bisect_left(sorted_n_list, n) + cnt_list[n], end=" ")
        cnt_list[n] += 1

if __name__ == "__main__":
    solution()

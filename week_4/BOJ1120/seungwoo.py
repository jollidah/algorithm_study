import sys

def solution():
    inp = sys.stdin.readline
    a, b = inp().split()
    res = 1e9
    for rp in range(len(b) - len(a) + 1):
        cnt = 0
        for lp in range(len(a)):
            if a[lp] != b[rp + lp]:
                cnt += 1
        res = min(cnt, res)
    print(res)

if __name__ == "__main__":
    solution()

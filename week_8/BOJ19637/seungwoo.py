import sys

def solution():
    def my_bisect(target):
        lp, rp = 0, len(pair_list) - 1
        while lp < rp:
            # print(lp, rp)
            mid = (lp + rp) // 2
            if pair_list[mid][0] < target:
                lp = mid + 1
            else:
                rp = mid
        return(lp)

    inp = sys.stdin.readline
    n, m = map(int, inp().split())
    pair_list = []
    for _ in range(n):
        pair = inp().split()
        pair_list.append((int(pair[1]), pair[0]))

    for _ in range(m):
        print(pair_list[my_bisect(int(inp()))][1])

if __name__ == "__main__":
    solution()

import sys

def solution():
    def check_dist(dist):
        next, cnt = dist, m
        for cur in rest_list:
            while cnt and next < cur:
                cnt -= 1
                next += dist
            if next >= cur:
                next = cur + dist
            else:
                return False
        return True

    inp = sys.stdin.readline
    n, m, l = map(int, inp().split())
    rest_list = sorted(list(map(int, inp().split()))) + [l]
    lp, rp = 0, l
    mid = (lp + rp) // 2
    while lp < rp:
        mid = (lp + rp) // 2
        if check_dist(mid):
            rp = mid
        else:
            lp = mid + 1
    print(lp)

if __name__ == "__main__":
    solution()

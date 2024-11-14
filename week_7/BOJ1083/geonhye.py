import sys
input = sys.stdin.readline

def solution(ls, s):
    for i in range(n):
        if s == 0:
            break
        mx = max(ls[i:i+s+1])
        mx_idx = ls.index(mx)
        
        for j in range(mx_idx, i, -1):
            ls[j], ls[j-1] = ls[j-1], ls[j]
        s -= mx_idx - i
    return " ".join(map(str, ls))

if __name__ == "__main__":
    n = int(input().strip())
    ls = list(map(int, input().strip().split()))
    s = int(input().strip())
    print(solution(ls, s))
import sys

def solution():
    inp = sys.stdin.readline
    target, l = map(int, inp().split())
    if l == 1:
        print(target)
        exit(0)
    for n in range(l, 101):
        div = target - ((n - 1) * n) // 2
        if div < 0:
            break
        quotient, remainder = divmod(div, n)
        if not remainder:
            print(*list(range(quotient, quotient + n)))
            exit(0)
    print(-1)

if __name__ == "__main__":
    solution()

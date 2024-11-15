import sys
input = sys.stdin.readline

def solution(ls):
    ls.sort()
    ls = sorted(ls, key = lambda x: sum([int(i) for i in x if i.isdigit()]))
    ls = sorted(ls, key = lambda x: len(x))

    print("\n".join(map(str, ls)))

if __name__ == "__main__":
    t = int(input().strip())
    ls = [input().strip() for _ in range(t)]
    solution(ls)
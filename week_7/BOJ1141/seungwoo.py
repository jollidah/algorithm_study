import sys

def solution():
    inp = sys.stdin.readline
    n = int(inp())
    str_list = sorted([inp().rstrip() for _ in range((n))])
    for i in range(len(str_list) - 1):
        if str_list[i] == str_list[i + 1][:len(str_list[i])]:
            n -= 1
    print(n)

if __name__ == "__main__":
    solution()

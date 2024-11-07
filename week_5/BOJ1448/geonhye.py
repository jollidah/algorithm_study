# 삼각형 만들기 / 30m

import sys
input = sys.stdin.readline

n = int(input().strip())
ls = sorted([int(input().strip()) for _ in range(n)], reverse=True)

def isTriangle(a, b, c):
    global ls
    if ls[a] < ls[b] + ls[c]:
        return True
    return False

def main():
    for a in range(len(ls)-2):
        b, c = a + 1, a + 2
        if isTriangle(a, b, c):
            return ls[a] + ls[b] + ls[c]
        else:
            while c < len(ls):
                if isTriangle(a, b, c):
                    return ls[a] + ls[b] + ls[c]
                c += 1

            while b < len(ls) - 1:
                c = b + 1
                if isTriangle(a, b, c):
                    return ls[a] + ls[b] + ls[c]
                b += 1
    else:
        return -1

if __name__ == '__main__':
    print(main())
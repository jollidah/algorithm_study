# 폴리오미노 / 25m

import sys
input = sys.stdin.readline

a = "AAAA"
b = "BB"

board = input().strip()

def main():
    global a
    global b
    global board

    ans = ""

    i = 0
    while i <len(board):
        if board[i:i+4] == "XXXX":
            ans += a
            i += 4
        elif board[i:i+2] == "XX":
            ans += b
            i += 2
        elif board[i] == ".":
            ans += "."
            i += 1
        else:
            return -1
    return ans

if __name__ == '__main__':
    print(main())
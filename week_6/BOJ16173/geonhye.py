# 점프왕 쩰리 / 40m

import sys
input = sys.stdin.readline

n = int(input().strip())
board = [list(map(int, input().split())) for _ in range(n)]

direction = [(1, 0), (0, 1)]

def jump(x, y):
    if board[x][y] == -1:
        return True
    elif board[x][y] == 0:
        return False
    else:
        move = board[x][y]
        for dx, dy in direction:
            next_x, next_y = x + move * dx, y + move * dy
            if 0 <= next_x < n and 0 <= next_y < n:
                if jump(next_x, next_y):
                    return True
        return False

def main():
    if jump(0, 0):
        print("HaruHaru")
    else:
        print("Hing")

if __name__ == '__main__':
    main()
import sys

def solution():
    inp, lines = sys.stdin.readline, []
    for _ in range(int(inp())):
        lines.append(int(inp().rstrip()))
    lines.sort(reverse=True)
    for a in range(len(lines) - 2):
        b, c = a + 1, a + 2
        while b < c:
            if lines[a] < (tmp_sum:=lines[b] + lines[c]):
                print(lines[a] + tmp_sum)
                exit(0)
            else:
                if b < len(lines) - 2:
                    max1, max2 = lines[b - 1] + lines[c], 0
                    if c < len(lines) - 1:
                        max2 = lines[b] + lines[c - 1]
                    if max1 > max2:
                        b += 1
                    else:
                        c += 1
                else:
                    break
    else:
        print(-1)

if __name__ == "__main__":
    solution()

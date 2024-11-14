import sys

def solution():
    inp = sys.stdin.readline
    l, ptr = int(inp()), 0
    n_list, n = list(map(int, inp().split())), int(inp())
    while n and ptr < l - 1:
        maxV, add_idx = n_list[ptr], 0
        for i in range(1, min(n + 1, l - ptr)):
            if n_list[ptr + i] > maxV:
                maxV = n_list[ptr + i]
                add_idx = i
        n_list = n_list[:ptr] + [maxV] + n_list[ptr: ptr + add_idx] + n_list[ptr + add_idx + 1:]
        n -= add_idx
        ptr += 1
    print(*n_list)

if __name__ == "__main__":
    solution()

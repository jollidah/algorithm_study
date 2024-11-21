import sys

def solution():
    def update_res(pin):
        if pin % 2 == 1:
            print(-1)
            exit(0)
        while pin >= 4:
            pin -= 4
            res.append("AAAA")
        if pin >= 2:
            pin -= 2
            res.append("BB")
        return pin

    inp, res, i, pin, update_required = sys.stdin.readline().rstrip(), [], 0, 0, False
    for i in range(len(inp)):
        if inp[i] == '.':
            pin = update_res(pin)
            res.append('.')
        else:
            pin += 1
    update_res(pin)

    print("".join(res))

if __name__ == "__main__":
    solution()

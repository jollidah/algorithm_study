import sys

def solution():
    minV, res, sub_list = 1e20, [], []
    def compare_update():
        nonlocal minV, res
        
        if minV > (tmp:=sum(map(lambda x: abs(x + n), sub_list))):
            minV = tmp
            res = [n]
        elif minV == tmp:
            res.append(n)
        else:
            return

    inp = sys.stdin.readline
    for _ in range(int(inp())):
        a, b = map(int, inp().split())
        sub_list.append(a - b)
    sub_list.sort()
    if sub_list[0] * sub_list[-1] > 0:
        n_list = sorted(list(map(lambda x: -1 * x, sub_list)))
        for n in n_list:
            compare_update()
    else:
        n_list = sorted(sub_list + list(map(lambda x: -1 * x, sub_list)))
        for n in n_list:
            compare_update()
    print(res[-1] - res[0] + 1)

if __name__ == "__main__":
    solution()

import sys

def solution():
    def is_left_small(a, b):
        if len(a) != len(b):
            return len(a) < len(b)

        s1, s2 = 0, 0
        for c in a:
            try:
                s1 += int(c)
            except:
                continue
        for c in b:
            try:
                s2 += int(c)
            except:
                continue
        if s1 != s2:
            return s1 < s2
        return a < b

    def quick_sort(sort_list):
        if len(sort_list) <= 1:
            return sort_list
        piv, s_list, b_list = 0, [], []
        for i in range(1, len(sort_list)):
            if is_left_small(sort_list[i], sort_list[piv]):
                s_list.append(sort_list[i])
            else:
                b_list.append(sort_list[i])
        return quick_sort(s_list) + [sort_list[piv]] + quick_sort(b_list)

    inp = sys.stdin.readline
    for res in quick_sort([inp().rstrip() for _ in range(int(inp()))]):
        print(res)

if __name__ == "__main__":
    solution()
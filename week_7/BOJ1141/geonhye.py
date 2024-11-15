import sys
input = sys.stdin.readline

n = int(input().strip())
word = [input().strip() for _ in range(n)]

word = sorted(word, key = lambda x: len(x))

res = 0
for i in range(n):
    is_prefix = False
    for j in range(i + 1, n):
        # 접두어 검사
        if word[i] == word[j][0:len(word[i])]:
            is_prefix = True
            break
    if not is_prefix:
        res += 1
print(res)
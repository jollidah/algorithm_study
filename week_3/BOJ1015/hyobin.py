import sys 
input = sys.stdin.readline

n = int(input())
a = map(int, input().split())

a_list = [i for i in a]
s_list = sorted(i for i in a_list)

answer = []

for i in a_list:
    answer.append(s_list.index(i))
    s_list[s_list.index(i)] = -1

for ans in answer:
    print(ans, end = ' ')

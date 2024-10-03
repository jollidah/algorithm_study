n = int(input())
a_lst = list(map(int, input().split()))
b_lst = list(map(int, input().split()))

def s_function(a_lst, b_lst):
  a_lst = sorted(a_lst)
  b_lst = sorted(b_lst, reverse=True)
  min_lst = [a * b for a, b in zip(a_lst, b_lst)]
  return sum(min_lst)

print(s_function(a_lst, b_lst))
n, m = map(int, input().split())
p = list(map(int, input().split()))

lst = [x for x in range(1, n+1)]

cnt = 0

def shift_left(lst, idx):
  lst = lst[idx:] + lst[:idx]
  return lst
  
def shift_right(lst, idx):
  lst = lst[-idx:] + lst[:-idx]
  return lst

for position in p:
  idx = lst.index(position)
  left = idx
  right = len(lst) - idx
  
  cnt += min(left, right)
  
  if left <= right:
    lst = shift_left(lst, idx)
  else:
    lst = shift_right(lst, right)
  
  lst.pop(0)

print(cnt)
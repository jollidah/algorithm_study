def is_prime(n):
  if n < 2:
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if n%i == 0:
      return False
  return True

n = int(input())

if n%2 != 0:
  print("Goldbach's conjecture is wrong")
else:
  for i in range(3, n, 2):
    if is_prime(i) and is_prime(n-i):
      print(f'{n} = {i} + {n-i}')
      break
    else:
      print("Goldbach's conjecture is wrong")